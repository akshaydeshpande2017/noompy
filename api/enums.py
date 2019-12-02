import enum


class FileOPS(enum.Enum):
    # FILE PATh
    FILE_PATH_DOES_NOT_EXISTS = "excel_path provided does not exist, please check"
    FILE_PATH_ERROR = "Please provide the excel_path"


class QueryOPS(enum.Enum):
    # QUERY OPERATION
    DELETE_ROW = "DELETEROW"
    DELETE_CELL = "DELETECELL"
    DELETE_COLUMN = "DELETECOLUMN"
    EMPTY_CELL_VALUE = ""


class ErrorMSG(enum.Enum):
    # CONSTANTS
    EMPTY_DATA_SOURCE = "Data source is EMPTY, Invalid Action."
    EMPTY_DF = "WHERE clause did not retrieve any matching result."
    KEY_ERROR = "Data or Key is None"
