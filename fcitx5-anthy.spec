Summary:	Anthy (Japanese IM) plugin for fcitx5
Name:		fcitx5-anthy
Version:	5.1.6
Release:	1
Source0:    https://github.com/fcitx/fcitx5-anthy/archive/refs/tags/%{version}.tar.gz
URL:		https://github.com/fcitx/fcitx5-anthy
License:	GPLv2
Group:		System/Internationalization
BuildRequires:	cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  lib64gettext-devel
BuildRequires:  lib64anthy-devel

# https://github.com/OpenMandrivaAssociation/distribution/issues/2918
Requires: locales-extra-charsets

%description
Anthy (Japanese IM) plugin for fcitx5.

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %name

%files -f %name.lang
%{_libdir}/fcitx5/libanthy.so
%{_datadir}/fcitx5/addon/anthy.conf
%{_datadir}/fcitx5/anthy/*
%{_datadir}/fcitx5/inputmethod/anthy.conf
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.Anthy.metainfo.xml
