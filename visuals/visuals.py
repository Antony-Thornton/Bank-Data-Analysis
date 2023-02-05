import pandas
import pandas as pd
import matplotlib.pyplot as plt
from itertools import cycle, islice

import Data.get_data

def create_chart_test(df):
    print("Printing a bar chart of all ")

    df = df[['housing', 'marital', 'balance']]

    pd.pivot_table(df, values='balance', index='marital').plot(kind='bar', stacked=True, color='red')

    plt.title("Bank balance by marital status")
    plt.xlabel("Status")
    plt.ylabel("Balance")
    plt.show()


    return df

def test():
    print("Successfully ran both functions")


def all_def():
    create_chart_test(df)
    test()


df = Data.get_data.create_data_frame()

