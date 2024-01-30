from ast import parse
from flake8_logger.checker import LoggerChecker

def test_positive_not_format():
    tree = parse('''
import logging
log = logging.getLogger(__name__)
log.warn('not format')
''')
    violations = list(LoggerChecker(tree).run())
    assert len(violations) == 0

def test_positive_format_simple():
    tree = parse('''
import logging
log = logging.getLogger(__name__)
log.warn('format %s', 'foo')
''')
    violations = list(LoggerChecker(tree).run())
    assert len(violations) == 0

def test_positive_format_dict_str():
    tree = parse('''
import logging
log = logging.getLogger(__name__)
log.warn('format %(xxx)s %(yyy)s', {'xxx':'foo', 'yyy':'bar'})
''')
    violations = list(LoggerChecker(tree).run())
    assert len(violations) == 0

def test_positive_format_dict_unicode():
    tree = parse('''
import logging
log = logging.getLogger(__name__)
log.warn(u'format %(xxx)s %(yyy)s', {u'xxx':'foo', 'yyy':'bar'})
''')
    violations = list(LoggerChecker(tree).run())
    assert len(violations) == 0

def test_positive_format_star_list():
    tree = parse('''
import logging
log = logging.getLogger(__name__)
log.warn('format %s', *['foo',])
''')
    violations = list(LoggerChecker(tree).run())
    assert len(violations) == 0

def test_positive_format_star_tuple():
    tree = parse('''
import logging
log = logging.getLogger(__name__)
log.warn('format %s', *('foo',))
''')
    violations = list(LoggerChecker(tree).run())
    assert len(violations) == 0

def test_positive_format_star_many():
    tree = parse('''
import logging
log = logging.getLogger(__name__)
args = ('foo', 'bar')
log.warn('format %s %s', *args)
''')
    violations = list(LoggerChecker(tree).run())
    assert len(violations) == 0

def test_positive_format_star_zero():
    tree = parse('''
import logging
log = logging.getLogger(__name__)
args = ()
log.warn('format', *args)
''')
    violations = list(LoggerChecker(tree).run())
    assert len(violations) == 0

def test_argument_missing():
    tree = parse('''
import logging
log = logging.getLogger(__name__)
log.warn('argument missing %s')
''')
    violations = list(LoggerChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('LG010 ')

def test_argument_extra():
    tree = parse('''
import logging
log = logging.getLogger(__name__)
log.warn('argument extra %s', 'foo', 'bar')
''')
    violations = list(LoggerChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('LG010 ')

def test_argument_dict_different():
    tree = parse('''
import logging
log = logging.getLogger(__name__)
log.warn('%(xxx)s', {'yyy':'foo'})
''')
    violations = list(LoggerChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('LG011 ')

def test_argument_dict_invalid():
    tree = parse('''
import logging
log = logging.getLogger(__name__)
log.warn('%(1)s', {1:'foo'})
''')
    violations = list(LoggerChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('LG012 ')

def test_call_log():
    tree = parse('''
import logging
log = logging.getLogger(__name__)
log.log(logging.WARN, 'argument missing %s')
''')
    violations = list(LoggerChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('LG010 ')

def test_child_not_format():
    tree = parse('''
import logging
class ChildLogger(logging.getLoggerClass()):
    _child = None
    @property
    def child(self):
        if self._child is None:
            self._child = logging.getLogger(self.name+'.child')
        return self._child
logging.setLoggerClass(ChildLogger)
log = logging.getLogger(__name__)
log.child.warn('not format')
''')
    violations = list(LoggerChecker(tree).run())
    assert len(violations) == 0

def test_child_argument_missing():
    tree = parse('''
import logging
class ChildLogger(logging.getLoggerClass()):
    _child = None
    @property
    def child(self):
        if self._child is None:
            self._child = logging.getLogger(self.name+'.child')
        return self._child
logging.setLoggerClass(ChildLogger)
log = logging.getLogger(__name__)
log.child.warn('argument missing %s')
''')
    violations = list(LoggerChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('LG010 ')
