%define name drakx-autoinstall-doc
%define version 10.0.3
%define release %mkrel 2

Summary:        Auto Install Documentation for Drakx
Name:           %{name}
Version:        %{version}
Release:        %{release}
Url:            http://members.shaw.ca/mandrake
Source0:        drakx-autoinstall-doc.tar.bz2
Source1:        so_split.tar.bz2
License:        GFDL
Group:          System/Configuration/Other
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
This package contains the AutoInstall documents, in OpenOffice.org binary
format, Post Script, PDF, one big HTML file and a HOWTO like set of smaller
HTML files.

The Mandrakelinux Distribution provides a facility, DrakX, which allows
for the automated installation on to computers that you use or manage.

The DrakX graphic installer has the capability of being used in both the
interactive and automated modes. These documents deal specifically with
it's automated capability.

Automated Installation is intended for situations where the same
'Install' set is to be placed on multiple computers. This can be a
substantial time saver for anyone. More importantly, the automation means
that you do not have to sit in front of each computer filling in the
blanks, picking this and that and hoping that you remember the selections
you chose the previous time.

%prep

%setup -q -n %{version}

# put source code in here too
bzip2 -dc %{SOURCE1} | tar xf -
# make sure executable is not present
rm -f Programs/so_split

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AutoInstall-%{version}.sxw
%doc AutoInstall-%{version}.ps AutoInstall-%{version}.pdf
%doc AutoInstall-%{version}.html HTML
%doc README build Programs
