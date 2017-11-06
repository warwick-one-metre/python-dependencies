#
# spec file for package python-MarkupSafe
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


Name:           python34-MarkupSafe
Version:        1.0
Release:        0
License:        BSD (FIXME:No SPDX)
Summary:        Implements a XML/HTML/XHTML Markup safe string for Python
Url:            http://github.com/pallets/markupsafe
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/M/MarkupSafe/MarkupSafe-%{version}.tar.gz
BuildRequires:  python34-devel
BuildRequires:  python34-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      x86_64

%description
MarkupSafe
==========

Implements a unicode subclass that supports HTML strings:

.. code-block:: python

    >>> from markupsafe import Markup, escape
    >>> escape("<script>alert(document.cookie);</script>")
    Markup(u'&lt;script&gt;alert(document.cookie);&lt;/script&gt;')
    >>> tmpl = Markup("<em>%s</em>")
    >>> tmpl % "Peter > Lustig"
    Markup(u'<em>Peter &gt; Lustig</em>')

If you want to make an object unicode that is not yet unicode
but don't want to lose the taint information, you can use the
``soft_unicode`` function.  (On Python 3 you can also use ``soft_str`` which
is a different name for the same function).

.. code-block:: python

    >>> from markupsafe import soft_unicode
    >>> soft_unicode(42)
    u'42'
    >>> soft_unicode(Markup('foo'))
    Markup(u'foo')

HTML Representations
--------------------

Objects can customize their HTML markup equivalent by overriding
the ``__html__`` function:

.. code-block:: python

    >>> class Foo(object):
    ...  def __html__(self):
    ...   return '<strong>Nice</strong>'
    ...
    >>> escape(Foo())
    Markup(u'<strong>Nice</strong>')
    >>> Markup(Foo())
    Markup(u'<strong>Nice</strong>')

Silent Escapes
--------------

Since MarkupSafe 0.10 there is now also a separate escape function
called ``escape_silent`` that returns an empty string for ``None`` for
consistency with other systems that return empty strings for ``None``
when escaping (for instance Pylons' webhelpers).

If you also want to use this for the escape method of the Markup
object, you can create your own subclass that does that:

.. code-block:: python

    from markupsafe import Markup, escape_silent as escape

    class SilentMarkup(Markup):
        __slots__ = ()

        @classmethod
        def escape(cls, s):
            return cls(escape(s))

New-Style String Formatting
---------------------------

Starting with MarkupSafe 0.21 new style string formats from Python 2.6 and
3.x are now fully supported.  Previously the escape behavior of those
functions was spotty at best.  The new implementations operates under the
following algorithm:

1.  if an object has an ``__html_format__`` method it is called as
    replacement for ``__format__`` with the format specifier.  It either
    has to return a string or markup object.
2.  if an object has an ``__html__`` method it is called.
3.  otherwise the default format system of Python kicks in and the result
    is HTML escaped.

Here is how you can implement your own formatting:

.. code-block:: python

    class User(object):

        def __init__(self, id, username):
            self.id = id
            self.username = username

        def __html_format__(self, format_spec):
            if format_spec == 'link':
                return Markup('<a href="/user/{0}">{1}</a>').format(
                    self.id,
                    self.__html__(),
                )
            elif format_spec:
                raise ValueError('Invalid format spec')
            return self.__html__()

        def __html__(self):
            return Markup('<span class=user>{0}</span>').format(self.username)

And to format that user:

.. code-block:: python

    >>> user = User(1, 'foo')
    >>> Markup('<p>User: {0:link}').format(user)
    Markup(u'<p>User: <a href="/user/1"><span class=user>foo</span></a>')

Markupsafe supports Python 2.6, 2.7 and Python 3.3 and higher.

%prep
%setup -q -n MarkupSafe-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*

%changelog