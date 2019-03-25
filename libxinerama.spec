%define major 1
%define libname %mklibname xinerama %{major}
%define devname %mklibname xinerama -d

%global optflags %{optflags} -O3

Summary:	The Xinerama Library
Name:		libxinerama
Version:	1.1.4
Release:	3
License:	MIT
Group:		Development/X11
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXinerama-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xext) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%description
The Xinerama Library.

%package -n %{libname}
Summary:	The Xinerama Library
Group:		Development/X11

%description -n %{libname}
The Xinerama Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{EVRD}
Provides:	libxinerama-devel = %{EVRD}

%description -n %{devname}
Development files for %{name}.

%prep
%autosetup -n libXinerama-%{version} -p1

%build
%configure \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libXinerama.so.%{major}*

%files -n %{devname}
%{_libdir}/libXinerama.so
%{_libdir}/pkgconfig/xinerama.pc
%{_includedir}/X11/extensions/*.h
%{_mandir}/man3/*
