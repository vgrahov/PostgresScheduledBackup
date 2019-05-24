import yaml


class ConfigHelper:
    def __init__(self, **kwargs):
        self.filname = kwargs.get("filename", "config.yml")
        self.loader = yaml.FullLoader

    def get_config(self):
        try:
            with open(self.filname,'r') as config_handler:
                cfg = yaml.load(config_handler, self.loader)
                return cfg
        except IOError:
            print "An error occurred while read file!"
            return None