# Eternal Terminal RPM

## Usage
### Prerequisites
#### Fedora
```
$ sudo dnf install rpm-build mock dnf-utils
```
#### EL7
```
$ sudo dnf install rpm-build mock yum-utils
```

### Initialize `mock`
List all mock environments available:
```
$ ls /etc/mock/*
```

Initialize mock:
```
$ sudo mock -r <chroot> --init
```

### Create SRPM
Create an SRPM that we can use to put through `mock`:

```
$ rpmbuild -bs eternal-terminal.spec
```

Output will be in `~/rpmbuild/SRPMS`.

### Build SRPM with `mock`
Run `mock` to build the SRPM into an actual package:

```
$ mock -r <chroot> rebuild rpmbuild/SRPMS/<srpm-file>
```

Output files go to `/var/lib/mock/<chroot>/result`.

### Publishing
You can publish the completed build to a service like PackageCloud or use an internal Yum distribution system like [Pulp](https://pulpproject.org/).
