from typing import Dict, List, Optional, Type, Union

import numpy as np
import pandas as pd
from pflacco.classical_ela_features import calculate_information_content
from pygmo import fast_non_dominated_sorting

# from pflacco.sampling import create_initial_sample
from scipy.spatial.distance import pdist, squareform

from optimization_problem_inspector import models


class OPIFeature:
    def __init__(
        self,
        variables: Optional[List[str]] = None,
        outputs: Optional[List[str]] = None,
        objectives: Optional[List[str]] = None,
        constraints: Optional[List[str]] = None,
        naming_pattern: str = "OPIFeature_short",
        naming_pattern_long: str = "OPIFeature_long",
        *args,
        **kwargs,
    ) -> None:
        self.variables = variables
        self.outputs = outputs
        self.objectives = objectives
        self.constraints = constraints

        self._short_to_long_names = {}
        raise NotImplementedError

    @classmethod
    def accepted_types(cls):
        return {
            models.ParameterGroup.VARIABLES: (models.Parameter,),
            models.ParameterGroup.OUTPUTS: (models.Parameter,),
            models.ParameterGroup.OBJECTIVES: (models.Parameter,),
            models.ParameterGroup.CONSTRAINTS: (models.Parameter,),
        }

    @property
    def short_to_long_names(self):
        return getattr(self, "_short_to_long_names", {})

    def compute(
        self, df: pd.DataFrame, **kwargs
    ) -> Union[Dict[str, float], pd.Series]:
        raise NotImplementedError


class CorrObj(OPIFeature):
    """Correlation of objectives. Use with numerical objectives problem."""

    def __init__(
        self,
        objectives: List[str],
        naming_pattern="corr__{o1}__vs__{o2}",
        naming_pattern_long="Objective correlation {o1} vs {o2}",
        *args,
        **kwargs,
    ) -> None:
        self.objectives = objectives
        self.naming_pattern = naming_pattern
        self.naming_pattern_long = naming_pattern_long

        self._short_to_long_names = {}

    @classmethod
    def accepted_types(cls):
        return {
            **super().accepted_types(),
            models.ParameterGroup.OBJECTIVES: (
                models.ParameterReal,
                models.ParameterInt,
            ),
        }

    def compute(self, df: pd.DataFrame, **kwargs) -> Dict[str, float]:
        feats = {}

        corrs = df[self.objectives].corr()

        for i, o1 in enumerate(self.objectives):
            for _, o2 in enumerate(self.objectives[i:]):
                if o1 == o2:
                    continue
                short_name = self.naming_pattern.format(o1=o1, o2=o2)
                feats[short_name] = corrs.loc[o1, o2]
                self._short_to_long_names[
                    short_name
                ] = self.naming_pattern_long.format(o1=o1, o2=o2)
        return feats


class MinCV(OPIFeature):
    """Minimum constraint violation. Use with numerical constraints problem."""

    def __init__(
        self,
        objectives: List[str],
        constraints: List[str],
        naming_pattern="minCV",
        naming_pattern_long="Minimum constraint violation",
        *args,
        **kwargs,
    ) -> None:
        self.objectives = objectives
        self.constraints = constraints
        self.naming_pattern = naming_pattern
        self._short_to_long_names = {naming_pattern: naming_pattern_long}

    @classmethod
    def accepted_types(cls):
        return {
            **super().accepted_types(),
            models.ParameterGroup.OBJECTIVES: (
                models.ParameterReal,
                models.ParameterInt,
            ),
        }

    def compute(self, df: pd.DataFrame, **kwargs) -> Dict[str, float]:
        feats = {}

        minCV = df[self.constraints].min().min()

        feats[self.naming_pattern] = minCV

        return feats


class FR(OPIFeature):
    """Feasibility ratio. Use with numerical constraints problem."""

    def __init__(
        self,
        objectives: List[str],
        constraints: List[str],
        naming_pattern="FR",
        naming_pattern_long="Feasibility ratio",
        *args,
        **kwargs,
    ) -> None:
        self.objectives = objectives
        self.constraints = constraints
        self.naming_pattern = naming_pattern
        self._short_to_long_names = {naming_pattern: naming_pattern_long}

    @classmethod
    def accepted_types(cls):
        return {
            **super().accepted_types(),
            models.ParameterGroup.OBJECTIVES: (
                models.ParameterReal,
                models.ParameterInt,
            ),
        }

    def compute(self, df: pd.DataFrame, **kwargs) -> Dict[str, float]:
        feats = {}

        FR = df[df[self.constraints].le(0).all(1)]

        feats[self.naming_pattern] = len(FR) / len(df)

        return feats


