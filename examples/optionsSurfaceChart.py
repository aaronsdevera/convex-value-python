# standard library imports
import os
# import convexvalue python lib
from convexvalue.core import CVObject
# import external libraries
import pandas as pd
import seaborn as sns

# seaborn theme
sns.set_theme(style='whitegrid')

# get API key from environment variables
API_KEY_ENV = os.environ.get('CV_API_KEY')

# configure the stock ticker symbol
SYMBOL = 'NET'
# configure the field we want-- for the "surface" chart, it's "volm" we need
FIELDS = 'volm'

# instantiate a CVObject
cvx = CVObject(API_KEY_ENV)

# get data using the getChain method
CVResponse = cvx.getChain(
    sym=SYMBOL,
    otm='true',
    stks=10000,
    exp='1',
    fields=FIELDS
)

# get the data from the CVObject response
optionsList = CVResponse['data']

# create a dataframe, with columns for strike price, columne, and flag (put/call)
df = pd.DataFrame(optionsList,columns=['strike', 'volm','flag'])

# we need to convert these columns to float/integer
df['strike'] = pd.to_numeric(df['strike'])
df['volm'] = pd.to_numeric(df['volm'])

# set up a seaborn plot, with differentiating colored lines for the flag
plt = sns.lineplot(data=df, x='strike', y='volm', hue='flag')

# create and save figure to disk
fig = plt.get_figure()
fig.savefig(f'plot_{SYMBOL}_strike_x_{FIELDS}.png')