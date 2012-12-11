%define	name	noflushd
%define	version	2.7.5
%define	release	%mkrel 7

Summary:	Daemon that sends idle disks to sleep
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Configuration/Other
Source0:	http://ufpr.dl.sourceforge.net/sourceforge/noflushd/%{name}_%{version}.orig.tar.bz2
Source1:	%{name}.sysconfig
Source2:	%{name}.init
URL:		http://noflushd.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires(pre):	rpm-helper

%description
noflushd is a simple daemon that monitors disk activity and spins down
disks whose idle time exceeds a certain timeout. It requires a kernel thread
named kupdate which is present in Linux kernel version 2.2.11 and later. For
earlier kernels, bdflush version 1.6 provides equal functionality.

%prep
%setup -q

%build
%configure --with-scheme=redhat
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%{makeinstall_std} initdir=%{_initrddir}
install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -D -m 755 %{SOURCE2} %{buildroot}%{_initrddir}/%{name}

# (sb) - remove misinstalled docs
rm -fr %{buildroot}/usr/doc

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README AUTHORS NEWS ChangeLog THANKS TODO BUGS
%{_sbindir}/%{name}
%config(noreplace) %{_initrddir}/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_mandir}/man8/%{name}.8*



%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 2.7.5-7mdv2011.0
+ Revision: 664790
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.7.5-5mdv2010.0
+ Revision: 430181
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 2.7.5-4mdv2009.0
+ Revision: 254057
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 2.7.5-2mdv2008.1
+ Revision: 141006
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Aug 11 2006 Stew Benedict <sbenedict@mandriva.com> 2.7.5-2mdv2007.0
- rebuild, Requires(pre)

* Tue Jul 26 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.7.5-1mdk
- 2.7.5

* Tue Nov 16 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 2.7.4-1mdk
- 2.7.4
- don't wipe out buildroot in %%prep

* Mon May 03 2004 Stew Benedict <sbenedict@mandrakesoft.com> 2.7.3-1mdk
- 2.7.3

* Thu Jan 22 2004 Stew Benedict <sbenedict@mandrakesoft.com> 2.7-1mdk
- 2.7

* Fri Jan 02 2004 Stew Benedict <sbenedict@mandrakesoft.com> 2.6.3-3mdk
- rebuild

