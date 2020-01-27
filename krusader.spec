#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : krusader
Version  : 2.7.2
Release  : 1
URL      : https://download.kde.org/stable/krusader/2.7.2/krusader-2.7.2.tar.xz
Source0  : https://download.kde.org/stable/krusader/2.7.2/krusader-2.7.2.tar.xz
Summary  : Advanced twin panel (commander style) file manager
Group    : Development/Tools
License  : GFDL-1.1 GPL-2.0
Requires: krusader-bin = %{version}-%{release}
Requires: krusader-data = %{version}-%{release}
Requires: krusader-lib = %{version}-%{release}
Requires: krusader-license = %{version}-%{release}
Requires: krusader-locales = %{version}-%{release}
Requires: krusader-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde

%description
This is the 0.2 release of libisofs. For changes, see the ChangeLog.
Libisofs implements the reading of the famous ISO-9660 (ECMA-119) file system,
found on CD-ROM media. It also supports the Rock Ridge Interchange Protocol and
Microsoft Joliet extensions. It allows user-mode programs to query the
filesystem volume descriptors and traverse through the directory structure.
Preliminary support for El-Torito boot CDs are added in version 0.2.

%package bin
Summary: bin components for the krusader package.
Group: Binaries
Requires: krusader-data = %{version}-%{release}
Requires: krusader-license = %{version}-%{release}

%description bin
bin components for the krusader package.


%package data
Summary: data components for the krusader package.
Group: Data

%description data
data components for the krusader package.


%package doc
Summary: doc components for the krusader package.
Group: Documentation
Requires: krusader-man = %{version}-%{release}

%description doc
doc components for the krusader package.


%package lib
Summary: lib components for the krusader package.
Group: Libraries
Requires: krusader-data = %{version}-%{release}
Requires: krusader-license = %{version}-%{release}

%description lib
lib components for the krusader package.


%package license
Summary: license components for the krusader package.
Group: Default

%description license
license components for the krusader package.


%package locales
Summary: locales components for the krusader package.
Group: Default

%description locales
locales components for the krusader package.


%package man
Summary: man components for the krusader package.
Group: Default

%description man
man components for the krusader package.


