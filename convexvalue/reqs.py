import json
import requests

from .const import *
from .utils import resultsToDataFrame

class ConvexValueResponse():
    request = None
    response = None
    status_code = None
    method = None
    cookies = None
    DATA = None

    def __init__(self, request, response):
        self.request = request
        self.response = response
        self.status_code = self.response.status_code
        self.method = self.request['method']
        self.cookies = self.response.cookies
        self.DATA = self.response.text
    
    def data(self):
        return json.loads(self.DATA)
    
    def json(self):
        return json.dumps(self.data())

    def df(self):
        return resultsToDataFrame(self.data())
    
    def plot(self):
        return self.df().plot()

    def __repr__(self):
        #return f'<ConvexValueResponse [{self.status_code}]>'
        return self
    
    def __str__(self):
        return self.json()
    
    def __dict__(self):
        return self.data()
    
def createSession(user_agent):
    s = requests.Session()

    s.headers.update({'user-agent': user_agent})

    return s

def makeRequest(session, method, url, params, body):
    return ConvexValueResponse(request={
            'method':method,
            'headers': session.headers,
            'url': url,
            'params': params,
            'body': body
        }, response=session.request(method, url, params=params, json=body))

def authenticateSession(session, email, password):
    body = {
        'email': email,
        'password': password
    }
    
    response = makeRequest(session, 'POST', CONST_LOGIN_URL, params=None, body=body)
    
    if response.status_code != 200:
        raise Exception(f'Failed to login: {response.status_code}')
    
    session.cookies.update(response.cookies)

    return session

def makeRequestQueryEndpoint(session, SQL_QUERY):
    response = makeRequest(session, 'POST', f'{CONST_API_URL}/query', params=None, body={'q': SQL_QUERY})

    if response.status_code != 200:
        raise Exception(f'Failed to query endpoint: {response.text}')

    return response