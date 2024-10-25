%define modname	Text-Diff

Summary:	Perform diffs on files and record sets
Name:		perl-%{modname}
Version:	1.45
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Text::Diff
Source0:	http://search.cpan.org/CPAN/authors/id/N/NE/NEILB/%{modname}-%{version}.tar.gz 
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test)
BuildRequires:	perl-devel
BuildRequires:	perl-Algorithm-Diff

%description
%name provides a basic set of services akin to the GNU diff utility.
It is not anywhere near as feature complete as GNU diff, but it is 
better integrated with Perl and available on all platforms. 

It is often faster than shelling out to a system's diff
executable for small files, and generally slower on larger files.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%{perl_vendorlib}/*
%{_mandir}/man3/*
