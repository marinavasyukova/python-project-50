import json
import yaml


def mkleaf(name, status, value):
    return {
        'name': name,
        'type': 'leaf',
        'status': status,
        'value': value
    }


def mkbranch(name, children=[]):
    return {
        'name': name,
        'type': 'branch',
        'children': children
    }


def is_branch(node):
    return node['type'] == 'branch'


def is_leaf(node):
    return node['type'] == 'leaf'


def correct_value(value):
    if isinstance(value, bool):
        value = str(value).lower()
    if value is None:
        value = 'null'
    return value


def get_children(branch):
    return branch.get('children', [])


def get_name(node):
    return node['name']


def get_value(node):
    return node['value']


def get_status(node, full=False):
    s = {'added': '+', 'deleted': '-', 'changed': ['-', '+'], 'equal': ' '}
    if full:
        return node['status']
    else:
        return s[node['status']]


def open_file(file_path):
    if file_path.endswith('.json'):
        return json.load(open(file_path))
    if file_path.endswith('.yaml') or file_path.endswith('.yml'):
        return yaml.load(open(file_path), Loader=yaml.Loader)


def gen_diff(first_file, second_file):
    diff = []
    keys_1 = set(first_file.keys())
    keys_2 = set(second_file.keys())
    unique_keys = sorted(list(keys_1.union(keys_2)))
    for k in unique_keys:
        if k in first_file and k not in second_file:  # deleted
            diff.append(mkleaf(k, 'deleted', first_file[k]))
        elif k not in first_file and k in second_file:  # added
            diff.append(mkleaf(k, 'added', second_file[k]))
        else:  # check equality
            if first_file[k] == second_file[k]:
                diff.append(mkleaf(k,
                                   'equal', first_file[k]))
            elif isinstance(first_file[k], dict
                            ) & isinstance(second_file[k], dict):  # recursion
                diff.append(mkbranch(k,
                            gen_diff(first_file[k], second_file[k])))
            else:  # different
                diff.append(mkleaf(k, 'changed', {
                    'old': first_file[k],
                    'new': second_file[k]}))
    return diff


def make_str(name, value, status, acc=0):
    result = ''
    if isinstance(status, list):  # if node changed
        result += make_str(name, value['old'], '-', acc)
        result += make_str(name, value['new'], '+', acc)
    elif isinstance(value, dict):
        result += f'  {"    "*acc}{status} {name}: '
        result += '{\n'
        for k, v in value.items():
            result += make_str(k, v, ' ', acc + 1)
        result += f'{"    "*(acc+1)}'
        result += '}\n'
    else:
        result += f'  {"    "*acc}{status} {name}: {correct_value(value)}\n'
    return result


def stylish(diff, acc=0, sep=' '):
    result = ''
    if acc == 0:
        result += '{\n'
    for node in diff:
        if is_leaf(node):
            result += make_str(get_name(node),
                               get_value(node), get_status(node), acc)
        else:
            result += f'{"    "*(acc+1)}{get_name(node)}: '
            result += '{\n'
            for child in get_children(node):
                result += stylish([child], acc + 1)
            result += f'{"    "*(acc+1)}'
            result += '}\n'
    if acc == 0:
        result += '}'
    return result


def generate_diff(first_path, second_path):
    first_file = open_file(first_path)
    second_file = open_file(second_path)
    return stylish(gen_diff(first_file, second_file))
