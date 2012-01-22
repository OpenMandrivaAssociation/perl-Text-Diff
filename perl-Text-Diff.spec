%define upstream_name	 Text-Diff
%define upstream_version 1.41

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 4

Summary:    Perform diffs on files and record sets
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:    http://search.cpan.org/CPAN/authors/id/R/RB/RBS/%{upstream_name}-%{upstream_version}.tar.gz 

BuildRequires:  perl-Algorithm-Diff
BuildArch:  noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
%name provides a basic set of services akin to the GNU diff utility.
It is not anywhere near as feature complete as GNU diff, but it is 
better integrated with Perl and available on all platforms. 

It is often faster than shelling out to a system's diff
executable for small files, and generally slower on larger files.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/*
%{_mandir}/man3/*

