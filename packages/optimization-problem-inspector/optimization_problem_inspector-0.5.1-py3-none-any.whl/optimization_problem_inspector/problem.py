import io
import json
from typing import Callable, Dict, List, Literal, Optional, Type

import pandas as pd
import yaml
from pydantic import BaseModel, validator

from optimization_problem_inspector.coco_interface import GBBOB
from optimization_problem_inspector.config import REFERENCE_BBOB_INDICES
from optimization_problem_inspector.logger import logger
from optimization_problem_inspector.models import (
    DataSpec,
    ExtraParameterGroup,
    ParameterGroup,
    ParameterReal,
    Spec,
)
from optimization_problem_inspector.sampling import (
    OPISampler,
    OPISamplerFactory,
)


class OPIDataProblemError(Exception):
    pass


class ProblemData:
    """Wrapper class to hold Optimization problem inspector problem
    and sample data, belonging to the problem.
    """

    def __init__(self, problem: "Problem", data: pd.DataFrame):
        """Wrapper class to hold Optimization problem inspector problem
        and sample data.

        Note, if data does not contain all the columns, mentioned in the
        problem specification, self.data property will be extended with
        empty columns, to align the data with problem specification.

        Raises:
            OPIDataProblemError: If data and problem specification do not
            align, raise error.

        Args:
            problem (Problem): Optimization problem inspector specification
            data (pd.DataFrame): DataFrame with sample data belonging to
                the specified problem.
        """
        self.problem = problem
        self.data = self._parse_and_validate_data(problem=problem, data=data)

    def _parse_and_validate_data(
        self, problem: "Problem", data: pd.DataFrame
    ) -> pd.DataFrame:
        """Check whether problem specification and data are aligned,
        column-wise. Columns of "VARIABLES" type should be the same,
        other types of columns will be added to data, if not yet present.

        Args:
            problem (Problem): Optimization problem inspector specification
            data (pd.DataFrame): DataFrame with sample data belonging to
                the specified problem.

        Raises:
            OPIDataProblemError: Problem variables not present in the data.
            OPIDataProblemError: Extra columns, not present in specification
                but present in the data.

        Returns:
            pd.DataFrame: Problem data, aligned with problem specification.
        """
        spec_input_columns = [
            p.name
            for p in problem.spec.dataSpec.parameters
            if p.parameterGroup == ParameterGroup.VARIABLES
        ]
        data_columns = data.columns
        spec_input_extra = set(spec_input_columns).difference(
            set(data_columns)
        )
        if spec_input_extra:
            raise OPIDataProblemError(
                "ProblemData cannot be instantiated because"
                " the specification and the data do not match"
                " for the problem variables"
                f" {spec_input_extra = }"
            )

        spec_all_columns = [p.name for p in problem.spec.dataSpec.parameters]
        spec_all_extra = set(spec_all_columns).difference(set(data_columns))
        data_all_extra = set(data_columns).difference(set(spec_all_columns))
        if data_all_extra:
            raise OPIDataProblemError(
                "ProblemData cannot be instantiated because"
                " the specification and the data do not match."
                f" {data_all_extra = }"
            )

        data_all = data[list(set(spec_all_columns).intersection(data_columns))]
        if spec_all_extra:
            data_all = pd.concat(
                [data_all, pd.DataFrame(columns=list(spec_all_extra))]
            )
        return data_all[spec_all_columns]


