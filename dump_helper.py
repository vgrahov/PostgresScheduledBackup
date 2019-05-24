import subprocess
import datetime


class DumpHelper:
    def __init__(self, **kwargs):
        self.host = kwargs.get("host","localhost")
        self.db_user = kwargs.get("db_user","postgres")
        self.db_name = kwargs.get("db_name","postgres")
        self.destination_path = kwargs.get("destination_path", "/tmp")
        self.date = kwargs.get("date", datetime.datetime.now().strftime("%Y-%m-%d-%H.%M.%S"))
        self.filename = kwargs.get("filename",self.db_name + '-' + self.date + '.tar.gz')

    def dump(self):
        cmd = 'cd ' + self.destination_path + \
              ' && '+'pg_dump -h {0} -U {1} --clean --create --format=t {2} | gzip > {3}'\
              .format(self.host, self.db_user, self.db_name, self.filename)

        return cmd

