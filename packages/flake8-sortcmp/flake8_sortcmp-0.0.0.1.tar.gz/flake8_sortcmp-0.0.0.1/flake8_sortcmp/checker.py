from .version import __version__
from ast import walk, Call, Name, List, Attribute

STC010 = "STC010 sorted(list, cmp=cmp) needs to be migrated to sorted(list, key=functools.cmp_to_key(cmp))"
STC011 = "STC011 list.sort(cmp=cmp) needs to be migrated to list.sort(key=functools.cmp_to_key(cmp))"

class SortcmpChecker(object):
    name = 'flake8_sortcmp'
    version = __version__

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        for node in walk(self.tree):
            if not isinstance(node, Call):
                continue
            if isinstance(node.func, Name) and node.func.id in ('sorted',):
                flake8warn = STC010
            elif isinstance(node.func, Attribute) and isinstance(node.func.value, (Name, Attribute, List)) and node.func.attr in ('sort',):
                flake8warn = STC011
            else:
                continue

            if any(keyword.arg == 'cmp' for keyword in node.keywords):
                yield node.lineno, node.col_offset, flake8warn, type(self)
