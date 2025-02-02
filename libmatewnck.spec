%define	major	0
%define	libname	%mklibname matewnck %{major}
%define	devname	%mklibname -d matewnck

Summary:	A Window Navigator Construction Kit
Name:		libmatewnck
Version:	1.4.0
Release:	2
License:	LGPLv2+
Group:		System/Libraries
URL:		https://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires: intltool
BuildRequires: mate-common
BuildRequires: gtk-doc
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(libstartup-notification-1.0)

%description
libmatewnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}
Requires:	%{name} >= %{version}

%description -n %{libname}
libmatewnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%package -n %{devname}
Summary:	Development libraries, include files for libmatewnck
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description -n %{devname}
libmatewnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static

%make 

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/matewnckprop
%{_bindir}/matewnck-urgency-monitor

%files -n %{libname}
%{_libdir}/libmatewnck.so.%{major}*
%{_libdir}/girepository-1.0/Matewnck-1.0.typelib

%files -n %{devname}
%doc ChangeLog README AUTHORS
%doc %{_datadir}/gtk-doc/html/libmatewnck
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/Matewnck-1.0.gir



%changelog
* Fri Aug 03 2012 Bogdano Arendartchuk <bogdano@mandriva.com> 1.4.0-2
+ Revision: 811640
- release bump (previous release partially installed into the repository)

* Thu Aug 02 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.4.0-1
+ Revision: 811635
- imported package libmatewnck

