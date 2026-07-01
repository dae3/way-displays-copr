%global forgeurl https://github.com/alex-courtis/way-displays
# upstream recommends clang
%global toolchain clang

Name:           way-displays
Version:        1.15.0
Release:        1%{?dist}
Summary:        Auto Manage Your Wayland Displays

%forgemeta

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}
Patch0:         tst.h.patch

BuildRequires: clang
BuildRequires: pkgconfig(wayland)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wlroots)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(yaml-cpp)
BuildRequires: pkgconfig(libcmocka)
BuildRequires: pkgconfig(libcmocka-cmake)

Requires:       wayland

%description
way-displays: Auto Manage Your Wayland Displays
credit: Stephen Barratt

- Set resolution/refresh: preferred, highest or custom
- Enable VRR / adaptive sync
- Arrange in a row or a column
- Auto scale based on DPI: 96 is a scale of 1
- Update when displays plugged/unplugged
- Update when laptop lid closed/opened
- Works out of the box: no configuration required.
- Wayland successor to xlayoutdisplay, inspired by kanshi.

%prep
%forgesetup
%setup -q
%patch 0 -p1

%build
%make_build CC=%{build_cc} CXX=%{build_cxx} PREFIX=%{_prefix} PREFIX_ETC=""
make man

%check
# The rpmbuild linker configuration breaks cmocka's mocking
#  the code generated here isn't packaged into the binary RPM,
#  so we can override back to defaults.
export CFLAGS="-DCMOCKA_DISABLE_DEPRECATION_WARNINGS -fPIE"
export LDFLAGS=""
make CC=%{build_cc} CXX=%{build_cxx} test

%install
%make_install PREFIX=%{_prefix} PREFIX_ETC=""

%files
%{_bindir}/way-displays
%config(noreplace) %{_sysconfdir}/way-displays/cfg.yaml
%{_mandir}/man1/way-displays.1*
%doc README.md doc/CONTRIBUTING.md
%license LICENSE


%changelog
* Sat Jun 27 2026 Daniel Everett
-
