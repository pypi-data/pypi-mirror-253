"""
@Project ：指纹识别 
@File    ：file_path.py
@IDE     ：PyCharm 
@Author  ：zhizhuo
@Date    ：2023/12/19 13:46 
"""
import os


class FileUtils:
    @staticmethod
    def build_path(*path_components):
        if path_components:
            path = os.path.join(*path_components)
        else:
            path = ""

        return path

    @staticmethod
    def get_abs_path(file_name):
        return os.path.abspath(file_name)

    @staticmethod
    def exists(file_name):
        return os.access(file_name, os.F_OK)

    @staticmethod
    def can_read(file_name):
        try:
            with open(file_name):
                pass
        except IOError:
            return False

        return True

    @classmethod
    def can_write(cls, path):
        while not cls.exists(path):
            path = cls.parent(path)

        return os.access(path, os.W_OK)

    @staticmethod
    def read(file_name):
        return open(file_name, "r").read()

    @classmethod
    def get_files(cls, directory):
        files = []

        for path in os.listdir(directory):
            path = os.path.join(directory, path)
            if cls.is_dir(path):
                files.extend(cls.get_files(path))
            else:
                files.append(path)

        return files

    @staticmethod
    def get_lines(file_name):
        with open(file_name, "r", errors="replace") as fd:
            return fd.read().splitlines()

    @staticmethod
    def is_dir(path):
        return os.path.isdir(path)

    @staticmethod
    def is_file(path):
        return os.path.isfile(path)

    @staticmethod
    def parent(path, depth=1):
        for _ in range(depth):
            path = os.path.dirname(path)

        return path

    @classmethod
    def create_dir(cls, directory):
        if not cls.exists(directory):
            os.makedirs(directory)

    @staticmethod
    def write_lines(file_name, lines, overwrite=False):
        if isinstance(lines, list):
            lines = os.linesep.join(lines)
        with open(file_name, "w" if overwrite else "a") as f:
            f.writelines(lines)


class PathInit(object):
    @staticmethod
    def SCRIPT_PATH():
        return FileUtils.parent(__file__, 3)
