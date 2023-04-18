from .__version__ import getVersion

CONST_PACKAGE_VERSION = getVersion()
CONST_USER_AGENT = f'ConvexValue Python Client v{CONST_PACKAGE_VERSION} - https://github.com/aaronsdevera/convex-value-python'

CONST_BASE_URL = 'https://convexvalue.com'
CONST_API_URL = f'{CONST_BASE_URL}/api'
CONST_LOGIN_URL = f'{CONST_BASE_URL}/login'
CONST_DEPRECATED_URL = 'https://vex.convexvalue.com'

