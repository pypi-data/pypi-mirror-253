import pytest
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

from src.auto_feature_engineering.feature_generator import generate_features


@pytest.fixture(scope="session")
def spark():
    spark = (
        SparkSession.builder.master("local[1]")
        .appName("local-tests")
        .config("spark.executor.cores", "1")
        .config("spark.executor.instances", "1")
        .config("spark.sql.shuffle.partitions", "1")
        .getOrCreate()
    )
    yield spark
    spark.stop()


def test_generate_features(spark):
    data = [
        ("1", "a", "2020-01-01"),
        ("2", "b", "2020-02-01"),
        ("3", "c", "2020-03-01"),
    ]

    # Create a Spark DataFrame
    original_df = spark.createDataFrame(data)
    yaml_data = {}
    # Apply the transformation function from before
    transformed_df = generate_features(original_df, yaml_data)

    expected_data = original_df

    assert expected_data == transformed_df
