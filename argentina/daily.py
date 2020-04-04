 
def daily(df):
    return df[df.case == 'CONFIRMADO'].reset_index().groupby(['index', 'place']).sum().unstack().fillna(0)
