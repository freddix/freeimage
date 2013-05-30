%define		uver	%(echo %{version} | tr -d .)

Summary:	Library for handling different graphics files formats
Name:		freeimage
Version:	3.15.4
Release:	1
License:	GPL and FIPL (see the license-fi.txt)
Group:		Libraries
Source0:	http://downloads.sourceforge.net/freeimage/FreeImage%{uver}.zip
# Source0-md5:	9f9a3b2c3c1b4fd24fe479e8aaee86b1
URL:		http://freeimage.sourceforge.net/index.html
BuildRequires:	libstdc++-devel
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FreeImage is a library project for developers who would like to
support popular graphics image formats like PNG, BMP, JPEG, TIFF and
others as needed by multimedia applications. FreeImage is easy to use,
fast, multithreading, safe.

%package devel
Summary:	Header files for FreeImage library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for FreeImage library.

%prep
%setup -qn FreeImage

sed -i "s|-O3|%{rpmcflags}|g" Makefile.gnu

%build
%{__make} \
	CC="%{__cc}"	\
	CXX="%{__cxx}"	\
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

install Dist/libfreeimage* $RPM_BUILD_ROOT%{_libdir}
install Dist/*.h $RPM_BUILD_ROOT%{_includedir}

ln -sf libfreeimage-%{version}.so \
	$RPM_BUILD_ROOT%{_libdir}/libfreeimage.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.linux Whatsnew.txt license-fi.txt
%attr(755,root,root) %{_libdir}/libfreeimage-*.*.*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfreeimage.so
%{_includedir}/FreeImage.h

