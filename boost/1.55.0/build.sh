#! /bin/bash

set PACKAGE_INSTALLATION_ROOT=~/packages
set PACKAGE_NAME=boost
set PACKAGE_VERSION=1.55.0

mkdir $PACKAGE_INSTALLATION_ROOT/$PACKAGE_NAME/$PACKAGE_VERSION

cd boost_1_55_0
./bootstrap.sh --prefix=$PACKAGE_INSTALLATION_ROOT/$PACKAGE_NAME/$PACKAGE_VERSION
./bjam cxxflags=-fPIC --disable-icu -a install
cd ..
cp package.py $PACKAGE_INSTALLATION_ROOT/$PACKAGE_NAME/$PACKAGE_VERSION

