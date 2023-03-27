import json
import yaml
from gendiff.tree_construction import mkleaf, mkbranch
from gendiff.formatters.stylish_format import stylish
from gendiff.formatters.plain_format import plain


def open_file(file_path):
    with open(file_path) as file:
        if file_path.endswith('.json'):
            return json.load(file)
        if file_path.endswith('.yaml') or file_path.endswith('.yml'):
            return yaml.load(file, Loader=yaml.Loader)


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


def generate_diff(first_path, second_path, format_name='stylish'):
    first_file = open_file(first_path)
    second_file = open_file(second_path)
    if format_name == 'json':
        return json.dumps(gen_diff(first_file, second_file), indent=4)
    if format_name == 'plain':
        return plain(gen_diff(first_file, second_file))
    return stylish(gen_diff(first_file, second_file))
