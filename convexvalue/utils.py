import os
import pandas as pd

def getCredentials():
    email = os.environ.get('CONVEX_VALUE_EMAIL')
    password = os.environ.get('CONVEX_VALUE_PASSWORD')

    if email and password:
        return (email, password)
    else:
        return (None , None)
    
def resultsToDataFrame(results):
    import pandas as pd
    return pd.DataFrame(results[1], columns=results[0])