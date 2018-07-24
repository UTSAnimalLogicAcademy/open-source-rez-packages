# -*- coding: utf-8 -*-

name = 'glew'

version = '2.0.0'

variants = [['platform-linux', 'arch-x86_64']]

def commands():
    env.LD_LIBRARY_PATH.append('{this.root}/lib64')
    appendenv('PKG_CONFIG_PATH', '{root}/lib/pkgconfig/')
