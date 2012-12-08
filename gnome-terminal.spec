Summary: GNOME terminal
Name: gnome-terminal
Version: 3.6.1
Release: 1
License: GPLv2+
Group: Graphical desktop/GNOME
URL: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/3.6/%{name}-%{version}.tar.xz
# (fc) 2.0.0-2mdk add -geometry support
Patch0:  gnome-terminal-2.25.3-geometry.patch
# (fc) 2.8.0-2mdk change default background (grey on black)
Patch2:	gnome-terminal-2.10.0-background.patch

BuildRequires:	gnome-doc-utils-devel
BuildRequires:	intltool itstool
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
BuildRequires:	scrollkeeper

%description
This is the GNOME terminal emulator application.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-schemas-install \
	--with-gtk=3.0
#	--disable-scrollkeeper \

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



%changelog
* Fri Oct  5 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-1
- update to 3.6.0

* Mon Sep 03 2012 Vladimir Testov <vladimir.testov@rosalab.ru> 3.4.1.1-1
- update to 3.4.1.1

* Fri Mar 09 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.1-1
+ Revision: 783451
- new version  3.2.1
- cleaned up spec

* Fri May 06 2011 Funda Wang <fwang@mandriva.org> 3.0.1-2mdv2011.0
+ Revision: 669784
- rebuild

* Tue Apr 26 2011 Funda Wang <fwang@mandriva.org> 3.0.1-1
+ Revision: 659122
- update to new version 3.0.1

* Sun Apr 10 2011 Funda Wang <fwang@mandriva.org> 3.0.0-1
+ Revision: 652335
- new version 3.0.0

* Tue Dec 21 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.33.3-1mdv2011.0
+ Revision: 623626
- update build deps
- update to new version 2.33.3

* Sun Nov 14 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.1-1mdv2011.0
+ Revision: 597524
- update to new version 2.32.1

* Sun Sep 26 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581133
- update to new version 2.32.0

* Sun Aug 29 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.91-1mdv2011.0
+ Revision: 574157
- new version
- bump vte dep

* Tue Aug 17 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.90-1mdv2011.0
+ Revision: 570769
- new version
- bump vte dep

* Fri Jul 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.3-1mdv2011.0
+ Revision: 563499
- new version
- update deps

* Sun Jul 11 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.2-1mdv2011.0
+ Revision: 550823
- update to new version 2.30.2

* Mon Apr 26 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.1-1mdv2010.1
+ Revision: 538976
- update to new version 2.30.1

* Tue Mar 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 529683
- new version
- bump vte dep

* Thu Mar 11 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.92-1mdv2010.1
+ Revision: 518254
- new version
- drop patch 1

