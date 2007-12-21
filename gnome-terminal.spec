Summary: GNOME terminal
Name: gnome-terminal
Version: 2.21.4
Release: %mkrel 1
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Source1: gnome-terminal-32.png
Source2: gnome-terminal-16.png
# (fc) 2.0.0-2mdk add -geometry support
Patch0:  gnome-terminal-2.6.1-geometry.patch
# (fc) 2.8.0-2mdk change default background (grey on black)
Patch2:	gnome-terminal-2.10.0-background.patch
Patch3: gnome-terminal-2.18.2-desktopentry.patch
License: GPL
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
BuildRequires: perl-XML-Parser
BuildRequires: gnome-doc-utils libxslt-proc
BuildRequires: desktop-file-utils
Requires(post): scrollkeeper >= 0.3
Requires(postun): scrollkeeper >= 0.3

%description
GNOME Terminal

%prep
%setup -q
%patch0 -p1 -b .geometry
%patch2 -p1 -b .background
%patch3 -p1

%build
%configure2_5x --with-widget=vte

%make

%install
rm -rf $RPM_BUILD_ROOT

GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std
rm -rf %buildroot/var

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-only-show-in="GNOME" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

mkdir -p $RPM_BUILD_ROOT{%_miconsdir,%_liconsdir}
cp -f %{SOURCE1} $RPM_BUILD_ROOT%{_iconsdir}/gnome-terminal.png
cp -f %{SOURCE2} $RPM_BUILD_ROOT%{_miconsdir}/gnome-terminal.png
cp -f $RPM_BUILD_ROOT/%{_datadir}/pixmaps/gnome-terminal.png $RPM_BUILD_ROOT%{_liconsdir}/gnome-terminal.png

%find_lang %{name} --with-gnome
for omf in %buildroot%_datadir/omf/%name/%name-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/%name-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done

%define schemas gnome-terminal

%post
%update_scrollkeeper
%post_install_gconf_schemas %{schemas}
%{update_menus}
if [ "$1" = "2" ]; then
		update-alternatives --remove xvt %{_bindir}/gnome-terminal
fi

%preun
%preun_uninstall_gconf_schemas %{schemas}
%postun
%clean_scrollkeeper
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog AUTHORS README NEWS HACKING
%{_sysconfdir}/gconf/schemas/*
%{_bindir}/*
%{_libdir}/bonobo/servers/*
%{_datadir}/applications/*
%{_datadir}/gnome-terminal
%{_datadir}/pixmaps/*
%dir %{_datadir}/omf/gnome-terminal
%{_datadir}/omf/gnome-terminal/*-C.omf
%{_iconsdir}/*.png
%{_liconsdir}/*.png
%{_miconsdir}/*.png

