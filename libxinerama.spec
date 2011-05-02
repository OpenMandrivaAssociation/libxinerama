%define libname %mklibname xinerama 1
%define develname  %mklibname xinerama -d
%define staticname  %mklibname xinerama -s -d

Name: libxinerama
Summary: The Xinerama Library
Version: 1.1.1
Release: %mkrel 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXinerama-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 7.5
BuildRequires: x11-util-macros >= 1.0.1

%description
The Xinerama Library

#-----------------------------------------------------------

%package -n %{libname}
Summary: The Xinerama Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
The Xinerama Library

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libname} = %{version}-%{release}
Requires: x11-proto-devel >= 7.5
Provides: libxinerama-devel = %{version}-%{release}
Provides: libxinerama1-devel = %{version}-%{release}
Obsoletes: %{mklibname xinerama 1 -d}

Conflicts: libxorg-x11-devel < 7.0
Conflicts: libxinerama-devel < 1.1

%description -n %{develname}
Development files for %{name}

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libXinerama.so
%{_libdir}/libXinerama.la
%{_libdir}/pkgconfig/xinerama.pc
%{_includedir}/X11/extensions/*.h

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}-%{release}
Provides: libxinerama-static-devel = %{version}-%{release}
Provides: libxinerama1-static-devel = %{version}-%{release}
Obsoletes: %{mklibname xinerama 1 -s -d}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libXinerama.a

#-----------------------------------------------------------

%prep
%setup -q -n libXinerama-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libXinerama.so.1
%{_libdir}/libXinerama.so.1.0.0
%_mandir/man3/*
