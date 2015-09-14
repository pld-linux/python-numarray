
%define		module	numarray

Summary:	Array manipulation and computations for python
Summary(pl.UTF-8):	Operacje i obliczenia na tablicach dla Pythona
Name:		python-%{module}
Version:	1.5.2
Release:	5
License:	GPL-like
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/numpy/%{module}-%{version}.tar.gz
# Source0-md5:	d2ecfc60fe4869c328b872540d04e0f7
Source1:	http://dl.sourceforge.net/numpy/%{module}-1.5.pdf
# Source1-md5:	922731aeb775b1f5eb3a0622750314e1
Patch0:		%{name}-includes.patch
Patch1:		%{name}-python25.patch
Patch2:		%{name}-refcount.patch
URL:		http://www.stsci.edu/resources/software_hardware/numarray
BuildRequires:	python
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
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

%description -l pl.UTF-8
Numarray zapewnia narzędzia do operacji oraz obliczeń na tablicach
podobne do tych, jakie zapewniają IDL, Matlab czy Octabe. Używając
numarray możliwe jest stworzenie bezpośrednio w Pythonie, nie używając
wstawek C, C++ czy Fortranowych, wielu wydajnych aplikacji do
przetwarzania danych numerycznych. Dla algorytmów, które nie pracują
wydajnie z tablicami, możliwe jest napisanie funkcji C, które mogą
czytać i zapisywać tablice numarray, i które mogą być wywoływane z
poziomu Pythona.

Numarray jest ponowną implementacją starszego modułu Pythona -
Numeric. Interfejsy tych modułów są do siebie bardzo podobne. Numarray
jest w większości przypadków kompatybilny wstecz, a sytuacja poprawi
się w nowszych wersjach.

%package devel
Summary:	Header files for python-numarray
Summary(pl.UTF-8):	Pliki nagłówkowe dla python-numarray
Group:		Development/Libraries

%description devel
Header files for python-numarray.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla python-numarray.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p0
cp %{SOURCE1} .

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
%doc README.txt *.pdf
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*

%files devel
%defattr(644,root,root,755)
%dir %{py_incdir}/%{module}
%{py_incdir}/%{module}/*
