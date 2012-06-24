Summary:	Miscellaneous editor extensions, you probably need this
Summary(pl):	Miscellaneous editor extensions, you probably need this
Name:		xemacs-edit-utils-pkg
%define 	srcname	edit-utils
Version:	1.76
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(cs):	Aplikace/Editory/Emacs
Group(da):	Programmer/Tekstbehandlere/Emacs
Group(de):	Applikationen/Editoren/Emacs
Group(es):	Aplicaciones/Editores/Emacs
Group(fr):	Applications/Editeurs/Emacs
Group(is):	Forrit/Ritlar/Emacs
Group(it):	Applicazioni/Editor/Emacs
Group(ja):	���ץꥱ�������/���ǥ���/Emacs
Group(no):	Applikasjoner/Editorer/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Group(pt):	Aplica��es/Editores/Emacs
Group(ru):	����������/���������/Emacs
Group(sl):	Programi/Urejevalniki/Emacs
Group(sv):	Till�mpningar/Editorer/Emacs
Group(uk):	�������Φ ��������/���������/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl 

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

gzip -9nf lisp/edit-utils/ChangeLog 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/edit-utils/ChangeLog.gz 
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
