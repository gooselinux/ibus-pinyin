Name:       ibus-pinyin
Version:    1.3.8
Release:    1%{?dist}
Summary:    The Chinese Pinyin and Bopomofo engines for IBus input platform
License:    GPLv2+
Group:      System Environment/Libraries
URL:        http://code.google.com/p/ibus
Source0:    http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:    http://ibus.googlecode.com/files/pinyin-database-1.2.99.tar.bz2
Patch0:     ibus-pinyin-HEAD.patch

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel
BuildRequires:  libuuid-devel
BuildRequires:  boost-devel >= 1.39
BuildRequires:  ibus-devel >= 1.2.0

# Requires(post): sqlite

Requires:   ibus >= 1.2.0

%description
The Chinese Pinyin and Bopomofo input methods for IBus platform.

%package    open-phrase
Summary:    The open phrase database for ibus Pinyin and Bopomofo
Group:      System Environment/Libraries
Requires(post): sqlite

%description open-phrase
The open phrase database for ibus Pinyin and Bopomofo engines.

%prep
%setup -q
%patch0 -p1
cp %{SOURCE1} data/db/open-phrase

%build
%configure --disable-static --enable-db-open-phrase
# make -C po update-gmo
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
# cd %{_datadir}/ibus-pinyin/db
# sqlite3 android.db ".read create_index.sql"

%post open-phrase
# cd %{_datadir}/ibus-pinyin/db
# sqlite3 open-phrase.db ".read create_index.sql"

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libexecdir}/ibus-engine-pinyin
%{_libexecdir}/ibus-setup-pinyin
%{_datadir}/ibus-pinyin/phrases.txt
%{_datadir}/ibus-pinyin/icons
%{_datadir}/ibus-pinyin/setup
%{_datadir}/ibus-pinyin/db/create_index.sql
%{_datadir}/ibus-pinyin/db/android.db
%dir %{_datadir}/ibus-pinyin
%dir %{_datadir}/ibus-pinyin/db
%{_datadir}/ibus/component/*

%files open-phrase
%{_datadir}/ibus-pinyin/db/open-phrase.db

%changelog
* Mon Jun 01 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.3.8-1
- Update to 1.3.8
- Resolves: rhbz#593591

* Mon May 03 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.3.5-1
- Update to 1.3.5
- Add MS double pinyin back.
- Fix a problem in double pinyin parser.

* Sun May 02 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.3.4-1
- Update to 1.3.4

* Thu Apr 15 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.3.3-1
- Update to 1.3.3

* Sun Apr 11 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.3.2-1
- Update to 1.3.2

* Mon Apr 05 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.3.1-1
- Update to 1.3.1

* Fri Mar 26 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.3.0-1
- Update to 1.3.0
- Fix some double pinyin problems.

* Thu Mar 18 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.2.99.20100318-1
- Update to 1.2.99.20100318
- Fix some double pinyin problems.

* Mon Mar 15 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.2.99.20100315-1
- Update to 1.2.99.20100315

* Mon Mar 08 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.2.99.20100308-1
- Update to 1.2.99.20100308

* Fri Feb 19 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.2.99.20100212-1
- Update to 1.2.99.20100212

* Thu Feb 11 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.2.99.20100211-1
- Update to 1.2.99.20100211
- Add BuildRequires libsigc++20-devel

* Tue Feb 02 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.2.99.20100202-1
- Update to 1.2.99.20100202

* Fri Dec 11 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.99.20091211-1
- Update to 1.2.99.20091211

* Thu Dec 10 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20090915-2
- Correct pinyin database download location.

* Tue Sep 15 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20090915-1
- Update to 1.2.0.20090915.
- Fix bug 508006 - The color of English Candidates doesn't work

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20090617-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 17 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20090617-1
- Update to 1.2.0.20090617.

* Fri Jun 12 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090612-1
- Update to 1.1.0.20090612.

* Mon May 25 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090303-2
- Update to HEAD version in upstream git repository
- Fix bug 500762 - The iBus input speed becomes much slower after "Fuzzy PinYin" enabled
- Fix bug 501218 - make the pinyin setup window come to the front
- Fix bug 500763 - User DB is unavailable in ibus for liveCD

* Tue Mar 3 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090303-1
- Update to 1.1.0.20090303.

* Wed Feb 25 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090225-1
- Update to 1.1.0.20090225.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0.20090211-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090211-1
- Update version to 1.1.0.20090211.

* Thu Feb 05 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090205-1
- Update version to 1.1.0.20090205.

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1.1.20081004-2
- Rebuild for Python 2.6

* Sat Oct 04 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20081004-1
- Update version to 0.1.1.20081004.

* Thu Sep 18 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080918-1
- Update version to 0.1.1.20080918.

* Mon Sep 01 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080901-1
- Update version to 0.1.1.20080901.

* Sat Aug 23 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080823-1
- The first version.
