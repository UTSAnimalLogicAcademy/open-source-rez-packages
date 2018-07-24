#! /bin/bash

export PACKAGE_INSTALLATION_ROOT=~/packages
export PACKAGE_NAME=glew
export PACKAGE_VERSION=2.0.0
export MAKE_THREADS=28

mkdir -p $PACKAGE_INSTALLATION_ROOT/$PACKAGE_NAME/$PACKAGE_VERSION

cd glew-2.0.0
make -j$MAKE_THREADS
make install GLEW_DEST=$PACKAGE_INSTALLATION_ROOT/$PACKAGE_NAME/$PACKAGE_VERSION -j$MAKE_THREADS
cd ..
cp package.py $PACKAGE_INSTALLATION_ROOT/$PACKAGE_NAME/$PACKAGE_VERSION


