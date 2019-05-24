import psycopg2
from config_helper import ConfigHelper
from dump_helper import DumpHelper


def main():

    cfg_helper = ConfigHelper()
    cfg = cfg_helper.get_config()
    print cfg

    dmp_helper = DumpHelper()
    dump = dmp_helper.dump()
    print dump


if __name__ == '__main__':
    main()