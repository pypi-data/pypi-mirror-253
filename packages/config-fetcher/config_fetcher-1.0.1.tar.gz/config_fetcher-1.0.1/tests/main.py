from configparser import ConfigParser
from config_fetcher import ConfigFetcher

if __name__ == '__main__':
    cf = ConfigFetcher('config.cf')
    cf.print_values()