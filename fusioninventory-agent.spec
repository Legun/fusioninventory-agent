Name: fusioninventory-agent
Version: 2.3.6
Release: 1%{?dist}
Summary: Fusion Inventory agent
License: GPL+
Group: Development/Libraries
URL: http://search.cpan.org/dist/FusionInventory-Agent/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
BuildRequires: perl >= 1:5.8.0
BuildRequires: perl(Compress::Zlib)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Which)
BuildRequires: perl(HTTP::Daemon)
BuildRequires: perl(HTTP::Proxy)
BuildRequires: perl(HTTP::Server::Simple)
BuildRequires: perl(HTTP::Server::Simple::Authen)
BuildRequires: perl(IO::Capture::Stderr)
BuildRequires: perl(IO::Socket::SSL)
BuildRequires: perl(IPC::Run)
BuildRequires: perl(LWP)
BuildRequires: perl(Net::CUPS) >= 0.6
BuildRequires: perl(Net::IP)
BuildRequires: perl(Proc::Daemon)
BuildRequires: perl(Proc::PID::File)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::MockModule)
BuildRequires: perl(Test::More) >= 0.93
BuildRequires: perl(Text::Template)
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl(XML::TreePP) >= 0.26
BuildRequires: perl(YAML)
Requires: perl(Compress::Zlib)
Requires: perl(File::Which)
Requires: perl(HTTP::Daemon)
Requires: perl(IO::Socket::SSL)
Requires: perl(LWP)
Requires: perl(Net::CUPS) >= 0.6
Requires: perl(Net::IP)
Requires: perl(Proc::Daemon)
Requires: perl(Proc::PID::File)
Requires: perl(Text::Template)
Requires: perl(UNIVERSAL::require)
Requires: perl(XML::TreePP) >= 0.26
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This is the agent object.

%prep
%setup -q -n %{name}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes fusioninventory-agent fusioninventory-injector fusioninventory-win32-service LICENSE memconf MYMETA.json MYMETA.yml README THANKS
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Apr 14 2012 http://blog.famillecollet.com 2.2.0-1
- Specfile autogenerated by cpanspec 1.78.