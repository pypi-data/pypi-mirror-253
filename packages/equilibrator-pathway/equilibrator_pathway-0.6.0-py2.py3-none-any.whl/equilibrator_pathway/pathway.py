"""analyze pathways using thermodynamic models."""

# The MIT License (MIT)
#
# Copyright (c) 2013 Weizmann Institute of Science
# Copyright (c) 2018-2020 Institute for Molecular Systems Biology,
# ETH Zurich
# Copyright (c) 2018-2020 Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from typing import Dict, Optional, Union

import numpy as np
import pandas as pd
from equilibrator_api import Q_, ComponentContribution, Reaction
from equilibrator_cache import Compound
from sbtab import SBtab

from . import Bounds, StoichiometricModel, open_sbtabdoc


class Pathway(StoichiometricModel):
    """A pathway parsed from user input.

    Designed for checking input prior to converting to a stoichiometric model.
    """

    def __init__(
        self,
        S: pd.DataFrame,
        compound_dict: Dict[str, Compound],
        reaction_dict: Dict[str, Reaction],
        fluxes: Q_,
        comp_contrib: Optional[ComponentContribution] = None,
        standard_dg_primes: Optional[Q_] = None,
        dg_sigma: Optional[Q_] = None,
        bounds: Optional[Bounds] = None,
        config_dict: Optional[Dict[str, str]] = None,
    ) -> None:
        """Initialize a Pathway object.

        Parameters
        ----------
        S : DataFrame
            stoichiometric matrix, where rows are the compound IDs and columns
            are the reaction IDs
        compound_dict : Dict[str, Compound]
            a dictionary of Compound objects, where the keys are their IDs
        reaction_dict : Dict[str, Reaction]
            a dictionary of Reaction objects, where the keys are their IDs
        fluxes : Quantity
            relative fluxes in same order as the columns of S
        comp_contrib : ComponentContribution
            a ComponentContribution object
        standard_dg_primes : Quantity, optional
            reaction energies (in kJ/mol)
        dg_sigma : Quantity, optional
            square root of the uncertainty covariance matrix (in kJ/mol)
        bounds : Bounds, optional
            bounds on metabolite concentrations (by default uses the
            "data/cofactors.csv" file in `equilibrator-api`)
        config_dict : dict, optional
            configuration parameters for Pathway analysis
        """
        super(Pathway, self).__init__(
            S=S,
            compound_dict=compound_dict,
            reaction_dict=reaction_dict,
            comp_contrib=comp_contrib,
            standard_dg_primes=standard_dg_primes,
            dg_sigma=dg_sigma,
            bounds=bounds,
            config_dict=config_dict,
        )

        assert fluxes.unitless or fluxes.check("[concentration]/[time]")
        self.fluxes = fluxes.flatten()
        assert self.fluxes.shape == (self.Nr,)
        self.I_dir = np.diag(np.sign(self.fluxes.magnitude).flat)

    def get_net_reaction_sparse(self) -> Dict[str, int]:
        """Get the net reaction as a sparse dictionary."""
        net_rxn_stoich = self.S @ self.fluxes.magnitude
        net_rxn_stoich = net_rxn_stoich[net_rxn_stoich != 0]
        return net_rxn_stoich.to_dict()

    @property
    def net_reaction(self) -> Reaction:
        """Calculate the sum of all the reactions in the pathway.

        :return: the net reaction
        """
        sparse = {
            self.compound_dict[cid].compound: coeff
            for cid, coeff in self.get_net_reaction_sparse().items()
        }
        return Reaction(sparse)

    @property
    def net_reaction_formula(self) -> str:
        """Calculate the sum of all the reactions in the pathway.

        :return: the net reaction formula
        """
        return self._sparse_to_formula(self.get_net_reaction_sparse())

    @classmethod
    def from_network_sbtab(
        cls,
        filename: Union[str, SBtab.SBtabDocument],
        comp_contrib: Optional[ComponentContribution] = None,
        freetext: bool = True,
        bounds: Optional[Bounds] = None,
    ) -> object:
        """Initialize a Pathway object using a 'network'-only SBtab.

        Parameters
        ----------
        filename : str, SBtabDocument
            a filename containing an SBtabDocument (or the SBtabDocument
            object itself) defining the network (topology) only
        comp_contrib : ComponentContribution, optional
            a ComponentContribution object needed for parsing and searching
            the reactions. also used to set the aqueous parameters (pH, I, etc.)
        freetext : bool, optional
            a flag indicating whether the reactions are given as free-text (i.e.
            common names for compounds) or by standard database accessions
            (Default value: `True`)
        bounds : Bounds, optional
            bounds on metabolite concentrations (by default uses the
            "data/cofactors.csv" file in `equilibrator-api`)

        Returns
        -------
            a Pathway object
        """
        stoich_model = StoichiometricModel.from_network_sbtab(
            filename=filename,
            comp_contrib=comp_contrib,
            freetext=freetext,
            bounds=bounds,
        )
        sbtabdoc = open_sbtabdoc(filename)
        reaction_df = sbtabdoc.get_sbtab_by_id("Reaction").to_data_frame()
        fluxes = reaction_df.RelativeFlux.apply(float).values * Q_("dimensionless")
        return Pathway.from_stoichiometric_model(stoich_model, fluxes)

    @classmethod
    def from_stoichiometric_model(
        cls,
        stoich_model: StoichiometricModel,
        fluxes: Optional[np.ndarray] = None,
    ) -> "Pathway":
        """Convert a StoichiometricModel into a Pathway.

        Assume all fluxes are 1.
        """
        if fluxes is None:
            fluxes = np.ones(stoich_model.Nr) * Q_(1)
        pp = Pathway(
            S=stoich_model.S,
            compound_dict=stoich_model.compound_dict,
            reaction_dict=stoich_model.reaction_dict,
            fluxes=fluxes,
            comp_contrib=stoich_model.comp_contrib,
            standard_dg_primes=stoich_model.standard_dg_primes,
            dg_sigma=stoich_model.dg_sigma,
            bounds=stoich_model._bounds,
            config_dict=stoich_model.config_dict,
        )
        return pp

    @classmethod
    def from_sbtab(
        cls,
        filename: Union[str, SBtab.SBtabDocument],
        comp_contrib: Optional[ComponentContribution] = None,
    ) -> "Pathway":
        """Parse and SBtabDocument and return a StoichiometricModel.

        Parameters
        ----------
        filename : str or SBtabDocument
            a filename containing an SBtabDocument (or the SBtabDocument
            object itself) defining the pathway
        comp_contrib : ComponentContribution, optional
            a ComponentContribution object needed for parsing and searching
            the reactions. also used to set the aqueous parameters (pH, I, etc.)

        Returns
        -------
        pathway: Pathway
            A Pathway object based on the configuration SBtab

        """
        comp_contrib = comp_contrib or ComponentContribution()

        (
            sbtabdoc,
            S,
            compound_dict,
            reaction_dict,
            standard_dg_primes,
            dg_sigma,
            bounds,
            config_dict,
        ) = cls._read_model_sbtab(filename, comp_contrib)

        # Read the Flux table
        # ---------------------------
        flux_sbtab = sbtabdoc.get_sbtab_by_id("Flux")
        assert flux_sbtab is not None, "Cannot find a 'Flux' table in the SBtab"
        flux_df = flux_sbtab.to_data_frame()

        missing_ids = set(S.columns).difference(flux_df.Reaction)
        assert len(missing_ids) == 0, (
            "Some IDs used in the `Reaction` table are not present in "
            "the `Flux` table: " + ", ".join(missing_ids)
        )

        fluxes = flux_df.set_index("Reaction").loc[S.columns, "Value"].apply(float)

        fluxes = np.array(fluxes.values, ndmin=2, dtype=float).T

        try:
            # convert fluxes to M/s if they are in some other absolute unit
            flux_unit = flux_sbtab.get_attribute("Unit")
            fluxes *= Q_(1.0, flux_unit)
        except SBtab.SBtabError:
            # otherwise, assume these are relative fluxes
            fluxes *= Q_("dimensionless")

        return cls(
            S=S,
            compound_dict=compound_dict,
            reaction_dict=reaction_dict,
            fluxes=fluxes,
            comp_contrib=comp_contrib,
            standard_dg_primes=standard_dg_primes,
            dg_sigma=None,
            bounds=bounds,
            config_dict=config_dict,
        )

    def to_sbtab(self) -> SBtab.SBtabDocument:
        """Export the pathway to an SBtabDocument."""
        sbtabdoc = super(Pathway, self).to_sbtab()

        # add the flux table
        flux_df = pd.DataFrame(
            data=[
                ("rate of reaction", rxn.rid, f"{flux:.3g}")
                for rxn, flux in zip(self.reactions, self.fluxes.magnitude)
            ],
            columns=["!QuantityType", "!Reaction", "!Value"],
        )
        flux_sbtab = SBtab.SBtabTable.from_data_frame(
            df=flux_df, table_id="Flux", table_type="Quantity"
        )
        flux_sbtab.change_attribute("Unit", self.fluxes.units)
        sbtabdoc.add_sbtab(flux_sbtab)

        return sbtabdoc