class Problem:
    """Wrapper class for a Optimization problem inspector problem.
    Can be used as an interface/parent class to implement your own custom
    problems.
    """

    def __init__(
        self,
        name: str,
        specification: Spec,
        eval_function: Optional[Callable] = None,
    ):
        """Optimization problem inspector problem class.

        Args:
            name (str): Name of the problem
            specification (Spec): Optimization problem inspector specification
            eval_function (Optional[Callable], optional): Evaluation function
                that can take in the pd.DataFrame sample input and generate
                outputs. Defaults to None, meaning no evaluations are done,
                when retrieving a problem sample.
        """
        self.name = name
        self.spec = specification
        self.eval_function = eval_function

    def make_sampler(
        self, sampler: Type[OPISampler], sampler_kwargs: Optional[Dict] = None
    ):
        """Helper method to generate a OPISampler instance
        for the given problem.

        Args:
            sampler (Type[OPISampler]): OPISampler class to use for sampling
            sampler_kwargs (_type_, optional): Any additional arguments
                to pass on to OPISamplerFactory. Defaults to None and is
                converted to empty dictionary.

        Returns:
            _type_: _description_
        """
        if sampler_kwargs is None:
            sampler_kwargs = {}
        return OPISamplerFactory(sampler, self.spec, **sampler_kwargs)

    def evaluate(self, sample: pd.DataFrame) -> pd.DataFrame:
        """Evaluate the given sample using self.eval_function.

        Args:
            sample (pd.DataFrame): Input data to evaluate.

        Raises:
            NotImplementedError: Evaluation function is not implemented.

        Returns:
            pd.DataFrame: Evaluation output.
        """
        if self.eval_function is not None:
            return self.eval_function(sample)
        raise NotImplementedError

    def get_problem_sample(
        self,
        sampler: Type[OPISampler],
        N: int,
        sampler_kwargs: Optional[Dict] = None,
    ) -> ProblemData:
        """Generate a problem sample, already evaluated if the eval_function
        was given.

        Args:
            sampler (Type[OPISampler]): OPISampler class to use for sampling.
            N (int): Number of samples to generate.
            sampler_kwargs (Optional[Dict], optional): Additional arguments
                to pass to the sampler instance generation. Defaults to None.

        Returns:
            ProblemData: Problem and evaluated data, wrapped into ProblemData
        """
        sample = self.make_sampler(
            sampler=sampler, sampler_kwargs=sampler_kwargs
        ).sample(N=N)
        try:
            sample = self.evaluate(sample)
        except NotImplementedError:
            pass
        return ProblemData(
            self,
            sample,
        )


# Reference problem-related classes
class GBBOBFunctionInstance(BaseModel):
    """Parameters that define s single GBBOB function instance.

    Args:
        f (int): GBBOB function id.
        i (int): GBBOB function instance.
    """

    f: int
    i: int


class GBBOBDefinition(BaseModel):
    """Model to define a single GBBOB problem.

    Args:
        dimensions (List[GBBOBFunctionInstance]):
            Dimension of the GBBOB problem.
        objectives (List[GBBOBFunctionInstance]):
            A list of functions instances used as objectives.
        ineq_const (List[GBBOBFunctionInstance]):
            A list of functions instances used as inequality constraints.
        feasibility_degree (float): Number indicating desired approximate
            share of feasible solutions.
        feasibility_sample_size (int): Whole number indicating the sample
            size to take when estimating feasibility.
    """

    dimensions: int
    objectives: List[GBBOBFunctionInstance]
    ineq_const: List[GBBOBFunctionInstance] | None
    feasibility_degree: float
    feasibility_sample_size: int


class GBBOBDefinitions(BaseModel):
    """Model that holds definitions of GBBOB reference problems

    Raises:
        ValueError: Validation errors upon mismatching dimensions
            of inputs, objectives and inequalities.
    """

    gbbob_definitions: List[GBBOBDefinition]

    @validator("gbbob_definitions", check_fields=False, always=True)
    def check_dimensions(cls, gbbob_definitions: List[GBBOBDefinition]):
        dimension_val = None
        objectives_len = None
        ineq_const_len = None
        for gbbob_defn in gbbob_definitions:
            if dimension_val is None:
                dimension_val = gbbob_defn.dimensions
            if objectives_len is None:
                objectives_len = len(gbbob_defn.objectives)
            if ineq_const_len is None:
                ineq_const_len = len(gbbob_defn.ineq_const or [])

            if dimension_val != gbbob_defn.dimensions:
                raise ValueError(
                    f"dimension_val ({dimension_val}) !="
                    f" gbbob_defn.dimensions ({gbbob_defn.dimensions})"
                )
            if objectives_len != (defn_obj_len := len(gbbob_defn.objectives)):
                raise ValueError(
                    f"objectives_len ({objectives_len}) !="
                    f" gbbob_defn.dimensions ({defn_obj_len})"
                )
            if ineq_const_len != (
                defn_ineq_const := len(gbbob_defn.ineq_const or [])
            ):
                raise ValueError(
                    f"ineq_const_len ({ineq_const_len}) !="
                    f" gbbob_defn.dimensions ({defn_ineq_const})"
                )

        return gbbob_definitions


