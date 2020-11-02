# libxinerama is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define major 1
%define libname %mklibname xinerama %{major}
%define devname %mklibname xinerama -d
%if %{with compat32}
%define lib32name libxinerama%{major}
%define dev32name libxinerama-devel
%endif

%global optflags %{optflags} -O3

Summary:	The Xinerama Library
Name:		libxinerama
Version:	1.1.4
Release:	4
License:	MIT
Group:		Development/X11
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXinerama-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xext) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
%if %{with compat32}
BuildRequires:	devel(libX11)
BuildRequires:	devel(libXext)
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXdmcp)
%endif

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

%description -n %{devname}
Development files for %{name}.

%if %{with compat32}
%package -n %{lib32name}
Summary:	The Xinerama Library (32-bit)
Group:		Development/X11

%description -n %{lib32name}
The Xinerama Library.

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11
Requires:	%{devname} = %{EVRD}
Requires:	%{lib32name} = %{EVRD}

%description -n %{dev32name}
Development files for %{name}.
%endif

%prep
%autosetup -n libXinerama-%{version} -p1
export CONFIGURE_TOP="`pwd`"
%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif
mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/libXinerama.so.%{major}*

%files -n %{devname}
%{_libdir}/libXinerama.so
%{_libdir}/pkgconfig/xinerama.pc
%{_includedir}/X11/extensions/*.h
%{_mandir}/man3/*

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libXinerama.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libXinerama.so
%{_prefix}/lib/pkgconfig/xinerama.pc
%endif
