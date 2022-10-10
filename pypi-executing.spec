#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-executing
Version  : 1.1.1
Release  : 15
URL      : https://files.pythonhosted.org/packages/48/5b/f636517f40fc5afb720354236cea729de30d440f06bdafb7f33ca969956c/executing-1.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/48/5b/f636517f40fc5afb720354236cea729de30d440f06bdafb7f33ca969956c/executing-1.1.1.tar.gz
Summary  : Get the currently executing AST node of a frame, and other information
Group    : Development/Tools
License  : MIT
Requires: pypi-executing-license = %{version}-%{release}
Requires: pypi-executing-python = %{version}-%{release}
Requires: pypi-executing-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
# executing
[![Build Status](https://github.com/alexmojaki/executing/workflows/Tests/badge.svg?branch=master)](https://github.com/alexmojaki/executing/actions) [![Coverage Status](https://coveralls.io/repos/github/alexmojaki/executing/badge.svg?branch=master)](https://coveralls.io/github/alexmojaki/executing?branch=master) [![Supports Python versions 2.7 and 3.4+, including PyPy](https://img.shields.io/pypi/pyversions/executing.svg)](https://pypi.python.org/pypi/executing)

%package license
Summary: license components for the pypi-executing package.
Group: Default

%description license
license components for the pypi-executing package.


%package python
Summary: python components for the pypi-executing package.
Group: Default
Requires: pypi-executing-python3 = %{version}-%{release}

%description python
python components for the pypi-executing package.


%package python3
Summary: python3 components for the pypi-executing package.
Group: Default
Requires: python3-core
Provides: pypi(executing)

%description python3
python3 components for the pypi-executing package.


%prep
%setup -q -n executing-1.1.1
cd %{_builddir}/executing-1.1.1
pushd ..
cp -a executing-1.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665418417
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-executing
cp %{_builddir}/executing-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-executing/44c582803d7005baacb1ad03bcc5ad393cbdd95f || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-executing/44c582803d7005baacb1ad03bcc5ad393cbdd95f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
