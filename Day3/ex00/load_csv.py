import sys
import pandas as pd

class DatasetError(Exception):
    """Base exception for dataset-related errors."""
    pass

def ft_shape(Dataset):
    """
    Ft_shape is function to write dataset's shape (width and height)
    Args: dataset (DataFrame, Pandas)
    """
    try:
        rows = 0
        columns = 0
        rows = len(Dataset)
        columns = len(Dataset.columns)
        print(f"Dimensions are: {rows}, {columns}")
    except Exception as e:
        print(e)
        sys.exit(1)
    return

def ft_validation(Dataset):
    """
    ft_validation is function to validate input dataset for basic edge cases: empty lines, empty dataset
    Args: dataset (DataFrame, Pandas)
    """
    try:
        if Dataset.size == 0:
            raise DatasetError("File is empty, no elements")
        if len(Dataset) == 0:
            raise DatasetError("No rows in file")
        if len(Dataset.columns) == 0:
            raise DatasetError("No columns in the file")
        for x in Dataset:
            for y in x:
                if not isinstance(y, (str, int, float)):
                    raise TypeError("value is not float or integer")
        print("Whole array was checked. Type of Data is correct: str, int or float")     
    except Exception as e:
        print(e)
        sys.exit()
    return

def load(path: str) -> pd.DataFrame:
    """
    load - function to load dataset from file and do basic tests: 
    - file exists 
    - file has CSV extension
    """
    try:
        if not path.endswith(".csv"):
            raise TypeError("File is not correct extension")
        Dataset = pd.read_csv(path)
        ft_validation(Dataset)
        ft_shape(Dataset)
    except Exception as e:
        print(e)
        sys.exit()
    return Dataset

def main():
    try:
        assert len(sys.argv) == 2, \
            "AssertionError: please provide one argument for file path"
        link = sys.argv[1]
        print(load(link))
    except AssertionError as msg:
        print(msg)
        sys.exit()
    except Exception as e:
        print(e)
        sys.exit()
    return


if __name__ == "__main__":
    main()
