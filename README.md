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
<code>
git clone git@github.com:bcvsolutions/podman-compose-rpm.git
</code>

To build package of podman compose run rpm build with specfile.
Build process need access to podman-compose repository(https://github.com/containers/podman-compose) to download newest release.
<br>
Before building it self you will need to copy patch files from repository to rpmbuild directory( Create ~/rpmbuild/SOURCES/ when they not exist ).
<br>
<code>cp podman-compose-rpm/patches/* ~/rpmbuild/SOURCES/
</code>

After that you can run build.
<br>
<code>rpmbuild -ba podman-compose-rpm/podman-compose.spec
</code>

Final rpm package will be in this directory:
<br>
<code>~/rpmbuild/RPMS/x86_64/
</code>

### Installation
For installation or update just run(example version):
<br>
<code>
yum install podman-compose-0.1.5-1.2.x86_64.rpm
</code>

For update run(example version):
<br>
<code>
yum update podman-compose-0.1.5-1.2.x86_64.rpm
</code>

For uninstallation run:
<br>
<code>
yum remove podman-compose
</code>

### Usage
Executable file will be this path
<br>
<code>
/usr/bin/podman-compose
</code>
