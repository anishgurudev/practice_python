import sys
import os
# Add project root to path
# sys.path.append(os.path.dirname(os.path.abspath(r"F:\Anish\PycharmProjects\PythonProjects\practice_python\Tests\2026\Fundamental\module_project_structure\project2\tests\test_login.py")))
from ..tests.test_login import test_login
# sys.path.append(os.path.dirname(os.path.abspath(r"F:\Anish\PycharmProjects\PythonProjects\practice_python\Tests\2026\Fundamental\module_project_structure\project2\utils\file_utils.py")))
from ..utils.loggers import log

def run_tests():
    log("Starting Test Execution")

    passed, failed = test_login()

    log(f"Passed Users: {passed}", "INFO")
    log(f"Failed Users: {failed}", "INFO")

    log("Test Execution Completed")


if __name__ == "__main__":
    run_tests()