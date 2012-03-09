Summary: GNOME terminal
Name: gnome-terminal
Version: 3.2.1
Release: 1
License: GPLv2+
Group: Graphical desktop/GNOME
URL: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
# (fc) 2.0.0-2mdk add -geometry support
Patch0:  gnome-terminal-2.25.3-geometry.patch
# (fc) 2.8.0-2mdk change default background (grey on black)
Patch2:	gnome-terminal-2.10.0-background.patch

BuildRequires:	gnome-doc-utils
BuildRequires:	intltool
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(glib-2.0)
#for gtk-builder-convert
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
#BuildRequires:	pkgconfig(ice)
BuildRequires:	libice-devel
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(vte-2.90)
BuildRequires:	pkgconfig(x11)

%description
This is the GNOME terminal emulator application.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-schemas-install \
	--disable-scrollkeeper \
	--with-gtk=3.0

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name} --with-gnome

%post
if [ "$1" = "2" ]; then
	update-alternatives --remove xvt %{_bindir}/gnome-terminal
fi

%files -f %{name}.lang
%doc AUTHORS README NEWS HACKING
%{_sysconfdir}/gconf/schemas/*
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/gnome-terminal

