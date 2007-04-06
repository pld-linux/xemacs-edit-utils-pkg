Summary:	Miscellaneous editor extensions
Summary(pl.UTF-8):	Różne rozszerzenia dla edytora
Name:		xemacs-edit-utils-pkg
%define		srcname	edit-utils
Version:	2.32
Release:	1	
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	c858e39c25478b3797a5859c991d7bc9
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Miscellaneous xemaqcs editor extensions, you probably want to have
installed in your system.

%description -l pl.UTF-8
Różne rozszerzenia dla xemacsa, które najprawdopodobniej chcesz mieć
zainstalowane w swoim systemie.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/edit-utils/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
%{_datadir}/xemacs-packages/info/edit-utils.info
%{_datadir}/xemacs-packages/info/tempo.info
%{_datadir}/xemacs-packages/pkginfo/MANIFEST.edit-utils
