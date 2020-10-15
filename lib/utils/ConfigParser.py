import configparser


class ConfigParser(object):

    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def safe_set(self, section, option, value):
        if self.config.has_section(section):
            self.config.set(section, option, str(value))
        else:
            self.config.add_section(section)
            self.config.set(section, option, str(value))

    def safe_get(self, section, option):
        if self.config.has_option(section, option):
            return self.config.get(section, option)
        else:
            return None

    def get_all_options(self, section):
        return dict(self.config.items(section))


#cfg = ConfigParser("/API_Automation/pytest-qbep-automation/config/config.cfg")
#print(cfg.get_all_options('KAFKA.TOPIC'))