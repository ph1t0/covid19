 
def daily_new_cases(df):
    news = df[df.case == 'CONFIRMADO'].reset_index().groupby(['index', 'place']).sum().unstack().fillna(0)
    news.columns = news.columns.droplevel()
    return news
