import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter
from load_csv import load
import sys


def ft_visualize(Dataset):
    """
    FT_visulalize - generate a plot of 2 country's data
    """
    try:
        Dataset = Dataset.set_index('country')
        Dataset = Dataset.replace({'M': '*1e6', 'k': '*1e3', 'B': '*1e9'},
                                  regex=True)
        Dataset = Dataset.map(pd.eval).astype(float)
        selected = Dataset.loc['France']
        selected_2nd = Dataset.loc['Belgium']
        years = selected.index.astype(int)
        values = selected.values.astype(float)
        values_2nd = selected_2nd.values.astype(float)
        fig, ax = plt.subplots()
        ax.plot(years, values, label='France')
        ax.plot(years, values_2nd, '-.', label='Belgium')

        def millions(x, pos):
            return f'{x/1e6:.1f}M'
        ax.yaxis.set_major_formatter(FuncFormatter(millions))
        ax.set_xlim(1800, 2050)
        ax.set_xticks(range(1800, 2050, 40))
        ax.set_yticks(range(0, 100000000, 20000000))
        ax.set_xlabel('Year')
        ax.set_ylabel('Population')
        ax.set_title('Population Projections')
        ax.legend()
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
