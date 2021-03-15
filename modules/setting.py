import os

from appdirs import AppDirs


class GetDirs:
    def __init__(self, appname, appauthor):
        self.appname = appname
        self.appauthor = appauthor
        self.dirs = {}

    def get_dirs(self):
        dir = AppDirs(self.appname, self.appauthor)
        self.dirs["userData"] = dir.user_data_dir
        self.dirs["userLog"] = dir.user_log_dir
        self.make_dir()
        return self.dirs

    def make_dir(self):
        for dir in self.dirs:
            try:
                os.makedirs(self.dirs[dir], exist_ok=True)
            except OSError:
                pass
        return True


def getDirs(appname, appauthor):
    get_dirs = GetDirs(appname, appauthor)
    return get_dirs.get_dirs()
