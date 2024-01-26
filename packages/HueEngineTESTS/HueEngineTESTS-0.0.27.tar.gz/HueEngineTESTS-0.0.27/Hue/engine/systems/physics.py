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
from Hue.engine.components import PositionComponent, VelocityComponent, ColliderComponent, HasComponent
from Hue.utils.globals import _ENTITY, _ENTITYMAP
from Hue.utils.profile import ProfileSystem


class CollisionData:
    def __init__(self) -> None:
        self._for = None
        self._none = False
        self._against = None
        self._massFor = None
        self._massAgainst = None
        self.point = pg.math.Vector2()
        self._velocityFor = pg.math.Vector2()

class PhysicsSystem:
    def __init__(self) -> None:
        self.g = 12.0
        self.f = 0.05
        self.SPF = 15
        self.frictionX = True
        self.frictionY = False

    def CalcFriction(self, componentV:VelocityComponent, dt:float=1.0):
        if self.frictionX:
            if (componentV.x > 0.0):
                componentV.x -= self.f*dt
                if (componentV.x < 0.0): componentV.x = 0.0
            
            elif (componentV.x < 0.0):
                componentV.x += self.f*dt
                if (componentV.x > 0.0): componentV.x = 0.0
        
        if self.frictionY:
            if (componentV.y > 0.0):
                componentV.y -= self.f*dt
                if (componentV.y < 0.0): componentV.y = 0.0
            
            elif (componentV.y < 0.0):
                componentV.y += self.f*dt
                if (componentV.y > 0.0): componentV.y = 0.0

    def ApplyGravity(self, dt:float=1.0) -> None:
        for entity in _ENTITYMAP.values():
            if (entity["DYNAMIC"] and HasComponent(entity, ["PositionComponent", "VelocityComponent"])):
                vel = entity["VelocityComponent"]
                mass = entity["MASS"]
                gf = (self.g*mass/20.0) * ( (mass*10)/(mass*10) )
                vel.y += gf * dt
            
    def PositionalUpdates(self, dt:float=1.0) -> None:
        for entity in _ENTITYMAP.values():
            if (entity["DYNAMIC"] and HasComponent(entity, ["PositionComponent", "VelocityComponent"])):
                entity["PositionComponent"].x += entity["VelocityComponent"].x * dt
                entity["PositionComponent"].y += entity["VelocityComponent"].y * dt
                if (HasComponent(entity, "SpriteComponent")):
                    entity["SpriteComponent"].rect.topleft = (
                        entity["PositionComponent"].x,
                        entity["PositionComponent"].y
                    ) 
                self.CalcFriction(entity["VelocityComponent"], dt)
                if (HasComponent(entity, "ColliderComponent")):
                    entity["ColliderComponent"].rect.x = entity["PositionComponent"].x
                    entity["ColliderComponent"].rect.y = entity["PositionComponent"].y

    def AABBNegX(self, component1:ColliderComponent, component2:ColliderComponent, componentV:VelocityComponent, componentP:PositionComponent) -> bool:
        if ( int(component1.rect.topleft[0]) == int(component2.rect.topright[0]) and ( component1.rect.topleft[1] <= component2.rect.bottomright[1] and component1.rect.bottomleft[1] >= component2.rect.topleft[1] ) ):
            componentP.x = component2.rect.x + component2.rect.w + 1
            componentV.x = 0.0
            return True
        return False
    
    def AABBPosX(self, component1:ColliderComponent, component2:ColliderComponent, componentV:VelocityComponent, componentP:PositionComponent) -> bool:
        if ( int(component1.rect.topright[0]) == int(component2.rect.topleft[0]) and ( component1.rect.topright[1] <= component2.rect.bottomleft[1] and component1.rect.bottomright[1] >= component2.rect.topright[1] ) ):
            componentP.x = component2.rect.x - component1.rect.w - 1
            componentV.x = 0.0
            return True
        return False

    def AABBNegY(self, component1:ColliderComponent, component2:ColliderComponent, componentV:VelocityComponent, componentP:PositionComponent) -> bool:
        if ( int(component1.rect.topleft[1]) == int(component2.rect.bottomleft[1]) and ( component1.rect.topleft[0] < component2.rect.bottomright[0] and component1.rect.topright[0] > component2.rect.bottomleft[0] ) ):
            componentP.y = component2.rect.y + component2.rect.h + 1
            componentV.y = 0.0
            return True
        return False

    def AABBPosY(self, component1:ColliderComponent, component2:ColliderComponent, componentV:VelocityComponent, componentP:PositionComponent) -> bool:
        if ( int(component1.rect.bottomleft[1]) == int(component2.rect.topleft[1]) and ( component1.rect.bottomleft[0] < component2.rect.topright[0] and component1.rect.bottomright[0] > component2.rect.topleft[0] ) ):
            componentP.y = component2.rect.y - component1.rect.h - 1
            componentV.y = 0.0
            return True
        return False

    def AABB(self) -> None:
        for eFor in _ENTITYMAP.values():
            if (eFor["DYNAMIC"] and HasComponent(eFor, ["PositionComponent","VelocityComponent","ColliderComponent"])):
                component1 = eFor["ColliderComponent"]
                componentV = eFor["VelocityComponent"]
                componentP = eFor["PositionComponent"]
            else: continue
            for eAgainst in _ENTITYMAP.values():
                if (not eAgainst["DYNAMIC"] and HasComponent(eAgainst, "ColliderComponent")):
                    component2 = eAgainst["ColliderComponent"]
                else: continue
                if (componentV.x < 0.0): self.AABBNegX(component1, component2, componentV, componentP)
                elif (componentV.x > 0.0): self.AABBPosX(component1, component2, componentV, componentP)
                if (componentV.y < 0.0): self.AABBNegY(component1, component2, componentV, componentP)
                elif (componentV.y > 0.0): self.AABBPosY(component1, component2, componentV, componentP)

    @ProfileSystem('Physics')
    def Update(self, dt:float=1.0) -> None:
        stepDelta = dt / self.SPF
        for step in range(self.SPF):
            self.ApplyGravity(dt=stepDelta)
            self.PositionalUpdates(dt=stepDelta)
            self.AABB()
