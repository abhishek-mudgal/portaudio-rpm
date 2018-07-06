Name:           portaudio
Version:        190600_20161030-1
Release:        1
Summary:        Portable Real-Time Audio Library
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://www.portaudio.com/
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  alsa-lib-devel
BuildRequires:  doxygen
BuildRequires:  libjack-devel

%description
PortAudio is a portable audio I/O library designed for cross-platform
support of audio. It uses a callback mechanism to request audio
processing. Audio can be generated in various formats, including 32 bit
floating point, and will be converted to the native format internally.

%prep
%setup -q -n %{name}-%{version}/portaudio

%build
./configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{?buildroot}
rm -f %{buildroot}/%{_libdir}/*.la

%files
%defattr(-,root,root)
%doc README.txt LICENSE.txt
%doc doc/html
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so
