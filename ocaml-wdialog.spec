Summary:	Toolkit for Dialog-Centric Web Applications
Summary(pl.UTF-8):   Wiązania TEMPLATE dla OCamla
Name:		ocaml-wdialog
Version:	2.1.2
%define _man_ver 2.1.1
Release:	0.1
License:	GPL v2+
Group:		Libraries
Vendor:		Gerd Stolpmann <gerd@gerd-stolpmann.de>
Source0:	http://dl.sourceforge.net/sourceforge/wdialog/wdialog-%{version}.tar.gz
# Source0-md5:	1380a8ae75f690043634c66f3f8ff8d1
Source1:	http://dl.sourceforge.net/sourceforge/wdialog/wdialog-manual-%{_man_ver}-html.tar.gz
# Source1-md5:	2a4f4c4fa1d8b1718a7938afdcc84add
URL:		http://wdialog.sourceforge.net/
BuildRequires:	ocaml-findlib-devel
BuildRequires:	ocaml-pxp-devel
BuildRequires:	ocaml-pcre-devel
BuildRequires:	ocaml-net-cgi-devel
BuildRequires:	ocaml >= 3.06
BuildRequires:	ocaml-ulex
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains files needed to run bytecode executables using
this library.

%description -l pl.UTF-8
Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających tej biblioteki.

%package devel
Summary:	Toolkit for Dialog-Centric Web Applications - development part
Summary(pl.UTF-8):   Wiązania TEMPLATE dla OCamla - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
This package contains files needed to develop OCaml programs using
this library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów używających
tej biblioteki.

%prep
%setup -q -n wdialog-%{version}

%build
# no %%configure please
./configure -without-wd-session-daemon
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
