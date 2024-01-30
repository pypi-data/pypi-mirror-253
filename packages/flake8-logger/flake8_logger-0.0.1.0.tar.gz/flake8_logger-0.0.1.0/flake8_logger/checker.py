from .version import __version__
from re import compile
from six import string_types
from ast import walk, Call, Name, Attribute, Str, Dict

try:
    from ast import Starred
except ImportError:
    Starred = None

LG010 = "LG010 the number of arguments for log.* is wrong."
LG011 = "LG011 the dict argument for log.* does not match with the format."
LG012 = "LG012 the dict argument for log.* contains non-str key."

class LoggerChecker(object):
    name = 'flake8_logger'
    version = __version__
    __fmtpattern = compile(r'%\(.*?\)')

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        for node in walk(self.tree):
            if not isinstance(node, Call):
                continue
            if not isinstance(node.func, Attribute):
                continue
            value = node.func.value
            while isinstance(value, Attribute):
                value = value.value
            if not isinstance(value, Name):
                continue
            if value.id not in ('log', 'logger', 'logging'):
                continue
            if node.func.attr in ('critical', 'exception', 'error', 'warn', 'warning', 'info', 'debug', 'verbose'):
                if len(node.args) == 0:
                    continue
                if not isinstance(node.args[0], Str):
                   # log argument is formatted by '%' or .format
                    continue
                fmt = node.args[0].s
                args = list(node.args[1:])
            elif node.func.attr == 'log':
                if len(node.args) < 2:
                    # actually invalid
                    continue
                # todo check node.args[0]
                if not isinstance(node.args[1], Str):
                   # log argument is formatted by '%' or .format
                    continue
                fmt = node.args[1].s
                args = list(node.args[2:])
            else:
                continue
            hasNArgs = False
            if getattr(node, 'starargs', None) is not None:  # Py2
                # args += getattr(node.starargs, 'elts', [])
                hasNArgs = True
            if len(args) > 0 and Starred is not None and isinstance(args[-1], Starred):  # Py3
                starargs = args.pop(-1).value
                # args += getattr(starargs, 'elts', [])
                hasNArgs = True
            if len(args) == 1 and isinstance(args[0], Dict):
                keys = [getattr(key, 's', None) for key in args[0].keys]
                if None not in keys and all(isinstance(key, string_types) for key in keys):
                    fmtKeys = [e[2:-1] for e in self.__fmtpattern.findall(fmt)]
                    if set(str(key) for key in keys) == set(str(key) for key in fmtKeys):
                        continue
                    else:
                        yield node.lineno, node.col_offset, LG011, type(self)
                else:
                    yield node.lineno, node.col_offset, LG012, type(self)
            numArgs = fmt.count('%') - 2*fmt.count('%%')
            if numArgs == len(args):
                continue
            if hasNArgs and numArgs >= len(args):
                continue
            yield node.lineno, node.col_offset, LG010, type(self)
