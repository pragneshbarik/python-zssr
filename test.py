import os

test_path = "test_data"
result_path = "P:\Parth\pytorch-ZSSR\results"

images = os.listdir(test_path)

for image in images :
    os.system(f'P:/Pragnesh/envs/pytorch/python.exe run_ZSSR_single_input.py "test_data/{image}" 0 0 X4_ONE_JUMP_IDEAL_CONF 0 results')