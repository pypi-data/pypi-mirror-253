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


class PositionComponent:
    def __init__(self, x:float=0.0, y:float=0.0) -> None:
        self.x = x
        self.y = y

class VelocityComponent:
    def __init__(self, xVelocity:float=0.0, yVelocity:float=0.0) -> None:
        self.x = xVelocity
        self.y = yVelocity

class SpriteComponent(pg.sprite.Sprite):
    def __init__(self, color:tuple|list= [50,86,32], size:tuple|list=[16,16]) -> None:
        super().__init__()
        self.image = pg.Surface(size)
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def SetColor(self, color:tuple|list=[53,20,62]) -> None:
        self.color = color
        self.image.fill(color)

class ColliderComponent(pg.sprite.Sprite):
    def __init__(self, position:tuple|list=(0,0), size:tuple|list=[16,16], color:tuple|list=[142,50,67]) -> None:
        super().__init__()
        self.color = color
        self.image = pg.Surface(size)
        self.image.set_colorkey((0, 0, 0))  # Set black as the transparent color
        self.image.fill((0, 0, 0))  # Fill with the transparent color
        pg.draw.rect(self.image, [255,255,255], self.image.get_rect(), width=1)  # Draw the border
        self.rect = self.image.get_rect(topleft=position)
    
    def SetColor(self, color:tuple|list=[142,50,67]) -> None:
        self.color = color
