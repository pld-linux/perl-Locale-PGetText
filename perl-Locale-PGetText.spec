%define	pdir	Locale
%define	pnam	PGetText
%include	/usr/lib/rpm/macros.perl
Summary:	Locale-PGetText perl module
Summary(pl):	Modu³ perla Locale-PGetText
Name:		perl-Locale-PGetText
Version:	0.16
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Locale-PGetText - pure perl i18n routines.

%description -l pl
Locale-PGetText - rutyny umiêdzynarodowiania napisane w czystym perlu.

%prep
%setup -q -n Locale-PGetText-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/Locale/PGetText.pm
%{_mandir}/man[13]/*