def make_simple_gbbob_defn(
    dimensions: int, objectives: int, fi: int, constraints=1, instance_offset=0
) -> GBBOBDefinition:
    """Given some basic information, build a GBBOBDefinition, where
    objectives and constraints are composed of the same BBOB function index,
    using only function instance to vary the functions.

    Args:
        dimensions (int): Number of input variables.
        objectives (int): Number of objectives.
        fi (int): Function index from BBOB used to build objective
            and constraint functions.
        constraints (int, optional): Number of constraints.
            Defaults to 1.
        instance_offset (int, optional): Function instance offset.
            Defaults to 0.

    Returns:
        GBBOBDefinition: GBBOBDefinition for a simplified GBBOB problem.
    """
    obj_instance_offset = instance_offset + 1
    objs = [
        GBBOBFunctionInstance(f=fi, i=i + obj_instance_offset)
        for i in range(objectives)
    ]
    ineq_instance_offset = instance_offset + 1 + len(objs)
    ineq_const = [
        GBBOBFunctionInstance(f=fi, i=i + ineq_instance_offset)
        for i in range(constraints)
    ]
    feas_degree = 0.5
    feas_n_samples = 100
    return GBBOBDefinition(
        dimensions=dimensions,
        objectives=objs,
        ineq_const=ineq_const,
        feasibility_degree=feas_degree,
        feasibility_sample_size=feas_n_samples,
    )


def GBBOBProblemFactory(
    gbbob_definition: GBBOBDefinition,
) -> Problem:
    """Generate Optimization problem inspector Problem from
    GBBOBDefinition.

    Args:
        gbbob_definition (GBBOBDefinition): Definition of the GBBOB problem.

    Returns:
        Problem: GBBOB-based Optimization problem inspector Problem
    """
    gbbob_definition_dict = gbbob_definition.dict()
    ineq_const = gbbob_definition_dict.get("ineq_const")
    objs = gbbob_definition_dict.get("objectives")
    if objs is None:
        raise ValueError("gbbob_definition.objectives cannot be None")
    general_bbob = GBBOB(
        n_var=gbbob_definition.dimensions,
        objs=objs,
        ineq_const=ineq_const,
        feas_degree=gbbob_definition.feasibility_degree,
        feas_n_samples=gbbob_definition.feasibility_sample_size,
    )

    input_params = []
    input_names = []
    # TODO: most likely
    for problem in general_bbob.fn:
        for i, (lb, ub) in enumerate(
            zip(problem.lower_bounds, problem.upper_bounds)
        ):
            input_name = f"x_{i+1}"
            input_names.append(input_name)
            input_params.append(
                ParameterReal(
                    name=input_name,
                    parameterGroup=ParameterGroup.VARIABLES,
                    lower_bound=lb,
                    upper_bound=ub,
                )
            )
        break

    objective_name = "F"
    objectives_params = [
        ParameterReal(
            name=f"{objective_name}_{i+1}",
            parameterGroup=ParameterGroup.OBJECTIVES,
        )
        for i, _ in enumerate(objs)
    ]

    constraint_name = "G"
    constraint_params = []
    if ineq_const:
        constraint_params = [
            ParameterReal(
                name=f"{constraint_name}_{i+1}",
                parameterGroup=ParameterGroup.CONSTRAINTS,
            )
            for i, _ in enumerate(ineq_const)
        ]

    extra_name = "V"
    extra_params = []
    if ineq_const:
        extra_params = [
            ParameterReal(
                name=f"{extra_name}",
                parameterGroup=ExtraParameterGroup(name="TOTAL_CONSTRAINT"),
            )
        ]

    specs = Spec(
        version="2022-12-15",
        dataSpec=DataSpec(
            parameters=input_params
            + objectives_params
            + constraint_params
            + extra_params
        ),
    )

    def eval_func(df: pd.DataFrame) -> pd.DataFrame:
        """Evaluate samples in df, taking into account the format
        of GBBOB.evaluate.

        Args:
            df (pd.DataFrame): Samples to evaluate

        Returns:
            pd.DataFrame: _description_
        """
        logger.debug(f"Evaluating {general_bbob.name}")
        output = general_bbob.evaluate(df[input_names].values)
        all_data = []
        if objectives_params:
            objectives = pd.DataFrame(
                output["F"].T, columns=[p.name for p in objectives_params]
            )
            all_data.append(objectives)
        if constraint_params:
            constraints = pd.DataFrame(
                output["G"].T, columns=[p.name for p in constraint_params]
            )
            all_data.append(constraints)
        if extra_params:
            extra = pd.DataFrame(
                output["V"].T, columns=[p.name for p in extra_params]
            )
            all_data.append(extra)

        return pd.concat([df, *all_data], axis="columns")

    return Problem(
        name=general_bbob.name, specification=specs, eval_function=eval_func
    )