* Thu Feb 11 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.6-2mdv2010.1
+ Revision: 504135
- fix proxy var (bug #57552)

* Thu Jan 14 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.6-1mdv2010.1
+ Revision: 491181
- new version
- bump vte dep

* Tue Dec 22 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.1-1mdv2010.1
+ Revision: 481470
- update to new version 2.29.1

* Mon Dec 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.2-1mdv2010.1
+ Revision: 478683
- update to new version 2.28.2

* Thu Oct 22 2009 Frederic Crozat <fcrozat@mandriva.com> 2.28.1-1mdv2010.0
+ Revision: 458822
- Release 2.28.1

* Mon Sep 21 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446590
- update to new version 2.28.0

* Sun Sep 06 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.92-1mdv2010.0
+ Revision: 432082
- new version

* Wed Aug 19 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.91-1mdv2010.0
+ Revision: 418276
- update to new version 2.27.91

* Mon Jun 29 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.3.1-1mdv2010.0
+ Revision: 390678
- new version
- remove build workaround

* Mon Jun 29 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.3-1mdv2010.0
+ Revision: 390615
- new version
- fix build

* Wed Jun 10 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.2-3mdv2010.0
+ Revision: 384684
- rebuild for new vte

* Tue Jun 02 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.2-2mdv2010.0
+ Revision: 382164
- rebuild for new libvte

* Wed May 20 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.2-1mdv2010.0
+ Revision: 377947
- update to new version 2.26.2

* Tue Apr 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.1-1mdv2009.1
+ Revision: 366940
- new version
- drop patch 3

* Wed Apr 01 2009 Frederic Crozat <fcrozat@mandriva.com> 2.26.0-2mdv2009.1
+ Revision: 363321
- Patch3 (SVN): various bug fixes, mostly add session saving support

* Sun Mar 15 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 355386
- new version
- drop patch 3

* Wed Mar 04 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.25.91-2mdv2009.1
+ Revision: 348419
- Add patch to fix gnome bug #572549 (crash on closing tabs)

* Tue Feb 17 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 341215
- update to new version 2.25.91

* Fri Jan 30 2009 Pascal Terjan <pterjan@mandriva.org> 2.25.5-2mdv2009.1
+ Revision: 335406
- Fix P0

* Mon Jan 19 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.5-1mdv2009.1
+ Revision: 331342
- update to new version 2.25.5

* Thu Dec 18 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.3-1mdv2009.1
+ Revision: 315972
- new version
- rediff patch 0
- update file list

* Mon Nov 24 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.2-1mdv2009.1
+ Revision: 306427
- update to new version 2.24.2

* Wed Oct 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.1.1-1mdv2009.1
+ Revision: 296485
- update to new version 2.24.1.1

* Tue Oct 21 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 295912
- new version
- drop patch 3

* Wed Oct 01 2008 Frederic Crozat <fcrozat@mandriva.com> 2.24.0-2mdv2009.0
+ Revision: 290546
- Patch3 (SVN): various bug fixes from SVN

* Mon Sep 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 286802
- new version

* Fri Sep 19 2008 Frederic Crozat <fcrozat@mandriva.com> 2.23.91-2mdv2009.0
+ Revision: 285904
- Remove patch1, no longer needed

* Sun Aug 31 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.91-1mdv2009.0
+ Revision: 277784
- new version

* Mon Aug 04 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.6-1mdv2009.0
+ Revision: 263528
- new version

* Thu Jul 03 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.4.2-1mdv2009.0
+ Revision: 231017
- new version
- drop icons
- update license
- patch1 to make it build

* Mon Jun 30 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.3-1mdv2009.0
+ Revision: 230130
- new version
- update buildrequires

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Thierry Vignaud <tv@mandriva.org>
    - put a real description

* Tue May 27 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.2-1mdv2009.0
+ Revision: 211619
- new version

* Wed Apr 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.1-1mdv2009.0
+ Revision: 192458
- new version
- drop patch 3

* Thu Mar 27 2008 Frederic Crozat <fcrozat@mandriva.com> 2.22.0-2mdv2008.1
+ Revision: 190743
- Patch3: various fixes from SVN

* Mon Mar 10 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 183883
- new version

* Tue Feb 26 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.92-1mdv2008.1
+ Revision: 175493
- new version

* Tue Feb 12 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.91.1-1mdv2008.1
+ Revision: 165905
- new version

* Tue Feb 12 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.91-1mdv2008.1
+ Revision: 165739
- new version
- drop patch 3

* Wed Jan 30 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.90-1mdv2008.1
+ Revision: 160222
- new version

* Thu Jan 17 2008 Thierry Vignaud <tv@mandriva.org> 2.21.5-2mdv2008.1
+ Revision: 154152
- do not package big changelog

* Tue Jan 15 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.5-1mdv2008.1
+ Revision: 152138
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Dec 21 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.4-1mdv2008.1
+ Revision: 136208
- new version
- bump deps

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Funda Wang <fwang@mandriva.org>
    - drop old menu

* Tue Dec 04 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.3-1mdv2008.1
+ Revision: 115273
- new version

* Tue Nov 27 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.3-1mdv2008.1
+ Revision: 113350
- new version

* Tue Sep 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.2-1mdv2008.0
+ Revision: 89469
- new version
- fix icon in desktop entry

* Mon Jul 02 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.1-2mdv2008.0
+ Revision: 47190
- drop patch 1, it was causing bug #25500

* Tue Jun 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.1-1mdv2008.0
+ Revision: 41257
- new version


* Tue Sep 26 2006 Frederic Crozat <fcrozat@mandriva.com> 2.16.0-2mdv2007.0
- Rebuild with latest ncurses

* Tue Sep 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.0-1mdv2007.0
- New release 2.16.0

* Tue Aug 01 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.4-1mdv2007.0
- New release 2.15.4

* Tue Jul 25 2006 Götz Waschk <waschk@mandriva.org> 2.15.3-1mdv2007.0
- bump deps
- New release 2.15.3

* Tue Jul 11 2006 Götz Waschk <waschk@mandriva.org> 2.15.2-1mdv2007.0
- bump deps
- New release 2.15.2

* Sun Jun 25 2006 Götz Waschk <waschk@mandriva.org> 2.15.1-4mdv2007.0
- fix buildrequires

* Sun Jun 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.15.1-3mdv2007.0
- rebuild with proper deps on x86_64

* Wed Jun 21 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.1-2mdv2007.0
- Use new macros
- Switch to xdg menu

* Fri Jun 02 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.1-1mdv2007.0
- Release 2.15.1

* Mon May 29 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.2-1mdk
- New release 2.14.2

* Mon Apr 17 2006 Götz Waschk <waschk@mandriva.org> 2.14.1-2mdk
- readd patch 1

* Thu Apr 13 2006 Frederic Crozat <fcrozat@mandriva.com> 2.14.1-1mdk
- Release 2.14.1
- Remove patches 1 (fixed upstream), 4 (merged upstream)

* Fri Feb 24 2006 Frederic Crozat <fcrozat@mandriva.com> 2.12.0-3mdk
- Use mkrel
- fix prereq

* Sun Nov 20 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.0-2mdk
- rebuild for new openssl

* Wed Oct 05 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.0-1mdk
- Release 2.12.0
- Remove patches 3, 5 (merged upstream)

* Tue Apr 19 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.0-1mdk 
- Release 2.10.0 (based on Götz Waschk package)
- Patch5 (CVS): fix po files
- Regenerate patch 2 to patch .schemas.in

* Fri Apr 01 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.2-5mdk 
- Patch4: fix i18n init for windows name

* Mon Mar 14 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.2-4mdk 
- Patch3 (hadess): fix DND from konqueror

* Wed Mar 09 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.2-3mdk 
- No longer install xvt alternative

* Wed Jan 05 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.2-2mdk 
- Rebuild with latest howl

* Wed Dec 08 2004 Götz Waschk <waschk@linux-mandrake.com> 2.8.2-1mdk
- fix gconf schema deinstallation
- fix omf file listing
- fix installation
- New release 2.8.2

* Mon Nov 29 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.0-2mdk
- Patch2: change default colors (grey on black)

* Tue Oct 19 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.0-1mdk
- New release 2.8.0
- Remove patch2 (merged upstream)

* Wed Sep 15 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.1-4mdk
- Update patch0 to handle -e like other term emulator when called through xvt

* Mon Jun 28 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.1-3mdk
- fix next-tab misbehaviour
- reallow libtoolize

* Wed Apr 21 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.1-2mdk
- Fix BuildRequires

* Sun Apr 18 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.1-1mdk
- new version

* Tue Apr 06 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.0-1mdk
- Release 2.6.0 (with Götz help)
- Regenerate patch0
- Remove patch1 (merged upstream)

* Wed Feb 18 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.4.2-2mdk
- Patch1 (CVS): workaround icewm bug to prevent crash

* Sun Nov 09 2003 Götz Waschk <waschk@linux-mandrake.com> 2.4.2-1mdk
- new version

* Wed Nov 05 2003 Götz Waschk <waschk@linux-mandrake.com> 2.4.1-1mdk
- drop patch 2 (obsolete)
- drop merged patch 1
- new version

