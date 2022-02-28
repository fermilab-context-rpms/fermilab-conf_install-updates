Name:		fermilab-conf_install-updates
Version:	1.0
Release:	1.1%{?dist}
Summary:	Configure automatic updates

Group:		Fermilab
License:	GPL
URL:		https://github.com/fermilab-context-rpms/fermilab-conf_install-updates

Source0:	30-fermilab-conf_install-updates.preset

BuildArch:	noarch

Requires(post):	dnf-automatic
BuildRequires:	systemd


%description
Systems on the Fermilab network must install updates on a regular basis.

%prep


%build


%install
%{__install} -D %{SOURCE0} %{buildroot}/%{_presetdir}/30-fermilab-conf_install-updates.preset


%post
%systemd_post dnf-automatic-install.timer
systemctl enable dnf-automatic-install.timer
systemctl start dnf-automatic-install.timer

%preun
%systemd_preun dnf-automatic-install.timer

%postun
%systemd_postun_with_restart dnf-automatic-install.timer


%files
%{_presetdir}/30-fermilab-conf_install-updates.preset


%changelog
* Wed Jan 29 2020 Pat Riehecky <riehecky@fnal.gov> 1.0-1
- Initial build for EL8
