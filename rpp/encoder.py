from uuid import UUID
from scanner import Symbol

def tostr(value):
    if isinstance(value, Symbol):
        return str(value)
    elif isinstance(value, str):
        return '"%s"' % value
    elif isinstance(value, UUID):
        return '{%s}' % value
    elif value is None:
        return '-'
    else:
        return str(value)

def encode(lists, indent=2, level=0):
    result = '<'
    for i, item in enumerate(lists):
        if not isinstance(item, list):
            raise TypeError("%r is not RPP serializable" % item)
        if i > 0:
            result += ' ' * (level + 1) * indent
        if all(not isinstance(x, list) for x in item):
            name, values = item[0].upper(), item[1:]
            strvalues = map(tostr, values)
            result += ' '.join([name] + strvalues)
        else:
            result += encode(item, level=(level + 1))
        result += '\n' if indent else ' '
    result += (' ' * level * indent) + '>'
    return result
