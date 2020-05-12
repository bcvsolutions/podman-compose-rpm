# podman-compose-rpm
RPM packaging for podman-compose on RHEL8/CentOS8. RPM package contains podman-copose script with is for using yml scripts with podman.
You can install RPM package or build it yourself by using specfile.

Podman-compose version: 0.1.5
Packge version: 1
Author of spec file:    Ludek Urban <ludek.urban@bcvsolutions.eu>


### Build

To build package of podman compose run:
`
rpmbuild -ba podman-compose.spec
`

SPEC file dowloads executable file from https://github.com/containers/podman-compose

Final rpm package will be in this path(default):
`
/root/rpmbuild/RPMS/x86_64/podman-compose-%{version}.x86_64.rpm
`

### Instalation
For instalation or update just run
`
yum install podman-compose-0.1.5-1.x86_64.rpm
`
For uninstalation run:

`
yum remove podman-compose
`

### Usage
Executable file will be instalated to
`
/usr/bin/podman-compose
`
