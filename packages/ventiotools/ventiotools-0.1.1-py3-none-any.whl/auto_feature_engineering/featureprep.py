from pyspark.sql.functions import *


def profile_data(df: DataFrame) -> dict:
    int_column = []
    float_column = []
    string_column = []
    categorical_column = []
    date_column = []
    datetime_column = []
    Numeric_Threshold = 0.9

    for selected_column in df.columns:
        if df.select(selected_column).distinct().count() < 20:
            categorical_column.append(selected_column)
        if (
            df.filter(
                (col(selected_column).rlike("^[+-]?([0-9]+)$"))
                & df[selected_column].isNotNull()
            ).count()
            / df.filter(df[selected_column].isNotNull()).count()
            > Numeric_Threshold
        ):
            int_column.append(selected_column)

        elif (
            df.filter(
                (col(selected_column).rlike("^[+-]?([0-9]*[.])?[0-9]+$"))
                & df[selected_column].isNotNull()
            ).count()
            / df.filter(df[selected_column].isNotNull()).count()
            > Numeric_Threshold
        ):
            float_column.append(selected_column)

        elif (
            df.filter(
                (col(selected_column).rlike("^([0-9]{4})-([0-1][0-9])-([0-3][0-9])$"))
                & df[selected_column].isNotNull()
            ).count()
            / df.filter(df[selected_column].isNotNull()).count()
            > Numeric_Threshold
        ):
            date_column.append(selected_column)

        elif (
            df.filter(
                (
                    col(selected_column).rlike(
                        "^([0-9]{4})-([0-1][0-9])-([0-3][0-9]) ([0-2][0-9]):([0-5][0-9]):([0-5][0-9])$"
                    )
                )
                & df[selected_column].isNotNull()
            ).count()
            / df.filter(df[selected_column].isNotNull()).count()
            > Numeric_Threshold
        ):
            datetime_column.append(selected_column)

        else:
            string_column.append(selected_column)

    return {
        "Integer Columns": int_column,
        "Float Columns": float_column,
        "String Columns": string_column,
        "Date Columns": date_column,
        "Datetime Columns": datetime_column,
        "Categorical Columns": categorical_column,
        "Numerical Columns": int_column + float_column,
    }


def impute_missing_values(
    df: DataFrame,
    column_types: dict,
    numeric_value: Union[str, int] = "mean",
    categorical_value: str = "missing",
) -> DataFrame:
    """
    Impute missing values based on the data type of the column.
    Args:
        df: Spark DataFrame
        column_types: Dictionary with column names and their data types
    Returns:
        Spark DataFrame with imputed missing values
    """
    for numerical_column in column_types["Numerical Columns"]:
        if numeric_value == "mean":
            numeric_value = df.select(mean(df[numerical_column])).collect()[0][0]
        if numeric_value == "median":
            numeric_value = df.select(median(df[numerical_column])).collect()[0][0]
        df = df.withColumn(
            numerical_column,
            when(df[numerical_column].isNull(), numeric_value).otherwise(
                df[numerical_column]
            ),
        )
    for string_column in column_types["String Columns"]:
        df = df.withColumn(
            string_column,
            when(df[string_column].isNull(), categorical_value).otherwise(
                df[string_column]
            ),
        )
    return df
