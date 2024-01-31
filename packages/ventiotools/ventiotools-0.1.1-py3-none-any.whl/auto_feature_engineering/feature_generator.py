from pyspark.ml.feature import OneHotEncoder, StringIndexer
from pyspark.ml.functions import vector_to_array
from pyspark.sql.functions import *
from pyspark.sql.window import Window


def generate_features(df: DataFrame, yaml_data: dict) -> DataFrame:
    # Generate features
    if "date_variables" in yaml_data:
        df = generate_date_features(df, yaml_data)
    if "categorical_variables" in yaml_data:
        df = generate_categorical_features(df, yaml_data)
    if "numerical_variables" in yaml_data:
        df = generate_numerical_features(df, yaml_data)
    return df


def generate_date_features(df: DataFrame, yaml_file: dict) -> DataFrame:
    """
    Generate date features based on the configuration file.
    Args:
        df: Spark DataFrame
        yaml_file: Configuration file
    Returns:
        Spark DataFrame with generated features
    """
    date_data = yaml_file["date_variables"]
    for date_var in date_data:
        columns_date = date_var["column"]
        extract_vars = date_var["extract"]
        for column in columns_date:
            for extract_var in extract_vars:
                df = df.withColumn(
                    column + "_" + extract_var, globals()[extract_var](column)
                )
                if date_var["encoding"] == "sin-cos":
                    df = sin_cos_encoder(df, column, extract_var)
    return df


def sin_cos_encoder(df: DataFrame, column: str, extract_var: str) -> DataFrame:
    """
    Generate sin and cos features from a date column.
    Args:
        df: Spark DataFrame
        column: Date column
    Returns:
        Spark DataFrame with generated features
    """
    if extract_var == "month":
        df = df.withColumn(
            column + "_" + extract_var + "_sin",
            sin(radians(col(column + "_" + extract_var) * (360 / 12))),
        )
        df = df.withColumn(
            column + "_" + extract_var + "_cos",
            cos(radians(col(column + "_" + extract_var) * (360 / 12))),
        )
    elif extract_var == "dayofmonth":
        df = df.withColumn(
            column + "_month_sin",
            when(
                col(column + "_month").isin([1, 3, 5, 7, 8, 10, 12]),
                sin(radians(col(column + "_month") * (360 / 31))),
            )
            .when(
                col(column + "_month") == 2,
                sin(radians(col(column + "_month") * (360 / 28))),
            )
            .otherwise(sin(radians(col(column + "_month") * (360 / 30)))),
        )
        df = df.withColumn(
            column + "_month_cos",
            when(
                col(column + "_month").isin([1, 3, 5, 7, 8, 10, 12]),
                cos(radians(col(column + "_month") * (360 / 31))),
            )
            .when(
                col(column + "_month") == 2,
                sin(radians(col(column + "_month") * (360 / 28))),
            )
            .otherwise(cos(radians(col(column + "_month") * (360 / 30)))),
        )
        df = df.drop(column + "_" + extract_var)
        df = df.drop(column + "_month")
    elif extract_var == "dayofweek":
        df = df.withColumn(
            column + "_" + extract_var + "_sin",
            sin(radians(col(column + "_" + extract_var) * (360 / 7))),
        )
        df = df.withColumn(
            column + "_" + extract_var + "_cos",
            cos(radians(col(column + "_" + extract_var) * (360 / 7))),
        )
        df = df.drop(column + "_" + extract_var)
    elif extract_var == "dayofyear":
        df = df.withColumn(column + "_year", year(col(column)))
        df = df.withColumn(
            column + "_dayofyear_sin",
            when(
                (col(column + "_year") % 4 == 0)
                & (
                    (col(column + "_year") % 100 != 0)
                    | (col(column + "_year") % 400 == 0)
                ),
                sin(radians(col(column + "_dayofyear") * (360 / 366))),
            ).otherwise(sin(radians(col(column + "_dayofyear") * (360 / 365)))),
        )
        df = df.withColumn(
            column + "_dayofyear_cos",
            when(
                (col(column + "_year") % 4 == 0)
                & (
                    (col(column + "_year") % 100 != 0)
                    | (col(column + "_year") % 400 == 0)
                ),
                cos(radians(col(column + "_dayofyear") * (360 / 366))),
            ).otherwise(cos(radians(col(column + "_dayofyear") * (360 / 365)))),
        )
        df = df.drop(column + "_" + extract_var)
        df = df.drop(column + "_year")
    elif extract_var == "weekofyear":
        df = df.withColumn(
            column + "_" + extract_var + "_sin",
            sin(radians(col(column + "_" + extract_var) * (360 / 52))),
        )
        df = df.withColumn(
            column + "_" + extract_var + "_cos",
            cos(radians(col(column + "_" + extract_var) * (360 / 52))),
        )
        df = df.drop(column + "_" + extract_var)
    return df


