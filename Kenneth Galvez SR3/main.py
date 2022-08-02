from re import M
from gl import Renderer, color, V2, V3


width = 800
height = 650

rend = Renderer(width, height)

rend.glLoadModel("Man.obj",
                 translate = V3(width/2, height/4, 0),
                 scale = V3(50,50,50))

rend.glFinish('output.bmp')