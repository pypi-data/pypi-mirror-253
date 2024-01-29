import enum
import os


class FilePathType(enum.Enum):
    S3 = "s3"
    LOCAL = "local"
    INTERNET = "internet"
    UNKNOWN = "unknown"


def identify_path_type(path: str) -> FilePathType:
    """
    Return file path type for different file handling
    Args:
        path: string file path

    Returns:
        FilePathType
    """
    if os.path.isfile(path):
        if os.path.exists(path):
            return FilePathType.LOCAL
        else:
            raise ValueError(
                f"{path} does not exist. Please check if this is a valid file path"
            )
    elif path.startswith("s3://"):
        return FilePathType.S3
    elif path.startswith("http"):
        return FilePathType.INTERNET
    else:
        return FilePathType.UNKNOWN
