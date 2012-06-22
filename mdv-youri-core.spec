%define rname	youri-core
%define name	mdv-%{rname}
%define version 0.9
%define svn	20120622
%define rel	1
%define release 1
%define distname %{rname}-%{version}-%{svn}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Youri Offers an Upload & Repository Infrastucture (Mandriva fork)
License:	GPL or Artistic
Group:		Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:	%{distname}.tar.bz2
#Patch0:		youri-core-0.9-20090417-rpm5-port.patch
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
%patch0 -p1 -b .rpm5~

%build
%{__perl} Makefile.PL \
  INSTALLDIRS=vendor \
  INSTALLVENDORLIB=%{_datadir}/%{name}/lib
%make pure_all

%install
rm -rf %{buildroot}
%make DESTDIR=%{buildroot} pure_install
rm -f %{buildroot}%{_mandir}/man3/*

%files 
%defattr(-,root,root)
%doc ChangeLog README
%{_mandir}/*/*
%{_datadir}/%{name}/lib/Youri
