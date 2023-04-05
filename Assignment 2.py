# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 16:03:21 2023

@author: abrah
"""
import pandas as pd
from scipy.stats import skew, kurtosis
import matplotlib.pyplot as plt
from matplotlib import cm
import seaborn as sns


def dataframe(file, countries, years):
    """
    Function to read all the csv files and return two dataframes, one with
    'years' and the other with 'countries' as columns. 'filename' is taken as
    the argument.
    """

    # read files into a dataframe
    df = pd.read_csv(file, skiprows=4)
    # cleaning the empty columns
    df.drop(["Country Code", "Indicator Code", "Indicator Name"],
            axis=1, inplace=True)
    df.dropna(how='any', thresh=100, axis=1, inplace=True)
    # setting and renaming the index
    df.set_index(['Country Name'], inplace=True)
    df.index.rename("Country", inplace=True)
    df.columns.name = "Year"
    # transposing
    df_t = df.transpose()
    df_t.dropna(how='all', axis=1, inplace=True)
    df = df.loc[countries, years]
    df_t = df_t.loc[years, countries]
    return df, df_t


def stat(df):
    """
    Function to do some basic statistics on the dataframes. Takes the
    dataframe with 'countries' as columns as the argument.
    """
    # generating statistical summary
    des = df.describe()
    sk = skew(df)
    kurt = kurtosis(df)
    sk = pd.DataFrame([sk], columns=des.columns, index=["skewness"])
    kurt = pd.DataFrame([kurt], columns=des.columns, index=["kurtosis"])
    stat = pd.concat([des, sk, kurt])
    print(stat)
    return


def plotdf(df, kind, name):
    """
    Function to plot the dataframes using the 'dataframe.plot' method.

    Arguments:
        The dataframe to be plotted.
        The kind of plot required.
        The title of the figure.
        The color scheme for the plot.
    """
    # using conditional statements for different kinds of plots
    if kind == "Line":
        ax = df.plot(subplots=True, figsize=(8, 9), fontsize=18, grid=True)
        ax[0].set_title(name, fontsize=20.5, fontweight='bold')
        ax[-1].set_xlabel(str(df.index.name), fontsize=25)
        for i in range(0, len(ax)):
            ax[i].legend(fontsize=14)
    elif kind == "bar":
        ax = df.plot.bar(rot=40, figsize=(10, 9), fontsize=18,
                         width=0.6, edgecolor='black')
        ax.set_title(name, fontsize=22, fontweight='bold')
        ax.set_xlabel(str(df.index.name), fontsize=28)
        ax.legend(fontsize=15)
    else:
        print("Only 'Line' or 'bar' plots available")
        plt.tight_layout()
        # saving and showing the plot
        plt.savefig((name + ".png"), dpi=500)
        plt.show()
        return


def makeheatmap(filename, country, indicators, c):
    """
    Function to plot the heatmap of a country's indicators.
    Parameteres:
        The country of which the heatmap is plotted.
        The color scheme.
        Reading the file with all indicators and countries.
    """

    # making the dataframe to be calculated for correlation
    df0 = pd.read_csv(filename, skiprows=4)
    df0.drop(columns=["Country Code", "Indicator Code"], inplace=True)
    # setting multi-index to easily select the country
    df0.set_index(["Country Name", "Indicator Name"], inplace=True)
    df1 = df0.loc[country].fillna(0).T
    # slicing the dataframe to have only the years with nonzero data
    df = df1.loc["1970":"2015", indicators]
    # renaming the columns for better visualization
    df.rename(columns={
        "Nitrous oxide emissions (thousand metric tons of CO2 equivalent)":
            "N20 Emissions",
            "Energy use (kg of oil equivalent per capita)":
                "Energy Use",
                "Forest area (% of the land area)":
                    "Forest (% of the land area)"
            }, inplace=True)
    # plotting the heatmap
    plt.figure(figsize=(6, 4))
    sns.heatmap(df.corr(), cmap=c, annot=True)
    plt.xticks(rotation=90)
    # setting a title and saving the figure
    plt.title(country,  fontweight='bold', fontsize='x-large',
              fontname="Times New Roman")
    plt.savefig(country+"'s Heatmap"+".png", dpi=350,
                bbox_inches='tight', pad_inches=.5)

    return


# countries to be plotted
countries = ["China", "India", "Australia", "United States",
             "Brazil", "United Kingdom"]
# years to be plotted for line
years = [str(i) for i in range(2000, 2013)]

# calling the files to be read
df, df_t = dataframe("nitrous_oxide.csv",
                     countries, years)

# using statistical function
stat(df_t)

# plotting the file according to the kind
plotdf(df_t, "Line", "Nitrous Oxide Emissions (% change)")

# years to be plotted for bar
years = [str(i) for i in range(1994, 2015, 5)]

# reading the files
ec, ec_t = dataframe("eletricity_from_coal.csv", countries, years)
ug, ug_t = dataframe("urban_growth.csv", countries, years)

# using statistical function
stat(ec_t)
stat(ug_t)

# plotting the file according to the kind
plotdf(ec, "bar", "Electicity Produced from Coal (% of total)")
plotdf(ug_t, "bar", "Urban Population Growth (annual %)")

# assigning indicators for the heatmaps
indicators = [
    "Urban population", "Arable land (% of land area)",
    "Forest area (% of land area)",
    "Nitrous oxide emissions (thousand metric tons of CO2 equivalent)",
    "CO2 emissions (kt)",
    "Energy use (kg of oil equivalent per capita)"]

# plotting the heatmaps
makeheatmap("co2_emission.csv", "China", indicators, cm.jet)
makeheatmap("co2_emission.csv", "Brazil", indicators, cm.bone)
