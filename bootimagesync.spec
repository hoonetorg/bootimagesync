Name:		bootimagesync
Version:	0.3
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
install -c -m0755 %{name}-links %{buildroot}/%{_bindir}/

install -d -m0755 %{buildroot}/%{_sysconfdir}/%{name}
#install -c -m0644 %{name}.conf %{buildroot}%{_sysconfdir}/%{name}/
install -d -m0644 %{buildroot}/%{_sysconfdir}/%{name}/%{name}.conf.d/
#install -c -m0644 %{name}.conf.d/* %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf.d/

install -d -m0644 %{buildroot}%{_docdir}/%{name}-%{version}/exampleconfigdir/%{name}.conf.d/
install -c -m0644 %{name}.conf %{buildroot}%{_docdir}/%{name}-%{version}/exampleconfigdir/
install -c -m0644 %{name}.conf.d/* %{buildroot}%{_docdir}/%{name}-%{version}/exampleconfigdir/%{name}.conf.d/

%files
%defattr(-,root,root,-)

%doc COPYRIGHT LICENSE README* 

%{_bindir}/%{name}
%{_bindir}/%{name}-links

%dir %attr(-,root,root) %{_sysconfdir}/%{name}
%dir %attr(-,root,root) %{_sysconfdir}/%{name}/%{name}.conf.d
#%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
#%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf.d/*

%dir %attr(-,root,root) %{_docdir}/%{name}-%{version}/exampleconfigdir/%{name}.conf.d
%doc %{_docdir}/%{name}-%{version}/exampleconfigdir/%{name}.conf
%doc %{_docdir}/%{name}-%{version}/exampleconfigdir/%{name}.conf.d/*

#%post
#semanage fcontext -a -t httpd_sys_rw_content_t '%{_sysconfdir}/%{name}(/.*)?' 2>/dev/null || :
#restorecon -R %{_sysconfdir}/%{name} || :

#%postun
#if [ $1 -eq 0 ] ; then  # final removal
#semanage fcontext -d -t httpd_sys_rw_content_t '%{_sysconfdir}/%{name}(/.*)?' 2>/dev/null || :
#fi

%changelog