class ReferenceProblemsGBBOB:
    """Helper object for defining a set of GBBOB reference problems."""

    def __init__(self, gbbob_definitions: GBBOBDefinitions):
        """Construct a set of GBBOB reference problems from the given
        GBBOBDefinitions object.

        Args:
            gbbob_definitions (GBBOBDefinitions): Containing a list of
                GBBOB definitions, where each uniquely specifies a
                GBBOB problem.
        """
        self.gbbob_definitions = gbbob_definitions
        self.problem_factories = [
            GBBOBProblemFactory(gbbob_definition=gbbob_definition)
            for gbbob_definition in gbbob_definitions.gbbob_definitions
        ]

    def __repr__(self) -> str:
        problems = [pf.name for pf in self.problem_factories]
        return f"ReferenceProblemsGBBOB(problem_factories={problems})"

    def __str__(self) -> str:
        return self.__repr__()

    def get_problem_samples(
        self,
        sampler: Type[OPISampler],
        N: int,
        sampler_kwargs: Optional[Dict] = None,
    ) -> List[ProblemData]:
        """Get problem samples for each GBBOB problem within the
        ReferenceProblemsGBBOB collection.

        Args:
            sampler (Type[OPISampler]): Sampler to use
            N (int): Sample size
            sampler_kwargs (Optional[Dict], optional): Any additional
                arguments to pass on to sampler. Defaults to None.

        Returns:
            List[ProblemData]: List of ProblemData, with positions
                aligned with the specified GBBOBProblems.
        """
        self.problem_samples = [
            pf.get_problem_sample(
                sampler=sampler, N=N, sampler_kwargs=sampler_kwargs
            )
            for pf in self.problem_factories
        ]
        return self.problem_samples

    @classmethod
    def from_simple_input(
        cls,
        dimensions: int,
        objectives: int,
        constraints: int = 1,
        function_indices: List[int] = REFERENCE_BBOB_INDICES,
    ) -> "ReferenceProblemsGBBOB":
        """Construct the reference problems set from basic problem information

        Args:
            dimensions (int): Number of variables.
            objectives (int): Number of objectives
            constraints (int, optional): Number of constraints. Defaults to 1.
            function_indices (List[int], optional): A list of function indices
                to use when constructing objective and constraint functions.
                Defaults to REFERENCE_BBOB_INDICES.

        Returns:
            ReferenceProblemsGBBOB: A collection of GBBOB reference problems.
        """
        gbbob_definitions = GBBOBDefinitions(
            gbbob_definitions=[
                make_simple_gbbob_defn(
                    dimensions=dimensions,
                    objectives=objectives,
                    fi=fi,
                    constraints=constraints,
                )
                for fi in function_indices
            ]
        )
        return cls(gbbob_definitions)

    def dumps(self, format: Literal["json", "yaml"] = "yaml") -> str:
        """Serialize the reference problem definition.

        Args:
            format (Literal["json", "yaml"], optional): What output format
                to use. Defaults to "yaml".

        Returns:
            str: Serialized GBBOB reference problems collection.
        """
        serialized_dict = {
            "ReferenceProblemsGBBOB": {**self.gbbob_definitions.dict()}
        }
        dumper_map = {
            "yaml": yaml.dump,
            "json": json.dumps,
        }
        return dumper_map[format](serialized_dict)

    @classmethod
    def loads(
        cls, data: str, format: Literal["json", "yaml"] = "yaml"
    ) -> "ReferenceProblemsGBBOB":
        """Deserialize the data back into the ReferenceProblemsGBBOB object.

        Args:
            data (str): The contents of the serialized reference problems.
            format (str, optional): Serialization format. Defaults to "yaml".

        Raises:
            ValueError: Unknown format.
            ValueError: The content cannot be deserialized.
                Specification error?

        Returns:
            ReferenceProblemsGBBOB:  collection of GBBOB reference problems.
        """
        if format == "yaml":
            with io.StringIO(data) as f:
                specs = yaml.safe_load(f)
        elif format == "json":
            specs = json.loads(data)
        else:
            raise ValueError(
                f"Format '{format}' not recognized. Use 'yaml' or 'json'."
            )
        definitions = specs.get("ReferenceProblemsGBBOB")
        if definitions is None:
            raise ValueError(
                f"Cannot load the {cls.__name__} from specs = \n{specs}"
            )

        return cls(GBBOBDefinitions.parse_obj(definitions))
