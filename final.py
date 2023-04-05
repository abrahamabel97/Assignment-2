# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 19:27:26 2023

@author: abrah
"""

import pandas as pd
import matplotlib.pyplot as plt


def lineplot(df, headers):
    """
    Function to create a lineplot. Arguments:
    A dataframe with columns taken as x and rows to be taken as y.
    A list containing the headers of the columns to plot.

    """

    plt.figure(figsize=(17, 6.5))

    # plotting each head
    for head in headers:
        plt.plot(df.columns, df.loc[head], label=head)

    # increasing size of ticks
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)

    # labelling the axes
    plt.xlabel("Year", fontsize=17)
    plt.ylabel("Growth Percentage", fontsize=17)

    # titling the plot
    plt.title("GDP Growth from 2010 to 2020", fontsize=25)

    plt.legend(fontsize=17)

    # saving as png
    plt.savefig("lineplot.png")

    plt.show()

    return


def bargraph(df):
    """
    Function to create a bargraph. Arguments:
    A dataframe with columns to be taken as x and rows to be taken as y
    Index of the row to be taken as y

    """

    plt.figure(figsize=(22, 10))
    plt.bar(df.index, df["Value"])

    # setting values and text size
    plt.xticks(df.index, fontsize=15)
    plt.yticks(fontsize=15)

    # setting the limits on x-axis
    plt.xlim(1995, 2006)

    # labelling
    plt.xlabel("Years", fontsize=20)
    plt.ylabel("Subscriptions (per 100 inhabitants)", fontsize=20)

    # titling the plot
    plt.title("Mobile-cellular Telephone Subscriptions", fontsize=30)

    # saving as png
    plt.savefig("bargraph.png")

    plt.show()

    return


def piechart(df):
    """
    Function to create a piechart. Arguments:
    A dataframe with columns to plot piecharts.
    Index of the column to be plotted in first piechart.
    Index of the row to be plotted in second piechart.

    """

    plt.figure(figsize=(20, 10))

    # plotting first pie chart
    plt.subplot(1, 2, 1)
    plt.pie(df[1990], labels=df.index,
            autopct='%1.0f%%', textprops={'fontsize': 20})

    plt.title("Population (1990)", fontsize=25)

    # plotting second pie chart
    plt.subplot(1, 2, 2)
    plt.pie(df[2020], labels=df.index,
            autopct='%1.0f%%', textprops={'fontsize': 20})

    plt.title("Population (2020)", fontsize=25)

    # saving as png
    plt.savefig("piechart.png")

    plt.show()

    return


# creating dataframe from the data
df_gdp = pd.read_excel("gdp_growth.xlsx", index_col=0)
df_population = pd.read_excel("population_growth.xlsx", index_col=0)
df_subscriptions = pd.read_csv("mobile_subscriptions.csv", index_col=0)

# listing and calling lineplot with dataframe
hd = df_gdp.index.tolist()
lineplot(df_gdp, hd)

# calling bargraph with dataframe
bargraph(df_subscriptions)

# calling piechart with dataframe
piechart(df_population)
