Name:		bootimagesync
Version:	0.1
Release:	1%{?dist}
Summary:	Bootimagesync - sync boot images for network installation of Linux 

Group:		Applications/System
License:	Apache License, Version 2.0
URL:		https://github.com/hoonetorg/%{name}
Source0:	https://github.com/hoonetorg/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	rpm-build
Requires:	bash, coreutils, cpio, curl, lftp, xz
Requires(post): policycoreutils-python
Requires(postun): policycoreutils-python

%description

%clean
rm -rf %{buildroot}

%prep
%setup -q

%install
rm -rf %{buildroot}
mkdir %{buildroot}

install -d -m0755 %{buildroot}/%{_bindir}/
install -c -m0755 %{name} %{buildroot}/%{_bindir}/

install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}
install -c -m0644 %{name}.conf %{buildroot}%{_sysconfdir}/%{name}/
install -r -m0644 %{name}.conf.d/ %{buildroot}%{_sysconfdir}/%{name}/

%files
%defattr(-,root,root,-)

%doc COPYRIGHT LICENSE README* 

%{buildroot}/%{_bindir}/%{name}

%dir %attr(-,root,root) %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf.d/

#%post
#semanage fcontext -a -t httpd_sys_rw_content_t '%{_sysconfdir}/%{name}(/.*)?' 2>/dev/null || :
#restorecon -R %{_sysconfdir}/%{name} || :

#%postun
#if [ $1 -eq 0 ] ; then  # final removal
#semanage fcontext -d -t httpd_sys_rw_content_t '%{_sysconfdir}/%{name}(/.*)?' 2>/dev/null || :
#fi

%changelog
