import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..')) # add parent dir
from utils.utils import *

from dataio.data_diffgen import DGen

dg = DGen(unit_size=(192,192))
dim = len(dg.unit_size)
x = np.zeros(shape=dg.unit_size)

for i in range(480):
	# init_coord = dg.get_init_coord(dg.unit_size, init_point='random_center',
	# 	random_center_distance=40)
	n_steps = np.random.randint(30,50)
	this_direction = tuple([np.random.randint(-2,3),np.random.randint(-2,3)])
	x += dg.generate_one_seed_binary_tree(
		n_steps=n_steps,
		directions=this_direction, 
		enlarge_range_forward=(2,2), 
		enlarge_range_backward=(2,2),
		q_constant=0.01, lower_threshold=0.1, block_factor=0.95,
		init_point='random_center',
		random_center_distance=30)
	# x = (x>0).astype(np.float)
x = normalize_numpy_array(x,target_min=0,target_max=1)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(x)
plt.show()