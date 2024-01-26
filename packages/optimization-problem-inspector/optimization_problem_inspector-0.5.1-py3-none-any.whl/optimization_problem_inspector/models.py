from enum import Enum
from typing import Any, List, Optional, Union

from pydantic import BaseModel, validator

from .logger import logger


class ParameterGroup(str, Enum):
    """Parameter group to classify each parameter"""

    VARIABLES = "VARIABLES"
    OUTPUTS = "OUTPUTS"
    CONSTRAINTS = "CONSTRAINTS"
    OBJECTIVES = "OBJECTIVES"


class ExtraParameterGroup(BaseModel):
    """Additional parameter group for parameters not belonging to any
    ParameterGroup

    Args:
        name (str): Name of the extra parameter group.
    """

    name: str


class Parameter(BaseModel):
    """Single problem parameter

    Args:
        name (str): Name of the parameter.
        parameterGroup (Union[ExtraParameterGroup, ParameterGroup]):
            Parameer group to which the parameter belongs.
    """

    name: str
    parameterGroup: Union[ExtraParameterGroup, ParameterGroup]


class ParameterCategorical(Parameter):
    """Object for describing categorical parameter

    Args:
        values (List[Any]): Definition of possible values the categorical
            parameter can assume.
    """

    values: List[Any]


class BoundedParameter(Parameter):
    """Object for describing bounded numerical parameter

    Args:
        lower_bound (Optional[Any]): Lower bound for the bounded
            numerical parameter.
        upper_bound (Optional[Any]): Upper bound for the bounded
            numerical parameter.
        step (Optional[Any]): Step size for the bounded numerical
            parameter that can only assume certain values.
    """

    # TODO: add the checks to ParameterInd and ParameterReal
    lower_bound: Optional[Any]
    upper_bound: Optional[Any]
    step: Optional[Any]

    @validator("upper_bound", always=True, check_fields=False)
    def check_bounds_if_variable(cls, ub, values, **kwargs):
        values.get("name")
        pg = values.get("parameterGroup")
        lb = values.get("lower_bound")
        # ub = values.get("upper_bound")

        logger.debug(f"{lb = }, {ub = }, {pg = }")
        if pg == ParameterGroup.VARIABLES:
            if lb is None or ub is None:
                raise ValueError(
                    "lower_bound and upper_bound cannot be None"
                    " when parameterGroup = 'VARIABLES'"
                )
        return ub

    @validator("step", check_fields=False, always=True)
    def check_step_ge_zero_or_none(cls, v):
        if v is not None and v < 0:
            raise ValueError(f"`step` should be >= 0 or None, not {v}")

        return v


class ParameterReal(BoundedParameter):
    """Object for describing real/float parameter

    Args:
        lower_bound (Optional[Any]): Lower bound for the bounded
            numerical parameter.
        upper_bound (Optional[Any]): Upper bound for the bounded
            numerical parameter.
        step (Optional[Any]): Step size for the bounded numerical
            parameter that can only assume certain values.
    """

    lower_bound: Optional[float] = None
    upper_bound: Optional[float] = None
    step: Optional[float] = None


class ParameterInt(Parameter):
    """Object for describing integer parameter

    Args:
        lower_bound (Optional[Any]): Lower bound for the bounded
            numerical parameter.
        upper_bound (Optional[Any]): Upper bound for the bounded
            numerical parameter.
        step (Optional[Any]): Step size for the bounded numerical
            parameter that can only assume certain values.
    """

    lower_bound: Optional[int] = None
    upper_bound: Optional[int] = None
    step: Optional[int] = 1


class DataSpec(BaseModel):
    """Optimization problem inspector data columns specification

    Args:
        parameters (List[Parameter]): __description__.
    """

    parameters: List[Parameter]


class Tag(BaseModel):
    """Optimization problem inspector tag

    Args:
        name (str): Tag name.
        value (str): Tag value.
    """

    name: str
    value: str


class Data(BaseModel):
    """Optimization problem inspector data

    Args:
        filename (Optional[str]): Name of the file containing the data.
    """

    filename: Optional[str] = None


class Spec(BaseModel):
    """Optimization problem inspector specification

    Args:
        version (str): __description__.
        dataSpec (DataSpec): __description__.
        data (Optional[Data]): __description__. Defaults to None.
        tags (Optional[List[Tag]]): __description__. Defaults to None.
    """

    version: str
    dataSpec: DataSpec
    data: Optional[Data] = None
    tags: Optional[List[Tag]] = None

    def get_columns(self) -> List[str]:
        """Get a full list of parameters.

        Returns:
            List[str]: List of parameters
        """
        return [param.name for param in self.dataSpec.parameters]
