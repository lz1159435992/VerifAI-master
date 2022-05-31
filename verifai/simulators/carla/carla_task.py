import time

import numpy as np
import pygame
import carla
from .carla_world import *

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import win32gui
import sys

from PIL import Image
import math
import os
import operator
from functools import reduce
from collections import Counter
#filePath:文件夹路径
def delete_file(filePath):
 if os.path.exists(filePath):
  for fileList in os.walk(filePath):
   for name in fileList[2]:
    os.chmod(os.path.join(fileList[0],name), stat.S_IWRITE)
    os.remove(os.path.join(fileList[0],name))
  shutil.rmtree(filePath)
  return "delete ok"
 else:
  return "no filepath"

class carla_task():
    #我添加的参数 screenShotPath
    def __init__(self,
                 n_sim_steps=500,
                 display_dim=(1280,720),
                 carla_host='127.0.0.1',
                 carla_port=2000,
                 carla_timeout=4.0,
                 world_map='Town03',
                 cam_transform=0,
                 screenshot_path=''):
        self.screenshot_path = screenshot_path
        self.n_sim_steps = n_sim_steps
        self.display_dim = display_dim
        self.client = carla.Client(carla_host, carla_port)
        self.client.set_timeout(carla_timeout)
        self.clock = pygame.time.Clock()
        self.world_map = world_map
        self.timestep = 0
        self.cam_transform = cam_transform
        print("[carla_task] Finished initializing carla task.")

    def step_world(self):
        # print("[carla_task] Stepping world.")
        self.world.world.wait_for_tick()
        # print("[carla_task] Before tick")
        self.world.tick(self.clock)
        # print("[carla_task] After tick")
        self.world.render(self.display)
        # print("[carla_task] After render")
        self.client.apply_batch(self.world.get_control_cmds())
        # print("[carla_task] Batch applied.")
        pygame.display.flip()


    def run_task(self, sample):
        try:
            pygame.init()
            pygame.font.init()
            self.hud = HUD(*self.display_dim)
            self.display = pygame.display.set_mode(
                self.display_dim,
                pygame.HWSURFACE | pygame.DOUBLEBUF
            )
            # print("[carla_task] Setting up world.")
            if self.client.get_world().get_map().name == self.world_map:
                self.world = World(self.client.get_world(), self.hud, 
                        cam_transform=self.cam_transform)
            else:
                self.world = World(self.client.load_world(self.world_map), 
                        self.hud, cam_transform=self.cam_transform)
            # print("[carla_task] World setup complete.")
            self.use_sample(sample)
            self.world.restart()
            self.timestep = 0
            while self.timestep < self.n_sim_steps:
                self.step_world()
                self.timestep += 1
            traj = self.trajectory_definition()
        finally:
            #time.sleep(5)
            #我添加的代码
            hwnd = win32gui.FindWindow(None, 'pygame window')
            print(hwnd)
            app = QApplication(sys.argv)
            screen = QApplication.primaryScreen()
            img = screen.grabWindow(hwnd).toImage()
            #为每张图片创建一个文件夹
            if not os.path.exists(self.screenshot_path + '/'):
                os.makedirs(self.screenshot_path + '/')
            if not os.path.exists(self.screenshot_path + '/'+str(hwnd)+'/'):
                os.makedirs(self.screenshot_path + '/'+str(hwnd)+'/')
            img.save(self.screenshot_path + '/'+str(hwnd)+'/'+'screenshot.png')

            #判断图片是否有问题

            # f = open('o.txt', 'w+')
            # im = Image.open(self.screenshot_path + '/'+str(hwnd)+'/'+'screenshot.png')
            # rgb_im = im.convert('RGB')
            # for i in range(256):
            #     for j in range(256):
            #         r, g, b = rgb_im.getpixel((i, j))
            #         print(r, g, b, file=f)
            # txt1 = open('o.txt', 'r', encoding='utf-8').read()
            # # txt2=open('p.txt','r',encoding='utf-8').read()
            #
            # for s in "' ' \n":
            #     txt1 = txt1.replace(s, '')
            #
            # count = Counter(txt1)
            # print("The frequency of each word is:", count)
            #
            # val = count.values()
            # print(val)
            #
            # sum = 0
            # for key, value in count.items():
            #     sum += value
            # print(' total of  pixels %d' % sum)
            # pre = 0
            # for key, value in count.items():
            #     pre = value / sum
            #     if (pre > 0.9):
            #         print("the picture is wrong")
            #         delete_file(self.screenshot_path + '/'+str(hwnd))
            #         break

            self.world.destroy()
            #我加入的暂停
            time.sleep(5)
            pygame.quit()
        return traj


    def use_sample(self, sample):
        raise NotImplementedError('Method should be implemented in subclass.')


    def trajectory_definition(self):
        raise NotImplementedError('Method should be implemented in subclass.')
