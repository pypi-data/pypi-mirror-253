# cli.py: CLI front-end
#
# Copyright (C) 2022 vkbasalt-cli Contributors
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 3.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# SPDX Identifier: GPL-3.0-only

import sys
import argparse
from vkbasalt.lib import parse

def vkbasalt_cli():

    parser = argparse.ArgumentParser(description="a utility to pass arguments to vkBasalt")
    parser.add_argument("-e", "--effects",
                        help="effects in a separated list of effect to use",
                        choices=["cas", "dls", "fxaa", "smaa", "lut"],
                        nargs="+")
    parser.add_argument("-o", "--output",
                        help="output file")
    parser.add_argument("-d", "--default",
                        help="use default configuration",
                        action="store_true")
    parser.add_argument("--toggle-key",
                        help="toggle key (default: Home)")
    parser.add_argument("--disable-on-launch",
                        help="disable on launch",
                        action="store_true")
    parser.add_argument("--cas-sharpness",
                        help="adjust CAS sharpness",
                        type=float)
    parser.add_argument("--dls-sharpness",
                        help="adjust DLS sharpness",
                        type=float)
    parser.add_argument("--dls-denoise",
                        help="adjust DLS denoise",
                        type=float)
    parser.add_argument("--fxaa-subpixel-quality",
                        help="adjust FXAA subpixel quality",
                        type=float)
    parser.add_argument("--fxaa-quality-edge-threshold",
                        help="adjust FXAA quality edge threshold",
                        type=float)
    parser.add_argument("--fxaa-quality-edge-threshold-min",
                        help="adjust FXAA quality edge threshold minimum",
                        type=float)
    parser.add_argument("--smaa-edge-detection",
                        default="luma",
                        help="adjust SMAA edge detection (default: %(default)s)",
                        choices=["luma", "color"])
    parser.add_argument("--smaa-threshold",
                        help="adjust SMAA threshold",
                        type=float)
    parser.add_argument("--smaa-max-search-steps",
                        help="adjust SMAA max search steps",
                        type=int)
    parser.add_argument("--smaa-max-search-steps-diagonal",
                        help="adjust SMAA max search steps diagonal",
                        type=int)
    parser.add_argument("--smaa-corner-rounding",
                        help="adjust SMAA corner rounding",
                        type=int)
    parser.add_argument("--lut-file-path",
                        help="specify LUT file path")
    parser.add_argument("--exec",
                        help="execute command")
    args = parser.parse_args()

    parse(args)

if __name__ == '__main__':
    vkbasalt_cli()
    sys.exit(0)
