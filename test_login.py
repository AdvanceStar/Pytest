import pytest
import time


class TestLogin:
    def test_01(self):
        # time.sleep(3)
        print("test 1")

if __name__ == "__main__":
    # pytest.main(['-vs', 'test_login.py', 'test_login.py'])

    # pytest.main(['-vs', './test_folder/test_folder_set_call.py::TestFolder::test_folder_main'])

    # pytest.main(['-vs', './test_folder/test_folder_set_call.py::test_04_func'])

    # pytest.main(['-vs', './test_folder', '-n=2'])

    pytest.main(['-vs', './test_folder', '-n=2', '--reruns=2'])
