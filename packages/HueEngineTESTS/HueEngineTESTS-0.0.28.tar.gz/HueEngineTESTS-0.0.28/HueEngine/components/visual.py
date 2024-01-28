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

from HueEngine.debug.debug import _LOGFUNC
from HueEngine.__core__ import _NULL, _ARRAY, pg


class TextureComponent:
    def __init__(self, color:_ARRAY[int]=[53,20,62]) -> _NULL:
        self.color = color
        self.texture = _NULL
        self.Refresh()

    def Refresh(self):
        self.texture = pg.Surface((32,32))
        self.texture.fill(self.color)
    
    def SetColor(self, color:_ARRAY[int]=[53,20,62]) -> _NULL:
        self.color = color
        self.image.fill(self.color)

    @_LOGFUNC
    def Load(self, fp:str):
        try:
            self.texture = pg.image.load(fp)
        except:
            return "Error Loading Texture!\n"
