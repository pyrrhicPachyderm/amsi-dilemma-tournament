#!/usr/bin/env python3

import os
import argparse
from stable_baselines3.common.env_util import make_vec_env
from sb3_contrib import ARS

import utils.rl.env as env

parser = argparse.ArgumentParser()
parser.add_argument("agent_name")
parser.add_argument("-n", "--num_steps", default = 1e6, type = int)
parser.add_argument("-e", "--num_env", default = 4, type = int)
args = parser.parse_args()

log_path = os.path.join("rl", "logs")
agent_path = os.path.join("rl", "agents", args.agent_name)

vec_env = make_vec_env(env.DilemmaEnv, n_envs = args.num_env)

model = ARS("MlpPolicy", vec_env, verbose = 0, tensorboard_log = log_path)
model.learn(total_timesteps = args.num_steps, progress_bar = True, tb_log_name = args.agent_name)
model.save(agent_path)