class UPO_N(OPIFeature):
    def __init__(
        self,
        objectives: List[str],
        constraints: List[str],
        naming_pattern="UPO_N",
        naming_pattern_long="UPO_N",  # TODO: better name
        *args,
        **kwargs,
    ) -> None:
        self.objectives = objectives
        self.constraints = constraints
        self.naming_pattern = naming_pattern
        self._short_to_long_names = {naming_pattern: naming_pattern_long}

    @classmethod
    def accepted_types(cls):
        return {
            **super().accepted_types(),
            models.ParameterGroup.OBJECTIVES: (
                models.ParameterReal,
                models.ParameterInt,
            ),
        }

    def compute(self, df: pd.DataFrame, **kwargs) -> Dict[str, float]:
        feats = {}
        ndf, dl, dc, ndl = fast_non_dominated_sorting(df[self.objectives])
        feats[self.naming_pattern] = sum(ndl == 0) / len(ndl)
        return feats


class PO_N(OPIFeature):
    def __init__(
        self,
        objectives: List[str],
        constraints: List[str],
        naming_pattern="PO_N",
        naming_pattern_long="PO_N",  # TODO: better name
        *args,
        **kwargs,
    ) -> None:
        self.objectives = objectives
        self.constraints = constraints
        self.naming_pattern = naming_pattern
        self._short_to_long_names = {naming_pattern: naming_pattern_long}

    @classmethod
    def accepted_types(cls):
        return {
            **super().accepted_types(),
            models.ParameterGroup.OBJECTIVES: (
                models.ParameterReal,
                models.ParameterInt,
            ),
        }

    def compute(self, df: pd.DataFrame, **kwargs) -> Dict[str, float]:
        feats = {}

        tmp = df[self.objectives]
        if len(self.constraints) > 0:
            constraint_sums = (
                df[self.constraints].applymap(lambda x: max(0, x)).sum(axis=1)
            )
            tmp = df.loc[constraint_sums == 0, self.objectives]

        ndf, dl, dc, ndl = fast_non_dominated_sorting(tmp)
        feats[self.naming_pattern] = sum(ndl == 0) / len(df)

        return feats

    def compare_sols(self, x, y):
        x_better = 1
        y_better = 1
        for i in range(len(x)):
            if x[i] > y[i]:
                x_better = 0
            elif x[i] < y[i]:
                y_better = 0
        if x_better == 0 and y_better == 0:  # Solutions are incomparable
            return 0
        if x_better == 1 and y_better == 0:  # Solution x dominates y
            return 1
        if x_better == 0 and y_better == 1:  # Solution y dominates x
            return -1


class neighbourhood_feats(OPIFeature):
    def __init__(
        self,
        objectives: List[str],
        constraints: List[str],
        variables: List[str],
        naming_pattern="neighbourhood_feats",
        number_neighbours: int = 10,
        *args,
        **kwargs,
    ) -> None:
        self.objectives = objectives
        self.constraints = constraints
        self.variables = variables
        self.naming_pattern = naming_pattern
        self.number_neighbours = number_neighbours

    @classmethod
    def accepted_types(cls):
        return {
            **super().accepted_types(),
            models.ParameterGroup.OBJECTIVES: (
                models.ParameterReal,
                models.ParameterInt,
            ),
        }

    def compute(self, df: pd.DataFrame, **kwargs) -> Dict[str, float]:
        feats = {}

        df["feasible_sols"] = df[self.constraints].sum(axis=1)
        df[df["feasible_sols"] > 0] = 1

        distances_decision_space = squareform(
            pdist(df[self.variables].values, metric="euclidean")
        )
        distances_objective_space = squareform(
            pdist(df[self.objectives].values, metric="euclidean")
        )
        distances_constraint_space = squareform(
            pdist(df[self.constraints].values, metric="euclidean")
        )
        dist_f_avg_rws = 0
        dist_c_avg_rws = 0
        sup_avg_rws = 0
        inf_avg_rws = 0
        inc_avg_rws = 0
        ind_avg_rws = 0

        comparing_boundry_crossings = []
        for i in range(len(distances_decision_space)):
            neighbour_idxs = np.argsort(distances_decision_space[i, :])[
                1 : self.number_neighbours + 1  # noqa E203
            ]
            dist_f_avg_rws += np.average(
                distances_objective_space[i, neighbour_idxs]
            )
            dist_c_avg_rws += np.average(
                distances_constraint_space[i, neighbour_idxs]
            )
            comparing_neighbours = []
            for j in neighbour_idxs:
                comparing_neighbours.append(
                    self.compare_sols(
                        df[self.objectives].iloc[i, :],
                        df[self.objectives].iloc[j, :],
                    )
                )
            comparing_boundry_crossings.append(
                df["feasible_sols"][i]
                == df["feasible_sols"][neighbour_idxs[0]]
            )
            comparing_neighbours = np.array(comparing_neighbours)
            sup_avg_rws += (comparing_neighbours == -1).sum()
            inf_avg_rws += (comparing_neighbours == 1).sum()
            inc_avg_rws += (comparing_neighbours == 0).sum()
            if (comparing_neighbours == -1).sum() == 0:
                ind_avg_rws += 1

        feats["dist_f_avg_rws"] = dist_f_avg_rws / len(
            distances_decision_space
        )
        feats["dist_c_avg_rws"] = dist_c_avg_rws / len(
            distances_decision_space
        )
        feats["sup_avg_rws"] = sup_avg_rws / len(distances_decision_space)
        feats["inf_avg_rws"] = inf_avg_rws / len(distances_decision_space)
        feats["inc_avg_rws"] = inc_avg_rws / len(distances_decision_space)
        feats["ind_avg_rws"] = ind_avg_rws / len(distances_decision_space)
        feats["ro_med"] = 1 - np.sum(comparing_boundry_crossings) / len(
            distances_decision_space
        )
        return feats

    def compare_sols(self, x, y):
        x_better = 1
        y_better = 1
        for i in range(len(x)):
            if x[i] > y[i]:
                x_better = 0
            elif x[i] < y[i]:
                y_better = 0
        if x_better == 0 and y_better == 0:  # Solutions are incomparable
            return 0
        if x_better == 1 and y_better == 0:  # Solution x dominates y
            return 1
        if x_better == 0 and y_better == 1:  # Solution y dominates x
            return -1


