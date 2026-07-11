%global tl_name xellipsis
%global tl_revision 47546

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Extremely configurable ellipses with formats for various style manuals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xellipsis
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xellipsis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xellipsis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xellipsis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The xellipsis package provides a system for configuring (almomst) every
possible aspect of ellipses, including preceding and proceeding
characters; the character itself; distances before and after each of
these; and number of characters. It comes with both a compatibility
option for standard LaTeX \ldots as well as preset package options for
the Chicago Manual of Style (Turabian); the Bluebook; and MLA
guidelines.

