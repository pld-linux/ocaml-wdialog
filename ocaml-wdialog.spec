Summary:	Toolkit for Dialog-Centric Web Applications
Summary(pl):	Wi±zania TEMPLATE dla OCamla
Name:		ocaml-wdialog
Version:	2.00
Release:	2
License:	GPL v2+
Group:		Libraries
Vendor:		Gerd Stolpmann <gerd@gerd-stolpmann.de>
Source0:	http://dl.sourceforge.net/sourceforge/wdialog/wdialog-%{version}.tar.gz
# Source0-md5:	38a17ae876f133d99da1f9fcc2acb02f
Source1:	http://dl.sourceforge.net/sourceforge/wdialog/wdialog-manual-%{version}-html.tar.gz
# Source1-md5:	40a1280113d80f3c1f8780584dcc7982
URL:		http://wdialog.sourceforge.net/
BuildRequires:	ocaml-findlib-devel
BuildRequires:	ocaml-pxp-devel
BuildRequires:	ocaml-pcre-devel
BuildRequires:	ocaml-net-cgi-devel
BuildRequires:	ocaml >= 3.06
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains files needed to run bytecode executables using
this library.

%description -l pl
Pakiet ten zawiera binaria potrzebne do uruchamiania programów
u¿ywaj±cych tej biblioteki.

%package devel
Summary:	Toolkit for Dialog-Centric Web Applications - development part
Summary(pl):	Wi±zania TEMPLATE dla OCamla - cze¶æ programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
This package contains files needed to develop OCaml programs using
this library.

%description devel -l pl
Pakiet ten zawiera pliki niezbêdne do tworzenia programów u¿ywaj±cych
tej biblioteki.

%prep
%setup -q -n wdialog-%{version}

%build
# no %%configure please
./configure
%{__make}
%{__make} opt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml

%{__make} install OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml

for f in wd-xmlcompiler wdialog wdialog-p4 ; do
	install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/$f
	mv -f $RPM_BUILD_ROOT%{_libdir}/ocaml/$f/META \
		$RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/$f/
	echo "directory = \"+$f\"" >> $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/$f/META
done

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
#%doc LICENSE *.mli
%{_libdir}/ocaml/w*/*.cm[ixa]*
%{_libdir}/ocaml/w*/*.a
%{_libdir}/ocaml/site-lib/*
#%{_examplesdir}/%{name}-%{version}
