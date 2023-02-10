import pandas
import pandas as pd
import matplotlib.pyplot as plt
from itertools import cycle, islice

import Data.get_data

def bar_chart(df):
    print("Printing a bar chart showing bank balance by marital status.")

    df = df[['housing', 'marital', 'balance']]

    pd.pivot_table(df, values='balance', index='marital').plot(kind='bar', stacked=True, color='red')

    plt.title("Bank balance by marital status")
    plt.xlabel("Status")
    plt.ylabel("Balance")
    plt.show()


    return df

def line_graph(df):

    df = df[['age', 'balance']]

    pd.pivot_table(df, values='balance', index='age').plot(kind='line')

    plt.title("Bank balance by age")
    plt.xlabel("Age")
    plt.ylabel("Balance")
    plt.show()



def all_def():
    bar_chart(df)
    line_graph(df)


df = Data.get_data.create_data_frame()

