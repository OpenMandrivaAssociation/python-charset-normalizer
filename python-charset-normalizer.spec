%define module charset-normalizer
%define oname charset_normalizer

Name:		python-charset-normalizer
Summary:	The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet.
Version:	3.4.5
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/charset-normalizer/
Source0:	https://files.pythonhosted.org/packages/source/c/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
A library that helps you read text from an unknown charset encoding.
Motivated by chardet, I'm trying to resolve the issue by taking a new approach. 
All IANA character set names for which the Python core library provides codecs are supported.

%files
%{_bindir}/normalizer
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
