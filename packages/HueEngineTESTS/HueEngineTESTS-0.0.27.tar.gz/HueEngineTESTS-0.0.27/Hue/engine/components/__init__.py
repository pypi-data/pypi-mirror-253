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


from .components import *
import pygame as pg, random
from Hue.utils.globals import _ENTITY, _MAXENTITIES, _ENTITYMAP

_COMPONENTS={
    "PositionComponent": PositionComponent,
    "VelocityComponent": VelocityComponent,
    "SpriteComponent": SpriteComponent,
    "ColliderComponent": ColliderComponent
}

def GetEntityCount() -> int:
    return len(_ENTITYMAP)

def DebugEntityCount() -> str:
    return f"<EC> | {len(_ENTITYMAP)}"

def CreateEntity() -> _ENTITY:
    Entity = {"ID":f"~{random.randint(999,9999)}","DYNAMIC":True,"MASS":50.0}
    if (len(_ENTITYMAP) < _MAXENTITIES):
        if (Entity["ID"] not in _ENTITYMAP):
            _ENTITYMAP[Entity["ID"]] = Entity
    else: print("\nMAXIMUM _ENTITY COUNT REACHED!!!\n")
    return Entity

def AddComponent(e:_ENTITY, component:str, system) -> bool:
    if (component in _COMPONENTS and component not in e):
        e[component] = _COMPONENTS[component]()
        match component:
            case "ColliderComponent":
                if ("PositionComponent" in e):
                    e[component].rect.x = e["PositionComponent"].x
                    e[component].rect.y = e["PositionComponent"].y
                else:
                    e.pop(component)
                    print("ERROR Attatching ColliderComponent To Entity With No PositionComponent!!!\n")
            case "SpriteComponent":
                if ("PositionComponent" in e and hasattr(system, "spriteGroup")):
                    e[component].rect.x = e["PositionComponent"].x
                    e[component].rect.y = e["PositionComponent"].y
                    system.spriteGroup.add(e[component])
                else: 
                    e.pop(component)
                    print("ERROR Attatching SpriteComponent To Entity With No PositionComponent!!!\n")
        return True
    return False

def HasComponent(entity:_ENTITY, component:list|str="PositionComponent") -> bool:
    if (type(component) != list):
        if (component in entity): return True
    else:
        count = 0
        bools = []
        for c in component:
            if (c in entity): bools.append(True)
            count+=1
        #print(f"Has all {count} components!\n")
        return True
    return False