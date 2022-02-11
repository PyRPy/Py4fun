# SPY 500 
"""

template from youtube:
https://www.youtube.com/watch?v=YjpGdFwIAxg

"""
import pandas as pd 
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
df = pd.read_html(url)
df = df[0]

print('--------------------------------')
print(df.head(10))

print('How many companies: ', len(df.Symbol))