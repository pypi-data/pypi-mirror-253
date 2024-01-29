from .version import __version__
from ast import walk, Call, Name, Dict, Attribute

class IteritemsChecker(object):
    name = 'flake8_iteritems'
    version = __version__

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        for node in walk(self.tree):
            if not isinstance(node, Call):
                continue
            # if isinstance(node.func, Name) and node.func.id in ('iteritems', 'iterkeys', 'itervalues',):
            #     # no need to check top-level iteritems() etc, they are not bound methods
            #     pass
            if not isinstance(node.func, Attribute):
                continue
            if isinstance(node.func.value, Dict):
                varName = '{}'  # todo: better print str(node.func.value)
            else:
                varName = ''
                value = node.func.value
                while isinstance(value, Attribute):
                    varName = '.' + value.attr + varName
                    value = value.value
                if isinstance(value, Name):
                    varName = value.id + varName
                else:
                    varName = '[...]' + varName  # todo: better print str(value)
            if not isinstance(node.func.value, (Name, Attribute, Dict)):
                continue
            if node.func.attr not in ('iteritems', 'iterkeys', 'itervalues',):
                continue
            if len(node.args) > 0:
                continue
            yield node.lineno, node.col_offset, 'ITI010 %s.%s() needs to be migrated to six.%s(%s)' % (varName, node.func.attr, node.func.attr, varName), type(self)
