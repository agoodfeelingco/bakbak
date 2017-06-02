#! /usr/bin/env AFDKOPython
# encoding: UTF-8
from __future__ import division, absolute_import, print_function, unicode_literals
import hindkit

def client_override(self):
    if self.name == "Google Fonts":
        self.tables["name"].update({
            0: hindkit.fallback(
                self.family.info.copyright,
                "Copyright {} Struckby (design@struckby.co)".format(self.release_year_range),
            ),
            7: None,
            8: "Struckby",
            9: "Saumya Kishore and Sanchit Sawaria",
            11: "https://struckby.co",
            13: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: http://scripts.sil.org/OFL",
            14: "http://scripts.sil.org/OFL",
        })
        self.tables["OS/2"].update({
            "Vendor": None,
        })
hindkit.Client.override = client_override

family = hindkit.Family(
    trademark = "Bak-Bak",
    script_name = "Devanagari",
    client_name = "Google Fonts",
    initial_release_year = 2017,
)
i = family.info
i.openTypeHheaAscender, i.openTypeHheaDescender, i.openTypeHheaLineGap = 1050, -350, 100
i.openTypeOS2TypoAscender, i.openTypeOS2TypoDescender, i.openTypeOS2TypoLineGap = 1050, -350, 100
i.openTypeOS2WinAscent, i.openTypeOS2WinDescent = 1100, 400

family.set_masters([
    ("Regular", 0),
])
family.set_styles([
    ("Regular", 0, 400),
])

project = hindkit.Project(
    family,
    fontrevision = "0.200",
    options = {

        "prepare_kerning": True,
        "prepare_mark_positioning": True,

        "match_mI_variants": 1,
        "position_marks_for_mI_variants": True,

        # "build_ttf": True,
        "do_style_linking": True,

        # "use_os_2_version_4": True,
        #     "prefer_typo_metrics": True,
        #     "is_width_weight_slope_only": True,

        "additional_unicode_range_bits": [0, 1, 2],

    },
)
project.build()
