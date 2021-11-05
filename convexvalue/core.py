from urllib.parse import urlencode
import requests

class CVObject:

    def __init__(self, user_input_api_key: str):
        self.API_KEY = user_input_api_key
        self.BASE_URL = 'https://vex.convexvalue.com/api/'
    
    class utils:
        def addAPIKey(self,params: dict):
            params.update({'ak':self.API_KEY})
            return params

        def processParams(self,params: dict):
            return urlencode(params)

        def joinURL(self,uri_path: str):
            return self.BASE_URL+uri_path

        def getURL(self, endpoint: str, params: dict):
            params = self.utils.addAPIKey(self,params)
            uri_path = f'{endpoint}?{self.utils.processParams(self,params)}'
            url = self.utils.joinURL(self,uri_path).replace('%2C',',').replace('%3E','>').replace('%3C','<')
            return url

        def makeRequest(self,target_url: str):
            headers = {
                'Host': 'vex.convexvalue.com:443',
                'Proxy-Connection': 'keep-alive',
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_0) AppleWebKit/537.36 (KHTML, like Gecko) ConvexValueMUX/4.0.7 Chrome/87.0.4280.141 Electron/11.4.3 Safari/537.36'
            }
            r = requests.get(target_url,headers=headers)
            if r.status_code == 200:
                if r.text:
                    try:
                        return r.json()
                    except:
                        return {'status':400,'message':r.text}
    
    def getFlowTableParams(self):
        endpoint = 'flowtableparams'

        params = {}
        
        target_url = self.utils.getURL(self,endpoint,params)
        
        return self.utils.makeRequest(self,target_url)
    
    def getChain(self, sym: str, otm: str, stks: int, exp: str, fields: str):
        '''
        getChain - gets the options chain for a symbol
        ----------
        PARAMS
        ----------
        sym: symbol of the stock ticker, e.g. AAPl
        otm: out-of-the-money, e.g. True
        stks: e.g. 5
        exp: expiration dates, e.g. 1,2,3
        fields: fields to bring into chart, e.g. vol,delta,gamma
        '''
        endpoint = 'chain'

        params = {
            'sym':sym,
            'otm': otm,
            'stks': stks,
            'exp': exp,
            'fields': fields
        }

        target_url = self.utils.getURL(self,endpoint,params)

        return self.utils.makeRequest(self,target_url)

    def tasQuery(self, lim: int, filters: str, root: str, dir: str, orderby: str):
        '''
        tasQuery - gets database result
        ----------
        PARAMS
        ----------
        lim: limit of data, e.g. 100
        filters: query filters, e.g. size>100
        root: symbol of stock, e.g. AAPL
        dir: direction, e.g. desc
        orderby: field to order by, e.g. size
        '''
        endpoint = 'tasdb'

        params = {
            'lim':lim,
            'filters': filters,
            'root': root,
            'dir': dir,
            'orderby': orderby
        }

        target_url = self.utils.getURL(self,endpoint,params)
        return self.utils.makeRequest(self,target_url)

    def getSeries(self, sym: str):
        endpoint = 'series'

        params = {
            'sym':sym
        }
        
        target_url = self.utils.getURL(self,endpoint,params)
        
        return self.utils.makeRequest(self,target_url)
    
    def activeOptionsQuery(self, lim: int, filters: str, dir: str, orderby: str):
        '''
        activeOptionsQuery - gets the options database result
        ----------
        PARAMS
        ----------
        lim: limit of data, e.g. 100
        filters: query filters, e.g. volm>100,delta<0.05,delta>0.05
        dir: direction, e.g. desc
        orderby: field to order by, e.g. dayVolume
        '''
        endpoint = 'optdb'

        params = {
            'lim':lim,
            'filters': filters,
            'dir': dir,
            'orderby': orderby
        }

        target_url = self.utils.getURL(self,endpoint,params)
        return self.utils.makeRequest(self,target_url)
    
    def getFlowTable(self, lim: int, fields: str, cat: str, list: str, page: int, minprem: int, maxprem: int):
        '''
        getFlowTable - gets the options flow table
        ----------
        PARAMS
        ----------
        lim: limit of data, e.g. 100
        fields: fields to bring into chart, e.g. value,price,volatility
        cat: direction, e.g. ALL
        list: field to order by, e.g. ALL
        page: pagination marker, e.g. 1
        minprem: minium premium filter, e.g. 0
        maxprem: maximum premium filter, e.g. 0
        '''
        endpoint = 'flowtable'

        params = {
            'limit':lim,
            'fields': fields,
            'cat': cat,
            'list': list,
            'page': page,
            'minprem': minprem,
            'maxprem': maxprem
        }

        target_url = self.utils.getURL(self,endpoint,params)
        return self.utils.makeRequest(self,target_url)

    def getFlowRep(self):
        '''
        getFlowRep - gets the options flow rep
        ----------
        PARAMS
        ----------
        '''
        endpoint = 'flowrep'

        params = {}

        target_url = self.utils.getURL(self,endpoint,params)
        return self.utils.makeRequest(self,target_url)
