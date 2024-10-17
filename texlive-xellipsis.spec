Name:		texlive-xellipsis
Version:	47546
Release:	2
Summary:	Extremely configurable ellipses with formats for various style manuals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xellipsis
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xellipsis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xellipsis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xellipsis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The xellipsis package provides a system for configuring
(almomst) every possible aspect of ellipses, including
preceding and proceeding characters; the character itself;
distances before and after each of these; and number of
characters. It comes with both a compatibility option for
standard LaTeX \ldots as well as preset package options for the
Chicago Manual of Style (Turabian); the Bluebook; and MLA
guidelines.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/xellipsis
%{_texmfdistdir}/tex/latex/xellipsis
%doc %{_texmfdistdir}/doc/latex/xellipsis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
