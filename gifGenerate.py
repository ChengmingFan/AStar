import imageio
import time
import os
def png2gif(source,gif_name,time):
    os.chdir(source)
    file_list = os.listdir()
    frames = []
    for png in file_list:
        frames.append(imageio.imread(png))
    imageio.mimsave(gif_name,frames,'GIF',duration=time)
    print('finish')

address = "D:\PycharmProjects\AStar\images"
png2gif(address,"D:\PycharmProjects\AStar\gif\\result.gif",0.05)