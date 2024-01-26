from clickhouse_driver.errors import ServerException


class RowsMismatchError(Exception):
    """
    Custom exception raised when the number of rows in S3 does not match ClickHouse within a specified percentage difference.

    Attributes:
        number_rows_s3 (int): Number of rows in S3.
        number_rows_clickhouse (int): Number of rows in ClickHouse.
        max_percentage_diff (float): Maximum allowed percentage difference.
    """

    def __init__(self, number_rows_s3, number_rows_clickhouse, max_percentage_diff):
        """
        Initialize the exception.

        Parameters:
            number_rows_s3 (int): Number of rows in S3.
            number_rows_clickhouse (int): Number of rows in ClickHouse.
            max_percentage_diff (float): Maximum allowed percentage difference.
        """
        self.number_rows_s3 = number_rows_s3
        self.number_rows_clickhouse = number_rows_clickhouse
        self.max_percentage_diff = max_percentage_diff
        message = (
            f"Number of rows in S3 ({number_rows_s3}) does not match ClickHouse ({number_rows_clickhouse})"
            f" within {max_percentage_diff}% difference."
            f" your score is {max_percentage_diff}% "
        )
        super().__init__(message)


class TableNotFoundError(Exception):
    """Exception raised when a table is not found in ClickHouse."""

    def __init__(self, table: str, database: str):
        self.table = table
        self.database = database
        self.message = f"Table {self.database}.{self.table} is not found in ClickHouse"
        super().__init__(self.message)


class TransferErrorAlreadyExists(Exception):
    """Exception raised when a table is not found in ClickHouse."""

    def __init__(self, table: str, database: str):
        self.table = table
        self.database = database
        self.message = f"""Table {self.database}.{self.table} is already exists in ClickHouse,
                         --drop-destination-table-if-exist set False, forbidden to recreate tables"""
        super().__init__(self.message)


class ExtractMetadataError(ServerException):
    """Exception raised when a table is not found in ClickHouse."""

    def __init__(self, table: str, database: str, s3_path: str):
        self.s3_path = s3_path
        self.database = database
        self.table = table
        self.message = f"""Error fetching metadata for the table {self.database}.{self.table} from the S3 path.
                           Please check if the requirement file exists (extracting finished) or if the file is in the correct format."""
        super().__init__(self.message)


class ClickHouseError(Exception):
    """Exception raised for ClickHouse connection errors."""

    def __init__(self, url: str, message: str):
        self.url = url
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.url}"


class ClickHouseColumnsDeclarationErrorS3(Exception):
    """Exception raised for ClickHouse connection errors."""

    def __init__(self, url: str, message: str):
        self.url = url
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.url}"


class S3Error(Exception):
    """Exception raised for S3 connection errors."""

    def __init__(self, url: str, message: str):
        self.url = url
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.url}"


class OnClusterClickhouseError(Exception):
    """Exception raised for On Cluster directive errors."""

    def __init__(self, table: str, database: str, cluster: str, message: str):
        self.database = database
        self.table = table
        self.cluster = cluster
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.database}.{self.table}. Your directive is: {self.cluster}"
