#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-X11-Protocol
Version  : 0.56
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/S/SM/SMCCAM/X11-Protocol-0.56.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SM/SMCCAM/X11-Protocol-0.56.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libx/libx11-protocol-perl/libx11-protocol-perl_0.56-7.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 MIT X11
Requires: perl-X11-Protocol-license = %{version}-%{release}
BuildRequires : buildreq-cpan

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

%description dev
dev components for the perl-X11-Protocol package.


%package license
Summary: license components for the perl-X11-Protocol package.
Group: Default

%description license
license components for the perl-X11-Protocol package.


%prep
%setup -q -n X11-Protocol-0.56
cd ..
%setup -q -T -D -n X11-Protocol-0.56 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/X11-Protocol-0.56/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-X11-Protocol
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-X11-Protocol/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.2/X11/Auth.pm
/usr/lib/perl5/vendor_perl/5.28.2/X11/Keysyms.pm
/usr/lib/perl5/vendor_perl/5.28.2/X11/Protocol.pm
/usr/lib/perl5/vendor_perl/5.28.2/X11/Protocol/Connection.pm
/usr/lib/perl5/vendor_perl/5.28.2/X11/Protocol/Connection/FileHandle.pm
/usr/lib/perl5/vendor_perl/5.28.2/X11/Protocol/Connection/INETFH.pm
/usr/lib/perl5/vendor_perl/5.28.2/X11/Protocol/Connection/INETSocket.pm
/usr/lib/perl5/vendor_perl/5.28.2/X11/Protocol/Connection/Socket.pm
/usr/lib/perl5/vendor_perl/5.28.2/X11/Protocol/Connection/UNIXFH.pm
/usr/lib/perl5/vendor_perl/5.28.2/X11/Protocol/Connection/UNIXSocket.pm
/usr/lib/perl5/vendor_perl/5.28.2/X11/Protocol/Constants.pm
/usr/lib/perl5/vendor_perl/5.28.2/X11/Protocol/Ext/BIG_REQUESTS.pm
/usr/lib/perl5/vendor_perl/5.28.2/X11/Protocol/Ext/DPMS.pm
/usr/lib/perl5/vendor_perl/5.28.2/X11/Protocol/Ext/RENDER.pm
/usr/lib/perl5/vendor_perl/5.28.2/X11/Protocol/Ext/SHAPE.pm
/usr/lib/perl5/vendor_perl/5.28.2/X11/Protocol/Ext/XC_MISC.pm
/usr/lib/perl5/vendor_perl/5.28.2/X11/Protocol/Ext/XFree86_Misc.pm

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
/usr/share/package-licenses/perl-X11-Protocol/deblicense_copyright
