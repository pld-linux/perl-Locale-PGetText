%include	/usr/lib/rpm/macros.perl
Summary:	Locale-PGetText perl module
Summary(pl):	Modu³ perla Locale-PGetText
Name:		perl-Locale-PGetText
Version:	0.16
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Locale/Locale-PGetText-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Locale-PGetText - pure perl i18n routines. 

%description -l pl
Locale-PGetText - rutyny umiêdzynarodowiania napisane w czystym perlu.

%prep
%setup -q -n Locale-PGetText-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Locale/PGetText
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13]/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/*

%{perl_sitelib}/Locale/PGetText.pm
%{perl_sitearch}/auto/Locale/PGetText

%{_mandir}/man[13]/*
