from enum import Enum

APP_NAME = "Optimization Problem Inspector"
"""Optimization Problem Inspector app name
"""

REFERENCE_BBOB_NAMES = {
    1: "Sphere",
    7: "StepEllipsoidal",
    12: "BentCigar",
    15: "Rastrigin",
    22: "Gallaghers",
}
"""Human-understandable names for the reference BBOB functions.

**DEPRECATED**: to be removed in next release.
"""


class TEXT(str, Enum):
    """All strings to use within the Optimization Problem Inspector
    application
    """

    APP_NAME = "Optimization Problem Inspector"
    APP_ACRONYM = "OPI"
    SEC_PROBLEM_SPECIFICATION = "Problem Specification"
    SEC_SAMPLE_GENERATION = "Sample Generation"
    SEC_SAMPLE_GENERATION_PARAMETERS = "Sample generation parameters"
    SEC_SAMPLE_GENERATION_METHOD = "Sample generation method"
    SEC_SAMPLE_GENERATION_PARAM_N = "Sample size"
    SEC_SAMPLE_GENERATION_WARNING = (
        "Warning! Sobol sampler and Latin Hypercube Sampler (LHSSampler)"
        " are not compatible with non-continuous or non-real parameters."
        " The sampling on problems with steps, integer parameters,"
        " or categorical parameters may produce wrong results or the results"
        " may not be as expected."
    )
    SAMPLE_GENERATION_BUTTON = "Generate sample and download"
    SEC_DATA = "Data"
    SEC_REFERENCE_PROBLEMS = "Comparison to Reference Problems"
    SEC_REF_FEATURES_SELECT = "Features to compute"
    SEC_REF_FEATURES_PARAMETERS = "Features parameters"
    SEC_REF_FEATURES_PLOT = "Compute and visualize features"
    REF_PROBLEM_TABLE_NAME = "Feature values table"
    REF_PROBLEM_THIS_PROBLEM_NAME = "This problem"
    REF_PROBLEM_DEFINITIONS_LABEL = "Reference problem definitions"
    REF_PROBLEM_TABLE_PROBLEM_NAME = "Problem name"
    REF_PROBLEM_TABLE_FEATURE_NAME = "Feature name"
    REF_PROBLEM_TABLE_FEATURE_VALUE = "Feature value"
    SEC_VIZUALIZATION = "Data Visualization"
    SEC_VIZUALIZATION_DIMENSION_SELECT = "Dimensions to plot"
    SEC_VIZUALIZATION_SPECIFICATION = "Plot options"
    SEC_VIZUALIZATION_PLOT = "Visualize"
    SEC_HELP = "Help"
    FOOTNOTE = (
        "Optimization Problem Inspector, &copy;"
        ' "Jožef Stefan" Institute,'
        "Department of Intelligent Systems, 2023"
    )
    DRAG_AND_DROP_OR_SELECT_FILES = "Drag and Drop or Select Files"
    DOWNLOAD_FIGURE_AS_HTML_BUTTON = "Download figure as HTML"
    DOWNLOAD_DATA_AS_CSV_BUTTON = "Download data as csv"
