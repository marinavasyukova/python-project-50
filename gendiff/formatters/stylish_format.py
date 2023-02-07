from gendiff.tree_construction import get_name, get_children, get_value
from gendiff.tree_construction import get_status, is_leaf


def correct_value(value):
    if isinstance(value, bool):
        value = str(value).lower()
    if value is None:
        value = 'null'
    return value


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
