from os import getenv
"""
Main configuration class for CSCL API App
    Configuration defaults are set for local development.
"""
MONGO_URL = getenv('CSCL_MONGO_URL', 'mongodb://mongo')
MONGO_USER = getenv('CSCL_MONGO_USER', 'mongo')
MONGO_PASS = getenv('CSCL_MONGO_PASS', 'supersecretpass')
CORS = getenv('CSCL_CORS_DOMAINS', '*')
