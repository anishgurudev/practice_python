import sys
import os
# sys.path.append(os.path.dirname(os.path.abspath(r"F:\Anish\PycharmProjects\PythonProjects\practice_python\Tests\2026\Fundamental\module_project_structure\project2\utils\file_utils.py")))
from ..utils.file_utils import read_json
# sys.path.append(os.path.dirname(os.path.abspath(r"F:\Anish\PycharmProjects\PythonProjects\practice_python\Tests\2026\Fundamental\module_project_structure\project2\utils\file_utils.py")))
from ..utils.loggers import log

def login(username, password, valid_users):
    for user in valid_users:
        if username == user["username"] and password == user["password"]:
            return True
    return False


def test_login():
    users = read_json("data/users.json")

    passed = []
    failed = []

    for user in users:
        result = login(user["username"], user["password"], users)

        if result:
            log(f"Login success for {user['username']}", "PASS")
            passed.append(user["username"])
        else:
            log(f"Login failed for {user['username']}", "FAIL")
            failed.append(user["username"])

    return passed, failed
