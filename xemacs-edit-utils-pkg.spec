### Comment
# This file is modified automatically by 'xemacs-adapter' script
# from PLD-project CVS repository: cvs.pld.org.pl, module SPECS
# For more details see comments in this script
### EndComment

Summary: 	Miscellaneous editor extensions, you probably need this.
Summary(pl):	Miscellaneous editor extensions, you probably need this.

Name:    	xemacs-edit-utils-pkg
%define 	srcname	edit-utils
Version: 	1.41
Release:	1

### Preamble
Copyright:	GPL
Group:    	Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
URL:      	http://www.xemacs.org
Source:   	ftp://ftp.xemacs.org/packages/%{srcname}-%{version}-pkg.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires: 	xemacs
Requires: 	xemacs-base-pkg
### EndPreamble

%description


%description -l pl 


%package el
Summary: 	Miscellaneous editor extensions, you probably need this. This package contains .el files
Summary(pl):	Miscellaneous editor extensions, you probably need this. Pliki ¿ród³owe .el

### ElPreamble
Group:    	Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires: 	%{name} = %{version}
### EndElPreamble


%description el
.el source files -- not necessary to run XEmacs

%description el -l pl
Pliki ¼ród³owe procedur w eLispie do XEmacsa.


### Main
%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
### EndMain

### PrePost
### EndPrePost

### Files
%files
%{_datadir}/xemacs-packages/lisp/*
### EndFiles
