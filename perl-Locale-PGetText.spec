%include	/usr/lib/rpm/macros.perl
%define	pdir	Locale
%define	pnam	PGetText
Summary:	Locale::PGetText -- pure perl i18n routines
Summary(pl):	Locale::PGetText -- funkcje i18n napisane w czystym Perlu
Name:		perl-Locale-PGetText
Version:	0.16
Release:	10
License:	?
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Locale::PGetText provides the same functionality as GNU gettext does, but
it is written in pure perl and doesn't require any system locale stuff.

%description -l pl
Locale::PGetText udostêpnia tak± sam± funkcjonalno¶æ, jak GNU gettext,
ale jest napisany w czystym Perlu i nie potrzebuje ¿adnych specyficznych
dla lokalizacji funkcji systemowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/Locale/PGetText.pm
%{_mandir}/man[13]/*
