from export.file_path import FileUtils

SCRIPT_PATH = FileUtils.parent(__file__, 3)
blacklist_file_name = FileUtils.build_path(SCRIPT_PATH, "config")
print(SCRIPT_PATH)
print(blacklist_file_name)
