"""thermo_models contains tools for running MDF and displaying results."""

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
import logging
from typing import Iterable, List, Optional, Tuple, Union

import cvxpy as cp
import numpy as np
import pandas as pd
from cvxpy.constraints.constraint import Constraint
from equilibrator_api import R, default_T
from scipy import stats

from .analysis_solution import PathwayAnalysisSolution
from .mdmc_solution import PathwayMdmcSolution
from .pathway import Pathway


class ThermodynamicModel(Pathway):
    """Container for doing pathway-level thermodynamic analysis."""

    def __init__(self, **kwargs) -> None:
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
            relative fluxes in same order as
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
        super(ThermodynamicModel, self).__init__(**kwargs)
        self._solver = self.config_dict.get("solver", "CLARABEL").upper()
        assert (
            self._solver in cp.installed_solvers()
        ), f"Solver `{self._solver}` is not installed"

    def _thermo_constraints(
        self,
        ln_conc: cp.Variable,
        slack: cp.Variable,
    ) -> Tuple[cp.Variable, List[cp.Constraint], List[cp.Constraint]]:
        """Create primal LP problem for Min-max Thermodynamic Driving Force.

        Parameters
        ----------
        ln_conc : cp.Variable
            a vector of CVXPY variables representing the log concentrations

        slack : cp.Variable
            a scalar CVXPY variable representing the driving-force slack
            (usually denoted B)

        Returns
        -------
        (covariance eigen-variables, covariance constraints, and second-law constraints)
        """

        _rt = (R * default_T).m_as("kJ/mol")
        dg_prime = (
            self.standard_dg_primes.m_as("kJ/mol") + _rt * self.S.T.values @ ln_conc
        )

        if self.dg_sigma is not None and self.dg_confidence > 0.0:
            # define the ΔG'0 covariance eigen-variables
            Nq = self.dg_sigma.shape[1]
            y = cp.Variable(shape=Nq, name="covariance eigenvalues")
            y_constraints = [
                cp.norm2(y) <= stats.chi2.ppf(self.dg_confidence, Nq) ** (0.5)
            ]
            dg_prime += self.dg_sigma.m_as("kJ/mol") @ y
        else:
            # when the covariance is not provided, or the confidence interval
            # is 0.0 (which means we only allow the exact mean values as possible
            # assignments to ΔG'0), we still add need to a placeholder variable
            # named 'y' (otherwise the solver raises an exception).
            y = None
            y_constraints = []

        dg_constraints = []
        for i, direction in enumerate(np.diag(self.I_dir)):
            if direction != 0:
                dg_constraints += [direction * dg_prime[i] <= -slack]
            else:
                dg_constraints += [direction * dg_prime[i] <= 1]  # placeholder

        return y, y_constraints, dg_constraints

    def _conc_constraints(
        self,
        ln_conc: cp.Variable,
        constant_only: bool = False,
    ) -> Tuple[List[Constraint], List[Constraint]]:
        """Add lower and upper bounds for the log concentrations.

        Arguments
        ---------
        ln_conc : cp.Variable
            the log-concentration variable, size should be (self.Nc, )
        constant_only : bool
            if True, only add bounds to the "constant" compounds, i.e. ones
            with 0 standard deviation
        """
        c_lbs = []
        c_ubs = []
        for j in range(self.Nc):
            if constant_only and self.ln_conc_sigma[j] > self.MINIMAL_STDEV:
                continue
            ci = self.ln_conc_sigma[j] * stats.chi2.ppf(self.ln_conc_confidence, 1) ** (
                0.5
            )
            lb = self.ln_conc_mu[j] - ci
            ub = self.ln_conc_mu[j] + ci
            c_lbs += [ln_conc[j] >= lb]
            c_ubs += [ln_conc[j] <= ub]
        return c_lbs, c_ubs

    @staticmethod
    def dual_value_to_float(x: Union[np.ndarray, float]) -> float:
        """Convert daul_values (which can be both arrays or floats) to a float."""
        if isinstance(x, np.ndarray):
            return float(x.item())
        elif isinstance(x, float):
            return x
        else:
            raise ValueError(
                "Input to `dual_value_to_float` must be a NumPy array or a float"
            )

    def mdf_analysis(self) -> PathwayAnalysisSolution:
        """Find the MDF (Max-min Driving Force).

        Returns
        -------
        a PathwayMDFData object with the results of MDF analysis.
        """
        from .mdf_solution import PathwayMdfSolution

        # ln-concentration variables (where the units are in M before taking
        # the log)
        ln_conc = cp.Variable(shape=self.Nc, name="log concentrations")
        c_lbs, c_ubs = self._conc_constraints(ln_conc)

        # the margin variable representing the MDF in units of kJ/mol
        B = cp.Variable(shape=1, name="minimum driving force")
        y, y_constraints, dg_constraints = self._thermo_constraints(ln_conc, B)

        objective = cp.Maximize(B)

        prob = cp.Problem(objective, y_constraints + dg_constraints + c_lbs + c_ubs)
        prob.solve(self._solver)
        if prob.status != "optimal":
            logging.warning("LP status %s", prob.status)
            raise Exception("Cannot solve MDF optimization problem")

        reaction_prices = np.array(
            [
                ThermodynamicModel.dual_value_to_float(c.dual_value)
                for c in dg_constraints
            ]
        ).round(5)
        compound_prices = np.array(
            [
                ThermodynamicModel.dual_value_to_float(upper.dual_value)
                - ThermodynamicModel.dual_value_to_float(lower.dual_value)
                for lower, upper in zip(c_lbs, c_ubs)
            ]
        ).round(5)

        return PathwayMdfSolution(
            self,
            score=prob.value,
            ln_conc=ln_conc.value,
            y=y.value if y is not None else None,
            reaction_prices=reaction_prices,
            compound_prices=compound_prices,
        )

    def get_zscores(self, ln_conc: Union[cp.Variable, Iterable]) -> Iterable:
        """Get the Z-scores for all the log-concentrations."""
        return map(
            lambda x: (x[0] - x[1]) / x[2] if x[2] > self.MINIMAL_STDEV else 0,
            zip(ln_conc, self.ln_conc_mu, self.ln_conc_sigma),
        )

    def mdmc_analysis(
        self,
        min_lb: float = 0.0,
        max_lb: Optional[float] = 10.0,
        n_steps: int = 100,
    ) -> PathwayMdmcSolution:
        """Find the MDMC (Maximum Driving-force and Metabolic Consistency.

        :return: a PathwayMdmcSolution object with the results of MDMC analysis.
        """
        # ln-concentration variables (where the units are in M before taking
        # the log)
        ln_conc = cp.Variable(shape=self.Nc, name="log concentrations")
        c_lbs, c_ubs = self._conc_constraints(ln_conc, constant_only=True)

        # the margin variable representing the MDF in units of kJ/mol
        B = cp.Variable(shape=1, name="minimum driving force")
        y, y_constraints, dg_constraints = self._thermo_constraints(ln_conc, B)

        z_scores = [z**2 for z in self.get_zscores(ln_conc)]
        objective = cp.Minimize(cp.sum(z_scores))

        # scan through a range of DF lower bounds to find all possible Pareto
        # optimal solutions to the bi-optimization problem (MDF and Z-score)
        data = []
        for lb in np.linspace(min_lb, max_lb, n_steps):
            prob = cp.Problem(
                objective,
                y_constraints + dg_constraints + c_lbs + c_ubs + [B >= lb],
            )
            prob.solve(self._solver)
            if prob.status != "optimal":
                logging.warning("LP status %s", prob.status)
                raise Exception("Cannot solve MDF optimization problem")

            data.append((lb, "primal", "obj", "mdmc", 0, prob.value))
            data += [
                (lb, "primal", "var", "log_conc", i, ln_conc.value[i])
                for i in range(self.Nc)
            ]
            if self.dg_sigma is not None:
                Nq = self.dg_sigma.shape[1]
                data += [
                    (
                        lb,
                        "primal",
                        "var",
                        "covariance_eigenvalue",
                        i,
                        y.value[i] if y is not None else None,
                    )
                    for i in range(Nq)
                ]
            data += [
                (
                    lb,
                    "shadow_price",
                    "cnstr",
                    "driving_force",
                    j,
                    ThermodynamicModel.dual_value_to_float(
                        dg_constraints[j].dual_value
                    ),
                )
                for j in range(self.Nr)
            ]
            zscores = self.get_zscores(ln_conc.value)
            for j, zscore in enumerate(zscores):
                data.append((lb, "zscore", "var", "log_conc", j, zscore))

        solution_df = pd.DataFrame(
            data=data,
            columns=[
                "df_lb",
                "value_type",
                "var_type",
                "var_name",
                "index",
                "value",
            ],
        )
        return PathwayMdmcSolution(self, solution_df)
