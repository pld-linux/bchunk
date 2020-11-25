Summary:	A CD image format converter from .bin/.cue to .iso/.cdr
Summary(pl.UTF-8):	Konwerter obrazów płyt CD z .bin/.cue do .iso/.cdr
Name:		bchunk
Version:	1.2.2
Release:	1
License:	GPL
Group:		Applications/Archiving
Source0:	http://he.fi/bchunk/%{name}-%{version}.tar.gz
# Source0-md5:	0eeb764647824062085872ddb0b28c5a
Patch0:		install.patch
URL:		http://he.fi/bchunk/
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
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
        LD="%{__cc}" \
        CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BIN_DIR=%{_bindir} \
	MAN_DIR=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/bchunk
%{_mandir}/man1/bchunk.1*
