#! /usr/bin/env AFDKOPython
# encoding: UTF-8
from __future__ import division, absolute_import, print_function, unicode_literals
import hindkit as kit

def override(self):
    self.style_scheme = kit.constants.STYLES_DUAL
    self.tables['name'].update({
        0: "Copyright 2016 Struckby. All Rights Reserved.",
        7: "Bakchod is a trademark of Struckby.",
        8: "Struckby",
        9: "Saumya Kishore",
        11: "http://struckby.co",
        12: None,
        13: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: http://scripts.sil.org/OFL",
        14: "http://scripts.sil.org/OFL",
    })
    self.tables['OS/2'].update({
        'Vendor': None,
    })
kit.Client.override = override

family = kit.Family(
    base_name = 'Bakchod',
    script_name = 'Devanagari',
)
family.set_styles(kit.constants.STYLES_SINGLE)

project = kit.Project(
    family,
    fontrevision = '0.100',
    options = {
        'prepare_mark_positioning': True,
        'match_mI_variants': 'single',
        'position_marks_for_mI_variants': True,
    },
)
project.build()
