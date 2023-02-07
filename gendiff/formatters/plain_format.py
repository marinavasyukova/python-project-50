from gendiff.tree_construction import get_name, get_children, get_value
from gendiff.tree_construction import get_status, is_branch
from gendiff.formatters.stylish_format import correct_value


def check_complex_value(value):
    if isinstance(value, str):
        value = f"'{value}'"
    if isinstance(value, dict):
        value = '[complex value]'
    return value


def make_str(name, value, status):
    result = ''
    if status == 'changed':
        old_value = check_complex_value(value['old'])
        new_value = check_complex_value(value['new'])
        result += f"Property '{name}' was updated. From "
        result += f"{correct_value(old_value)} to {correct_value(new_value)}\n"
    value = check_complex_value(value)
    if status == 'added':
        result += f"Property '{name}' was added "
        result += f"with value: {correct_value(value)}\n"
    if status == 'deleted':
        result += f"Property '{name}' was removed\n"
    return result


def plain(diff, name=''):
    result = ''
    for node in diff:
        if is_branch(node):
            for child in get_children(node):
                result += plain([child], name + f'{get_name(node)}.')
        else:
            if get_status(node, True) != 'equal':
                result += make_str(name + get_name(node),
                                   get_value(node), get_status(node, True))
    if name == '':
        result = result[:-1]
    return result
