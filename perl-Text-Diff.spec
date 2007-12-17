%define realname	Text-Diff

Name:		perl-%{realname}
Version:	0.35
Release:	%mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Perform diffs on files and record sets
Source0:   http://search.cpan.org/CPAN/authors/id/R/RB/RBS/%{realname}-%{version}.tar.bz2 
Url:		http://www.cpan.org
BuildRequires:	perl-devel
BuildRequires:  perl-Algorithm-Diff
BuildArch:      noarch

%description
%name provides a basic set of services akin to the GNU diff utility.
It is not anywhere near as feature complete as GNU diff, but it is 
better integrated with Perl and available on all platforms. 

It is often faster than shelling out to a system's diff
executable for small files, and generally slower on larger files.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{perl_vendorlib}/*
%{_mandir}/man3/*