def generate_numerical_features(df: DataFrame, yaml_file: dict) -> DataFrame:
    """
    Generate numerical features based on the configuration file.
    Args:
        df: Spark DataFrame
        yaml_file: Configuration file
    Returns:
        Spark DataFrame with generated features
    """
    numerical_data = yaml_file["numerical_variables"]
    for num_var in numerical_data:
        columns_num = num_var["column"]
        aggregations = num_var["aggregation"]
        groupby_variables = num_var["group"]
        df_temp = df.groupBy(groupby_variables).agg(
            max(columns_num[0]).alias("temp_grouped")
        )
        for column in columns_num:
            for aggregation in aggregations:
                if "time_var" in num_var:
                    df = generate_timeseries_features(df, num_var, column, aggregation)
                df_temp = df_temp.join(
                    (df.groupBy(groupby_variables).agg(globals()[aggregation](column))),
                    on=groupby_variables,
                )
        df_temp = df_temp.drop("temp_grouped")
        df = df.join(df_temp, on=groupby_variables, how="left")
    df = df.orderBy(groupby_variables[0], ascending=[True])
    return df


def generate_timeseries_features(
    df: DataFrame, num_var: dict, column: str, aggregation: str
) -> DataFrame:
    """
    Generate timeseries features based on the configuration file.
    Args:
        df: Spark DataFrame
        num_var: Numerical Variable
        column: column to generate features
        aggregation: aggregation to apply
    Returns:
        Spark DataFrame with generated features
    """
    df = df.withColumn(
        "timestamp", unix_timestamp(col(num_var["time_var"]), "yyyy-MM-dd HH:mm:ss")
    )
    if "rolling" in num_var:
        df = df.withColumn(
            column + "_" + aggregation + "_rolling" + "_" + str(num_var["rolling"]),
            globals()[aggregation](col(column)).over(
                Window.partitionBy(num_var["group"])
                .orderBy("timestamp")
                .rowsBetween((-num_var["rolling"] + 1), 0)
            ),
        )
    if "accumulating" in num_var:
        df = df.withColumn(
            column + "_" + aggregation + "_accumulating",
            globals()[aggregation](col(column)).over(
                Window.partitionBy(num_var["group"])
                .orderBy("timestamp")
                .rangeBetween(Window.unboundedPreceding, 0)
            ),
        )
    if "lagging" in num_var:
        df = df.withColumn(
            column + "_lagging" + "_" + str(num_var["lagging"]),
            lag(col(column), num_var["lagging"]).over(
                Window.partitionBy(num_var["group"]).orderBy("timestamp")
            ),
        )
    df = df.drop("timestamp")
    return df


def generate_categorical_features(df: DataFrame, yaml_file: dict) -> DataFrame:
    """
    Generate categorical features based on the configuration file.
    Encoding used: One Hot Encoding
    Args:
        df: Spark DataFrame
        yaml_file: Configuration file
    Returns:
        Spark DataFrame with generated features
    """
    index_var = yaml_file["df_index"]
    categorical_data = yaml_file["categorical_variables"]
    columns_cat = categorical_data["column"]
    df = df.na.fill(value="missing", subset=columns_cat)
    for column in columns_cat:
        indexer = StringIndexer(inputCol=column, outputCol=column + "_numeric")
        indexer_fitted = indexer.fit(df)
        df_indexed = indexer_fitted.transform(df)
        encoder = OneHotEncoder(
            inputCols=[column + "_numeric"],
            outputCols=[column + "_onehot"],
            dropLast=False,
        )
        df_onehot = encoder.fit(df_indexed).transform(df_indexed)
        df_col_onehot = df_onehot.select(
            "*", vector_to_array(column + "_onehot").alias("col_onehot")
        )
        num_categories = len(df_col_onehot.first()["col_onehot"])
        cols_expanded = [
            (col("col_onehot")[i].alias(f"{column}_{indexer_fitted.labels[i]}"))
            for i in range(num_categories)
        ]
        df_cols_onehot = df_col_onehot.select(index_var, *cols_expanded)
        df = df.join(df_cols_onehot, on=index_var).drop(column)
    return df
