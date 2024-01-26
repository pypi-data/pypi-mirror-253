import os
import sys


def set_num_threads(nt=1, disp=1):
    """see https://github.com/numbbo/coco/issues/1919
    and https://twitter.com/jeremyphoward/status/1185044752753815552
    """
    try:
        import mkl
    except ImportError:
        disp and print("mkl is not installed")
    else:
        mkl.set_num_threads(nt)
    nt = str(nt)
    for name in [
        "OPENBLAS_NUM_THREADS",
        "NUMEXPR_NUM_THREADS",
        "OMP_NUM_THREADS",
        "MKL_NUM_THREADS",
    ]:
        os.environ[name] = nt
    disp and print("setting mkl threads num to", nt)


if sys.platform.lower() not in ("darwin", "windows"):
    set_num_threads(1)

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
"""Logging level to use
"""

REFERENCE_BBOB_INDICES = [
    1,  # Sphere Function
    7,  # Step Ellipsoidal Function
    12,  # Bent Cigar Function
    15,  # Rastrigin Function
    22,  # Gallagher's Gaussian 21-hi Peaks Function
]
"""Default reference BBOB function indices to use for reference problems.
"""

PLOT_WIDTH_MULTIPLIER = 300
"""When plotting multiple parameters horizontally, this is approximately
the width dedicated to a single parameter.
"""

PLOT_HEIGHT_MULTIPLIER = 150
"""When plotting multiple parameters vertically, this is approximately
the height dedicated to a single parameter.
"""

PLOT_MARGIN = 150
"""Margin when plotting to allow for axis labels and ticks.
"""

PLOT_HEIGHT_STATIC_DEFAULT = 600
"""Default plot height.
"""

FEAT_CALCULATION_TIME_WARN_THRESHOLD_S = 1
"""Threshold in seconds that determines when to log a warning
if the feature computation takes too long.
"""
