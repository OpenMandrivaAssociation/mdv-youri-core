%define rname	youri-core
%define name	mdv-%{rname}
%define version 0.9
%define svn	20071219
%define rel	1
%define release %mkrel 1.%{svn}.%{rel}
%define distname %{rname}-%{version}-%{svn}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Youri Offers an Upload & Repository Infrastucture (Mandriva fork)
License:	GPL or Artistic
Group:		Development/Other
Source:		%{distname}.tar.bz2
Url:		http://youri.zarb.org
BuildRequires:	perl(Test::Distribution)
BuildRequires:	perl(Pod::Simple::HTMLBatch)
BuildRequires:	perl(DateTime::Format::Duration)
BuildRequires:  perl(CGI)
BuildRequires:  perl(XML::RSS)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(SOAP::Lite)
BuildRequires:  perl(MIME::Entity)
BuildRequires:  perl(URPM)
BuildRequires:  perl(DBI)
BuildRequires:  perl(YAML)
BuildRequires:  perl(XML::Twig)
BuildRequires:  perl(Expect)
BuildRequires:  perl(AppConfig)
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
%{_datadir}/%{name}/lib/Youri
