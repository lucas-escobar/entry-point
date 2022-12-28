import configparser as conf


def get_data_path():
    c = conf.ConfigParser()
    c.read('./config/config.ini')
    return c['Paths']['data_path']
