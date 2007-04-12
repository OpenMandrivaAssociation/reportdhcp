%define name	reportdhcp
%define version 2.1
%define release %mkrel 5

Summary:	Displays statistics and lease entries for ISC DHCPD
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Monitoring
URL:		http://www.omar.org/opensource/reportdhcp/
Source0:	%{name}.pl-%{version}.tar.bz2
Patch0:		%{name}.patch
Requires:	dhcp-server
Requires:	webserver
#Requires:	perl
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildArch:	noarch

%description
Reportdhcp.pl is a CGI script written in perl. It displays
statistics and lease entries for ISC DHCPD by parsing the
dhcpd.conf and dhcpd.leases files. reportdhcp.pl version 2
supports version 3.0p1 and above of the ISC DHCP distribution.

%prep

%setup -q -c -n %{name}-%{version}
%patch0 -p0

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/var/www/cgi-bin
install -m755 %{name}.pl %{buildroot}/var/www/cgi-bin/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc CHANGELOG README
%attr(755,root,root) /var/www/cgi-bin/%{name}.pl


* Fri Jun 03 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1-4mdk
- rebuild

* Sun May 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.1-3mdk
- build release

* Thu Jan 16 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 2.1-2mdk
- build release

* Fri Sep 20 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 2.1-1mdk
- new version
- fix P0
- misc spec file fixes

* Fri Jul 19 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 2.0b-2mdk
- <title></title> mess fix
- rpmlint fix

* Thu Jul 18 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 2.0b-1mdk
- initial cooker contrib

