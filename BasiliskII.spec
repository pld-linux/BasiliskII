Summary:	A software emulation of the Aplle Macintosh
Summary(pl):	Programowy emulator komputera Macintosh
Name:		BasiliskII
Version:	0.9
Release:	1
License:	GPL
Group:		Applications/Emulators
Group(de):	Applikationen/Emulators
Group(pl):	Aplikacje/Emulatory
Source0:	http://iphcip1.physik.uni-mainz.de/~cbauer/%{name}_src_31052001.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.uni-mainz.de/~bauec002/B2Main.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
BasiliskII is a software emulation of Aple Macintosh system hardware,
which enables you to run most available Mac software. Since it is a
software emulation, no extra or special hardware is needed. BasiliskII
can be run with MacOS 7.X or 8.X (but 7.0.0 is not recommended) ROM
file are not included in this archive, You need a really mac 68k
Warning!!! This is the alpha release!!!

%description -l pl
BasiliskII jest programowym emulatorem komputera Aplle Macintosh,
pozwal±jacym na uruchomienie wiêkszosci aplikacji MacOSa. Emulacja
przeprowadzana jest programowo, wiêc nie jest konieczne posiadanie
dodatkowego sprzêtu. BasiliskII mo¿e pracowaæ z MacOSem 7.X lub 8.X
(aczkolwiek 7.0.0 nie jest polecany) Uwaga!!! Program jest w stadium
alfa!!!!

%prep
%setup -q 
%patch -p1

%build
cd src/Unix
CXXFLAGS="%{rpmcflags}"
CPPFLAGS="%{rpmcflags}"
LDFLAGS="%{rpmldflags}"
export CPPFLAGS CXXFLAGS LDFLAGS
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

(cd src/Unix
%{__make} install DESTDIR=$RPM_BUILD_ROOT)

gzip -9nf ChangeLog README TECH TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%doc src/Unix/Linux
%attr(755,root,root) %{_bindir}/*
