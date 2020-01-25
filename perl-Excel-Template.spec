#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Excel
%define		pnam	Template
Summary:	Excel::Template - create Excel files from templates
Name:		perl-Excel-Template
Version:	0.33
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7916450329aa3308a80b4f1ebbe69a17
URL:		http://search.cpan.org/dist/Excel-Template/
%if %{with tests}
BuildRequires:	perl-Spreadsheet-WriteExcel
BuildRequires:	perl-version
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a module used for templating Excel files. Its genesis came
from the need to use the same datastructure as HTML::Template, but
provide Excel files instead. The existing modules don't do the trick,
as they require replication of logic that's already been done within
HTML::Template.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/%{pdir}
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
