Summary:	GGZ Gaming Zone - KDE frontends and clients
Summary(pl.UTF-8):	GGZ Gaming Zone - interfejsy i klienci KDE
Name:		ggz-kde-games
Version:	0.0.14.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://mirrors.dotsrc.org/ggzgamingzone/ggz/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b70e6934e7a1bbbcacd5d33c4d81ccc3
URL:		http://www.ggzgamingzone.org/
BuildRequires:	gettext-devel
BuildRequires:	ggz-client-libs-devel >= 0.0.14
BuildRequires:	kdelibs-devel >= 3
BuildRequires:	libggz-devel >= 0.0.14
BuildRequires:	librsvg-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	qt-devel >= 3
Requires(post,preun):	ggz-client-libs >= 0.0.14
Requires:	ggz-client-libs >= 0.0.14
Requires:	kdelibs >= 3
Requires:	libggz >= 0.0.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GGZ Gaming Zone - KDE frontends and clients.

%description -l pl.UTF-8
GGZ Gaming Zone - interfejsy i klienci KDE.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# collect modules.ggz pieces
install -d $RPM_BUILD_ROOT%{_datadir}/ggz/ggz-config
for d in KReversi fyrdman kcc kconnectx kdots keepalive koenig krosswater ktictactux muehle ; do
	cp -p ${d}/module.dsc $RPM_BUILD_ROOT%{_datadir}/ggz/ggz-config/${d}.dsc
done
%{__rm} $RPM_BUILD_ROOT%{_sysconfdir}/ggz.modules

# po: KReversi fyrdman kdots koenig krosswater ktictactux muehle
# khtml: muehle
%find_lang %{name} --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
for d in KReversi fyrdman kcc kconnectx kdots keepalive koenig krosswater ktictactux muehle ; do
	%{_bindir}/ggz-config --install --modfile=%{_datadir}/ggz/ggz-config/${d}.dsc --force
done

%preun
if [ "$1" = "0" ]; then
	for d in KReversi fyrdman kcc kconnectx kdots keepalive koenig krosswater ktictactux muehle ; do
		%{_bindir}/ggz-config --remove --modfile=%{_datadir}/ggz/ggz-config/${d}.dsc
	done
fi


%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS QuickStart.GGZ README* TODO muehle/muehle.txt
%attr(755,root,root) %{_libdir}/ggz/fyrdman
%attr(755,root,root) %{_libdir}/ggz/ggz.kreversi
%attr(755,root,root) %{_libdir}/ggz/kcc
%attr(755,root,root) %{_libdir}/ggz/kconnectx
%attr(755,root,root) %{_libdir}/ggz/kdots_client
%attr(755,root,root) %{_libdir}/ggz/keepalive
%attr(755,root,root) %{_libdir}/ggz/koenig
%attr(755,root,root) %{_libdir}/ggz/krosswater_client
%attr(755,root,root) %{_libdir}/ggz/ktictactux_client
%attr(755,root,root) %{_libdir}/ggz/muehle
%{_datadir}/apps/ggz.kreversi
%{_datadir}/apps/kconnectx
%{_datadir}/apps/koenig
%{_datadir}/apps/ktictactux
%{_datadir}/config/fyrdmanrc
%{_datadir}/config/kccrc
%{_datadir}/config/koenigrc
%{_datadir}/config/ktictactuxrc
%{_datadir}/config/muehlerc
%{_datadir}/ggz/ggz-config/KReversi.dsc
%{_datadir}/ggz/ggz-config/fyrdman.dsc
%{_datadir}/ggz/ggz-config/kcc.dsc
%{_datadir}/ggz/ggz-config/kconnectx.dsc
%{_datadir}/ggz/ggz-config/kdots.dsc
%{_datadir}/ggz/ggz-config/keepalive.dsc
%{_datadir}/ggz/ggz-config/koenig.dsc
%{_datadir}/ggz/ggz-config/krosswater.dsc
%{_datadir}/ggz/ggz-config/ktictactux.dsc
%{_datadir}/ggz/ggz-config/muehle.dsc
%{_datadir}/ggz/fyrdman
%{_datadir}/ggz/kcc
%{_datadir}/ggz/kdots
%{_datadir}/ggz/keepalive
%{_datadir}/ggz/kreversi
%{_datadir}/ggz/krosswater
%{_datadir}/ggz/ktictactux
%{_datadir}/ggz/muehle
%{_desktopdir}/fyrdman.desktop
%{_desktopdir}/kcc.desktop
%{_desktopdir}/keepalive.desktop
%{_desktopdir}/ktictactux.desktop
%{_desktopdir}/muehle.desktop
%{_mandir}/man6/muehle-ai.pl.6*
