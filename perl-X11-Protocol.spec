#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-X11-Protocol
Version  : 0.56
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/S/SM/SMCCAM/X11-Protocol-0.56.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SM/SMCCAM/X11-Protocol-0.56.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libx/libx11-protocol-perl/libx11-protocol-perl_0.56-7.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 MIT X11
Requires: perl-X11-Protocol-license = %{version}-%{release}
Requires: perl-X11-Protocol-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
X11::Protocol, version 0.56
module is free software; you can redistribute and/or modify it under
the same terms as Perl itself. (As an exception, the file Keysyms.pm,
which is derived from a file in the standard X11 distribution, has
another, less restrictive copying policy, as do some of the extension
modules in the directory Protocol/Ext: see those files for details).

%package dev
Summary: dev components for the perl-X11-Protocol package.
Group: Development
Provides: perl-X11-Protocol-devel = %{version}-%{release}
Requires: perl-X11-Protocol = %{version}-%{release}

%description dev
dev components for the perl-X11-Protocol package.


%package license
Summary: license components for the perl-X11-Protocol package.
Group: Default

%description license
license components for the perl-X11-Protocol package.


%package perl
Summary: perl components for the perl-X11-Protocol package.
Group: Default
Requires: perl-X11-Protocol = %{version}-%{release}

%description perl
perl components for the perl-X11-Protocol package.


%prep
%setup -q -n X11-Protocol-0.56
cd %{_builddir}
tar xf %{_sourcedir}/libx11-protocol-perl_0.56-7.debian.tar.xz
cd %{_builddir}/X11-Protocol-0.56
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/X11-Protocol-0.56/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-X11-Protocol
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-X11-Protocol/ea8979370f00ba610d869f0c987a24b5687fe658 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/X11::Auth.3
/usr/share/man/man3/X11::Keysyms.3
/usr/share/man/man3/X11::Protocol.3
/usr/share/man/man3/X11::Protocol::Connection.3
/usr/share/man/man3/X11::Protocol::Connection::FileHandle.3
/usr/share/man/man3/X11::Protocol::Connection::INETFH.3
/usr/share/man/man3/X11::Protocol::Connection::INETSocket.3
/usr/share/man/man3/X11::Protocol::Connection::Socket.3
/usr/share/man/man3/X11::Protocol::Connection::UNIXFH.3
/usr/share/man/man3/X11::Protocol::Connection::UNIXSocket.3
/usr/share/man/man3/X11::Protocol::Ext::BIG_REQUESTS.3
/usr/share/man/man3/X11::Protocol::Ext::DPMS.3
/usr/share/man/man3/X11::Protocol::Ext::RENDER.3
/usr/share/man/man3/X11::Protocol::Ext::SHAPE.3
/usr/share/man/man3/X11::Protocol::Ext::XC_MISC.3
/usr/share/man/man3/X11::Protocol::Ext::XFree86_Misc.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-X11-Protocol/ea8979370f00ba610d869f0c987a24b5687fe658

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