class constr_obj_corr(OPIFeature):
    def __init__(
        self,
        objectives: List[str],
        constraints: List[str],
        naming_pattern="constr_obj_corr",
        *args,
        **kwargs,
    ) -> None:
        self.objectives = objectives
        self.constraints = constraints
        self.naming_pattern = naming_pattern

    @classmethod
    def accepted_types(cls):
        return {
            **super().accepted_types(),
            models.ParameterGroup.OBJECTIVES: (
                models.ParameterReal,
                models.ParameterInt,
            ),
        }

    def compute(self, df: pd.DataFrame, **kwargs) -> Dict[str, float]:
        feats = {}

        df2 = df[self.objectives]
        df2["constr"] = df[self.constraints].sum(axis=1)

        corrs = df2.corr()

        feats["corr_cobj_min"] = corrs["constr"].min()
        np.fill_diagonal(corrs.values, -2)
        feats["corr_cobj_max"] = corrs["constr"].max()

        return feats


class H_MAX(OPIFeature):
    def __init__(
        self,
        objectives: List[str],
        constraints: List[str],
        variables: List[str],
        naming_pattern="H_MAX",
        *args,
        **kwargs,
    ) -> None:
        self.objectives = objectives
        self.constraints = constraints
        self.variables = variables
        self.naming_pattern = naming_pattern

    @classmethod
    def accepted_types(cls):
        return {
            **super().accepted_types(),
            models.ParameterGroup.OBJECTIVES: (
                models.ParameterReal,
                models.ParameterInt,
            ),
        }

    def compute(self, df: pd.DataFrame, **kwargs) -> Dict[str, float]:
        feats = {}
        for obj in self.objectives:
            feats["h_max_" + obj] = calculate_information_content(
                df[self.variables],
                df[obj],
                ic_sorting="nn",
            )["ic.h_max"]
        return feats


def OPIFeatureFactory(
    opi_feature: Type[OPIFeature],
    problem_spec: models.Spec,
    *args,
    **kwargs,
) -> OPIFeature:
    """Helper factory to generate OPIFeature instance, based on the
    input Optimization problem inspector specification `problem_spec`
    and `opi_feature` class.

    Args:
        opi_feature (Type[opi_feature]): OPIFeature class to use
        problem_spec (models.Spec): Optimization problem inspector
            specification
        *args: Any additional args to pass on to the opi_feature
            initialization method
        **kwargs: Any additional kwargs to pass on to the opi_feature
            initialization method

    Returns:
        OPIFeature: OPIFeature instance for feature computation, adjusted
            to the given problem specification.
    """
    variables = []
    outputs = []
    objectives = []
    constraints = []

    accepted_types = opi_feature.accepted_types()

    for parameter in problem_spec.dataSpec.parameters:
        for pgroup, plist in zip(
            [
                models.ParameterGroup.VARIABLES,
                models.ParameterGroup.OUTPUTS,
                models.ParameterGroup.OBJECTIVES,
                models.ParameterGroup.CONSTRAINTS,
            ],
            [
                variables,
                outputs,
                objectives,
                constraints,
            ],
        ):
            if parameter.parameterGroup == pgroup:
                if isinstance(
                    parameter,
                    accepted_types.get(pgroup, (models.Parameter,)),
                ):
                    plist.append(parameter.name)

    return opi_feature(
        variables=variables,
        outputs=outputs,
        objectives=objectives,
        constraints=constraints,
        *args,
        **kwargs,
    )


FEATURES_LIST = [
    CorrObj,
    MinCV,
    FR,
    UPO_N,
    PO_N,
    neighbourhood_feats,
    constr_obj_corr,
    H_MAX,
]
"""List of registered OPIFeature classes.
"""
