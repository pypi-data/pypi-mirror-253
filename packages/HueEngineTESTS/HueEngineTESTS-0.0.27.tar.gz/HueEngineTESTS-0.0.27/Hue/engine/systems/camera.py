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

from pygame import Rect as pgRect

class Camera:
    def __init__(self, x:float=0.0, y:float=0.0) -> None:
        self.x = x
        self.y = y
        self._zoom = 1.0
        self._width = 400
        self._height = 300

    def SetViewWidth(self, vW:int=400) -> None:
        self._width = vW

    def SetViewHeight(self, vH:int=300) -> None:
        self._height = vH

    def _GetViewPort(self) -> pgRect:
        return pgRect(self.x, self.y, self._width / self._zoom, self._height / self._zoom)
