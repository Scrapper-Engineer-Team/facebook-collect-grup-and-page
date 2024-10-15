import configparser
import os
import logging

class ConfigManager:
    def __init__(self, config_file="config.ini"):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.load_config()

    def load_config(self):
        """Load the configuration file"""
        if os.path.exists(self.config_file):
            self.config.read(self.config_file)
            logging.info(f"Configuration loaded from {self.config_file}")
        else:
            logging.error(f"{self.config_file} not found")
            raise FileNotFoundError(f"{self.config_file} not found")

    def get_cookies(self):
        """Read cookies from the config file"""
        try:
            return dict(self.config['cookies'])
        except KeyError as e:
            logging.error(f"Error reading cookies from config: {e}")
            raise

    def update_cookies(self, new_cookies):
        """Update cookies in the config file"""
        if not isinstance(new_cookies, dict):
            logging.error("new_cookies must be a dictionary")
            raise ValueError("new_cookies must be a dictionary")

        self.config['cookies'] = new_cookies
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)
        logging.info(f"Cookies updated in {self.config_file}")

