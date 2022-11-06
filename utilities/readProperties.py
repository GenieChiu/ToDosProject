import configparser

config = configparser.RawConfigParser()
config.read(".\\congfigurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url
    