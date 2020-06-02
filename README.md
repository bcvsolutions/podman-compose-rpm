# podman-compose-rpm
RPM packaging for podman-compose on RHEL8/CentOS8. RPM package contains podman-copose script with is for using yml scripts with podman.
You can install RPM package or build it yourself by using specfile.

Podman-compose version: 0.1.5

Packge version: 1.1

Author of spec file:    Ludek Urban <ludek.urban@bcvsolutions.eu>


### Build

For build podman-compose-rpm you need to have installed these packages: rpmbuild, wget, gunzip.
For the first step clone repository:

<code>
git clone git@github.com:bcvsolutions/podman-compose-rpm.git
</code>


To build package of podman compose run rpm build with specfile:
Build process need access to podman-compose repository(https://github.com/containers/podman-compose) to download newest release.

<code>
rpmbuild -ba podman-compose-rpm/podman-compose.spec
</code>

Final rpm package will be in this path(default):

<code>
~/rpmbuild/RPMS/x86_64/podman-compose-%{PODMAN-COMPOSE_VERSION}-%{RPM_VERSION}.x86_64.rpm
</code>

### Instalation
For instalation or update just run

<code>
yum install podman-compose-%{PODMAN-COMPOSE_VERSION}-%{RPM_VERSION}.x86_64.rpm
</code>


For uninstalation run:

<code>
yum remove podman-compose
</code>

### Usage
Executable file will be this path

<code>
/usr/bin/podman-compose
</code>
