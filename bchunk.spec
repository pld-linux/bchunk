Summary:	A CD image format converter from .bin/.cue to .iso/.cdr
Summary(pl):	Konwerter obrazów p³yt CD z .bin/.cue do .iso/.cdr
Name:		bchunk
Version:	1.1.1
Release:	1
License:	GPL
Vendor:		Heikki Hannikainen <hessu@pspt.fi>
Group:		Applications/Archiving
Source0:	http://hes.iki.fi/bchunk/%{name}-%{version}.tar.gz
# Source0-md5: 9a86fde990df3a58fad51876139f121c
URL:		http://hes.iki.fi/bchunk/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The bchunk package contains a UNIX/C rewrite of the BinChunker
program.. BinChunker converts a CD image in a .bin/.cue format
(sometimes .raw/.cue) into a set of .iso and .cdr tracks. The
.bin/.cue format is used by some non-UNIX CD-writing software, but is
not supported on most other CD-writing programs.

%description -l pl
Konwerter obrazów CD z formatu .bin/.cue (czasami .raw/.cue) do
formatu .iso i ¶cie¿ek .cdr. Format .bin/.cue jest czasami u¿ywany
przez niektóre nie-UNIXowe programy do wypalania CD, a nie jest
wspierany przez wiêkszo¶æ uniksowych programów do wypalania.

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
