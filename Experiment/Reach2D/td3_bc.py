from copy import deepcopy
from rlfd.params.td3 import reach2d_params

params_config = deepcopy(reach2d_params)

params_config["config"] = ("TD3_BC",)
# Offline training with bc
params_config["offline_num_epochs"] = 200
# Online training with be as regularizer
params_config["agent"]["demo_strategy"] = "BC"
params_config["agent"]["sample_demo_buffer"] = True
# Tuned values
params_config["agent"]["bc_params"]["q_filter"] = (False,)
params_config["agent"]["bc_params"]["prm_loss_weight"] = (1e-2,)
params_config["seed"] = tuple(range(3))