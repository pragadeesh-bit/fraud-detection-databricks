
from pyspark.sql import SparkSession
from src.silver import clean_transactions


def test_clean_transactions():

    spark = (
        SparkSession.builder
        .master("local[1]")
        .appName("FraudDetectionTest")
        .getOrCreate()
    )

    data = [
        (1, 100, "SUCCESS"),
        (2, -50, "SUCCESS"),
        (3, 200, "FAILED"),
        (None, 300, "SUCCESS")
    ]

    columns = ["transaction_id", "amount", "status"]

    df = spark.createDataFrame(data, columns)

    result = clean_transactions(df)

    assert result.count() == 1

    spark.stop()
