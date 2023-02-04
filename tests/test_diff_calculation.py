from gendiff import generate_diff


def test_generate_diff():
    first_path = '/Users/marina/hexlet/python-project-50/tests/fixtures/file1.json'
    second_path = '/Users/marina/hexlet/python-project-50/tests/fixtures/file2.json'
    result = open('/Users/marina/hexlet/python-project-50/tests/fixtures/result_json', 'r') 
    assert generate_diff(first_path, second_path) == result.read()