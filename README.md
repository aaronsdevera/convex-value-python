# convex-value-python
Python API wrapper library for [Convex Value](https://convexvalue.com/) API.

Further Links:
* [Convex Value homepage](https://convexvalue.com/)
* [@ConvexValue on Twitter](https://twitter.com/convexvalue)
* [JB on Twitter](https://twitter.com/jbtobar_)

# Authentication
Use environment variables for your ConvexValue credentials. This will be used when instantiating a `ConvexValue`. 

Avoid hardcoding your credentials, set them as environment variables:
```
export CONVEX_VALUE_EMAIL=<email>
export CONVEX_VALUE_PASSWORD=<password>
```

## Using
```
# import the library
from convexvalue import ConvexValue

# instantiate a CV Object
cvx = ConvexValue()

# print out the flow rep for Cloudflare (NET)
print(cvx.getFlowRep('NET'))
```

## Supported methods

| Method Name | Description | Object Method | Parameters
| ----------- | ----------- | ----------- |  ----------- |
| getFlowTableParams | gets the available parameters for usage in fields and filters | `CVObject.getFlowTableParams()` | None
| getChain | gets the options chain for a symbol | `CVObject.getChain(sym: str, otm: str, stks: int, exp: str, fields: str)` | `sym`: symbol of the stock ticker, e.g. AAPl <br> `otm`: out-of-the-money, e.g. True <br> `stks`: e.g. 5 <br> exp: expiration dates, e.g. 1,2,3 <br> `fields`: fields to bring into chart, e.g. vol,delta,gamma 
| tasQuery | gets database result | `CVObject.tasQuery(lim: int, filters: str, root: str, dir: str, orderby: str)` | `lim`: limit of data, e.g. 100 <br>  `filters`: query filters, e.g. size>100 <br> `root`: symbol of stock, e.g. AAPL <br> dir: direction, e.g. desc <br> `orderby`: field to order by, e.g. size
| getSeries | gets simple series data for a symbol | `CVObject.getSeries(sym: str)` | `sym`: symbol of the stock ticker, e.g. AAPl
| activeOptionsQuery | gets the options database result | `CVObject.activeOptionsQuery(lim: int, filters: str, dir: str, orderby: str)` | `lim`: limit of data, e.g. 100 <br> `filters`: query filters, e.g. volm>100,delta<0.05,delta>0.05 <br> `dir`: direction, e.g. desc <br> `orderby`: field to order by, e.g. dayVolume
| getFlowTable | gets the options flow table | `CVObject.getFlowTable(lim: int, fields: str, cat: str, list: str, page: int, minprem: int, maxprem: int)` | `lim`: limit of data, e.g. 100  <br> `fields`: fields to bring into chart, e.g. value,price,volatility <br> `cat`: direction, e.g. ALL <br> `list`: field to order by, e.g. ALL <br> `page`: pagination marker, e.g. 1  <br> `minprem`: minium premium filter, e.g. 0 <br> `maxprem`: maximum premium filter, e.g. 0
| getFlowRep | gets the options flow rep | `CVObject.getFlowRep()`| None