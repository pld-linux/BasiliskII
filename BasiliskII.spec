Summary:	A software emulation of the Aplle Macintosh
Summary(pl):	Programowy emulator komputera Macintosh
Name:		BasiliskII
Version:	0.9
Release:	2
License:	GPL
Group:		Applications/Emulators
Source0:	http://iphcip1.physik.uni-mainz.de/~cbauer/%{name}_src_31052001.tar.gz
# Source0-md5:	5017e21226c27a4a029da0486dcf04e1
Source1:	%{name}.desktop
Source2:	AppleX.png
Patch0:		%{name}-devices.patch
URL:		http://www.uni-mainz.de/~bauec002/B2Main.html
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BasiliskII is a software emulation of Aple Macintosh system hardware,
which enables you to run most available Mac software. Since it is a
software emulation, no extra or special hardware is needed. BasiliskII
can be run with MacOS 7.X or 8.X (but 7.0.0 is not recommended) ROM
file are not included in this archive, You need a really mac 68k
Warning!!! This is the alpha release!!!

%description -l pl
BasiliskII jest programowym emulatorem komputera Aplle Macintosh,
pozwalaj±cym na uruchomienie wiêkszo¶ci aplikacji MacOSa. Emulacja
przeprowadzana jest programowo, wiêc nie jest konieczne posiadanie
dodatkowego sprzêtu. BasiliskII mo¿e pracowaæ z MacOSem 7.X lub 8.X
(aczkolwiek 7.0.0 nie jest polecany) Uwaga!!! Program jest w stadium
alfa!!!!

%prep
%setup -q
%patch0 -p1

%build
cd src/Unix
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install -C src/Unix \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Amusements
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Amusements
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TECH TODO
%doc src/Unix/Linux
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Amusements/*
%{_pixmapsdir}/*
