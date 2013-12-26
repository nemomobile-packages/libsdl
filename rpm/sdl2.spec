Summary: Simple DirectMedia Layer 2
Name: SDL2
Version: 2.0.1
Release: 1
Source: http://www.libsdl.org/release/%{name}-%{version}.tar.gz
URL: http://www.libsdl.org/
License: zlib
Group: System/GUI/Other
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(glesv1_cm)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libpulse-simple)


%description
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

%package devel
Summary: Simple DirectMedia Layer 2 - Development libraries
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

This is the libraries, include files and other resources you can use
to develop SDL applications.


%prep
%setup -q 

%build
%configure --disable-video-x11 --enable-video-wayland --enable-pulseaudio
make

%install
%make_install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc BUGS.txt COPYING.txt CREDITS.txt README-SDL.txt README.txt TODO.txt WhatsNew.txt
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%doc BUGS.txt COPYING.txt CREDITS.txt INSTALL.txt README-gesture.txt README-hg.txt README-linux.txt README-platforms.txt README-porting.txt README-SDL.txt README-touch.txt README.txt TODO.txt WhatsNew.txt
%{_bindir}/*-config
%{_libdir}/lib*.so
%{_includedir}/*/*.h
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*
