%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	GNOME terminal
Name:		gnome-terminal
Version:	 3.16.1
Release:	3
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-terminal/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	vala
BuildRequires:	vala-devel
BuildRequires:	vala-tools
BuildRequires:	appdata-tools
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	rarian
BuildRequires:	xsltproc
BuildRequires:	gnome-shell
BuildRequires:	pkgconfig(dconf)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(glib-2.0)
#for gtk-builder-convert
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(vte-2.91)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(libnautilus-extension)

%description
This is the GNOME terminal emulator application.

%prep
%setup -q
%apply_patches

%build
%configure \
	--disable-schemas-install \
	--disable-migration \
	--with-gtk=3.0

%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%post
if [ "$1" = "2" ]; then
	update-alternatives --remove xvt %{_bindir}/gnome-terminal
fi

%files -f %{name}.lang
%doc AUTHORS NEWS HACKING
%{_bindir}/*
%{_datadir}/applications/*
%{_libdir}/nautilus/extensions-3.0/libterminal-nautilus.so
%{_libexecdir}/gnome-terminal-server
%{_datadir}/appdata/gnome-terminal.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Terminal.service
%{_datadir}/glib-2.0/schemas/org.gnome.Terminal.gschema.xml
%{_datadir}/gnome-shell/search-providers/gnome-terminal-search-provider.ini

