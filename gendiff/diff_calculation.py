import json


def make_string(key, value):
    if isinstance(value, bool):
        value = str(value).lower()
    return (f'{key}: {value}')


def generate_diff(first_path, second_path):
    first_file = json.load(open(first_path))
    second_file = json.load(open(second_path))
    result = '{\n'
    keys_1 = set(first_file.keys())
    keys_2 = set(second_file.keys())
    unique_keys = sorted(list(keys_1.union(keys_2)))
    for k in unique_keys:
        if k in first_file and k not in second_file:
            result += f'- {make_string(k, first_file[k])}\n'
        elif k not in first_file and k in second_file:
            result += f'+ {make_string(k,second_file[k])}\n'
        else:
            if first_file[k] == second_file[k]:
                result += f'  {make_string(k, first_file[k])}\n'
            else:
                result += f'- {make_string(k, first_file[k])}\n+ {make_string(k,second_file[k])}\n'
    result += '}'
    return result

# print(generate_diff(first_file, second_file))

# print(make_string('follow', True))
