Summary:   A software emulation of the Aplle Macintosh
Summary(pl): Programowy emulator komputera Macintosh
Name:      BasiliskII
Version:   0.7
Release:   1
URL:       http://www.uni-mainz.de/~bauec002/B2Main.html
Source:    BasiliskII_src_250799.tar.gz
Copyright: GPL
Group:     Applications/Emulators
Group(pl):  Aplikacje/Emulatory
BuildRoot: /tmp/%{name}-%{version}-root

%description
BasiliskII is a software emulation of Aple Macintosh system
hardware, which enables you to run most available Mac software.  Since
it is a software emulation, no extra or special hardware is needed.
BasiliskII can be run with MacOS 7.X or 8.X (but 7.0.0 is not recommended)
ROM file are not included in this archive, You need a really mac 68k
Warning!!! This is the alpha release!!!

%description -l pl
BasiliskII jest programowym emulatorem komputera Aplle Macintosh, pozwal±jacym na 
uruchomienie wiêkszosci aplikacji MacOSa. Emulacja przeprowadzana jest programowo wiêc 
nie jest konieczne posiadanie dodatkowego sprzêtu. 
BasiliskII mo¿e pracowaæ z MacOSem 7.X lub 8.X (aczkolwiek 7.0.0 nie jest polecany)
Uwaga!!! Program jest w stadium alfa!!!!

%prep
%setup -n %{name}

%build
cd src/Unix
CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" CPPFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr

make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/lib/BasiliskII/Linux
install -d $RPM_BUILD_ROOT/usr/X11R6/bin

install -m755 -s src/Unix/BasiliskII $RPM_BUILD_ROOT/usr/X11R6/bin

cp -R src/Unix/Linux/* $RPM_BUILD_ROOT/usr/lib/BasiliskII/Linux
mkdir docs
cp CHANGES COPYING README TECH TODO docs
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc docs/*
/usr/lib/BasiliskII
/usr/X11R6/bin/*

%changelog
* Wed Jul 28 1999 Roman Niewiarowski <newrom@pasjo.net.pl>
  [0.7-1]
-  with 32-bit clean ROMs, the CPU type is now reported as a 68030
          (for those OpenTransport fans :-)
- added new prefs item "nosound" to disable sound output
- sound output implemented for BeOS, Linux, Solaris and AmigaOS (requires Sound Manager 3.x)
- dummy/audio_dummy.cpp: created
- dummy/prefs_dummy.cpp: created
- dummy/xpram_dummy.cpp: created
- macos_util.cpp: added FileDiskLayout()
- video.cpp: removed useless BlankMousePointer flag
- uae_cpu: updated to UAE 0.8.9
- uae_cpu/gencpu.c: fixed bug in CAS2, OpenTransport works now
- Unix: moved Linux- and FreeBSD-specific files to their respective directories
- Unix: added 64-bit data types (needed by timer_unix.cpp)
- Unix: added keyboard translation method using raw keycodes instead of keysyms (controlled by "keycodes" and "keycodefile" prefs items) which doesn't depend on the selected keymap
- Unix: when running as root, Basilisk II tries to assign real-time priorities to some threads
- Unix: calls to nanosleep() protected by autoconf define
- Unix/main_unix.cpp: tick thread replaced by POSIX.4 timer when possible
- Unix/timer_unix.cpp: uses POSIX.4 timing facilities when possible
- Unix/video_x.cpp: all X calls during emulation are now done from the redraw thread which is also active in DGA mode; as a result, XLockServer()/XUnlockServer() are no longer necessary
- Unix/sysdeps.h: changed C++ comments to C comments as this file is included by some *.c files in uae_cpu [Brian J. Johnson]
- Unix/sysdeps.h: added unaligned access functions for SGI MIPSPro compiler [Brian J. Johnson]
- Unix/Irix/unaligned.c: created [Brian J. Johnson]
* Fri Jul 23 1999 Roman Niewiarowski <newrom@pasjo.net.pl>
  [0.6-1]
- First rpm release
- Hallo World ;)
