list = ['D:/Anaconda/envs/Scenic','D:/Anaconda/envs/Scenic/Library/mingw-w64/bin','D:/Anaconda/envs/Scenic/Library/usr/bin','D:/Anaconda/envs/Scenic/Library/bin','D:/Anaconda/envs/Scenic/Scripts','D:/Anaconda/envs/Scenic/bin','D:/Anaconda/condabin','C:/ProgramData/Oracle/Java/javapath','C:/Windows/system32','C:/Windows','C:/Windows/System32/Wbem','C:/Windows/System32/WindowsPowerShell/v1.0','C:/Windows/System32/OpenSSH','C:/Program Files (x86)/NVIDIA Corporation/PhysX/Common','C:/Program Files/NVIDIA Corporation/NVIDIA NvDLISR','C:/WINDOWS/system32','C:/WINDOWS;C:/WINDOWS/System32/Wbem','C:/WINDOWS/System32/WindowsPowerShell/v1.0','C:/WINDOWS/System32/OpenSSH;D:/Program Files (x86)/Git/cmd','D:/Program Files/Java/jdk1.8.0_66/bin','D:/Program Files/Java/jdk1.8.0_66/jre/bin','C:/Program Files (x86)/Windows Kits/8.1/Windows Performance Toolkit','C:/Program Files/Cppcheck;E:/MinGW-W64/mingw64/bin','C:/Users/LZ/AppData/Local/Microsoft/WindowsApps','C:/Program Files/Bandizip','D:/PyCharm 2019.3.3/bin']

import sys
# for i in list:
#     #i.replace("\","/")
#     sys.path.append(i)
# sys.path.append('D:/Anaconda/envs/scenic/Lib/site-packages')
# sys.path.append('D:/Anaconda/envs/scenic/Library/bin')
# sys.path.append('D:/Anaconda/envs/scenic/Scripts')
sys.path.append('D:/carla/VerifAI-master')
sys.path.append('D:/carla/VerifAI-master/PythonAPI/carla/agents')
sys.path.append('D:/carla/VerifAI-master/verifai')
# sys.path.append('D:/Anaconda/envs/Scenic/Lib/site-packages/numpy')
# sys.path.append('D:/Anaconda/Library/bin')
# sys.path.append('D:/Anaconda/Library/Scripts')
# sys.path.append('D:/Anaconda')
# from verifai.simulators.carla.client_carla import *
# from verifai.simulators.carla.carla_world import *
# from verifai.simulators.carla.carla_task import *

from dotmap import DotMap
sys.path.remove('D:\Anaconda\envs\Scenic\lib\site-packages')
sys.path.remove(r'D:/Anaconda/envs/scenic/Lib/site-packages')
#sys.path.remove('D:/Anaconda/envs/Scenic/lib/site-packages')
#sys.path.remove('D:/Anaconda/envs/Scenic/Lib/site-packages')
for i in sys.path:
    print(i)
from verifai.simulators.carla.carla_scenic_task import *
sys.path.remove('D:/carla/VerifAI-master')
sys.path.remove('D:/carla/VerifAI-master/PythonAPI/carla/agents')
sys.path.remove('D:/carla/VerifAI-master/verifai')
os.chdir('D:\Anaconda\envs\Scenic\Lib\site-packages\shapely\DLLs')
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
#从外面传进来的截图路径
screenShotPath = sys.argv[1]
world_map = sys.argv[2]
# sys.stdout.write('第一个参数 {}\n'.format(screenShotPath))
# sys.stdout.write('第二个参数 {}\n'.format(world_map))
# screenShotPath = 'F:/autodrive_data/mutants_carla_challenge_6/Town02/ScreenShot'
# simulation_data.task = scenic_sampler_task(world_map='Town02')
simulation_data.task = scenic_sampler_task(world_map=world_map)
simulation_data.task.screenshot_path=screenShotPath

#print(simulation_data.task)

client_task = ClientCarla(simulation_data)
try:
    while client_task.run_client():
        time.sleep(5)
        pass
except:
    print('场景生成出现问题')
else:
    print('场景生成成功')
print('End of all simulations.')
sys.exit()
