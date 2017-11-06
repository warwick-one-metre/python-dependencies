#
# spec file for package python-Pillow
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

%define debug_package %{nil}

Name:           python34-Pillow
Version:        4.3.0
Release:        0
License:        Standard PIL License (FIXME:No SPDX)
Summary:        Python Imaging Library (Fork)
Url:            https://python-pillow.org
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/P/Pillow/Pillow-%{version}.tar.gz
BuildRequires:  python34-devel
BuildRequires:  python34-setuptools
BuildRequires:  libjpeg-devel, zlib-devel, freetype-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      x86_64

%description
Pillow
======

Python Imaging Library (Fork)
-----------------------------

Pillow is the friendly PIL fork by `Alex Clark and Contributors <https://github.com/python-pillow/Pillow/graphs/contributors>`_. PIL is the Python Imaging Library by Fredrik Lundh and Contributors.

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |linux| |macos| |windows| |coverage|
    * - package
      - |zenodo| |version|

.. |docs| image:: https://readthedocs.org/projects/pillow/badge/?version=latest
   :target: https://pillow.readthedocs.io/?badge=latest
   :alt: Documentation Status

.. |linux| image:: https://img.shields.io/travis/python-pillow/Pillow/master.svg?label=Linux%20build
   :target: https://travis-ci.org/python-pillow/Pillow
   :alt: Travis CI build status (Linux)

.. |macos| image:: https://img.shields.io/travis/python-pillow/pillow-wheels/latest.svg?label=macOS%20build
   :target: https://travis-ci.org/python-pillow/pillow-wheels
   :alt: Travis CI build status (macOS)

.. |windows| image:: https://img.shields.io/appveyor/ci/python-pillow/Pillow/master.svg?label=Windows%20build
   :target: https://ci.appveyor.com/project/python-pillow/Pillow
   :alt: AppVeyor CI build status (Windows)

.. |coverage| image:: https://coveralls.io/repos/python-pillow/Pillow/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/python-pillow/Pillow?branch=master
   :alt: Code coverage

.. |zenodo| image:: https://zenodo.org/badge/17549/python-pillow/Pillow.svg
   :target: https://zenodo.org/badge/latestdoi/17549/python-pillow/Pillow

.. |version| image:: https://img.shields.io/pypi/v/pillow.svg
   :target: https://pypi.python.org/pypi/Pillow/
   :alt: Latest PyPI version

.. end-badges



More Information
----------------

- `Documentation <https://pillow.readthedocs.io/>`_

  - `Installation <https://pillow.readthedocs.io/en/latest/installation.html>`_
  - `Handbook <https://pillow.readthedocs.io/en/latest/handbook/index.html>`_

- `Contribute <https://github.com/python-pillow/Pillow/blob/master/.github/CONTRIBUTING.md>`_

  - `Issues <https://github.com/python-pillow/Pillow/issues>`_
  - `Pull requests <https://github.com/python-pillow/Pillow/pulls>`_

- `Changelog <https://github.com/python-pillow/Pillow/blob/master/CHANGES.rst>`_

  - `Pre-fork <https://github.com/python-pillow/Pillow/blob/master/CHANGES.rst#pre-fork>`_




%prep
%setup -q -n Pillow-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*
/usr/bin/*

%changelog
