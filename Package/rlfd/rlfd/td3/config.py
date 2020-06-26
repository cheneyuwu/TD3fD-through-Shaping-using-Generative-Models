import numpy as np

from rlfd.td3 import td3

default_params = {
    # config summary
    "alg": "td3",
    "config": "default",
    # environment config
    "env_name": "InvertedPendulum-v2",
    "r_scale": 1.0,
    "r_shift": 0.0,
    "eps_length": 0,
    "env_args": {},
    "gamma": 0.99,
    "fix_T": False,
    # DDPG config
    "ddpg": {
        # training
        "random_exploration_cycles": 0,
        "num_epochs": int(1e3),
        "num_cycles": 1000,
        "num_batches": 1,
        "batch_size": 100,
        # use demonstrations
        "batch_size_demo": 128,
        "sample_demo_buffer": False,
        "initialize_with_bc": False,
        "initialize_num_epochs": 0,
        "use_demo_reward": False,
        "demo_strategy": "none",  # ["none", "bc", "nf", "gan"]
        # normalize observation
        "norm_eps": 0.01,
        "norm_clip": 5,
        # actor critic networks
        "scope": "ddpg",
        "layer_sizes": [400, 300],
        "twin_delayed": True,
        "policy_freq": 2,
        "policy_noise": 0.2,
        "policy_noise_clip": 0.5,
        "q_lr": 1e-3,
        "pi_lr": 1e-3,
        "action_l2": 0.0,
        # double q learning
        "polyak": 0.995,
        # multi step return
        "use_n_step_return": False,
        "bc_params": {
            "q_filter": False,
            "prm_loss_weight": 1.0,
            "aux_loss_weight": 1.0
        },
        "shaping_params": {
            # potential weight decay
            "potential_decay_scale": 1.0,
            "potential_decay_epoch": 0,
            "num_epochs": int(4e3),
            "batch_size": 128,
            "num_ensembles": 2,
            "nf": {
                "num_masked": 2,
                "num_bijectors": 4,
                "layer_sizes": [256, 256],
                "prm_loss_weight": 1.0,
                "reg_loss_weight": 200.0,
                "potential_weight": 3.0,
            },
            "gan": {
                "layer_sizes": [256, 256, 256],
                "latent_dim": 6,
                "gp_lambda": 0.1,
                "critic_iter": 5,
                "potential_weight": 3.0,
            },
        },
        # replay buffer setup
        "buffer_size": int(1e6),
    },
    # rollouts config
    "rollout": {
        "num_episodes": None,
        "num_steps": 1,
        "noise_eps": 0.1,
        "polyak_noise": 0.0,
        "random_eps": 0.0,
        "compute_q": False,
        "history_len": 300,
    },
    "evaluator": {
        "num_episodes": 4,
        "num_steps": None,
        "noise_eps": 0.0,
        "polyak_noise": 0.0,
        "random_eps": 0.0,
        "compute_q": True,
        "history_len": 300,
    },
    "seed": 0,
}


def configure_td3(params):
  # Extract relevant parameters.
  td3_params = params["ddpg"]
  # Update parameters
  td3_params.update({
      "dims": params["dims"].copy(),  # agent takes an input observations
      "max_u": params["max_u"],
      "eps_length": params["eps_length"],
      "fix_T": params["fix_T"],
      "gamma": params["gamma"],
      "info": {
          "env_name": params["env_name"],
          "r_scale": params["r_scale"],
          "r_shift": params["r_shift"],
          "eps_length": params["eps_length"],
          "env_args": params["env_args"],
          "gamma": params["gamma"],
      },
  })
  policy = td3.TD3(**td3_params)
  return policy