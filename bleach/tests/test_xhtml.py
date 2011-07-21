from nose.tools import eq_

import bleach

TAG = ['br']
XHTML = 'some<br/>xhtml'

def test_clean():
    eq_(XHTML.replace('/', ''), bleach.clean(XHTML, tags=TAG))
    eq_(XHTML, bleach.clean(XHTML, tags=TAG, xhtml=True))


def test_linkify():
    eq_(XHTML.replace('/', ''), bleach.linkify(XHTML))
    eq_(XHTML, bleach.linkify(XHTML, xhtml=True))
