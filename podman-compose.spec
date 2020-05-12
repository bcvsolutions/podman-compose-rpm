Name:           podman-compose
Version:        0.1.5
Release:        1
Summary:        Package for docker-compose.
Group:          Applications/Tools
License:        GNU 2.0
URL:            https://github.com/containers/podman-compose
Packager:       Ludek Urban
BuildRoot:      "%{_tmppath}/podman-compose-build-root"
Requires:       python3, podman, python3-pyyaml

%description

Package for podman-compose which is for configuring podman images using compose file.

%prep
# we have no source, so nothing here

%build
wget https://github.com/containers/podman-compose/archive/v%{version}.tar.gz -O podman-compose-%{version}.tar.gz
gunzip podman-compose-%{version}.tar.gz
tar -xf podman-compose-%{version}.tar
mv podman-compose-%{version}/podman_compose.py %{name}

%install

mkdir -p %{buildroot}/usr/bin/
install -m 755 %{name} %{buildroot}/usr/bin/%{name}

%files
/usr/bin/%{name}

%clean
#we not use clean

%changelog

* Fri Mar 6 2020 Ludek Urban <ludek.urban@bcvsolutions.eu> 0.1.5
- Package creation


