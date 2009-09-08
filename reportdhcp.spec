%define name	reportdhcp
%define version 2.1
%define release %mkrel 9

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

