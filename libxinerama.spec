%define major 1
%define libname %mklibname xinerama %{major}
%define devname %mklibname xinerama -d

Summary:	The Xinerama Library
Name:		libxinerama
Version:	1.1.3
Release:	4
License:	MIT
Group:		Development/X11
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXinerama-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xext) >= 1.0.0
BuildRequires:	x11-proto-devel >= 7.5
BuildRequires:	x11-util-macros >= 1.0.1

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
Obsoletes:	%{_lib}xinerama1-devel < 1.1.2
Obsoletes:	%{_lib}xinerama-static-devel < 1.1.2
# Due to moved man page, to be removed later
Conflicts:	%{libname} < 1.1.3-4
# To be removed soon
Conflicts:	%{name}-manpage < 1.1.3-4
Obsoletes:	%{name}-manpage < 1.1.3-4

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
