%define rname	youri-core
%define name	mdv-%{rname}
%define version 0.9
%define svn	20090417
%define rel	3
%define release %mkrel 1.%{svn}.%{rel}
%define distname %{rname}-%{version}-%{svn}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Youri Offers an Upload & Repository Infrastucture (Mandriva fork)
License:	GPL or Artistic
Group:		Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		%{distname}.tar.bz2
Url:		http://youri.zarb.org
Requires:	perl-YAML
Requires:	perl(Test::Distribution)
Requires:	perl(Pod::Simple::HTMLBatch)
Requires:	perl(DateTime::Format::Duration)
Requires:  perl(CGI)
Requires:  perl(XML::RSS)
Requires:  perl(List::MoreUtils)
Requires:  perl(LWP::UserAgent)
Requires:  perl(SOAP::Lite)
Requires:  perl(MIME::Entity)
Requires:  perl(URPM)
Requires:  perl(DBI)
Requires:  perl(YAML)
Requires:  perl(XML::Twig)
Requires:  perl(Expect)
Requires:  perl(AppConfig)
Buildarch:	noarch

%description
YOURI stands for "Youri Offers an Upload & Repository Infrastucture". It aims
to build tools making management of a coherent set of packages easier.

This package contains YOURI core components used by the Mandriva build system.

%prep
%setup -q -n %{distname}

%build
%{__perl} Makefile.PL \
  INSTALLDIRS=vendor \
  INSTALLVENDORLIB=%{_datadir}/%{name}/lib
%make pure_all

%install
rm -rf %{buildroot}
%make DESTDIR=%{buildroot} pure_install

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc ChangeLog README
%if %mdvver > 200900
%{_mandir}/*/*
%endif
%{_datadir}/%{name}/lib/Youri
