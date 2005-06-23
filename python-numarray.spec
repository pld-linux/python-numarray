
%define		module	numarray

Summary:	Array manipulation and computations for python
Summary(pl):	Manipulacje macierzami oraz obliczenia dla pythona
Name:		python-%{module}
Version:	1.3.2
Release:	1
License:	GPL-like
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/numpy/%{module}-%{version}.tar.gz
# Source0-md5:	d8ac1672089ec45d04f3da618a5926bd
Source1:	http://dl.sourceforge.net/numpy/%{module}-1.3.html.tar.gz
# Source1-md5:	ef0477bf9a75ba8acc5929f765dcf91d
URL:		http://www.stsci.edu/resources/software_hardware/numarray
BuildRequires:	python
BuildRequires:	python-devel >= 1:2.3
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Numarray provides array manipulation and computational capabilities
similar to those found in IDL, Matlab, or Octave. Using numarray, it
is possible to write many efficient numerical data processing
applications directly in Python without using any C, C++ or Fortran
code (as well as doing such analysis interactively within Python or
PyRAF). For algorithms that are not well suited for efficient
computation using array facilities it is possible to write C functions
(and eventually Fortran) that can read and write numarray arrays that
can be called from Python.

Numarray is a re-implementation of an older Python array module called
Numeric. In general its interface is very similar. It is mostly
backward compatible and will be becoming more so in future releases.

%description -l pl
Numarray zapewnia narz�dzia do manipulacji tablicami oraz oblicze�
podobne do tych, jakie zapewniaj� IDL, Matlab czy Octabe. U�ywaj�c
numarray mo�liwe jest stworzenie bezpo�rednio w pythonie, nie u�ywaj�c
wstawek C, C++ czy Fortranowych, wielu wydajnych aplikacji do
przetwarzania danych numerycznych. Dla algorytm�w, kt�re nie pracuj�
wydajnie z tablicami, mo�liwe jest napisanie funkcji C, kt�re mog�
czyta� i zapisywa� tablice numarray, i kt�re mog� by� wywo�ywane z
poziomu Pythona.

Numarray jest ponown� implementacj� starszego modu�u Pythona -
Numeric. Interfejsy tych modu��w s� do siebie bardzo podobne. Numarray
jest w wi�kszo�ci przypadk�w kompatybilny wstecz, a sytuacja poprawi
si� w nowszych wersjach.

%package devel
Summary:	Header files for python-numarray
Summary(pl):	Pliki nag��wkowe dla python-numarray
Group:		Development/Libraries

%description devel
Header files for python-numarray

%description devel -l pl
Pliki nag��wkowe dla python-numarray

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name '*.py' | \
	grep -v examples | \
	xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*

%files devel
%defattr(644,root,root,755)
%dir %py_incdir/%{module}
%py_incdir/%{module}/*
