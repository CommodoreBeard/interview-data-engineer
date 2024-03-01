from typing import List, Dict, Any, Generator
import os
import psycopg2
from contextlib import contextmanager
import logging


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@contextmanager
def database_connection() -> Generator[psycopg2.extensions.connection, None, None]:
    connection = psycopg2.connect(
        dbname=os.getenv("PGDATABASE", "sales"),
        user=os.getenv("PGUSER", "postgres"),
        password=os.getenv("PGPASSWORD", "mysecretpassword"),
        host=os.getenv("PGHOST", "localhost"),
        port=os.getenv("PGPORT", "5432"),
    )
    try:
        yield connection
    finally:
        connection.close()


def read_csv_data(file_path: str) -> List[Dict[str, Any]]:
    pass


def clean_price(value: str) -> float:
    """
    Clean price values, removing currency symbols and converting to float.
    """
    # Remove non-numeric characters except the decimal point
    cleaned_value = ''.join(c for c in value if c.isdigit() or c == '.')
    return float(cleaned_value) if cleaned_value else 0.0


def clean_value(key: str, value: str) -> Any:
    """
    Clean data based on key, including handling of date formats.
    """
    if key == "Price":
        return clean_price(value)
    else:
        return value


def clean_data(data: List[Dict[str, str]], id_fields: List[str] = ['ProductID', 'SaleID', 'RetailerID']) -> List[Dict[str, Any]]:
    """
    Clean data by applying specific cleaning logic based on the key of each item.
    Log and exclude rows where any of the specified ID fields are missing or not integers.

    Parameters:
    - data: The list of data rows to clean.
    - id_fields: The list of ID fields to validate for each row.

    Returns:
    - The cleaned data as a list of dictionaries.
    """
    cleaned_data: List[Dict[str, Any]] = []
    seen: set = set()

    for row in data:
        cleaned_row = {key: clean_value(key, value) for key, value in row.items()}
        identifier = tuple(sorted(cleaned_row.items()))

        if identifier not in seen:
            seen.add(identifier)
            cleaned_data.append(cleaned_row)

    return cleaned_data

def validate_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    pass


def transform_data(raw_data: List[Dict[str, Any]]):
    pass

def publish_data(
    product_dim: List[Dict[str, Any]],
    retailer_dim: List[Dict[str, Any]],
    date_dim: List[Dict[str, Any]],
    sales_fact: List[Dict[str, Any]],
) -> None:
    pass
