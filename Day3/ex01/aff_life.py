import matplotlib.pyplot as plt
import pandas as pd 
from matplotlib.ticker import MultipleLocator
from load_csv import load
import sys


def ft_visualize(Dataset):
    try:
        Dataset = Dataset.set_index('country')
        selected = Dataset.loc['France']
        years = selected.index.astype(int)
        values = selected.values.astype(float)
        fig, ax = plt.subplots()
        ax.plot(years, values)
        ax.set_xticks(range(1800, 2101, 40))  
        ax.set_xlabel('Year')
        ax.set_ylabel('Life expectancy')
        ax.set_title('France Life Expectancy') 
        plt.show()
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