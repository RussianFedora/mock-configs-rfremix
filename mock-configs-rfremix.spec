Summary:        Mock config files for the Russian Fedora Remix
Name:           mock-configs-rfremix
Version:        1.7.1
Release:        1%{?dist}

Group:          Development/Tools
License:        BSD
URL:            http://russianfedora.pro
Source0:        %{name}-%{version}.tar.bz2

BuildArch:      noarch
Requires:       mock


%description
Mock config files for RFRemix Distribution


%prep
%setup -q


%build
#Nothing to build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/mock
install -pm 0644 *.cfg $RPM_BUILD_ROOT%{_sysconfdir}/mock


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/mock/*.cfg


%changelog
* Mon Dec 26 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 1.7.1-1
- added configs for RFRemix 26
- update active configs

* Sat Oct  8 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 1.7.0-1
- added configs for RFRemix 25
- use dnf by default

* Tue Jun 28 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 1.6.1-1
- update repos for new RPM Fusion policy

* Tue Apr  5 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 1.6.0-2.R
- update description

* Tue Apr  5 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 1.6.0-1.R
- added configs for RFRemix 24

* Tue Oct 27 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 1.5.0-1.R
- added configs for RFRemix 23

* Wed Jan 28 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 1.4.0-2.R
- added dist tag

* Thu Nov  7 2013 Arkady L. Shane <ashejn@russianfedora.ru> - 1.4.0-1.R
- added RFRemix 20 and 21

* Mon Apr  8 2013 Arkady L. Shane <ashejn@russianfedora.ru> - 1.3.0-1.R
- added RFRemix 19

* Mon Sep 17 2012 Arkady L. Shane <ashejn@russianfedora.ru> - 1.2.1-1.R
- added RFRemix 18

* Mon Sep 19 2011 Arkady L. Shane <ashejn@russianfedora.ru> - 1.2.0-1.R
- added RFRemix 17 
- added RERemix 6
- drop old files
- many fixes

* Mon Sep 19 2011 Arkady L. Shane <ashejn@russianfedora.ru> - 1.1.5-1.R
- added configs for RFRemix 16 (devel, will fix before release)

* Thu Oct 21 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 1.1.4-1
- update mirrorurls for 12, 13, 14 and rawhide versions
- added rfremix-15 for future
- fix arch in rawhide

* Mon Oct  4 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 1.1.3-1
- fix russianfedora-fixes name
- fix koji urls
- added RFRemix 14

* Tue Jul  6 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 1.1.2-1
- fix release path (not rawhide)

* Fri Jul  2 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 1.1.1-1
- fix all urls

* Fri Jul  2 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 1.1.0-1
- added RFRemix 13 config files
- fixed .fc?? prefix for RFRemix 12 and 13

* Wed Oct 21 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 1.0-1
- initial build
