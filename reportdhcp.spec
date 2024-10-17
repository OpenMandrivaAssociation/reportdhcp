%define name	reportdhcp
%define version 2.1
%define release 10

Summary:	Displays statistics and lease entries for ISC DHCPD
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Monitoring
URL:		https://www.omar.org/opensource/reportdhcp/
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



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.1-9mdv2010.0
+ Revision: 433334
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.1-8mdv2009.0
+ Revision: 260232
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.1-7mdv2009.0
+ Revision: 248373
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.1-5mdv2008.1
+ Revision: 140746
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - kill changelog left by repsys


* Fri Jul 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+2006-07-14 19:06:04 (41177)
- rebuild && mkrel

* Fri Jul 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+2006-07-14 19:04:14 (41176)
Import reportdhcp

* Fri Jun 03 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1-4mdk
- rebuild

* Sun May 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.1-3mdk
- build release

