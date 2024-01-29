doc = """
vos-data-utils - a utility library for ValueOfSpace data work with Python
==========================================================================

Main Features
-------------
Correction function for dates related to building permit, commencement, and completion in the Building Permit Information
Support for current legal district data and change history
Correction function to align with the current legal district by reflecting changes in legal district data
Conversion function to transform address strings into Parcel Number (PNU)
Generation function for unique transaction case IDs in ValueofSpace
"""
version = "0.0.3" 
author = "ValueOfSpace"
description = "description"
license = "MIT"

def __version__():
    return version

def __author__():
    return author

def __description__():
    return description

def __license__():
    return license

def __doc__():
    return doc

def __test__():
    from vdutils.tests.tests import __run_test__
    __run_test__() 
