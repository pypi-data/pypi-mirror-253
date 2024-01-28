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

import HueEngine
from .__init__ import Processor

class TransformProcessor(Processor):
    def __init__(self) -> None:
        super().__init__()

    def Move(self, transform, velocity, dt):
        transform.x += velocity.vX * dt
        transform.y += velocity.vY * dt

    def ApplyFriction(self, velocity, dt):
        if (velocity.vX > 0.0):
            velocity.vX -= 0.8 * dt
            if (velocity.vX <= 0.0): velocity.vX = 0.0
        elif (velocity.vX < 0.0):
            velocity.vX += 0.8 * dt
            if (velocity.vX >= 0.0): velocity.vX = 0.0

        if (velocity.vY > 0.0):
            velocity.vY -= 0.8 * dt
            if (velocity.vY <= 0.0): velocity.vY = 0.0
        elif (velocity.vY < 0.0):
            velocity.vY += 0.8 * dt
            if (velocity.vY >= 0.0): velocity.vY = 0.0

    def ApplyGravity(self, velocity, dt):
        velocity.vY += 300 * dt

    def Process(self, *args, dt:float=1.0, **kwargs) -> None:
        for entity, transform in HueEngine.fetchAllTypes(HueEngine.TransformComponent):
            velocity = HueEngine.fetchComponent(entity, HueEngine.VelocityComponent)
            if transform and velocity:
                self.ApplyGravity(velocity, dt)
                self.Move(transform, velocity, dt)
                self.ApplyFriction(velocity, dt)
