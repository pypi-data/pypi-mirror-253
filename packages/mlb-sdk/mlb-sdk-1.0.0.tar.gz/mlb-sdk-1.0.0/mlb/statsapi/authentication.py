''' Module defines the behind the scenese token handling'''

import logging
import configparser
import os
import requests
import cachetools.func
from mlb.statsapi.settings import (
    BASE_URL, TIMEOUT, TOKEN_LIFETIME, ENVIRONMENT_VARIABLES, DEFAULT_CONFIG_PATH
)

LOGGER = logging.getLogger("mlb.statsapi.auth")

class Auth:
    
    def __init__(self):
        self.configure()
        
    def configure(self, email=None, password=None, profile_name=None):
        if profile_name and (email or password):
            raise ValueError("cannot specify both a profile_name and manual credentials")
        
        if (email and not password) or (password and not email):
            raise ValueError("mlb.auth.configure(...) requires both an email and a password")
        
        if email and password:
            self.method = "passed-credentials"
            self.email = email
            self.password = password
            self.profile_name = None
            LOGGER.debug(f"credentials passed to the configure method")
            return
            
        environment_variables_present = (
            ENVIRONMENT_VARIABLES.EMAIL in os.environ and
            ENVIRONMENT_VARIABLES.PASSWORD in os.environ
        )
        
        if environment_variables_present:
            self.method = "environment-variables"
            self.email = os.environ.get(ENVIRONMENT_VARIABLES.EMAIL)
            self.password = os.environ.get(ENVIRONMENT_VARIABLES.PASSWORD)
            self.profile_name = None
            LOGGER.debug(f"credentials found in environment variables")
            return
        
        config_path = os.environ.get(
            ENVIRONMENT_VARIABLES.CONFIG_PATH,
            DEFAULT_CONFIG_PATH
        ).replace("~", os.path.expanduser('~'))
        
        profile_name = profile_name if profile_name else "default"
        config = configparser.ConfigParser()
        config.read(config_path)
        
        if not profile_name in config:
            LOGGER.warning(f" profile_name '{profile_name}' not found in config path '{config_path}' - mlb sdk will not work")
            self.method = None
            self.email = None
            self.password = None
            self.profile_name = None
            return

        self.method = "config-file"
        self.email = config[profile_name].get("email")
        self.password = config[profile_name].get("password")
        self.profile_name = profile_name
        LOGGER.debug(f"credentials found in '{config_path}' profile_name '{profile_name}'")
        return 

        # except Exception as e:
            


    @cachetools.func.ttl_cache(ttl=TOKEN_LIFETIME)
    def token(self):
        '''
        token
        '''
        url = f"{BASE_URL}/v1/authentication/okta/token"
        result = requests.post(
            url,
            auth=(
                self.email,
                self.password,
            ),
            timeout=TIMEOUT)
        result.raise_for_status()
        return result.json()

    def get_headers(self):
        '''
        token
        '''
        return {
            "Authorization": f"Bearer {self.token().get('access_token')}"
        }


# singleton object to hold the credentials information
auth = Auth()
