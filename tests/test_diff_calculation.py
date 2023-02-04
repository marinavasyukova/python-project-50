from gendiff import generate_diff


def test_generate_diff():
    first_json = 'tests/fixtures/file1.json'
    second_json = 'tests/fixtures/file2.json'
    first_yaml = 'tests/fixtures/file1.yaml'
    second_yaml = 'tests/fixtures/file2.yaml'
    result = open('tests/fixtures/result_json', 'r') 
    assert generate_diff(first_json, second_json) == result.read()
    assert generate_diff(first_yaml, second_yaml) == result.read()