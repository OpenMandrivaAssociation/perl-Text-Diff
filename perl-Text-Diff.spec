%define upstream_name	 Text-Diff
%define upstream_version 1.41

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Perform diffs on files and record sets
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:	http://search.cpan.org/CPAN/authors/id/R/RB/RBS/%{upstream_name}-%{upstream_version}.tar.gz 

BuildRequires:	perl-devel
BuildRequires:	perl-Algorithm-Diff
BuildArch:	noarch

%description
%name provides a basic set of services akin to the GNU diff utility.
It is not anywhere near as feature complete as GNU diff, but it is 
better integrated with Perl and available on all platforms. 

It is often faster than shelling out to a system's diff
executable for small files, and generally slower on larger files.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.410.0-4mdv2012.0
+ Revision: 765757
- rebuilt for perl-5.14.2
- rebuilt again for perl-5.14.x

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.410.0-2
+ Revision: 764262
- rebuilt for perl-5.14.x

* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.410.0-1
+ Revision: 660020
- update to new version 1.41

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.370.0-2
+ Revision: 654326
- rebuild for updated spec-helper

* Fri Jul 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.370.0-1mdv2011.0
+ Revision: 396743
- update to 1.37
- using %%perl_convert_version
- fixed license field

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.35-6mdv2009.0
+ Revision: 224206
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.35-5mdv2008.1
+ Revision: 151359
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 0.35-4mdv2007.0
+ Revision: 108449
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Text-Diff

* Sat Feb 05 2005 Sylvie Terjan <erinmargault@mandrake.org> 0.35-3mdk
- rebuild for new perl

* Sun Jun 06 2004 Michael Scherer <misc@mandrake.org> 0.35-2mdk 
- add BuildRequires

* Tue Mar 09 2004 Michael Scherer <misc@mandrake.org> 0.35-1mdk 
- First MandrakeSoft Package

