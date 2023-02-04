from gendiff import generate_diff


def test_generate_diff():
    first_path = 'tests/fixtures/file1.json'
    second_path = 'tests/fixtures/file2.json'
    result = open('tests/fixtures/result_json', 'r') 
    assert generate_diff(first_path, second_path) == result.read()