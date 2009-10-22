Summary: GNOME terminal
Name: gnome-terminal
Version: 2.28.1
Release: %mkrel 1
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
# (fc) 2.0.0-2mdk add -geometry support
Patch0:  gnome-terminal-2.25.3-geometry.patch
# (fc) 2.8.0-2mdk change default background (grey on black)
Patch2:	gnome-terminal-2.10.0-background.patch
License: GPLv2+
URL: http://www.gnome.org/
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: gtk+2.0 >= 2.5.4
BuildRequires: gettext
BuildRequires: vte-devel >= 0.13.4
BuildRequires: gtk+2-devel >= 2.5.4
BuildRequires: glib2-devel >= 2.15.0
BuildRequires: libgnomeui2-devel
BuildRequires: libglade2.0-devel
BuildRequires: startup-notification-devel >= 0.8
BuildRequires: scrollkeeper
BuildRequires: intltool >= 0.39.99
BuildRequires: gnome-doc-utils libxslt-proc
BuildRequires: desktop-file-utils
Requires(post): scrollkeeper >= 0.3
Requires(postun): scrollkeeper >= 0.3

%description
This is the GNOME terminal emulator application.

%prep
%setup -q
%patch0 -p1 -b .geometry
%patch2 -p1 -b .background

%build
%configure2_5x 

%make

%install
rm -rf $RPM_BUILD_ROOT

GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std
rm -rf %buildroot/var

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-only-show-in="GNOME" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


%find_lang %{name} --with-gnome
for omf in %buildroot%_datadir/omf/%name/%name-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/%name-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done

%define schemas gnome-terminal

%post
%if %mdkversion < 200900
%update_scrollkeeper
%post_install_gconf_schemas %{schemas}
%{update_menus}
%endif
if [ "$1" = "2" ]; then
		update-alternatives --remove xvt %{_bindir}/gnome-terminal
fi

%preun
%preun_uninstall_gconf_schemas %{schemas}
%if %mdkversion < 200900
%postun
%clean_scrollkeeper
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README NEWS HACKING
%{_sysconfdir}/gconf/schemas/*
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/gnome-terminal
%dir %{_datadir}/omf/gnome-terminal
%{_datadir}/omf/gnome-terminal/*-C.omf

