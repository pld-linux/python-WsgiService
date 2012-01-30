%define 	module	WsgiService
Summary:	WSGI framework for easy creation of REST services
Summary(pl.UTF-8):	Narzędzie do łatwego tworzenia usług REST.
Name:		python-%{module}
Version:	0.3
Release:	1
License:	BSD
Group:		Development/Languages/Python
# http://pypi.python.org/packages/source/W/WsgiService/WsgiService-0.3.zip#md5=f689f60aa16cb84aeccb72f621ed3156
Source0:	http://pypi.python.org/packages/source/W/%{module}/%{module}-%{version}.zip
# Source0-md5:	f689f60aa16cb84aeccb72f621ed3156
URL:		http://pypi.python.org/pypi/WsgiService
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-decorator
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The primary guiding principle is that the actual service should be as
easy and small to write as possible. The WsgiService framework will do
for the developer:
- Abstract away error and status code handling
- Make it easy to create machine readable output
- Easily validate input
- Easy deployment using good configuration file handling
- Make testing easy
- Create usable REST API documentation from source
- Content negotiation to automatically use the correct output format
  WsgiService is not planning to be a full-featured frontend framework.
  Use your existing framework of choice for that, e.g. Pylons.

%description -l pl.UTF-8
Główną zasadą tworzenia uługi powinna być łatwość i mała ilość kodu do
zapisania. WsgiService dostarcza programiście:
- Wersje abstrakcji dla błędów i statusu.
- Łatwość tworzenia wyników przeznaczonych do przetwarzania dalej.
- Łatwość sprawdzania poprawnośći na wejścu
- Łatwe uruchamianie przy dobrym użyciu plików konfiguracyjnych
- Łatwe testowanie
- Tworzenie dokumentacji REST ze źródeł.
- Automatyczną negocjację formatu odpowidzi. WsgiService nie planuje
  być pełnym frontendem usług REST. Należy używać istniejących do wyboru
  np Pylons.


%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# %doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
# %{py_sitedir}/*.py[co]
%{py_sitescriptdir}/wsgiservice
# %attr(755,root,root) %{py_sitedir}/*.so
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/WsgiService-*.egg-info
%endif
# %{_examplesdir}/%{name}-%{version}
