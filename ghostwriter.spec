Name:           ghostwriter
Version:        1.7.3
Release:        1%{dist}
Summary:        Cross-platform, aesthetic, distraction-free Markdown editor

License:        GPLv3+
URL:            https://wereturtle.github.io/ghostwriter/
Source0:        https://github.com/wereturtle/ghostwriter/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  qt5-linguist
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

Requires:       hicolor-icon-theme

%description
ghostwriter is a Windows and Linux text editor for Markdown, which is a plain
text markup format created by John Gruber. For more information about Markdown,
please visit John Gruber’s website at http://www.daringfireball.net.
ghostwriter provides a relaxing, distraction-free writing environment, whether
your masterpiece be that next blog post, your school paper, or your NaNoWriMo
novel. For a tour of its features, please visit the ghostwriter project page.

%prep
%autosetup


%build
lrelease-qt5 %{name}.pro
%qmake_qt5 PREFIX=%{_prefix}
%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license COPYING
%doc README.md CREDITS.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.{png,svg}
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man1/%{name}.1.gz


%changelog
* Mon Oct 29 2018 Vasiliy N. Glazov <vascom2@gmail.com> 1.7.3-1
- Update to 1.7.3

* Sat Apr 28 2018 opensuse-packaging@opensuse.org
- Update to version 1.6.2.0.git20180415:
  * Bump up version number. Update translations.
  * Fix line break tokenizing to not include paragraph breaks.
  * Fixes #315. Work around slow load of QPrinter constructor in Fedora 27 by lazy loading the class for default printer settings only when needed for printing rather than during app startup.
  * Bump up version number.
  * Work around Qt 5.10 bug where application will crash on loading another document if the text cursor is not first set to the beginning of the document.
  * Update timestamp in appdata
  * Fixes #302.  Look for default translations for Qt elements to use in ghostwriter's translations path if they are not found on the standard Qt path
  * Update credits with Chinese translation author
  * Add qtbase_* to translations
  * fix broken french translation file
