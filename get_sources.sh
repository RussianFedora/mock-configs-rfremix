#!/bin/sh
NR=$(rpm -q --specfile *.spec --qf "%{name}-%{version}")

rm -rf $NR
git clone -q git://github.com/Tigro/mock-configs-rfremix.git $NR
tar -ca --exclude-vcs --exclude-vcs-ignores -f $NR.tar.bz2 $NR --exclude=.git
rm -rf $NR
