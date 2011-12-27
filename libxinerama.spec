%define major 1
%define libname %mklibname xinerama %{major}
%define develname  %mklibname xinerama -d

Name: libxinerama
Summary: The Xinerama Library
Version: 1.1.1
Release: 4
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXinerama-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 7.5
BuildRequires: x11-util-macros >= 1.0.1

%description
The Xinerama Library

%package -n %{libname}
Summary: The Xinerama Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
The Xinerama Library

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}-%{release}
Provides: libxinerama-devel = %{version}-%{release}
Obsoletes: %{_lib}xinerama1-devel
Obsoletes: %{_lib}xinerama-static-devel
Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libXinerama-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXinerama.so.%{major}*
%_mandir/man3/*

%files -n %{develname}
%{_libdir}/libXinerama.so
%{_libdir}/pkgconfig/xinerama.pc
%{_includedir}/X11/extensions/*.h

