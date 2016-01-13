Summary: NethServer tomcat configuration
Name: nethserver-tomcat
Version: 1.0.1
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: tomcat, tomcat-webapps, tomcat-admin-webapps, java-1.7.0-openjdk
Requires: nethserver-base

BuildRequires: perl
BuildRequires: nethserver-devtools 

%description
NethServer tomcat configuration

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist
echo "%doc COPYING" >> %{name}-%{version}-filelist

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update

%changelog
* Tue May 19 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- Tomcat7 application server - Feature #3132 [NethServer]
- First public release

