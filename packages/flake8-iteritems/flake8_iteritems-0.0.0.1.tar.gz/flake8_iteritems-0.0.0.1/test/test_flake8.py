from sys import version_info
from pytest import mark
from ast import parse
from flake8_iteritems.checker import IteritemsChecker

def test_positive_items():
    tree = parse('''
d = {}
d.items()
''')
    violations = list(IteritemsChecker(tree).run())
    assert len(violations) == 0

def test_positive_keys():
    tree = parse('''
d = {}
d.keys()
''')
    violations = list(IteritemsChecker(tree).run())
    assert len(violations) == 0

def test_positive_values():
    tree = parse('''
d = {}
d.values()
''')
    violations = list(IteritemsChecker(tree).run())
    assert len(violations) == 0

def test_iteritems():
    tree = parse('''
d = {}
d.iteritems()
''')
    violations = list(IteritemsChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('ITI010 ')

def test_iterkeys():
    tree = parse('''
d = {}
d.iterkeys()
''')
    violations = list(IteritemsChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('ITI010 ')

def test_itervalues():
    tree = parse('''
d = {}
d.itervalues()
''')
    violations = list(IteritemsChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('ITI010 ')

def test_positive_iteritems():
    tree = parse('''
import six
d = {}
six.iteritems(d)
''')
    violations = list(IteritemsChecker(tree).run())
    assert len(violations) == 0

def test_positive_iterkeys():
    tree = parse('''
import six
d = {}
six.iterkeys(d)
''')
    violations = list(IteritemsChecker(tree).run())
    assert len(violations) == 0

def test_positive_itervalues():
    tree = parse('''
import six
d = {}
six.itervalues(d)
''')
    violations = list(IteritemsChecker(tree).run())
    assert len(violations) == 0

def test_toplevel_iteritems():
    tree = parse('''
from six import iteritems
d = {}
iteritems(d)
''')
    violations = list(IteritemsChecker(tree).run())
    assert len(violations) == 0

def test_immediate():
    tree = parse('''
{}.iteritems()
''')
    violations = list(IteritemsChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('ITI010 ')

def test_positive_immediate():
    tree = parse('''
import six
six.itervalues({})
''')
    violations = list(IteritemsChecker(tree).run())
    assert len(violations) == 0

def test_attribute1():
    tree = parse('''
class C:
    d = {}
C.d.iteritems()
''')
    violations = list(IteritemsChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('ITI010 ')

def test_positive_attribute1():
    tree = parse('''
import six
class C:
    d = {}
six.iteritems(C.d)
''')
    violations = list(IteritemsChecker(tree).run())
    assert len(violations) == 0

def test_attribute2():
    tree = parse('''
class C:
    d = {}
C().d.iteritems()
''')
    violations = list(IteritemsChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('ITI010 ')

def test_positive_attribute2():
    tree = parse('''
import six
class C:
    d = {}
six.iteritems(C().d)
''')
    violations = list(IteritemsChecker(tree).run())
    assert len(violations) == 0
