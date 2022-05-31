import sys
list = ['D:/Anaconda/envs/Scenic','D:/Anaconda/envs/Scenic/Library/mingw-w64/bin','D:/Anaconda/envs/Scenic/Library/usr/bin','D:/Anaconda/envs/Scenic/Library/bin','D:/Anaconda/envs/Scenic/Scripts','D:/Anaconda/envs/Scenic/bin','D:/Anaconda/condabin','C:/ProgramData/Oracle/Java/javapath','C:/Windows/system32','C:/Windows','C:/Windows/System32/Wbem','C:/Windows/System32/WindowsPowerShell/v1.0','C:/Windows/System32/OpenSSH','C:/Program Files (x86)/NVIDIA Corporation/PhysX/Common','C:/Program Files/NVIDIA Corporation/NVIDIA NvDLISR','C:/WINDOWS/system32','C:/WINDOWS;C:/WINDOWS/System32/Wbem','C:/WINDOWS/System32/WindowsPowerShell/v1.0','C:/WINDOWS/System32/OpenSSH;D:/Program Files (x86)/Git/cmd','D:/Program Files/Java/jdk1.8.0_66/bin','D:/Program Files/Java/jdk1.8.0_66/jre/bin','C:/Program Files (x86)/Windows Kits/8.1/Windows Performance Toolkit','C:/Program Files/Cppcheck;E:/MinGW-W64/mingw64/bin','C:/Users/LZ/AppData/Local/Microsoft/WindowsApps','C:/Program Files/Bandizip','D:/PyCharm 2019.3.3/bin']
for i in list:
    #i.replace("\","/")
    sys.path.append(i)
sys.path.append('D:/Anaconda/envs/scenic/Lib/site-packages')
sys.path.append('D:/Anaconda/envs/scenic/Library/bin')
sys.path.append('D:/Anaconda/envs/scenic/Scripts')
sys.path.append('D:/Anaconda/envs/Scenic/Lib/site-packages/numpy')
sys.path.append('D:/Anaconda/Library/bin')
sys.path.append('D:/Anaconda/Library/Scripts')
sys.path.append('D:/Anaconda')
sys.path.append('D:/carla/VerifAI-master')
import os
from verifai.samplers.scenic_sampler import ScenicSampler
from dotmap import DotMap
from verifai.falsifier import generic_falsifier


os.chdir('D:\Anaconda\envs\Scenic\Lib\site-packages\shapely\DLLs')

#path_to_scenic_file = 'E:\\VerifAI-master\\examples\\carla\\scenic\\adjacentOpposingPair.sc'
#path_to_scenic_file = 'F:/drive_scene_7/mutants_add/0/carla_challenge_7.scenic'

#path_to_scenic_file = 'F:/drive_scene/original_script/carla_challenge_6.scenic'
#path_to_scenic_file = 'F:/drive_scene_5/original_script/carla_challenge_5.scenic'
#path_to_scenic_file = 'F:/drive_scene_7/original_script/carla_challenge_7.scenic'
#path_to_scenic_file = 'F:/drive_scene_ajust/original_script/adjacentOpposingPair.scenic'
path_to_scenic_file = 'F:/drive_scene_car/original_script/car.scenic'

#path_to_scenic_file = 'F:/autodrive_data/original-mutate/carla_challenge_6.scenic'
#screenShotPath = 'F:/autodrive_data//meta'
sampler = ScenicSampler.fromScenario(path_to_scenic_file)
#print(sampler)
#原数量为20
MAX_ITERS = 20
PORT = 8888
MAXREQS = 5
#BUFSIZE = 4096
BUFSIZE = 1024

falsifier_params = DotMap()
falsifier_params.n_iters = MAX_ITERS
falsifier_params.save_error_table = False
falsifier_params.save_good_samples = False

server_options = DotMap(port=PORT, bufsize=BUFSIZE, maxreqs=MAXREQS)

falsifier = generic_falsifier(sampler=sampler, sampler_type='scenic',
                              falsifier_params=falsifier_params,
                              server_options=server_options)

falsifier.run_falsifier()
print(falsifier.sampler_type)
print("Scenic Samples")
for i in falsifier.samples.keys():
    print("Sample: ", i)
    print(falsifier.samples[i])


# To save all samples: uncomment this
# pickle.dump(falsifier.samples, open("generated_samples.pickle", "wb"))
