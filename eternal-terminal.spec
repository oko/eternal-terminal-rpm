Name: eternal-terminal
Version: 4.2.0
Release: 1%{?dist}
Summary: Eternal Terminal is a remote shell that automatically reconnects without interrupting the session.

License: Apache 2.0
URL: https://github.com/MisterTea/EternalTCP
Source0: https://github.com/MisterTea/EternalTCP/archive/et-v%{version}.tar.gz

BuildRequires: boost-devel
BuildRequires: libsodium-devel
BuildRequires: ncurses-devel
BuildRequires: protobuf-devel
BuildRequires: protobuf-compiler
BuildRequires: cmake
BuildRequires: glog-devel
BuildRequires: gflags-devel
BuildRequires: wget
BuildRequires: unzip
Requires: boost
Requires: libsodium
Requires: ncurses
Requires: glog
Requires: gflags
Requires: protobuf

%description


%prep
%setup -q -n EternalTCP-et-v%{version}


%build
mkdir build
pushd build
cmake ../ -DCMAKE_C_FLAGS="%{optflags}" -DCMAKE_CXX_FLAGS="%{optflags}"
make %{?_smp_mflags}
popd


%install
pushd build
%make_install
popd


%files
/usr/local/bin/et
/usr/local/bin/etserver
%doc



%changelog

