# https://stackoverflow.com/questions/62267544/generate-pydantic-model-from-a-dict
import json
from copy import deepcopy
from io import TextIOWrapper
from typing import Any

import yaml

from .logger import logger
from .models import (
    Data,
    DataSpec,
    ExtraParameterGroup,
    ParameterCategorical,
    ParameterGroup,
    ParameterInt,
    ParameterReal,
    Spec,
    Tag,
)

MODELS = [
    ExtraParameterGroup,
    ParameterGroup,
    ParameterReal,
    ParameterInt,
    ParameterCategorical,
    DataSpec,
    Tag,
    Data,
    Spec,
]
"""Models to use when building the optimization problem inspector
specification
"""

MODEL_NAMES = {
    (klass.__name__[0].lower() + klass.__name__[1:]): klass for klass in MODELS
}
"""Model names to class mapping
"""


def build_model(dict_model: Any, lvl: int = 1) -> Any:
    """Given the dictionary as parsed from yaml or json spec,
    recursively transform the model into such dictionary that
    can be ingested by the Optimization Problem Inspector Spec.

    NOTE: this part is necessary only because we want a more human
    readable version of the dictionary. We could use the built-in
    serialization supported by the pydantic library itself, however,
    there the models are parsed based on the arguments provided.
    We have different models with exact same parameters available,
    which would confuse the pydantic library deserialization.

    Args:
        dict_model (Any): _description_
        lvl (int, optional): What is the current level of recursion.
            Defaults to 1.

    Raises:
        ValueError: Could not parse the input dictionary.

    Returns:
        Any: In the first level of recursion, return the dictionary-serialized
            Optimization Problem Inspector Spec.

    """
    logger.debug(lvl * "++||")
    logger.debug(dict_model)
    output_model = {}

    if isinstance(dict_model, (str, int, float)) or dict_model is None:
        return deepcopy(dict_model)

    for k, v in dict_model.items():
        if k in MODEL_NAMES.keys():
            if MODEL_NAMES[k] == ParameterGroup:
                if isinstance(v, dict):
                    output_model[k] = ExtraParameterGroup(**v)
                else:
                    output_model[k] = getattr(ParameterGroup, v)
            else:
                logger.debug(k, "\t", v)
                if v is None:
                    output_model[k] = MODEL_NAMES[k]()
                else:
                    output_model[k] = MODEL_NAMES[k](
                        **build_model(deepcopy(v), lvl=lvl + 1)
                    )
        elif isinstance(v, (list, tuple)):
            ls = []
            for vi in v:
                ls.append(build_model(deepcopy(vi), lvl=lvl + 1))
            output_model[k] = tuple(ls)

        elif isinstance(v, (str, int, float)) or v is None:
            output_model[k] = deepcopy(v)
        else:
            raise ValueError(f"Field {k}: {v} has invalid syntax")

    # NOTE: this is to catch the list of parameters
    if len(output_model) == 1:
        for mt_name, mv in output_model.items():
            mt = MODEL_NAMES.get(mt_name)
            if mt is not None and isinstance(mv, mt):
                logger.debug(lvl * " ", mt, mv.__class__.__name__, mv)
                return deepcopy(mv)
    logger.debug(lvl * " ", output_model)
    return output_model


def load_spec(file: TextIOWrapper) -> Spec:
    """Load the optimization problem inspector specification
    from the yaml-based file-stream.

    Usage:

    ```python
    with open("opi_spec.yaml", "r") as f:
       load_spec(f)
    ```

    Args:
        file (TextIOWrapper): File handler from the opened file.

    Returns:
        Spec: Optimization problem inspector specification model
    """
    dict_model = yaml.safe_load(file)
    deserialized_kwargs = build_model(dict_model=dict_model)
    if isinstance(deserialized_kwargs, DataSpec):
        deserialized_kwargs = {"dataSpec": deserialized_kwargs}
    return Spec(**deserialized_kwargs)


def dumps_spec(spec: Spec) -> str:
    """Serialize the Optimization problem inspector specification
    model into a yaml string that can be read back and de-serialized
    into specification model again.

    Args:
        spec (Spec): The Optimization problem inspector specification model
            to be serialized.

    Returns:
        str: yaml string, serialized Optimization problem inspector
            specification model.
    """
    spec_dict = json.loads(spec.json())
    parameters = []
    params_spec = spec.dataSpec.parameters
    params_dict = spec_dict.get("dataSpec", {}).get("parameters", [])
    for p_spec, p_dict in zip(params_spec, params_dict):
        p_name = type(p_spec).__name__
        p_name = p_name[0].lower() + p_name[1:]
        parameters.append({p_name: p_dict})

    spec_dict["dataSpec"]["parameters"] = parameters

    return yaml.dump(spec_dict)
