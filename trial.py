# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 16:03:21 2023

@author: abrah
"""
import pandas as pd
import scipy.stats


def dataframe(file, countries, years):
    """


    Parameters
    ----------
    file : TYPE
        DESCRIPTION.
    countries : TYPE
        DESCRIPTION.
    years : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """

    df = pd.read_csv(file, skiprows=4)
    df.drop(["Country Code", "Indicator Code", "Indicator Name"],
            axis=1, inplace=True)
    df.dropna(how='any', thresh=100, axis=1, inplace=True)
    df.set_index(['Country Name'], inplace=True)
    df.index.rename("Country", inplace=True)
    df.columns.name = "Year"
    df_t = df.transpose()
    df_t.dropna(how='all', axis=1, inplace=True)
    df = df.loc[countries, years]
    df_t = df_t.loc[years, countries]
    return df, df_t


def stat(df):
    """


    Parameters
    ----------
    df : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """

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


    Parameters
    ----------
    df : TYPE
        DESCRIPTION.
    kind : TYPE
        DESCRIPTION.
    name : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """

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
        ax.legend(fontsize=23)
    else:
        print("Only 'Line' or 'bar' plots available")
        plt.tight_layout()
        plt.savefig((name + ".png"), dpi=500)
        plt.show()
        return

countries = ["China", "India", "Greenland", "United States", "Nepal", "United Kingdom"]

years = [str(i) for i in range(2000, 2015)]

df, df_t = dataframe("electricity from oil, gas, coal.csv", countries, years)
co, co_t = dataframe("co2 emission per capita.csv", countries, years)

stat(df_t)

stat(co_t)

plotdf(df_t, "Line", "Electicity Produced from Oil, Gas, Coal (% of total)")

plotdf(co_t, "Line", "CO2 Emmission per capita")

years [str(i) for i in range(1994, 2015, 5)]

nu, nu t = dataframe("electricity from nuclear.csv", countries, years)


