# -*- coding: utf-8 -*-

# Resource object code
#
# Created: 周一 1月 25 14:56:42 2021
#      by: The Resource Compiler for PySide2 (Qt v5.12.9)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\x00r\
[\
Controls]\x0d\x0aStyle\
=Material\x0d\x0a\x0d\x0a[Un\
iversal]\x0d\x0aTheme=\
System\x0d\x0aAccent=R\
ed\x0d\x0a\x0d\x0a[Material]\
\x0d\x0aTheme=Light\x0d\x0aA\
ccent=LightBlue\x0d\
\x0a\
"

qt_resource_name = b"\
\x00\x15\
\x08\x1e\x16f\
\x00q\
\x00t\x00q\x00u\x00i\x00c\x00k\x00c\x00o\x00n\x00t\x00r\x00o\x00l\x00s\x002\x00.\
\x00c\x00o\x00n\x00f\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
