import sys
import pandas as pd
import os


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


def ft_validation(Dataset) -> pd.DataFrame:
    """
    ft_validation is function to validate input dataset
    for basic edge cases: empty lines, empty dataset.
    Args: dataset (DataFrame, Pandas)
    """
    try:
        if Dataset.size == 0:
            raise DatasetError("File is empty, no elements")
        if len(Dataset) == 0:
            raise DatasetError("No rows in file")
        if len(Dataset.columns) == 0:
            raise DatasetError("No columns in the file")
        indexes_dropping = []
        for index, row in zip(Dataset.index, Dataset.itertuples(index=False, name=None)):
            values = row[1:]
            inv_count = 0
            for val in values:
                if pd.isna(val) or not isinstance(val, (int, float)):
                    inv_count += 1
            if inv_count > (len(values) / 2):
                print(f"Row", {row[:10]}, " is not valid, more than half of values is Nan OR not numeric. This row will be dropped.")
                indexes_dropping.append(index)
        Dataset = Dataset.drop(indexes_dropping)
        if len(Dataset) > 1:
            print("Whole array was checked. Data is correct (more than 1 row left)")
        else:
            raise DatasetError("File is empty, no elements after validation line by line")
    except Exception as e:
        print(e)
        sys.exit()
    return Dataset


def load(path: str) -> pd.DataFrame | None:
    """
    load - function to load dataset from file and do basic tests:
    - file exists
    - file has CSV extension
    """
    try:
        if not os.path.isfile(path):
            raise OSError("File is not found / does not exist")
        if not path.endswith(".csv"):
            raise TypeError("File is not correct extension")
        dataset = pd.read_csv(path)
        dataset = ft_validation(dataset)
        if dataset is None:
            raise Exception("dataset is not valid")
        ft_shape(dataset)
    except Exception as e:
        print(e)
        return None
    return dataset


def main():
    """
    Docstring for main: main func
    """
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
