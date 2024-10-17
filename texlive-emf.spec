Name:		texlive-emf
Version:	42023
Release:	2
Summary:	Support for the EMF symbol
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/emf
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX support for the symbol for the EMF
in electric circuits and electrodynamics. It provides support
for multiple symbols but does not provide any fonts. The fonts
themselves must be aquired otherwise. However the fonts are
part of a normal TeX Live installation.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/emf
%doc %{_texmfdistdir}/doc/latex/emf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
