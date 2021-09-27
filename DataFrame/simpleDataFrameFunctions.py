import pandas as pd
import math
import numpy as np

def dropUnnamedCol(df):
    """
    DF= col_1|col_2|Unnamed:1|Unnamed:2
        1    |42   |null     | null

    dropUnnamedCol(DF)
    OUTPUT:
    col_1|col_2
    1    |42


    :param df: DataFrame which you want to filter
    :return:
    """
    list_of_col=[]
    for col in df.columns:
        if not str(col).__contains__('Unnamed'):
            list_of_col.append(col)
    return df[list_of_col]


def dfNanDropper(dataFrame,ColumnName):
    """
    Usage:
    DF= col_1|col_2|col_3|col_4
        1    |42   |NaN  |Nan
        5    |23   |12   |Nan

    dfNanDropper(DF,"col_3")

    OUTPUT:
    col_1|col_2|col_3|col_4
    5    |23   |12   |Nan

    :param dataFrame: Dataframe
    :param ColumnName:  Name of column which is you want to drop nan values
    :return:
    """

    for i in range(0, len(dataFrame)):
        try:
            if math.isnan(dataFrame[ColumnName][i]):
                limit = i
                break
        except TypeError:
            if pd.isnull(dataFrame[ColumnName][i]):
                limit = i
                break

    for i in range(0, len(dataFrame)):
        if i >= limit:
            dataFrame = dataFrame.drop(index=i)
    return dataFrame

df=pd.DataFrame({
    'name': [
        "sds",
        "sdsddds",
        np.nan
    ],
    'surname': [
        np.nan,
        "dsds",
        "ddsds"
    ]

})
