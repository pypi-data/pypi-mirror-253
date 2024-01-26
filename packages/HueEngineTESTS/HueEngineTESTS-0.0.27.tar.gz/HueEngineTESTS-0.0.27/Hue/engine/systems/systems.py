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

import pygame as pg
from .camera import Camera
from .physics import PhysicsSystem
from .render import RenderingSystem
from Hue.utils.globals import _ENTITY, _ENTITYMAP

class Systems():
    def __init__(self, winX:int=800, winY:int=600, _WINFLAGS:tuple|list=[]):
        self.clock = pg.time.Clock()
        self.window = pg.display.set_mode((winX, winY), *_WINFLAGS)
        self.screen = pg.Surface((self.window.get_width(), self.window.get_height()))
        self.camera = Camera(self.window.get_width()/2, self.window.get_height()/2)
        self.renderSystem = RenderingSystem(self.window)
        self.physicsSystem = PhysicsSystem()
        self._UPTIME = 0.0
        self._ACTIVE = []
        self._VIEWPORTRECT = None

    def _ViewportCalculation(self, entity:_ENTITY) -> bool:
        self._VIEWPORTRECT = self.camera._GetViewPort()
        if ("SpriteComponent" in entity and self._VIEWPORTRECT.colliderect(entity["SpriteComponent"].rect)):
            return True
        return False

    def CalculateActiveEntities(self, dt:float=1.0) -> pg.Rect:
        self._ACTIVE = list(filter(self._ViewportCalculation, _ENTITYMAP.values()))
        self.renderSystem._ACTIVE = self._ACTIVE.copy()

    def Run(self, dt:float) -> None:
        self._UPTIME += dt
        self.CalculateActiveEntities(dt)
        self.physicsSystem.Update(dt)
        self.renderSystem.Update(dt)
        self.renderSystem.Blit()
        

