%global tl_name emf
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1
Release:	%{tl_revision}.1
Summary:	Support for the EMF symbol
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/emf
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/emf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/emf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX support for the symbol for the EMF in
electric circuits and electrodynamics. It provides support for multiple
symbols but does not provide any fonts; the fonts are part of a normal
TeX Live installation.

