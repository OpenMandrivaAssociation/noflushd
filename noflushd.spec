%define	name	noflushd
%define	version	2.7.5
%define	release	%mkrel 2

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

