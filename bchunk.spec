Summary:	A CD image format converter from .bin/.cue to .iso/.cdr
Summary(pl.UTF-8):   Konwerter obrazów płyt CD z .bin/.cue do .iso/.cdr
Name:		bchunk
Version:	1.2.0
Release:	0.1
License:	GPL
Group:		Applications/Archiving
Source0:	http://hes.iki.fi/bchunk/%{name}-%{version}.tar.gz
# Source0-md5:	6a613da3f34f9a303f202d2e9731d231
URL:		http://hes.iki.fi/bchunk/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The bchunk package contains a UNIX/C rewrite of the BinChunker
program.. BinChunker converts a CD image in a .bin/.cue format
(sometimes .raw/.cue) into a set of .iso and .cdr tracks. The
.bin/.cue format is used by some non-UNIX CD-writing software, but is
not supported on most other CD-writing programs.

%description -l pl.UTF-8
Konwerter obrazów CD z formatu .bin/.cue (czasami .raw/.cue) do
formatu .iso i ścieżek .cdr. Format .bin/.cue jest czasami używany
przez niektóre nieuniksowe programy do wypalania CD, a nie jest
obsługiwany przez większość uniksowych programów do wypalania.

%prep
%setup -q

%build
%{__cc} %{rpmcflags} %{name}.c -o %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bchunk $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/bchunk
