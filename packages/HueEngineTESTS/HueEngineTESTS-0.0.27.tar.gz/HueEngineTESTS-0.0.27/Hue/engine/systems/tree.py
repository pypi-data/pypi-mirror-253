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

pgRect = pg.Rect

class Quadtree:
    def __init__(self, depthLevel:int=0, nodeBounds:pgRect=pgRect(0,0,800,600)):
        """
        Initializes a Quadtree node.

        Args:
            depthLevel (int): The current depth depthLevel of the Quadtree node.
            nodeBounds (pg.Rect): The rectangular nodeBounds of this Quadtree node.
        """
        self.MAX_OBJECTS = 10
        self.MAX_depthLevelS = 5

        self.depthLevel = depthLevel
        self.objects = []
        self.nodeBounds = nodeBounds
        self.nodes = [None, None, None, None]

    def Split(self) -> None:
        """
        Splits the node into 4 subnodes by dividing the node into four equal parts.
        """
        subWidth = self.nodeBounds.width / 2
        subHeight = self.nodeBounds.height / 2
        x = self.nodeBounds.x
        y = self.nodeBounds.y

        self.nodes[0] = Quadtree(self.depthLevel + 1, pg.Rect(x + subWidth, y, subWidth, subHeight))
        self.nodes[1] = Quadtree(self.depthLevel + 1, pg.Rect(x, y, subWidth, subHeight))
        self.nodes[2] = Quadtree(self.depthLevel + 1, pg.Rect(x, y + subHeight, subWidth, subHeight))
        self.nodes[3] = Quadtree(self.depthLevel + 1, pg.Rect(x + subWidth, y + subHeight, subWidth, subHeight))

    def GetIndex(self, entity) -> int:
        """
        Determines where an object belongs in the Quadtree.

        Args:
            rect (pg.Rect): The rectangle representing the object's nodeBounds.

        Returns:
            int: The index of the node (0-3) where the object fits or -1 if it cannot completely fit within a child node.
        """
        index = -1
        verticalMidpoint = self.nodeBounds.x + (self.nodeBounds.width / 2)
        horizontalMidpoint = self.nodeBounds.y + (self.nodeBounds.height / 2)
        # Object can completely fit within the top quadrants
        topQuadrant = (entity["PositionComponent"].y < horizontalMidpoint and entity["PositionComponent"].y + entity["ColliderComponent"].rect.height < horizontalMidpoint)
        # Object can completely fit within the bottom quadrants
        bottomQuadrant = (entity["PositionComponent"].y > horizontalMidpoint)

        # Object can completely fit within the left quadrants
        if entity["PositionComponent"].x < verticalMidpoint and entity["PositionComponent"].x + entity["ColliderComponent"].rect.width < verticalMidpoint:
            if topQuadrant:
                index = 1
            elif bottomQuadrant:
                index = 2
        # Object can completely fit within the right quadrants
        elif entity["PositionComponent"].x > verticalMidpoint:
            if topQuadrant:
                index = 0
            elif bottomQuadrant:
                index = 3

        return index

    def Insert(self, obj) -> None:
        """
        Inserts an object into the Quadtree. If the node exceeds its capacity, it will Split and add objects to its subnodes.

        Args:
            obj (Object): The object to Insert.
        """
        if self.nodes[0] is not None:
            index = self.GetIndex(obj)

            if index != -1:
                self.nodes[index].Insert(obj)
                return
        
        if obj not in self.objects: self.objects.append(obj)

        if len(self.objects) > self.MAX_OBJECTS and self.depthLevel < self.MAX_depthLevelS:
            if self.nodes[0] is None:
                self.Split()

            i = 0
            while i < len(self.objects):
                index = self.GetIndex(self.objects[i])
                if index != -1:
                    self.nodes[index].Insert(self.objects.pop(i))
                else:
                    i += 1

    def Retrieve(self, returnObjects, entity) -> list:
        """
        Returns all objects that could collide with the given object.

        Args:
            returnObjects (list): A list to hold all detected objects.
            rect (pg.Rect): The rectangle representing the object's nodeBounds.

        Returns:
            list: A list of all detected objects.
        """
        index = self.GetIndex(entity)
        if index != -1 and self.nodes[0] is not None:
            self.nodes[index].Retrieve(returnObjects, entity)

        returnObjects.extend(self.objects)
        return returnObjects
