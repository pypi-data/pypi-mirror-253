import ipython_autoimport
import rpy2.ipython
import coconut
import itables
import itables.options
import matplotlib_inline as mpl_inline
import plotly.io as pio
import plotly.express as px
import os
import random
import numpy as np
import polars as pl
import pandas as pd

def configure_plot_output(ipython):
    # display Matplotlib plots as resizable widgets
    ipython.magic("matplotlib widget")
    # display plots at a higher resolution (see https://gist.github.com/minrk/3301035)
    mpl_inline.backend_inline.set_matplotlib_formats("retina")
    # configure Plotly
    plotly_conf = pio.renderers["jupyterlab"].config
    # download plots at their currently rendered size
    plotly_conf["toImageButtonOptions"] = { "height": None, "width": None }
    # zoom in and out of plots using the mouse scroll wheel and/or a two-finger scrolling
    plotly_conf["scrollZoom"] = True
    # pan on drag (instead of zoom)
    for template in pio.templates:
        pio.templates[template].layout["dragmode"] = "pan"


def configure_df_output(tbl_width_chars=8192, fmt_str_lengths=1024, itables_maxBytes=8*1024*1024):
    # display all dataframes as interactive HTML tables
    itables.init_notebook_mode(all_interactive=True)
    # increase table size limit to 8 MiB
    itables.options.maxBytes = itables_maxBytes
    # set default text colour of form elements to grey to make them visible in dark mode as well
    # display cells in monospace for better alignment
    itables.options.css = ".itables select,input { color: #808080; } td { font-family: monospace; }"
    # extend range of available table lengths, increase default to 20
    itables.options.lengthMenu = [20, 10, 25, 50, 100, 200, 500, 1000]

    # set Polars output format to Markdown, which can be displayed with IPython.display.Markdown
    pl.Config.set_tbl_formatting("ASCII_MARKDOWN")
    # Markdown output only works well with inline datatypes for columns
    pl.Config.set_tbl_column_data_type_inline(True)
    # cell output can be scrolled horizontally, so we can increase length limits
    pl.Config.set_fmt_str_lengths(fmt_str_lengths)
    pl.Config.set_tbl_width_chars(tbl_width_chars)
    pl.Config.set_tbl_cols(-1)
    pl.Config.set_tbl_rows(60)
    # same for Pandas
    pd.set_option("display.max_colwidth", None)
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", tbl_width_chars)
    pd.set_option('display.max_rows', 60)


def set_seed(seed=42):
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)

    try:
        import torch
        torch.manual_seed(seed)
        torch.cuda.manual_seed(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    except ImportError:
        pass

    try:
        import tensorflow as tf
        tf.random.set_seed(seed)
        tf.experimental.numpy.random.seed(seed)
        tf.set_random_seed(seed)
        os.environ["TF_CUDNN_DETERMINISTIC"] = "1"
        os.environ["TF_DETERMINISTIC_OPS"] = "1"
    except ImportError:
        pass


def load_ipython_extension(ipython):
    """
    Initialise a Jupyter notebook with useful extensions and reasonable defaults.
    """
    # load extensions useful for interactive use
    ipython_autoimport.load_ipython_extension(ipython)
    # workaround. autoreload is not in sys.path and cannot be imported directly
    ipython.magic("load_ext autoreload")

    # load extensions for additional languages that can be used in the same notebook
    rpy2.ipython.load_ipython_extension(ipython)
    coconut.load_ipython_extension(ipython)

    # configure plot output formatting
    configure_plot_output(ipython)
    # configure dataframe output formatting
    configure_df_output()
    # try to make the results reproducible
    set_seed()
