Name:		texlive-uafthesis
Version:	57349
Release:	1
Summary:	Document class for theses at University of Alaska Fairbanks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uafthesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uafthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uafthesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is an "unofficial" official class.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/uafthesis/uafthesis.cls
%doc %{_texmfdistdir}/doc/latex/uafthesis/Makefile
%doc %{_texmfdistdir}/doc/latex/uafthesis/README.md
%doc %{_texmfdistdir}/doc/latex/uafthesis/bib_styles/agufull08.bst
%doc %{_texmfdistdir}/doc/latex/uafthesis/bib_styles/unsrtabbrv3.bst
%doc %{_texmfdistdir}/doc/latex/uafthesis/example/abstract.tex
%doc %{_texmfdistdir}/doc/latex/uafthesis/example/acknowledgements.tex
%doc %{_texmfdistdir}/doc/latex/uafthesis/example/apx1.tex
%doc %{_texmfdistdir}/doc/latex/uafthesis/example/build.sh
%doc %{_texmfdistdir}/doc/latex/uafthesis/example/ch1.tex
%doc %{_texmfdistdir}/doc/latex/uafthesis/example/ch2.tex
%doc %{_texmfdistdir}/doc/latex/uafthesis/example/ch3.tex
%doc %{_texmfdistdir}/doc/latex/uafthesis/example/custom-macros.tex
%doc %{_texmfdistdir}/doc/latex/uafthesis/example/example.loa.bk
%doc %{_texmfdistdir}/doc/latex/uafthesis/example/example.tex
%doc %{_texmfdistdir}/doc/latex/uafthesis/example/example.toc.bk
%doc %{_texmfdistdir}/doc/latex/uafthesis/example/fig/fivebatteries.png
%doc %{_texmfdistdir}/doc/latex/uafthesis/example/fig/onebattery.png
%doc %{_texmfdistdir}/doc/latex/uafthesis/example/quotepage.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
