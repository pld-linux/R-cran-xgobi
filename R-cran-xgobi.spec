%define		fversion	%(echo %{version} |tr r -)
%define		modulename	xgobi
Summary:	Interface to the XGobi and XGvis programs for graphical data analysis
Summary(pl.UTF-8):   Interfejsy do programów XGobi i XGvis do graficznej analizy danych
Name:		R-cran-%{modulename}
Version:	1.2r12
Release:	2
License:	Copyright (C) by Bellcore, non-profit use and redistribution permitted (see COPYING for details)
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	3edae689c69c12ef71df1ee269c1b1b8
BuildRequires:	R-base >= 2.4.0
Requires(post,postun):	R-base >= 2.4.0
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interface to the XGobi and XGvis programs for graphical data analysis.

%description -l pl.UTF-8
Interfejsy do programów XGobi i XGvis do graficznej analizy danych.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)

%postun
if [ -f %{_libdir}/R/bin/Rcmd ];then
	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)
fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/{DESCRIPTION,README,COPYING,ChangeLog}
%{_libdir}/R/library/%{modulename}
