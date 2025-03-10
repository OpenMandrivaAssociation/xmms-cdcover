%define name xmms-cdcover
%define version 0.2
%define release %mkrel 11

Name: %{name}
Summary: Visualization plugin for xmms that displays a CD cover if available
Version: %{version}
Release: %{release}
Source: http://ducts.27b-6.de/cdcover/dist/%name-%version.tar.bz2
URL: https://ducts.27b-6.de/cdcover/
License: GPLv2+
Group: Sound
Requires: xmms
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: xmms-devel
BuildRequires: gdk-pixbuf-devel
BuildRequires: automake

%description
CDCover is a plugin for xmms, which displays a graphic dependent on
the currently played song. Normal usage would be to display the 
CD covers for the different songs. The graphics are retrieved from
your computer. Therefore searchpaths can be defined, where a corresponding
cover is searched for.

%prep

%setup -q
autoreconf -fi

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot/%_libdir/xmms/Visualization/libcdcover.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS INSTALL ChangeLog NEWS README
%{_libdir}/xmms/Visualization/libcdcover.so

