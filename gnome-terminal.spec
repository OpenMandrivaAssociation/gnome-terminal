%define _disable_rebuild_configure 1
%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _userunitdir /usr/lib/systemd/user/

Summary:	GNOME terminal
Name:		gnome-terminal
Version:	3.46.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org/
# Source at gnome.org is no longer updated for gnome-terminal... use package from gitlab instead
#Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-terminal/%{url_ver}/%{name}-%{version}.tar.xz
Source0:  https://gitlab.gnome.org/GNOME/gnome-terminal/-/archive/%{version}/gnome-terminal-%{version}.tar.bz2

BuildRequires:	meson
BuildRequires:	appstream-util
BuildRequires:  docbook-xsl
BuildRequires:	vala
BuildRequires:	vala-devel
BuildRequires:	vala-tools
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	rarian
BuildRequires:	xsltproc
BuildRequires:	gnome-shell
BuildRequires:	pkgconfig(dconf)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gio-2.0) >= 2.33.2
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0)
#for gtk-builder-convert
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libpcre2-8)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(vte-2.91) >= 0.54.1
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(libnautilus-extension-4)
BuildRequires:	pkgconfig(uuid)
BuildRequires:  systemd
BuildRequires:	libxml2-utils
BuildRequires:	libxslt-proc

Recommends:	%{name}-nautilus

%description
This is the GNOME terminal emulator application.

%package nautilus
Summary:	Open a terminal in a specified folder
Group:		Graphical desktop/GNOME

Provides:	nautilus-open-terminal = %{version}-%{release}
Obsoletes:	nautilus-open-terminal < 0.20-6

%description nautilus
An extension for Nautilus which allows you to open a terminal in arbitrary
local folders.

%prep
%setup -q
%autopatch -p1

%build
%meson -Dnautilus_extension=true

%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%{_bindir}/*
%{_datadir}/applications/*
#{_libdir}/nautilus/extensions-3.0/libterminal-nautilus.so
%{_libdir}/gnome-terminal/gschemas.compiled
%{_libexecdir}/gnome-terminal-server
%{_libexecdir}/gnome-terminal-preferences
%{_datadir}/dbus-1/services/org.gnome.Terminal.service
%{_datadir}/glib-2.0/schemas/org.gnome.Terminal.gschema.xml
%{_datadir}/gnome-shell/search-providers/gnome-terminal-search-provider.ini
#{_datadir}/metainfo/*gnome*.appdata.xml
%{_datadir}/metainfo/*gnome*.metainfo.xml
%{_mandir}/man1/gnome-terminal.1.*
%{_iconsdir}/hicolor/*/apps/org.gnome.Terminal*.svg
%{_userunitdir}/gnome-terminal-server.service

%files nautilus
#{_libdir}/nautilus/extensions-3.0/libterminal-nautilus.so
