%define major 1
%define libname %mklibname xinerama %{major}
%define develname %mklibname xinerama -d

Name:		libxinerama
Summary:	The Xinerama Library
Version:	1.1.3
Release:	3
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
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
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{version}
Requires:	%{name}-manpage = %{EVRD}

%description -n %{libname}
The Xinerama Library.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{EVRD}
Provides:	libxinerama-devel = %{EVRD}
Obsoletes:	%{_lib}xinerama1-devel < 1.1.2
Obsoletes:	%{_lib}xinerama-static-devel < 1.1.2
Conflicts:	libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}.

%package manpage
Summary:	Manpage for %{name}
Group:		Books/Howtos
BuildArch:	noarch
Conflicts:	%{mklibname xinerama 1} < 1.1.3-3

%description manpage
Manual for %{name}.


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

%files manpage
%{_mandir}/man3/*

%files -n %{develname}
%{_libdir}/libXinerama.so
%{_libdir}/pkgconfig/xinerama.pc
%{_includedir}/X11/extensions/*.h



%changelog
* Sat Mar 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.2-1
+ Revision: 783938
- version update 1.1.2

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.1.1-4
+ Revision: 745733
- rebuild
- disabled static build
- removed .la files
- cleaned up spec
- employed major macro

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-3
+ Revision: 662423
- mass rebuild

* Sat Feb 19 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.1.1-2
+ Revision: 638656
- dropped the major from devel and static  pkg
- added proper provides and obsoletes

* Thu Oct 28 2010 Thierry Vignaud <tv@mandriva.org> 1.1.1-1mdv2011.0
+ Revision: 589779
- new release

* Mon Nov 09 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.1-1mdv2010.1
+ Revision: 463713
- New version: 1.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.3-3mdv2010.0
+ Revision: 425927
- rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-2mdv2009.0
+ Revision: 264973
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Apr 14 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2009.0
+ Revision: 192984
- new release

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.
    - Update BuildRequires and rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-3mdv2008.1
+ Revision: 150857
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Apr 20 2007 Thierry Vignaud <tv@mandriva.org> 1.0.2-2mdv2008.0
+ Revision: 16015
- package man pages
- new release

