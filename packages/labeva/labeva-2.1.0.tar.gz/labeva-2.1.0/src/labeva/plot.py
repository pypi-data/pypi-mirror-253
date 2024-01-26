"""
Apply settings to matplotlib
"""

# %%
from datetime import datetime
from os import makedirs
from os import path

import matplotlib as mpl
import matplotlib.pyplot as plt


# %%
# === SETTINGS ===
PLOTTING = True
"""Enabe or disable plotting. to be used like `if PLOTTING: ...`"""
FASTRUN = False
"""Can be used to check whether to take smaller data sets to test code faster"""

# %%
FIGURE_COLOR = "tab:blue"
"""Default color"""
FIGURE_SAVE = True
"""Whether `figure_save()` saves the figures"""
FIGURE_DIR_SUBDIR = "fig"
"""Subdirectory of working directory to save figures in + timestamp (if not overwritten)"""
FIGURE_DIR_TIME = datetime.now()
"""Defaults to `datetime.now()`"""
FIGURE_DIR = path.join(
    FIGURE_DIR_SUBDIR, f"{FIGURE_DIR_TIME.strftime('%Y-%m-%dT%H-%M-%S')}"
)
"""Directory to save figures used by `figure_save()`"""
MPL_COLORS_TAB = [
    "tab:blue",
    "tab:green",
    "tab:orange",
    "tab:red",
    "tab:purple",
    "tab:pink",
    "tab:olive",
    "tab:cyan",
    "tab:gray",
    "tab:brown",
]
"""Set of MPL 'tab:' colors"""


# %%
# === PLOT SETTINGS ===
def figure_save(figure_name: str, fileformat: str | None, **kwargs) -> None:
    """
    saves the current matplotlib figure to a file

    Args:
        figure_name: File name
        **kwargs: Additional keyword arguments passed to `pyplot.savefig()`
    """
    dirname = FIGURE_DIR
    if fileformat is None:
        fileformat = mpl.rcParams["savefig.format"]
    if FIGURE_SAVE and not FASTRUN:
        if not path.isdir(dirname):
            makedirs(dirname)
        return plt.savefig(
            path.join(
                dirname, figure_name + "." + fileformat
            ),
            **kwargs,
        )


save_figure = figure_save
"""aliase for `figure_save()`. legacy support, to be removed in a later version"""


# %%
def plt_setup(
    plotting: bool = None,
    size: (int, int) = None,
    dpi: int = None,
    save: bool = None,
    dirname: str = None,
    dir_subdir: str = None,
    dir_time: str = None,
    fastrun: bool = None,
):
    """
    Sets up default matplotlib settings and changes by the module provided constants

    Args:
        plotting: whether to compute plots
        size: Size of mpl figures
        dpi: DPI of mpl figures
        save: whether to save mpl figures (effects `figure_save`)
        dirname: Directory to save image files to
        dir_subdir: Compute directory to save image files to with subdirectory name and timestamp (no effect if `dirname` is given)
        dir_time:
        fastrun:
    """
    global PLOTTING
    global FIGURE_SAVE
    global FASTRUN
    global FIGURE_SAVE
    global FIGURE_DIR
    global FIGURE_DIR_SUBDIR
    global FIGURE_DIR_TIME

    if plotting is not None:
        PLOTTING = plotting
    if fastrun is not None:
        FASTRUN = fastrun

    if save is not None:
        FIGURE_SAVE = save

    if dir_subdir is not None:
        FIGURE_DIR_SUBDIR = dir_subdir
    if dir_time is not None:
        FIGURE_DIR_TIME = dir_time

    if dirname is not None:
        FIGURE_DIR = dirname
    elif dir_subdir is not None:
        FIGURE_DIR = path.join(
            FIGURE_DIR_SUBDIR, f"{FIGURE_DIR_TIME.strftime('%Y-%m-%dT%H-%M-%S')}"
        )
    else:
        pass

    mpl.rcParams["figure.figsize"] = size
    mpl.rcParams["figure.dpi"] = dpi

    # mpl.rcParams['text.latex.preamble'] = r"\usepackage{siunitx}"


# === PLOT LAYOUT ===
def args_err(
    *,
    ls: str = "",
    marker: str = ".",
    mec: str = "k",
    ms: int = 7,
    ecolor: str = "k",
    elinewidth: int = 2,
    capsize: int = 5,
    capthick: int = 2,
    **kwargs: str | int,
) -> dict[str, str | int]:
    """
    Provides (default) parameters for `plt.errorbar`. Can be used like
    ```python
    plt.errorbar(xdata, ydata, xerr=xerr, yerr=yerr, **args_err())
    ```
    If `None` is given, no value is set.

    Args:
        ls: line style
        marker: marker style
        mec: marker edge color
        ms: marker size
        ecolor: error bar color
        elinewidth: error bar line width
        capsize: error bar cap size
        capthick: error bar cap thickness
        **kwargs: other valid `plt.errorbar` parameters can be provided

    Returns:
        Dictionary with parameters
    """
    dct = {}
    for key, value in locals().items():
        if value is not None:
            dct[key] = value
    dct.update(dct["kwargs"])
    del dct["dct"], dct["kwargs"]
    return dct
