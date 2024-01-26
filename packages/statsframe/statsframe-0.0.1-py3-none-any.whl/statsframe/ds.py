from __future__ import annotations

# Main ds imports ----
import pandas as pd
import polars as pl
import polars.selectors as cs

from ._tbl_data import DataFrameLike  # , SeriesLike

cat_cols = []


def skim(
    data: pl.DataFrame,
    type: str = "numeric",
    stats: str = "simple",
    output: str = "polars",
    float_precision: int = 1,
    histogram: bool = False,
    title: str = "Summary Statistics",
    notes: str = None,
    align: str = "r",
) -> pl.DataFrame:
    """
    Summary Statistics.

    Generates summary statistics for a given DataFrame.

    Args:
        data (DataFrameLike): The input DataFrame. Can be pandas or polars.
        type (str, optional): The type of summary statistics to generate.
            Defaults to "numeric".
        output (str, optional): The output format for the summary statistics.
            Defaults to None.
        stats (str, optional): The summary statistics to return. Defaults to "simple".
        float_precision (int, optional): The number of decimal places to round
            float values when formatting in table output.
            Defaults to 2.
        histogram (bool, optional): Whether to include a histogram in the output.
            Defaults to False.
        title (str, optional): The title of the summary statistics table.
            Defaults to "Summary Statistics".
        notes (str, optional): Additional notes or comments.
            Defaults to None.
        align (str, optional): The alignment of the table columns.
            Defaults to "r".

    Returns:
        pl.DataFrame: The summary statistics table.

    Examples:
        # Generate summary statistics for a numeric DataFrame
        summary = skim(data)

        # Generate summary statistics for a categorical DataFrame
        summary = skim(data, type="categorical")

        # Generate summary statistics in markdown format
        summary = skim(data, output="markdown")
    """

    # methods depend on the data being a polars DataFrame
    data = convert_to_pl_df(data)

    # check if the data is numeric or categorical
    if type == "numeric":
        stats_tab, float_cols = _skim_numeric(data, stats=stats)
    elif type == "categorical":
        stats_tab, float_cols = _skim_categorical(data, stats=stats)
    else:
        raise ValueError("Invalid type argument")

    # format the output
    output_dict = {
        "polars": None,
        "markdown": "ASCII_MARKDOWN",
        "simple": "NOTHING",
    }
    tbl_formatting = output_dict[output]

    if output == "polars":
        tbl_formatting = None
    elif output == "markdown":
        tbl_formatting = "ASCII_MARKDOWN"
    elif output == "simple":
        tbl_formatting = "NOTHING"
    else:
        raise ValueError("Invalid output argument")

    # details for the table formatting
    align_dict = {"r": "RIGHT", "l": "LEFT", "c": "CENTER"}
    tbl_align = align_dict[align]
    shape_details = f"Rows: {data.height}, Columns: {data.width}"

    with pl.Config(
        float_precision=float_precision,
        tbl_formatting=tbl_formatting,
        tbl_cell_alignment=tbl_align,
        tbl_hide_column_names=False,
        tbl_hide_column_data_types=True,
        tbl_hide_dataframe_shape=True,
    ):
        print(f"{title}")
        print(f"{shape_details}")
        print(stats_tab)
    return stats_tab


def _skim_numeric(data: pl.DataFrame, stats: str = "simple") -> pl.DataFrame:
    """
    Generates summary statistics for a numeric datatypes in a DataFrame.

    Args:
        data (pl.DataFrame): The input DataFrame.
        stats (str, optional): The summary statistics to return. Defaults to "simple".

    Returns:
        pl.DataFrame: The summary statistics table.
    """
    stats_dict = {
        "simple": ["Missing (%)", "Mean", "SD", "Min", "Median", "Max"],
        "moments": ["Mean", "Variance", "Skewness", "Kurtosis"],
        "detail": [
            "Missing (%)",
            "Mean",
            "SD",
            "Min",
            "Median",
            "Max",
            "Skewness",
            "Kurtosis",
        ],
    }

    float_cols = stats_dict[stats]
    int_cols = ["Unique (#)"]
    stats_cols = int_cols + float_cols

    if stats == "simple":
        stats_tab = (
            data.select(cs.numeric().n_unique())
            .cast(pl.Float64, strict=True)
            .extend(
                data.select(
                    cs.numeric()
                    .null_count()
                    .truediv(data.height)
                    .cast(pl.Float64, strict=True)
                )
            )
            .extend(data.select(cs.numeric().mean()))
            .extend(data.select(cs.numeric().std()))
            .extend(data.select(cs.numeric().min().cast(pl.Float64, strict=True)))
            .extend(data.select(cs.numeric().median()))
            .extend(data.select(cs.numeric().max().cast(pl.Float64, strict=True)))
            .transpose(include_header=True, header_name="", column_names=stats_cols)
            .with_columns(pl.col("Unique (#)").cast(pl.Int64, strict=True))
        )
    elif stats == "moments":
        stats_tab = (
            data.select(cs.numeric().n_unique())
            .cast(pl.Float64, strict=True)
            .extend(data.select(cs.numeric().mean()))
            .extend(data.select(cs.numeric().std()))
            .extend(data.select(cs.numeric().skew()))
            .extend(data.select(cs.numeric().kurtosis()))
            .transpose(include_header=True, header_name="", column_names=stats_cols)
            .with_columns(pl.col("Unique (#)").cast(pl.Int64, strict=True))
        )
    elif stats == "detail":
        stats_tab = (
            data.select(cs.numeric().n_unique())
            .cast(pl.Float64, strict=True)
            .extend(
                data.select(
                    cs.numeric()
                    .null_count()
                    .truediv(data.height)
                    .cast(pl.Float64, strict=True)
                )
            )
            .extend(data.select(cs.numeric().mean()))
            .extend(data.select(cs.numeric().std()))
            .extend(data.select(cs.numeric().min().cast(pl.Float64, strict=True)))
            .extend(data.select(cs.numeric().median()))
            .extend(data.select(cs.numeric().max().cast(pl.Float64, strict=True)))
            .extend(data.select(cs.numeric().skew()))
            .extend(data.select(cs.numeric().kurtosis()))
            .transpose(include_header=True, header_name="", column_names=stats_cols)
            .with_columns(pl.col("Unique (#)").cast(pl.Int64, strict=True))
        )
    else:
        raise ValueError("Invalid stats argument")
    return stats_tab, float_cols


def _skim_categorical(data: pl.DataFrame, stats: str = "simple") -> pl.DataFrame:
    """
    Generates summary statistics for a numeric datatypes in a DataFrame.

    Args:
        data (pl.DataFrame): The input DataFrame.
        stats (str, optional): The summary statistics to return. Defaults to "simple".

    Returns:
        pl.DataFrame: The summary statistics table.
    """
    raise NotImplementedError("Not implemented")


def convert_to_pl_df(data: DataFrameLike) -> pl.DataFrame:
    """
    Converts a DataFrame-like object to a polars DataFrame.

    Args:
        data (DataFrameLike): The input DataFrame-like (pandas or polars DataFrame`)
            object.

    Returns:
        pl.DataFrame: The converted polars DataFrame.

    Raises:
        ValueError: If the input data is not a polars or pandas DataFrame.
    """
    if isinstance(data, pl.DataFrame):
        return data
    elif isinstance(data, pd.DataFrame):
        return pl.from_pandas(data)
    else:
        raise ValueError("Input data must be a polars or pandas DataFrame")
