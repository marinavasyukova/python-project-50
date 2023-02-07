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