%prep
%setup -q -n krusader-2.7.2
cd %{_builddir}/krusader-2.7.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1580136585
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1580136585
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/krusader
cp %{_builddir}/krusader-2.7.2/COPYING %{buildroot}/usr/share/package-licenses/krusader/88b77b0ab41e8ccea0e250320bacb1312c51328c
cp %{_builddir}/krusader-2.7.2/doc-extras/fdl-license %{buildroot}/usr/share/package-licenses/krusader/8a12932679231476029f5ecc43fedb84b3bfc325
cp %{_builddir}/krusader-2.7.2/iso/libisofs/COPYING %{buildroot}/usr/share/package-licenses/krusader/2d29c273fda30310211bbf6a24127d589be09b6c
pushd clr-build
%make_install
popd
%find_lang krusader

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/krusader

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.krusader.desktop
/usr/share/icons/hicolor/128x128/apps/krusader_root.png
/usr/share/icons/hicolor/128x128/apps/krusader_user.png
/usr/share/icons/hicolor/16x16/apps/krusader_blue.png
/usr/share/icons/hicolor/16x16/apps/krusader_red.png
/usr/share/icons/hicolor/16x16/apps/krusader_root.png
/usr/share/icons/hicolor/16x16/apps/krusader_user.png
/usr/share/icons/hicolor/22x22/apps/krusader_blue.png
/usr/share/icons/hicolor/22x22/apps/krusader_red.png
/usr/share/icons/hicolor/22x22/apps/krusader_root.png
/usr/share/icons/hicolor/22x22/apps/krusader_shield.png
/usr/share/icons/hicolor/22x22/apps/krusader_user.png
/usr/share/icons/hicolor/32x32/apps/krusader_blue.png
/usr/share/icons/hicolor/32x32/apps/krusader_red.png
/usr/share/icons/hicolor/32x32/apps/krusader_root.png
/usr/share/icons/hicolor/32x32/apps/krusader_shield.png
/usr/share/icons/hicolor/32x32/apps/krusader_user.png
/usr/share/icons/hicolor/48x48/apps/krusader_blue.png
/usr/share/icons/hicolor/48x48/apps/krusader_red.png
/usr/share/icons/hicolor/48x48/apps/krusader_root.png
/usr/share/icons/hicolor/48x48/apps/krusader_shield.png
/usr/share/icons/hicolor/48x48/apps/krusader_user.png
/usr/share/icons/hicolor/64x64/apps/krusader_blue.png
/usr/share/icons/hicolor/64x64/apps/krusader_red.png
/usr/share/icons/hicolor/64x64/apps/krusader_root.png
/usr/share/icons/hicolor/64x64/apps/krusader_shield.png
/usr/share/icons/hicolor/64x64/apps/krusader_user.png
/usr/share/krusader/icons/hicolor/16x16/actions/kr_combine.png
/usr/share/krusader/icons/hicolor/16x16/actions/kr_comparedirs.png
/usr/share/krusader/icons/hicolor/16x16/actions/kr_diskusage.png
/usr/share/krusader/icons/hicolor/16x16/actions/kr_mountman.png
/usr/share/krusader/icons/hicolor/16x16/actions/kr_syncbrowse_off.png
/usr/share/krusader/icons/hicolor/16x16/actions/kr_syncbrowse_on.png
/usr/share/krusader/icons/hicolor/16x16/actions/kr_unselect.png
/usr/share/krusader/icons/hicolor/22x22/actions/kr_combine.png
/usr/share/krusader/icons/hicolor/22x22/actions/kr_comparedirs.png
/usr/share/krusader/icons/hicolor/22x22/actions/kr_diskusage.png
/usr/share/krusader/icons/hicolor/22x22/actions/kr_mountman.png
/usr/share/krusader/icons/hicolor/22x22/actions/kr_unselect.png
/usr/share/krusader/icons/hicolor/32x32/actions/kr_combine.png
/usr/share/krusader/icons/hicolor/32x32/actions/kr_comparedirs.png
/usr/share/krusader/icons/hicolor/32x32/actions/kr_diskusage.png
/usr/share/krusader/icons/hicolor/32x32/actions/kr_mountman.png
/usr/share/krusader/icons/hicolor/32x32/actions/kr_unselect.png
/usr/share/krusader/layout.xml
/usr/share/krusader/midnight_commander.color
/usr/share/krusader/splash.png
/usr/share/krusader/total_commander.color
/usr/share/krusader/total_commander.keymap
/usr/share/krusader/total_commander.keymap.info
/usr/share/krusader/useraction_examples.xml
/usr/share/kservices5/iso.protocol
/usr/share/kservices5/krarc.protocol
/usr/share/kxmlgui5/krusader/krusaderlisterui.rc
/usr/share/kxmlgui5/krusader/krusaderui.rc
/usr/share/kxmlgui5/krusader/krviewer.rc
/usr/share/metainfo/org.kde.krusader.appdata.xml
/usr/share/xdg/kio_isorc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/de/krusader/advanced-functions.docbook
/usr/share/doc/HTML/de/krusader/archives.docbook
/usr/share/doc/HTML/de/krusader/basic-functions.docbook
/usr/share/doc/HTML/de/krusader/bookmarks.docbook
/usr/share/doc/HTML/de/krusader/checksum.docbook
/usr/share/doc/HTML/de/krusader/compare.docbook
/usr/share/doc/HTML/de/krusader/configuration-files.docbook
/usr/share/doc/HTML/de/krusader/credits-and-license.docbook
/usr/share/doc/HTML/de/krusader/diskusage.docbook
/usr/share/doc/HTML/de/krusader/editors-note.docbook
/usr/share/doc/HTML/de/krusader/faq.docbook
/usr/share/doc/HTML/de/krusader/features.docbook
/usr/share/doc/HTML/de/krusader/glossary.docbook
/usr/share/doc/HTML/de/krusader/help.docbook
/usr/share/doc/HTML/de/krusader/index.cache.bz2
/usr/share/doc/HTML/de/krusader/index.docbook
/usr/share/doc/HTML/de/krusader/installation.docbook
/usr/share/doc/HTML/de/krusader/introduction.docbook
/usr/share/doc/HTML/de/krusader/keyboard-commands.docbook
/usr/share/doc/HTML/de/krusader/konfigurator.docbook
/usr/share/doc/HTML/de/krusader/krusader-tools.docbook
/usr/share/doc/HTML/de/krusader/locate.docbook
/usr/share/doc/HTML/de/krusader/menu-commands.docbook
/usr/share/doc/HTML/de/krusader/mount.docbook
/usr/share/doc/HTML/de/krusader/mouse-commands.docbook
/usr/share/doc/HTML/de/krusader/occupied-space.docbook
/usr/share/doc/HTML/de/krusader/profiles.docbook
/usr/share/doc/HTML/de/krusader/release-overview.docbook
/usr/share/doc/HTML/de/krusader/remote-connections.docbook
/usr/share/doc/HTML/de/krusader/search.docbook
/usr/share/doc/HTML/de/krusader/splitter.docbook
/usr/share/doc/HTML/de/krusader/synchronizer.docbook
/usr/share/doc/HTML/de/krusader/user-interface.docbook
/usr/share/doc/HTML/de/krusader/useraction-xml.docbook
/usr/share/doc/HTML/de/krusader/useractions.docbook
/usr/share/doc/HTML/de/krusader/vfs.docbook
/usr/share/doc/HTML/de/krusader/viewer-editor.docbook
/usr/share/doc/HTML/en/krusader/Icon-edit-delete.png
/usr/share/doc/HTML/en/krusader/actionman.png
/usr/share/doc/HTML/en/krusader/advanced-functions.docbook
/usr/share/doc/HTML/en/krusader/archives.docbook
/usr/share/doc/HTML/en/krusader/basic-functions.docbook
/usr/share/doc/HTML/en/krusader/bookmanadd.png
/usr/share/doc/HTML/en/krusader/bookmanedit.png
/usr/share/doc/HTML/en/krusader/bookmarks.docbook
/usr/share/doc/HTML/en/krusader/checksum.docbook
/usr/share/doc/HTML/en/krusader/cmdline.png
/usr/share/doc/HTML/en/krusader/compare.docbook
/usr/share/doc/HTML/en/krusader/configuration-files.docbook
/usr/share/doc/HTML/en/krusader/copyjob.png
/usr/share/doc/HTML/en/krusader/credits-and-license.docbook
/usr/share/doc/HTML/en/krusader/diskusage.docbook
/usr/share/doc/HTML/en/krusader/editors-note.docbook
/usr/share/doc/HTML/en/krusader/faq.docbook
/usr/share/doc/HTML/en/krusader/features.docbook
/usr/share/doc/HTML/en/krusader/fnkeys.png
/usr/share/doc/HTML/en/krusader/glossary.docbook
/usr/share/doc/HTML/en/krusader/help.docbook
/usr/share/doc/HTML/en/krusader/index.cache.bz2
/usr/share/doc/HTML/en/krusader/index.docbook
/usr/share/doc/HTML/en/krusader/installation.docbook
/usr/share/doc/HTML/en/krusader/introduction.docbook
/usr/share/doc/HTML/en/krusader/keyboard-commands.docbook
/usr/share/doc/HTML/en/krusader/kgstartup.png
/usr/share/doc/HTML/en/krusader/konfigurator.docbook
/usr/share/doc/HTML/en/krusader/krusader-tools.docbook
/usr/share/doc/HTML/en/krusader/krusader1.png
/usr/share/doc/HTML/en/krusader/listpanel.png
/usr/share/doc/HTML/en/krusader/locate.docbook
/usr/share/doc/HTML/en/krusader/mainwindow.png
/usr/share/doc/HTML/en/krusader/menu-commands.docbook
/usr/share/doc/HTML/en/krusader/mount.docbook
/usr/share/doc/HTML/en/krusader/mountman.png
/usr/share/doc/HTML/en/krusader/mouse-commands.docbook
/usr/share/doc/HTML/en/krusader/occupied-space.docbook
/usr/share/doc/HTML/en/krusader/profiles.docbook
/usr/share/doc/HTML/en/krusader/release-overview.docbook
/usr/share/doc/HTML/en/krusader/remote-connections.docbook
/usr/share/doc/HTML/en/krusader/search.docbook
/usr/share/doc/HTML/en/krusader/search_advanced.png
/usr/share/doc/HTML/en/krusader/search_general.png
/usr/share/doc/HTML/en/krusader/splitter.docbook
/usr/share/doc/HTML/en/krusader/syncdir.png
/usr/share/doc/HTML/en/krusader/synchronizer.docbook
/usr/share/doc/HTML/en/krusader/tabbed_browsing.png
/usr/share/doc/HTML/en/krusader/terminalEmu.png
/usr/share/doc/HTML/en/krusader/toolbar.png
/usr/share/doc/HTML/en/krusader/user-interface.docbook
/usr/share/doc/HTML/en/krusader/useraction-xml.docbook
/usr/share/doc/HTML/en/krusader/useractions.docbook
/usr/share/doc/HTML/en/krusader/vfs.docbook
/usr/share/doc/HTML/en/krusader/viewer-editor.docbook
/usr/share/doc/HTML/it/krusader/advanced-functions.docbook
/usr/share/doc/HTML/it/krusader/archives.docbook
/usr/share/doc/HTML/it/krusader/basic-functions.docbook
/usr/share/doc/HTML/it/krusader/bookmarks.docbook
/usr/share/doc/HTML/it/krusader/checksum.docbook
/usr/share/doc/HTML/it/krusader/compare.docbook
/usr/share/doc/HTML/it/krusader/configuration-files.docbook
/usr/share/doc/HTML/it/krusader/credits-and-license.docbook
/usr/share/doc/HTML/it/krusader/diskusage.docbook
/usr/share/doc/HTML/it/krusader/editors-note.docbook
/usr/share/doc/HTML/it/krusader/faq.docbook
/usr/share/doc/HTML/it/krusader/features.docbook
/usr/share/doc/HTML/it/krusader/glossary.docbook
/usr/share/doc/HTML/it/krusader/help.docbook
/usr/share/doc/HTML/it/krusader/index.cache.bz2
/usr/share/doc/HTML/it/krusader/index.docbook
/usr/share/doc/HTML/it/krusader/installation.docbook
/usr/share/doc/HTML/it/krusader/introduction.docbook
/usr/share/doc/HTML/it/krusader/keyboard-commands.docbook
/usr/share/doc/HTML/it/krusader/konfigurator.docbook
/usr/share/doc/HTML/it/krusader/krusader-tools.docbook
/usr/share/doc/HTML/it/krusader/locate.docbook
/usr/share/doc/HTML/it/krusader/menu-commands.docbook
/usr/share/doc/HTML/it/krusader/mount.docbook
/usr/share/doc/HTML/it/krusader/mouse-commands.docbook
/usr/share/doc/HTML/it/krusader/occupied-space.docbook
/usr/share/doc/HTML/it/krusader/profiles.docbook
/usr/share/doc/HTML/it/krusader/release-overview.docbook
/usr/share/doc/HTML/it/krusader/remote-connections.docbook
/usr/share/doc/HTML/it/krusader/search.docbook
/usr/share/doc/HTML/it/krusader/splitter.docbook
/usr/share/doc/HTML/it/krusader/synchronizer.docbook
/usr/share/doc/HTML/it/krusader/user-interface.docbook
/usr/share/doc/HTML/it/krusader/useraction-xml.docbook
/usr/share/doc/HTML/it/krusader/useractions.docbook
/usr/share/doc/HTML/it/krusader/vfs.docbook
/usr/share/doc/HTML/it/krusader/viewer-editor.docbook
/usr/share/doc/HTML/nl/krusader/advanced-functions.docbook
/usr/share/doc/HTML/nl/krusader/archives.docbook
/usr/share/doc/HTML/nl/krusader/basic-functions.docbook
/usr/share/doc/HTML/nl/krusader/bookmarks.docbook
/usr/share/doc/HTML/nl/krusader/checksum.docbook
/usr/share/doc/HTML/nl/krusader/compare.docbook
/usr/share/doc/HTML/nl/krusader/configuration-files.docbook
/usr/share/doc/HTML/nl/krusader/credits-and-license.docbook
/usr/share/doc/HTML/nl/krusader/diskusage.docbook
/usr/share/doc/HTML/nl/krusader/editors-note.docbook
/usr/share/doc/HTML/nl/krusader/faq.docbook
/usr/share/doc/HTML/nl/krusader/features.docbook
/usr/share/doc/HTML/nl/krusader/glossary.docbook
/usr/share/doc/HTML/nl/krusader/help.docbook
/usr/share/doc/HTML/nl/krusader/index.cache.bz2
/usr/share/doc/HTML/nl/krusader/index.docbook
/usr/share/doc/HTML/nl/krusader/installation.docbook
/usr/share/doc/HTML/nl/krusader/introduction.docbook
/usr/share/doc/HTML/nl/krusader/keyboard-commands.docbook
/usr/share/doc/HTML/nl/krusader/konfigurator.docbook
/usr/share/doc/HTML/nl/krusader/krusader-tools.docbook
/usr/share/doc/HTML/nl/krusader/locate.docbook
/usr/share/doc/HTML/nl/krusader/menu-commands.docbook
/usr/share/doc/HTML/nl/krusader/mount.docbook
/usr/share/doc/HTML/nl/krusader/mouse-commands.docbook
/usr/share/doc/HTML/nl/krusader/occupied-space.docbook
/usr/share/doc/HTML/nl/krusader/profiles.docbook
/usr/share/doc/HTML/nl/krusader/release-overview.docbook
/usr/share/doc/HTML/nl/krusader/remote-connections.docbook
/usr/share/doc/HTML/nl/krusader/search.docbook
/usr/share/doc/HTML/nl/krusader/splitter.docbook
/usr/share/doc/HTML/nl/krusader/synchronizer.docbook
/usr/share/doc/HTML/nl/krusader/user-interface.docbook
/usr/share/doc/HTML/nl/krusader/useraction-xml.docbook
/usr/share/doc/HTML/nl/krusader/useractions.docbook
/usr/share/doc/HTML/nl/krusader/vfs.docbook
/usr/share/doc/HTML/nl/krusader/viewer-editor.docbook
/usr/share/doc/HTML/pt/krusader/advanced-functions.docbook
/usr/share/doc/HTML/pt/krusader/archives.docbook
/usr/share/doc/HTML/pt/krusader/basic-functions.docbook
/usr/share/doc/HTML/pt/krusader/bookmarks.docbook
/usr/share/doc/HTML/pt/krusader/checksum.docbook
/usr/share/doc/HTML/pt/krusader/compare.docbook
/usr/share/doc/HTML/pt/krusader/configuration-files.docbook
/usr/share/doc/HTML/pt/krusader/credits-and-license.docbook
/usr/share/doc/HTML/pt/krusader/diskusage.docbook
/usr/share/doc/HTML/pt/krusader/editors-note.docbook
/usr/share/doc/HTML/pt/krusader/faq.docbook
/usr/share/doc/HTML/pt/krusader/features.docbook
/usr/share/doc/HTML/pt/krusader/glossary.docbook
/usr/share/doc/HTML/pt/krusader/help.docbook
/usr/share/doc/HTML/pt/krusader/index.cache.bz2
/usr/share/doc/HTML/pt/krusader/index.docbook
/usr/share/doc/HTML/pt/krusader/installation.docbook
/usr/share/doc/HTML/pt/krusader/introduction.docbook
/usr/share/doc/HTML/pt/krusader/keyboard-commands.docbook
/usr/share/doc/HTML/pt/krusader/konfigurator.docbook
/usr/share/doc/HTML/pt/krusader/krusader-tools.docbook
/usr/share/doc/HTML/pt/krusader/locate.docbook
/usr/share/doc/HTML/pt/krusader/menu-commands.docbook
/usr/share/doc/HTML/pt/krusader/mount.docbook
/usr/share/doc/HTML/pt/krusader/mouse-commands.docbook
/usr/share/doc/HTML/pt/krusader/occupied-space.docbook
/usr/share/doc/HTML/pt/krusader/profiles.docbook
/usr/share/doc/HTML/pt/krusader/release-overview.docbook
/usr/share/doc/HTML/pt/krusader/remote-connections.docbook
/usr/share/doc/HTML/pt/krusader/search.docbook
/usr/share/doc/HTML/pt/krusader/splitter.docbook
/usr/share/doc/HTML/pt/krusader/synchronizer.docbook
/usr/share/doc/HTML/pt/krusader/user-interface.docbook
/usr/share/doc/HTML/pt/krusader/useraction-xml.docbook
/usr/share/doc/HTML/pt/krusader/useractions.docbook
/usr/share/doc/HTML/pt/krusader/vfs.docbook
/usr/share/doc/HTML/pt/krusader/viewer-editor.docbook
/usr/share/doc/HTML/sv/krusader/advanced-functions.docbook
/usr/share/doc/HTML/sv/krusader/archives.docbook
/usr/share/doc/HTML/sv/krusader/basic-functions.docbook
/usr/share/doc/HTML/sv/krusader/bookmarks.docbook
/usr/share/doc/HTML/sv/krusader/checksum.docbook
/usr/share/doc/HTML/sv/krusader/compare.docbook
/usr/share/doc/HTML/sv/krusader/configuration-files.docbook
/usr/share/doc/HTML/sv/krusader/credits-and-license.docbook
/usr/share/doc/HTML/sv/krusader/diskusage.docbook
/usr/share/doc/HTML/sv/krusader/editors-note.docbook
/usr/share/doc/HTML/sv/krusader/faq.docbook
/usr/share/doc/HTML/sv/krusader/features.docbook
/usr/share/doc/HTML/sv/krusader/glossary.docbook
/usr/share/doc/HTML/sv/krusader/help.docbook
/usr/share/doc/HTML/sv/krusader/index.cache.bz2
/usr/share/doc/HTML/sv/krusader/index.docbook
/usr/share/doc/HTML/sv/krusader/installation.docbook
/usr/share/doc/HTML/sv/krusader/introduction.docbook
/usr/share/doc/HTML/sv/krusader/keyboard-commands.docbook
/usr/share/doc/HTML/sv/krusader/konfigurator.docbook
/usr/share/doc/HTML/sv/krusader/krusader-tools.docbook
/usr/share/doc/HTML/sv/krusader/locate.docbook
/usr/share/doc/HTML/sv/krusader/menu-commands.docbook
/usr/share/doc/HTML/sv/krusader/mount.docbook
/usr/share/doc/HTML/sv/krusader/mouse-commands.docbook
/usr/share/doc/HTML/sv/krusader/occupied-space.docbook
/usr/share/doc/HTML/sv/krusader/profiles.docbook
/usr/share/doc/HTML/sv/krusader/release-overview.docbook
/usr/share/doc/HTML/sv/krusader/remote-connections.docbook
/usr/share/doc/HTML/sv/krusader/search.docbook
/usr/share/doc/HTML/sv/krusader/splitter.docbook
/usr/share/doc/HTML/sv/krusader/synchronizer.docbook
/usr/share/doc/HTML/sv/krusader/user-interface.docbook
/usr/share/doc/HTML/sv/krusader/useraction-xml.docbook
/usr/share/doc/HTML/sv/krusader/useractions.docbook
/usr/share/doc/HTML/sv/krusader/vfs.docbook
/usr/share/doc/HTML/sv/krusader/viewer-editor.docbook
/usr/share/doc/HTML/uk/krusader/actionman.png
/usr/share/doc/HTML/uk/krusader/advanced-functions.docbook
/usr/share/doc/HTML/uk/krusader/archives.docbook
/usr/share/doc/HTML/uk/krusader/basic-functions.docbook
/usr/share/doc/HTML/uk/krusader/bookmanadd.png
/usr/share/doc/HTML/uk/krusader/bookmanedit.png
/usr/share/doc/HTML/uk/krusader/bookmarks.docbook
/usr/share/doc/HTML/uk/krusader/checksum.docbook
/usr/share/doc/HTML/uk/krusader/compare.docbook
/usr/share/doc/HTML/uk/krusader/configuration-files.docbook
/usr/share/doc/HTML/uk/krusader/credits-and-license.docbook
/usr/share/doc/HTML/uk/krusader/diskusage.docbook
/usr/share/doc/HTML/uk/krusader/editors-note.docbook
/usr/share/doc/HTML/uk/krusader/faq.docbook
/usr/share/doc/HTML/uk/krusader/features.docbook
/usr/share/doc/HTML/uk/krusader/fnkeys.png
/usr/share/doc/HTML/uk/krusader/glossary.docbook
/usr/share/doc/HTML/uk/krusader/help.docbook
/usr/share/doc/HTML/uk/krusader/index.cache.bz2
/usr/share/doc/HTML/uk/krusader/index.docbook
/usr/share/doc/HTML/uk/krusader/installation.docbook
/usr/share/doc/HTML/uk/krusader/introduction.docbook
/usr/share/doc/HTML/uk/krusader/keyboard-commands.docbook
/usr/share/doc/HTML/uk/krusader/kgstartup.png
/usr/share/doc/HTML/uk/krusader/konfigurator.docbook
/usr/share/doc/HTML/uk/krusader/krusader-tools.docbook
/usr/share/doc/HTML/uk/krusader/krusader1.png
/usr/share/doc/HTML/uk/krusader/listpanel.png
/usr/share/doc/HTML/uk/krusader/locate.docbook
/usr/share/doc/HTML/uk/krusader/mainwindow.png
/usr/share/doc/HTML/uk/krusader/menu-commands.docbook
/usr/share/doc/HTML/uk/krusader/mount.docbook
/usr/share/doc/HTML/uk/krusader/mountman.png
/usr/share/doc/HTML/uk/krusader/mouse-commands.docbook
/usr/share/doc/HTML/uk/krusader/occupied-space.docbook
/usr/share/doc/HTML/uk/krusader/profiles.docbook
/usr/share/doc/HTML/uk/krusader/release-overview.docbook
/usr/share/doc/HTML/uk/krusader/remote-connections.docbook
/usr/share/doc/HTML/uk/krusader/search.docbook
/usr/share/doc/HTML/uk/krusader/search_advanced.png
/usr/share/doc/HTML/uk/krusader/search_general.png
/usr/share/doc/HTML/uk/krusader/splitter.docbook
/usr/share/doc/HTML/uk/krusader/syncdir.png
/usr/share/doc/HTML/uk/krusader/synchronizer.docbook
/usr/share/doc/HTML/uk/krusader/user-interface.docbook
/usr/share/doc/HTML/uk/krusader/useraction-xml.docbook
/usr/share/doc/HTML/uk/krusader/useractions.docbook
/usr/share/doc/HTML/uk/krusader/vfs.docbook
/usr/share/doc/HTML/uk/krusader/viewer-editor.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kio_iso.so
/usr/lib64/qt5/plugins/kio_krarc.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/krusader/2d29c273fda30310211bbf6a24127d589be09b6c
/usr/share/package-licenses/krusader/88b77b0ab41e8ccea0e250320bacb1312c51328c
/usr/share/package-licenses/krusader/8a12932679231476029f5ecc43fedb84b3bfc325

%files man
%defattr(0644,root,root,0755)
/usr/share/man/de/man1/krusader.1
/usr/share/man/it/man1/krusader.1
/usr/share/man/man1/krusader.1
/usr/share/man/nl/man1/krusader.1
/usr/share/man/pt/man1/krusader.1
/usr/share/man/sv/man1/krusader.1
/usr/share/man/uk/man1/krusader.1

%files locales -f krusader.lang
%defattr(-,root,root,-)

