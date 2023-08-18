Name: switcheroo-control
Version: 2.6
Release: 1
Source0: https://gitlab.freedesktop.org/hadess/switcheroo-control/-/archive/%{version}/switcheroo-control-%{version}.tar.bz2
# Upstream patches between 2.6 and archiving
Patch0: https://gitlab.freedesktop.org/hadess/switcheroo-control/-/commit/c483c0994fcf1915ab22de5ea07e281543c4098b.patch
Patch1: https://gitlab.freedesktop.org/hadess/switcheroo-control/-/commit/e31b3686784f14d93fa7117cd4d0d9c40b65ff8c.patch
Patch2: https://gitlab.freedesktop.org/hadess/switcheroo-control/-/commit/9ba30e9eeeeee53831f6619bb2dd49aec7c1059b.patch
Summary: D-Bus service to check the availability of dual-GPU
URL: https://gitlab.freedesktop.org/hadess/switcheroo-control
License: GPL-3.0
Group: System/Libraries
BuildRequires: meson ninja
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(systemd) systemd

%description
D-Bus service to check the availability of dual-GPU

%prep
%autosetup -p1
%meson

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/switcherooctl
%{_prefix}/lib/systemd/system/switcheroo-control.service
%{_prefix}/lib/udev/hwdb.d/30-pci-intel-gpu.hwdb
%{_libexecdir}/switcheroo-control
%{_datadir}/dbus-1/system.d/net.hadess.SwitcherooControl.conf
