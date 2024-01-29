# jupyter-interactive

Initialise a Jupyter notebook with useful extensions and reasonable defaults.

## Usage

    %load_ext jupyter_interactive

## Features

- Enable [autoimport](https://github.com/anntzer/ipython-autoimport) of missing
  modules.
- Enable the
  [`%autoreload`](https://ipython.org/ipython-doc/3/config/extensions/autoreload.html)
  keyword to reload all modules in the current session.
- Enable the `%%R` and `%%coconut` magic to execute specific cells using
  [R](https://rpy2.github.io/) and
  [Coconut](https://coconut-lang.org/).
- Configure plot output formatting:
    - Display Matplotlib plots as interactive, resizable widgets (using
      [`ipympl`](https://matplotlib.org/ipympl/)).
    - Display Matplotlib plots at a higher resolution.
    - Zoom in and out of Plotly figures using the mosue scroll wheel and/or
      two-finger scrolling.
    - Download Plotly figures at their currently rendered size.
    - Ensure that dragging Plotly figures results in panning (rather than
      zooming).
- Configure the output formatting of dataframes:
    - Display dataframes as interactive HTML tables (using
      [`itables`](https://mwouts.github.io/itables/quick_start.html)).
    - Increase the table size limit to 8 MiB.
    - Adjust default colours for better contrast.
    - Display cell contents in a monospace font.
    - Extend the range of available table lengths.
    - Make Polars dataframes output Markdown when printed.
    - Show all dataframe columns, even if there are many of them.
- Try to make results reproducible by setting the seed for the built-in
  `random` module, NumPy, and, if available, PyTorch and Tensorflow.
