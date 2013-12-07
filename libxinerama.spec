%define major 1
%define libname %mklibname xinerama %{major}
%define devname %mklibname xinerama -d

Summary:	The Xinerama Library
Name:		libxinerama
Version:	1.1.3
Release:	8
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
%setup -qn libXinerama-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXinerama.so.%{major}*

%files -n %{devname}
%{_libdir}/libXinerama.so
%{_libdir}/pkgconfig/xinerama.pc
%{_includedir}/X11/extensions/*.h
%{_mandir}/man3/*

