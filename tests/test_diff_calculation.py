from gendiff import generate_diff


def test_generate_diff_plain_json():
    first_json = 'tests/fixtures/file1_plain.json'
    second_json = 'tests/fixtures/file2_plain.json'
    f = open('tests/fixtures/result_plain', 'r')
    result = f.read()
    f.close()
    assert generate_diff(first_json, second_json) == result


def test_generate_diff_plain_yaml():
    first_yaml = 'tests/fixtures/file1_plain.yaml'
    second_yaml = 'tests/fixtures/file2_plain.yaml'
    f = open('tests/fixtures/result_plain', 'r')
    result = f.read()
    f.close()
    assert generate_diff(first_yaml, second_yaml) == result


def test_generate_diff_nested_json():
    first_json = 'tests/fixtures/file1_nested.json'
    second_json = 'tests/fixtures/file2_nested.json'
    f = open('tests/fixtures/result_nested', 'r')
    result = f.read()
    f.close()
    assert generate_diff(first_json, second_json) == result


def test_generate_diff_nested_yaml():
    first_yaml = 'tests/fixtures/file1_nested.yaml'
    second_yaml = 'tests/fixtures/file2_nested.yaml'
    f = open('tests/fixtures/result_nested', 'r')
    result = f.read()
    f.close()
    assert generate_diff(first_yaml, second_yaml) == result