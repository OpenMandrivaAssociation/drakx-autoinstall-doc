%define name drakx-autoinstall-doc
%define version 10.0.3
%define release 8

Summary:        Auto Install Documentation for Drakx
Name:           %{name}
Version:        %{version}
Release:        %{release}
Url:            https://members.shaw.ca/mandrake
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

The Mandriva Linux Distribution provides a facility, DrakX, which allows
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


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 10.0.3-7mdv2011.0
+ Revision: 617900
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 10.0.3-6mdv2010.0
+ Revision: 428341
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 10.0.3-5mdv2009.0
+ Revision: 244541
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 10.0.3-3mdv2008.1
+ Revision: 136380
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 10.0.3-3mdv2008.0
+ Revision: 64713
- fix description

* Thu Aug 16 2007 Thierry Vignaud <tv@mandriva.org> 10.0.3-2mdv2008.0
+ Revision: 64219
- use %%mkrel
- Import drakx-autoinstall-doc




* Sun May 2 2004 David Eastcott <david@eastcott.net> 10.0.3-1mdk
- minor adjustments
- changed distribution name to Mandrakelinux
- Creating a Mastering File Set: added definition for a seconf DVD
- A Script Based Updater: adjusted script to use find instead of ls
- Alternate for Creating an Updated CD Set: adjusted script to create both DVDs

* Fri Mar 12 2004 David Eastcott <david@eastcott.net> 10.0.2-1mdk
- add descriptions/usage for hd_grub.img
- adjust useSupermount for 'magicdev'
- issues for Community Release
- lots of other things - see the documents New Versions for more
- details

* Tue Feb 24 2004 David Eastcott <david@eastcott.net> 10.0.1-1mdk
- updates for stage1 improvements, see document for details
- reformated document for clean html generation
- updated so_split for bugs due to reformatting

* Sun Feb 15 2004 David Eastcott <david@eastcott.net> 10.0.0-1mdk
- updates for 10.0, see document for details
- fix toc line count in so_split pgm

* Tue Feb 10 2004 David Eastcott <david@eastcott.net> 9.2.2-1mdk
- update Replay Install for deleted steps

* Mon Feb 9 2004 David Eastcott <david@eastcott.net> 9.2.1-1mdk
- added description for netauto parameter,
- corrected Advanced Features examples,
- added IP-based Naming example for DHCP server

* Wed Jan 25 2004 David Eastcott <david@eastcott.net> 9.2.0-1mdk
- updates for 9.2

* Sun Sep 8 2002 David Eastcott <david@eastcott.net> 9.0.1-1mdk
- mostly updates to examples to reflect 9.0
- bootloader - revert rename of 'entries; news are still renamed to old_...
- services - added dm to System list
- keyboard - added GRP_TOGGLE entry

* Wed Aug 21 2002 David Eastcott <david@eastcott.net> 9.0.0-1mdk
- updates for 9.0

* Fri Jul 26 2002 David Eastcott <david@eastcott.net> 8.2.2-1mdk
- general typo fixes, added warning note about CLEAN_TMP to
- miscellaneous

* Wed Mar 13 2002 David Eastcott <david@eastcott.net> 8.2.1-1mdk
- replace the section Creating an Updated Installation CD Set,
- correct option-identifier inr DHCP Server - Method 4,
- expand description in DHCP Notes

* Sat Mar 9 2002 David Eastcott <david@eastcott.net> 8.2.0-1mdk
- updated for 8.2
- fix so_split for H4 html conversions
- reworked 'syslinux.cfg' section, new Advanced Features section,
- updated Replay Install, updated Creating an Updated ...
- lots of minor changes too.

* Wed Jan 2 2002 David Eastcott <david@eastcott.net> 8.1.2-1mdk
- cleanups, fix bk grnd for older netscapes, fix html refs for wacom links.
- added so_split source for re-creating all files.

* Sun Dec 30 2001 Lenny Cartier <lenny@mandrakesoft.com> 8.1.1-1mdk
- provides the great documentation for DrakX AutoInstall by
  David Eastcott <david@eastcott.net> 8.1.1-1mdk
  - first rpm release


# end of file
