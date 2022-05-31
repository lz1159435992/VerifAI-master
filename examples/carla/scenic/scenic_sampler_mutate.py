from verifai.samplers.scenic_sampler import ScenicSampler
from dotmap import DotMap
from verifai.falsifier import generic_falsifier
import sys
import numpy as np
#path_to_scenic_file = 'E:\\VerifAI-master\\examples\\carla\\scenic\\adjacentOpposingPair.sc'
#path_to_scenic_file = 'C:\\Users\\LZ\\PycharmProjects\\Scenic\\examples\\carla\\carla_challenge_6.scenic'
#从外面传进来的截图路径
sys.stdout.write('第一个参数 {}\n'.format(sys.argv[0]))
sys.stdout.write('第二个参数 {}\n'.format(sys.argv[1]))
sys.stdout.write('第三个参数 {}\n'.format(sys.argv[2]))

path_to_scenic_file = sys.argv[1]
MAX_ITERS = int(sys.argv[2])
# path_to_scenic_file = 'F:/autodrive_data/mutants_carla_challenge_6/Town02/Town02.scenic'
#screenShotPath = 'F:/autodrive_data//meta'
sampler = ScenicSampler.fromScenario(path_to_scenic_file)
#print(sampler)
#原数量为20
#MAX_ITERS = 20
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
