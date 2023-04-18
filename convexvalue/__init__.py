from .const import *
from .utils import getCredentials
from .reqs import *


class ConvexValue:
    PACKAGE_VERSION = None
    USER_AGENT = None

    CONVEX_VALUE_EMAIL, CONVEX_VALUE_PASSWORD = '', ''

    CONVEX_VALUE_SESSION = None

    def __init__(self):
        self.PACKAGE_VERSION = CONST_PACKAGE_VERSION
        self.USER_AGENT = CONST_USER_AGENT
        
        self.CONVEX_VALUE_EMAIL, self.CONVEX_VALUE_PASSWORD = getCredentials()
        
        self.CONVEX_VALUE_SESSION = authenticateSession(createSession(self.USER_AGENT),email=self.CONVEX_VALUE_EMAIL,password=self.CONVEX_VALUE_PASSWORD)

    def query_sql(self, SQL_QUERY: str = None):
        '''
        Query the ConvexValue API with a SQL query.
        The available tables are in a CSV format below:
        
        schema,name,type
        public,daylist,materialized view
        public,futrootdir,table
        public,opt_dir,table
        public,opt_full,materialized view
        public,opt_full_view,view
        public,opt_greeks,table
        public,opt_oich,materialized view
        public,opt_profile,table
        public,opt_quote,table
        public,opt_summary,table,
        public,opt_tas,table
        public,opt_trade,table
        public,opth,table
        public,opth_exps,materialized view
        public,tas,table
        public,tash,table
        public,trm,table
        public,trmh,table
        public,und_dir,table
        public,und_flow,table
        public,und_full,materialized view
        public,und_full_view,view
        public,und_profile,table
        public,und_quote,table
        public,und_summary,table
        public,und_tas,table
        public,und_trade,table
        public,und_underlying,table
        public,undh,table
        '''
        if SQL_QUERY:
            return makeRequestQueryEndpoint(self.CONVEX_VALUE_SESSION, SQL_QUERY)
        else:
            raise Exception('No SQL query provided.')