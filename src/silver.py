from pyspark.sql import DataFrame


def clean_transactions(df: DataFrame) -> DataFrame:
    """
    Clean banking transaction data.

    Rules:
    1. Remove transactions with null transaction IDs.
    2. Remove transactions with invalid amounts.
    3. Keep only successful transactions.
    dbwashzbjxn
    """

    
cleaned_df = (
    df.filter("transaction_id IS NOT NULL")
      .filter("amount > 0")
      .filter("status = 'SUCCESS'")
)

    return cleaned_df
