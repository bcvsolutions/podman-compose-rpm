Name:           podman-compose
Version:        0.1.5
Release:        1.2
Summary:        Package for docker-compose.
Group:          Applications/Tools
License:        GNU 2.0
URL:            https://github.com/containers/podman-compose
Patch0:		podman-compose-0.1.5-stop.patch
Packager:       Ludek Urban
BuildRoot:      "%{_tmppath}/podman-compose-build-root"
Requires:	python3, podman, python3-pyyaml

%description

Package for podman-compose which is for configuring podman images using compose file.

%prep

# we have no source, so nothing here

%build
wget https://github.com/containers/podman-compose/archive/v%{version}.tar.gz -O podman-compose-%{version}.tar.gz
gunzip podman-compose-%{version}.tar.gz
tar -xf podman-compose-%{version}.tar
mv podman-compose-%{version}/podman_compose.py %{name}
mv podman-compose-%{version}/README.md README.md
mv podman-compose-%{version}/docs docs
mv podman-compose-%{version}/LICENSE LICENSE
%patch0

%install

# main script
mkdir -p %{buildroot}/usr/bin/
install -m 755 %{name} %{buildroot}/usr/bin/%{name}
# docs 
mkdir -p %{buildroot}/usr/share/doc/podman-compose/docs
install -m 644 docs/* %{buildroot}/usr/share/doc/podman-compose/docs/
# readme
install -m 644 README.md %{buildroot}/usr/share/doc/podman-compose/README.md
# licence
mkdir -p %{buildroot}/usr/share/licenses/podman-compose
install -m 644 LICENSE %{buildroot}/usr/share/licenses/podman-compose/LICENSE

%files
%doc README.md docs/
%license LICENSE
/usr/bin/%{name}


%clean
#we not use clean

%changelog

* Tue May 12 2020 Ludek Urban <ludek.urban@bcvsolutions.eu> 0.1.5
- added README and licence file to package

* Fri Mar 6 2020 Ludek Urban <ludek.urban@bcvsolutions.eu> 0.1.5
- Package creation

