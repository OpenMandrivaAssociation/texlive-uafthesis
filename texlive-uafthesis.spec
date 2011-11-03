# revision 22206
# category Package
# catalog-ctan /macros/latex/contrib/uafthesis
# catalog-date 2011-04-25 19:25:49 +0200
# catalog-license lppl
# catalog-version 5.0
Name:		texlive-uafthesis
Version:	5.0
Release:	1
Summary:	Document class for theses at University of Alaska Fairbanks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uafthesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uafthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uafthesis.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is an "unofficial" official class.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/uafthesis/uafthesis.cls
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
%doc %{_texmfdistdir}/doc/latex/uafthesis/example/example.bib
%doc %{_texmfdistdir}/doc/latex/uafthesis/example/example.loa.bk
%doc %{_texmfdistdir}/doc/latex/uafthesis/example/example.pdf
%doc %{_texmfdistdir}/doc/latex/uafthesis/example/example.tex
%doc %{_texmfdistdir}/doc/latex/uafthesis/example/example.toc.bk
%doc %{_texmfdistdir}/doc/latex/uafthesis/example/fig/fivebatteries.png
%doc %{_texmfdistdir}/doc/latex/uafthesis/example/fig/onebattery.png
%doc %{_texmfdistdir}/doc/latex/uafthesis/example/quotepage.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
