Summary: GNOME terminal
Name: gnome-terminal
Version: 3.0.1
Release: %mkrel 2
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
BuildRequires: vte-devel >= 0.26.0
BuildRequires: gtk+2-devel >= 2.18.0
BuildRequires: glib2-devel >= 2.26.0
BuildRequires: libGConf2-devel >= 2.31.3
BuildRequires: GConf2
BuildRequires: gsettings-desktop-schemas-devel >= 0.1.0
BuildRequires: libsm-devel
BuildRequires: libice-devel
BuildRequires: startup-notification-devel >= 0.8
BuildRequires: scrollkeeper
BuildRequires: intltool >= 0.39.99
BuildRequires: gnome-doc-utils libxslt-proc
BuildRequires: desktop-file-utils

%description
This is the GNOME terminal emulator application.

%prep
%setup -q
%apply_patches

%build
%configure2_5x --disable-schemas-install --disable-scrollkeeper --with-gtk=2.0
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-only-show-in="GNOME" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang %{name} --with-gnome
for omf in %buildroot%_datadir/omf/%name/%name-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/%name-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done

%post
if [ "$1" = "2" ]; then
	update-alternatives --remove xvt %{_bindir}/gnome-terminal
fi

%preun
%preun_uninstall_gconf_schemas %{name}

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
