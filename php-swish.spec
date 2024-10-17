%define modname swish
%define dirname %{modname}
%define soname %{modname}.so
%define inifile B08_%{modname}.ini

Summary:	Swish-e bindings
Name:		php-%{modname}
Version:	0.5.0
Release:	2
Group:		Development/PHP
License:	PHP License
URL:		https://pecl.php.net/package/swish/
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
BuildRequires:	php-devel >= 3:5.2.0
BuildRequires:	swish-e-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This extension provides bindings to the Swish-e API.

%prep

%setup -q -n %{modname}-%{version}
[ "../package*.xml" != "/" ] && mv ../package*.xml .

%build
%serverbuild

phpize
%configure2_5x --with-libdir=%{_lib} \
    --with-%{modname}=shared,%{_prefix}
%make
mv modules/*.so .

%install
rm -rf %{buildroot} 

install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_sysconfdir}/php.d

install -m755 %{soname} %{buildroot}%{_libdir}/php/extensions/

cat > %{buildroot}%{_sysconfdir}/php.d/%{inifile} << EOF
extension = %{soname}
EOF

%post
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
	%{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc CREDITS README swish.php package*.xml
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}



%changelog
* Sun May 06 2012 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-1mdv2012.0
+ Revision: 797178
- 0.5.0 (the patch was added)

* Sun May 06 2012 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-14
+ Revision: 797015
- fix build
- rebuild for php-5.4.x

* Sun Jan 15 2012 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-13
+ Revision: 761303
- rebuild

* Wed Aug 24 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-12
+ Revision: 696476
- rebuilt for php-5.3.8

* Fri Aug 19 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-11
+ Revision: 695471
- rebuilt for php-5.3.7

* Sat Mar 19 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-10
+ Revision: 646691
- rebuilt for php-5.3.6

* Sat Jan 08 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-9mdv2011.0
+ Revision: 629881
- rebuilt for php-5.3.5

* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-8mdv2011.0
+ Revision: 628195
- ensure it's built without automake1.7

* Wed Nov 24 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-7mdv2011.0
+ Revision: 600537
- rebuild

* Sun Oct 24 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-6mdv2011.0
+ Revision: 588874
- rebuild

* Fri Mar 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-5mdv2010.1
+ Revision: 514664
- rebuilt for php-5.3.2

* Sat Jan 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-4mdv2010.1
+ Revision: 485489
- rebuilt for php-5.3.2RC1

* Sat Nov 21 2009 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-3mdv2010.1
+ Revision: 468260
- rebuilt against php-5.3.1

* Wed Oct 07 2009 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-2mdv2010.0
+ Revision: 455463
- rebuild

* Tue Oct 06 2009 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-1mdv2010.0
+ Revision: 454759
- import php-swish


* Tue Oct 06 2009 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-1mdv2010.0
- initial Mandriva package
