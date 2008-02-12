%define libxinerama %mklibname xinerama 1
Name: libxinerama
Summary: The Xinerama Library
Version: 1.0.2
Release: %mkrel 4
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXinerama-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The Xinerama Library

#-----------------------------------------------------------

%package -n %{libxinerama}
Summary: The Xinerama Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxinerama}
The Xinerama Library

#-----------------------------------------------------------

%package -n %{libxinerama}-devel
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libxinerama} = %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libxinerama-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxinerama}-devel
Development files for %{name}

%files -n %{libxinerama}-devel
%defattr(-,root,root)
%{_libdir}/libXinerama.so
%{_libdir}/libXinerama.la
%{_libdir}/pkgconfig/xinerama.pc

#-----------------------------------------------------------

%package -n %{libxinerama}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxinerama}-devel = %{version}
Provides: libxinerama-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxinerama}-static-devel
Static development files for %{name}

%files -n %{libxinerama}-static-devel
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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libxinerama}
%defattr(-,root,root)
%{_libdir}/libXinerama.so.1
%{_libdir}/libXinerama.so.1.0.0
%_mandir/man3/*


