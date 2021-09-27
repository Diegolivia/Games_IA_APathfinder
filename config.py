import pyglet
import pyglet.image as pyi
import os

#Drawing Orchestator
Gfx_batch=pyglet.graphics.Batch()
GfxOrd_Background=pyglet.graphics.OrderedGroup(0)
GfxOrd_Foreground=pyglet.graphics.OrderedGroup(1)
GfxOrd_BoardObjects=pyglet.graphics.OrderedGroup(3)
GfxOrd_Players=pyglet.graphics.OrderedGroup(4)

SIZE = 800
BOARD_SIZE=20
NUMPLAYERS=3
BOARD_BORDER = int(SIZE/15)

imgPath="Media/IndexMedia.txt"