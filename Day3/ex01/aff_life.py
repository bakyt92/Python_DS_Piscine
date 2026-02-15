import matplotlib.pyplot as plt
import pandas as pd 
from load_csv import load
import sys


def ft_visualize(Dataset):
    try:
        Dataset = Dataset.set_index('country')
        selected = Dataset.loc['France']
        print(Dataset)
        print(selected)
    except Exception as e:
        print(e)
        sys.exit(1)
    return

def main():
    try:
        assert len(sys.argv) == 2, \
            "AssertionError: please provide one argument for file path"
        link = sys.argv[1]
        Dataset = load(link)
        ft_visualize(Dataset)
    except Exception as e:
        print(e)
        sys.exit(1)
    return


if __name__ == "__main__":
    main()