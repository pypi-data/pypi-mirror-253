#  Hue Engine ©️
#  2023-2024 Setoichi Yumaden <setoichi.dev@gmail.com>
#
#  This software is provided 'as-is', without any express or implied
#  warranty.  In no event will the authors be held liable for any damages
#  arising from the use of this software.
#
#  Permission is granted to anyone to use this software for any purpose,
#  including commercial applications, and to alter it and redistribute it
#  freely, subject to the following restrictions:
#
#  1. The origin of this software must not be misrepresented; you must not
#     claim that you wrote the original software. If you use this software
#     in a product, an acknowledgment in the product documentation would be
#     appreciated but is not required.
#  2. Altered source versions must be plainly marked as such, and must not be
#     misrepresented as being the original software.
#  3. This notice may not be removed or altered from any source distribution.

import os, platform
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = str(True)
import pygame as pg
from pygame.locals import *
from .utils import *
from .engine.components import *
from .engine.systems import *
from .GUI import *
from .HueGame.HueGame import *
from .version import __version__,__DEV__,__versionTag__
pg.font.init()



def _Hue() -> None:
    print(
        f"\nHue Engine v{__version__}\n2023-2024 {__DEV__}\n\nThis software is provided 'as-is', without any express or implied\nwarranty.  In no event will the authors be held liable for any damages\narising from the use of this software.\n\nPermission is granted to anyone to use this software for any purpose,\nincluding commercial applications, and to alter it and redistribute it\nfreely, subject to the following restrictions:\n\n1. The origin of this software must not be misrepresented; you must not\nclaim that you wrote the original software. If you use this software\nin a product, an acknowledgment in the product documentation would be\nappreciated but is not required.\n2. Altered source versions must be plainly marked as such, and must not be\nmisrepresented as being the original software.\n3. This notice may not be removed or altered from any source distribution.\n"
    )


if "HueEngine_HIDE_PROMPT" not in os.environ:
    print(
        f"Hue Engine {__version__} (pygame-ce {pg.ver}, SDL2 {'.'.join(map(str, pg.get_sdl_version()))}, Python {platform.python_version()})\n"
    )