import pyglet
import pyglet.image as pyi
import os

#Drawing Orchestator
Gfx_batch=pyglet.graphics.Batch()
GfxOrd_Background=pyglet.graphics.OrderedGroup(0)
GfxOrd_Foreground=pyglet.graphics.OrderedGroup(1)
GfxOrd_BoardObjects=pyglet.graphics.OrderedGroup(3)

SIZE = 800
BOARD_SIZE=20
NUMPLAYERS=4

imgPath="Media/IndexMedia.txt"
imgBoard = pyi.load('Media/BoardHQ.png')
imgSlot = pyi.load('Media/SlotHQ.png')

BOARD_BORDER = int(SIZE/15)
BACKGROUND_SCALE = SIZE/imgBoard.width
SLOT_SCALE = BACKGROUND_SCALE*(9/BOARD_SIZE)
JUMP = imgSlot.width*SLOT_SCALE