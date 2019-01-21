# -*- coding: utf-8 -*-

name = 'usd_maya'

version = '19.01'

requires = [
    'usd-19.01',
    'PyOpenGL-3.1.0'
]

build_requires = [
    'cmake-3.2',
]

variants = [
    ['platform-linux', 'arch-x86_64', 'maya-2017'],
    ['platform-linux', 'arch-x86_64', 'maya-2018']
]

def commands():
    env.MAYA_SCRIPT_PATH.append("{this.root}/third_party/maya/share/usd/plugins/usdMaya/resources/")
    env.MAYA_SHELVES_ICONS = "{this.root}/third_party/maya/share/usd/plugins/usdMaya/resources/"
    env.MAYA_SHELF_PATH.append("{this.root}/third_party/maya/share/usd/plugins/usdMaya/resources/")
    env.MAYA_PLUG_IN_PATH.append("{this.root}/third_party/maya/plugin")
    env.XBMLANGPATH.append("{this.root}/third_party/maya/share/usd/plugins/usdMaya/resources/")
    env.MAYA_VP2_DEVICE_OVERRIDE.set("VirtualDeviceGL")
    env.MAYA_VP2_USE_VP1_SELECTION.set(1)
