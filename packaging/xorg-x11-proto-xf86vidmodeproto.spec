
Name:       xorg-x11-proto-xf86vidmodeproto
Summary:    X.Org X11 Protocol xf86vidmodeproto
Version:    2.3
Release:    3.8
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/xf86vidmodeproto-%{version}.tar.gz
Source1001: packaging/xorg-x11-proto-xf86vidmodeproto.manifest 
Provides:   xf86vidmodeproto
BuildRequires: pkgconfig(xorg-macros)


%description
Description: %{summary}



%prep
%setup -q -n %{name}-%{version}

%build
cp %{SOURCE1001} .
%reconfigure --disable-static \
    --libdir=%{_datadir}

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}






%files
%manifest xorg-x11-proto-xf86vidmodeproto.manifest
%defattr(-,root,root,-)
%{_datadir}/pkgconfig/xf86vidmodeproto.pc
%{_includedir}/X11/extensions/xf86vmstr.h
%{_includedir}/X11/extensions/xf86vm.h
%{_includedir}/X11/extensions/xf86vmproto.h


