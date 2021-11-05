import os
from convexvalue.core import CVObject

API_KEY_ENV = os.environ.get('CV_API_KEY')

cvx = CVObject(API_KEY_ENV)

test = cvx.getSeries('NET')

test = cvx.getFlowTableParams()

test = cvx.getChain(
    sym='NET',
    otm='true',
    stks=5,
    exp='1,2,3',
    fields='vol,delta,gamma'
)

test = cvx.tasQuery(
    lim=10,
    filters='size>100',
    root='AAPL',
    dir='desc',
    orderby='size'
)

test = cvx.activeOptionsQuery(
    lim=10,
    filters='volm>100,delta<0.05,delta>0.05',
    dir='desc',
    orderby='dayVolume'
)

test = cvx.getFlowTable(
    lim=10,
    fields='value,price,volatility',
    cat='desc',
    list='dayVolume',
    page=1,
    minprem=0,
    maxprem=0
)

test = cvx.getFlowRep()

print(
    test
)