Summary:	Game Music Emulators
Name:		libgme
Version:	0.5.5
Release:	1
License:	LGPL v2.1+
Group:		Applications/Sound
Source0:	http://game-music-emu.googlecode.com/files/game-music-emu-%{version}.tbz2
# Source0-md5:	94459001a763fb76209a550a03b7949e
URL:		http://code.google.com/p/game-music-emu/
BuildRequires:	cmake >= 2.6
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Game_Music_Emu is a collection of video game music file emulators that
support the following formats and systems:

AY        ZX Spectrum/Amstrad CPC
GBS       Nintendo Game Boy
GYM       Sega Genesis/Mega Drive
HES       NEC TurboGrafx-16/PC Engine
KSS       MSX Home Computer/other Z80 systems (doesn't support FM sound)
NSF/NSFE  Nintendo NES/Famicom (with VRC 6, Namco 106, and FME-7 sound)
SAP       Atari systems using POKEY sound chip
SPC       Super Nintendo/Super Famicom
VGM/VGZ   Sega Master System/Mark III, Sega Genesis/Mega Drive,BBC Micro

Features:
* Can be used in C and C++ code
* High emphasis has been placed on making the library very easy to use
* One set of common functions work with all emulators the same way
* Several code examples, including music player using SDL
* Portable code for use on any system with modern or older C++ compilers
* Adjustable output sample rate using quality band-limited resampling
* Uniform access to text information fields and track timing information
* End-of-track fading and automatic look ahead silence detection
* Treble/bass and stereo echo for AY/GBS/HES/KSS/NSF/NSFE/SAP/VGM
* Tempo can be adjusted and individual voices can be muted while playing
* Can read music data from file, memory, or custom reader function/class
* Can access track information without having to load into full emulator
* M3U track listing support for multi-track formats
* Modular design allows elimination of unneeded emulators/features

This library has been used in game music players for Windows, Linux on
several architectures, Mac OS, MorphOS, Xbox, PlayStation Portable,
GP2X, and Nintendo DS.

%package devel
Summary:	libgme library - developemnt files
Summary(pl.UTF-8):	Biblioteka libgme - pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Game_Music_Emu is a collection of video game music file emulators that
support the following formats and systems:

AY        ZX Spectrum/Amstrad CPC
GBS       Nintendo Game Boy
GYM       Sega Genesis/Mega Drive
HES       NEC TurboGrafx-16/PC Engine
KSS       MSX Home Computer/other Z80 systems (doesn't support FM sound)
NSF/NSFE  Nintendo NES/Famicom (with VRC 6, Namco 106, and FME-7 sound)
SAP       Atari systems using POKEY sound chip
SPC       Super Nintendo/Super Famicom
VGM/VGZ   Sega Master System/Mark III, Sega Genesis/Mega Drive,BBC Micro

Features:
* Can be used in C and C++ code
* High emphasis has been placed on making the library very easy to use
* One set of common functions work with all emulators the same way
* Several code examples, including music player using SDL
* Portable code for use on any system with modern or older C++ compilers
* Adjustable output sample rate using quality band-limited resampling
* Uniform access to text information fields and track timing information
* End-of-track fading and automatic look ahead silence detection
* Treble/bass and stereo echo for AY/GBS/HES/KSS/NSF/NSFE/SAP/VGM
* Tempo can be adjusted and individual voices can be muted while playing
* Can read music data from file, memory, or custom reader function/class
* Can access track information without having to load into full emulator
* M3U track listing support for multi-track formats
* Modular design allows elimination of unneeded emulators/features

This library has been used in game music players for Windows, Linux on
several architectures, Mac OS, MorphOS, Xbox, PlayStation Portable,
GP2X, and Nintendo DS.

The libgme-devel package contains the header files and documentation
needed to develop applications with libgme.

%description devel -l pl.UTF-8
Pakiet libgme-devel zawiera pliki nagłówkowe i dokumentację potrzebne
do kompilowania aplikacji korzystających z libgme.

%prep
%setup -q -n game-music-emu-%{version}

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	.
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc changes.txt design.txt gme.txt readme.txt
%attr(755,root,root) %{_libdir}/libgme.so.0.5.3
%ghost %attr(755,root,root) %{_libdir}/libgme.so.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/gme
%{_libdir}/libgme.so
