import configparser
import os

class ConfigManager:
    def __init__(self, config_file="config.ini"):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            self.config.read(self.config_file)
        else:
            raise FileNotFoundError(f"{self.config_file} not found")

    def get_cookies(self):
        """Membaca cookies dari file config"""
        return dict(self.config['cookies'])

    def update_cookies(self, new_cookies):
        """Memperbarui cookies di file config"""
        self.config['cookies'] = new_cookies
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)