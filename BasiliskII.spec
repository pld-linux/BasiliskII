Summary:   A software emulation of the Aplle Macintosh
Summary(pl): Programowy emulator Maca
Name:      BasiliskII
Version:   0.6
Release:   1
URL:       http://www.uni-mainz.de/~bauec002/B2Main.html
Source:    BasiliskII_src_120799.tar.gz
Copyright: GPL
Group:     Applications/Emulators
Group(pl): Aplikacje/Emulatory
Vendor: PLD
Packager: Roman Niewiarowski <newrom@pasjo.net.pl>
BuildRoot: /tmp/%{name}-%{version}-root

%description
BasiliskII is a software emulation of Aple Macintosh system
hardware, which enables you to run most available Mac software.  Since
it is a software emulation, no extra or special hardware is needed.
BasiliskII can be run with MacOS 7.X or 8.X (but 7.0.0 is not recommended)
ROM file are not included in this archive, You need a really mac 68k
Warning!!! This is the alpha release!!!

%description -l pl
BasiliskII jest programowym emulatorem komputera Aplle Macintosh, 
pozwal±jacym na uruchomienie wiêkszosci aplikacji MacOSa. 
Emulacja przeprowadzana jest programowo wiêc  nie jest konieczne posiadanie 
dodatkowego sprzêtu.  BasiliskII mo¿e pracowaæ z MacOSem 7.X lub 8.X 
(aczkolwiek 7.0.0 nie jest polecany)
Uwaga!!! Program jest w stadium alfa!!!!

%prep
%setup -q

%build
cd src/Unix
./configure --prefix=/usr

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
* Fri Jul 23 1999 Roman Niewiarowski <newrom@pasjo.net.pl>
  [0.6-1]
- First rpm release
- Hallo World ;)

%changelog -l pl
* Fri Jul 23 1999 Roman Niewiarowski <newrom@pasjo.net.pl>
  [0.6-1]
- Pierwsze wydanie w rpmie :)
- Hallo World ;)
