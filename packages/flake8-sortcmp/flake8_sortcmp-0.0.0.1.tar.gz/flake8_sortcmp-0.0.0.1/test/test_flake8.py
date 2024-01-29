from sys import version_info
from pytest import mark
from ast import parse
from flake8_sortcmp.checker import SortcmpChecker

def test_positive_sorted_nothing():
    tree = parse('''
sorted([2, 1])
''')
    violations = list(SortcmpChecker(tree).run())
    assert len(violations) == 0

def test_positive_sort_nothing():
    tree = parse('''
[2, 1].sort()
''')
    violations = list(SortcmpChecker(tree).run())
    assert len(violations) == 0

def test_positive_sorted_key():
    tree = parse('''
sorted([2, 1], key=int)
''')
    violations = list(SortcmpChecker(tree).run())
    assert len(violations) == 0

def test_positive_sort_key():
    tree = parse('''
[2, 1].sort(key=int)
''')
    violations = list(SortcmpChecker(tree).run())
    assert len(violations) == 0

def test_sorted():
    tree = parse('''
sorted([2, 1], cmp=lambda a,b: a-b)
''')
    violations = list(SortcmpChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('STC010 ')

def test_sort():
    tree = parse('''
[2, 1].sort(cmp=lambda a,b: a-b)
''')
    violations = list(SortcmpChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('STC011 ')

def test_attribute1_sorted():
    tree = parse('''
class A:
    l = [2, 1]
sorted(A.l, cmp=lambda a,b: a-b)
''')
    violations = list(SortcmpChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('STC010 ')

def test_attribute1_sort():
    tree = parse('''
class A:
    l = [2, 1]
A.l.sort(cmp=lambda a,b: a-b)
''')
    violations = list(SortcmpChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('STC011 ')

def test_attribute2_sorted():
    tree = parse('''
class A:
    l = [2, 1]
sorted(A().l, cmp=lambda a,b: a-b)
''')
    violations = list(SortcmpChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('STC010 ')

def test_attribute2_sort():
    tree = parse('''
class A:
    l = [2, 1]
A().l.sort(cmp=lambda a,b: a-b)
''')
    violations = list(SortcmpChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('STC011 ')
