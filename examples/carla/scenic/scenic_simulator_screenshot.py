from verifai.simulators.carla.client_carla import *
from verifai.simulators.carla.carla_world import *
from verifai.simulators.carla.carla_task import *
from verifai.simulators.carla.carla_scenic_task import *

import numpy as np
from dotmap import DotMap
import carla

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import win32gui
import sys

# Falsifier (not CARLA) params
#端口
PORT = 8888
#BUFSIZE = 4096
BUFSIZE = 1024
simulation_data = DotMap()
simulation_data.port = PORT
simulation_data.bufsize = BUFSIZE
# Note: The world_map param below should correspond to the MapPath 
# specified in the scenic file. E.g., if world_map is 'Town01',
# the MapPath in the scenic file should be the path to Town01.xodr.


simulation_data.task = scenic_sampler_task(world_map='Town01')
print(simulation_data.task)

client_task = ClientCarla(simulation_data)

while client_task.run_client():
    # time.sleep(5)
    # hwnd = win32gui.FindWindow(None, 'pygame window')
    # print(hwnd)
    # app = QApplication(sys.argv)
    # screen = QApplication.primaryScreen()
    # img = screen.grabWindow(hwnd).toImage()
    # img.save("screenshot.png")
    time.sleep(5)
    pass
print('End of all simulations.')
