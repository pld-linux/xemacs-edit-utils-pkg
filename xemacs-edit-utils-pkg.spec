Summary:	Miscellaneous editor extensions, you probably need this
Summary(pl):	Ró¿ne rozszerzenia edytora, prawdopodobnie bêdziesz tego potrzebowa³
Name:    	xemacs-edit-utils-pkg
%define		srcname edit-utils
Version: 	1.45
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Source0:	ftp://ftp.xemacs.org/packages/%{srcname}-%{version}-pkg.tar.gz
URL:		http://www.xemacs.org/
BuildRoot:	/tmp/%{name}-%{version}-root
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-base-pkg

%description
Miscellaneous editor extensions, you probably need this/

%description -l pl 
Ró¿ne rozszerzenia edytora, prawdopodobnie bêdziesz tego potrzebowa³.

%package el
Summary:	Miscellaneous editor extensions, you probably need this. This package contains .el files
Summary(pl):	Miscellaneous editor extensions, you probably need this. Pliki ¿ród³owe .el
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description el
.el source files -- not necessary to run XEmacs.

%description el -l pl
Pliki ¼ród³owe procedur w eLispie do XEmacsa.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

gzip -9nf lisp/edit-utils/ChangeLog 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/edit-utils/ChangeLog.gz 
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
