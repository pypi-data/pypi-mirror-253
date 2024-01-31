from conftest import get_tests_folder, get_data_path

import os.path

tests_folder_root = os.path.abspath(os.path.dirname(__file__))
data_folder_root = os.path.join(tests_folder_root, "data")


def test_get_tests_folder():

    tests_folder = get_tests_folder()
    assert os.path.samefile(tests_folder, tests_folder_root)


def test_get_tests_data_root_folder():

    data_folder = get_data_path()
    assert os.path.samefile(data_folder, data_folder_root)


def test_get_tests_data_routes_folder():

    routes_folder = get_data_path("routes")
    routes_folder_expected = os.path.join(data_folder_root, "routes")
    assert os.path.samefile(routes_folder, routes_folder_expected)
