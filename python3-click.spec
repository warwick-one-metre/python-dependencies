Name:           python3-click
Version:        7.0
Release:        0
Url:            https://palletsprojects.com/p/click/
Summary:        Composable command line interface toolkit
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/c/click/Click-%{version}.tar.gz
BuildRequires:  python3-devel
BuildArch:      noarch

%description
\$ click\_
==========

Click is a Python package for creating beautiful command line interfaces
in a composable way with as little code as necessary. It's the "Command
Line Interface Creation Kit". It's highly configurable but comes with
sensible defaults out of the box.

It aims to make the process of writing command line tools quick and fun
while also preventing any frustration caused by the inability to
implement an intended CLI API.

Click in three points:

-   Arbitrary nesting of commands
-   Automatic help page generation
-   Supports lazy loading of subcommands at runtime


Installing
----------

Install and update using `pip`_:

.. code-block:: text

    $ pip install click

Click supports Python 3.4 and newer, Python 2.7, and PyPy.

.. _pip: https://pip.pypa.io/en/stable/quickstart/


A Simple Example
----------------

What does it look like? Here is an example of a simple Click program:

.. code-block:: python

    import click

    @click.command()
    @click.option("--count", default=1, help="Number of greetings.")
    @click.option("--name", prompt="Your name",
                  help="The person to greet.")
    def hello(count, name):
        """Simple program that greets NAME for a total of COUNT times."""
        for _ in range(count):
            click.echo("Hello, %s!" % name)

    if __name__ == '__main__':
        hello()

And what it looks like when run:

.. code-block:: text

    $ python hello.py --count=3
    Your name: Click
    Hello, Click!
    Hello, Click!
    Hello, Click!


Donate
------

The Pallets organization develops and supports Click and other popular
packages. In order to grow the community of contributors and users, and
allow the maintainers to devote more time to the projects, `please
donate today`_.

.. _please donate today: https://palletsprojects.com/donate


Links
-----

*   Website: https://palletsprojects.com/p/click/
*   Documentation: https://click.palletsprojects.com/
*   License: `BSD <https://github.com/pallets/click/blob/master/LICENSE.rst>`_
*   Releases: https://pypi.org/project/click/
*   Code: https://github.com/pallets/click
*   Issue tracker: https://github.com/pallets/click/issues
*   Test status:

    *   Linux, Mac: https://travis-ci.org/pallets/click
    *   Windows: https://ci.appveyor.com/project/pallets/click

*   Test coverage: https://codecov.io/gh/pallets/click

%prep
%setup -q -n Click-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
