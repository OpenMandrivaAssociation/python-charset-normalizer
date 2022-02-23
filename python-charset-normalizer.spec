%define module charset-normalizer

Summary:	The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet.
Name:		python-%{module}
Version:	2.0.12
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/c/charset-normalizer/charset-normalizer-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/charset-normalizer/
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:  python3dist(setuptools)

%description
A library that helps you read text from an unknown charset encoding.
Motivated by chardet, I'm trying to resolve the issue by taking a new approach. 
All IANA character set names for which the Python core library provides codecs are supported.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/normalizer
%{python_sitelib}/charset_normalizer-%{version}-py*.*.egg-info
%{python_sitelib}/charset_normalizer/
