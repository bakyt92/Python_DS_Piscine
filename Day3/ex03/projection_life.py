import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter, ScalarFormatter
from load_csv import load
import sys


def ft_two_datasets(Dataset_expectancy, Dataset_gdp):
    """
    ft_two_datasets - generate a scatter plot of 2 country's data
    """
    try:
        Dataset_expectancy = Dataset_expectancy.set_index('country')
        Dataset_gdp = Dataset_gdp.set_index('country')
        Dataset_gdp = Dataset_gdp.replace({'M': '*1e6', 'k': '*1e3'},
                                          regex=True)
        Dataset_gdp = Dataset_gdp.map(pd.eval).astype(float)
        Dataset_expectancy = Dataset_expectancy['1900']
        Dataset_gdp = Dataset_gdp['1900']
        common_countries = \
            Dataset_gdp.index.intersection(Dataset_expectancy.index)
        Dataset_expectancy = Dataset_expectancy.loc[common_countries]
        Dataset_gdp = Dataset_gdp.loc[common_countries]
        # print(Dataset_expectancy)
        # print(Dataset_gdp)
        expectancy_years = Dataset_expectancy.values.astype(float)
        gdp = Dataset_gdp.values.astype(float)
        fig, ax = plt.subplots()
        ax.scatter(gdp, expectancy_years)
        ax.set_xscale('log')
        ax.xaxis.set_major_formatter(ScalarFormatter())
        ax.ticklabel_format(axis='x', style='plain')

        def format_gdp(x, pos):
            if x >= 1000:
                return f'{x/1000:.0f}k'
            else:
                return f'{x:.0f}'
        ax.xaxis.set_major_formatter(FuncFormatter(format_gdp))
        # ax.set_xlim(1800, 2050)
        # ax.set_xticks(range(1800, 2050, 40))
        # ax.set_yticks(range(0, 100000000, 20000000))
        ax.set_xlabel('Gross domestic product')
        ax.set_ylabel('Life expectancy')
        ax.set_title('1900 Y')
        ax.grid(True, alpha=0.3)
        plt.show()
    except Exception as e:
        print(e)
        sys.exit(1)
    return


def main():
    try:
        assert len(sys.argv) == 3, \
            "AssertionError: please provide two arguments for file path"
        link = sys.argv[1]
        link2 = sys.argv[2]
        Dataset1 = load(link)
        Dataset2 = load(link2)
        if link.startswith("life"):
            ft_two_datasets(Dataset1, Dataset2)
        else:
            ft_two_datasets(Dataset2, Dataset1)
    except Exception as e:
        print(e)
        sys.exit(1)
    return


if __name__ == "__main__":
    main()
