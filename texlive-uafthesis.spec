%global tl_name uafthesis
%global tl_revision 57349

Name:		texlive-%{tl_name}
Epoch:		1
Version:	12.12
Release:	%{tl_revision}.1
Summary:	Document class for theses at University of Alaska Fairbanks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uafthesis
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uafthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uafthesis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is an "unofficial" official class.

