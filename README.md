# podman-compose-rpm
RPM packaging for podman-compose on RHEL8/CentOS8. RPM package contains podman-copose script with is for using yml scripts with podman.
You can install RPM package or build it yourself by using specfile.

Podman-compose version: 0.1.5

Package version: 1.2

Author of spec file:    Ludek Urban <ludek.urban@bcvsolutions.eu>


### Build

For build podman-compose-rpm you need to have installed these packages: rpmbuild, wget, gunzip.
For the first step clone repository:
<br>
```
git clone git@github.com:bcvsolutions/podman-compose-rpm.git
```

To build package of podman compose run rpm build with specfile.
Build process need access to podman-compose repository(https://github.com/containers/podman-compose) to download newest release.
<br>

After that you can run build but you also need to specify SOURCE directory:

```
rpmbuild -ba --define "_sourcedir $PWD/podman-compose-rpm/patche/" podman-compose-rpm/podman-compose.spec
```

Final rpm package will be in this directory:
<br>
```
~/rpmbuild/RPMS/x86_64/
```

### Installation
For installation or update just run(example version):
<br>
```
yum install podman-compose-0.1.5-1.2.x86_64.rpm
```

For update run(example version):
<br>
```
yum update podman-compose-0.1.5-1.2.x86_64.rpm
```

For uninstallation run:
<br>
```
yum remove podman-compose
```

### Usage
Executable file will be this path
<br>
```
/usr/bin/podman-compose
```
