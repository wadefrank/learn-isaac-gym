from legged_gym.utils.helpers import get_args, update_cfg_from_args, class_to_dict, parse_sim_params
from legged_gym.envs.humanoid.g1_config import G1Cfg
from legged_gym.envs.base.legged_robot import LeggedRobot
from legged_gym import PROJECT_ROOT_DIR
import torch
import numpy as np

# config
args = get_args()
env_cfg = G1Cfg()
env_cfg, _ = update_cfg_from_args(env_cfg, None, args)
sim_params = {"sim": class_to_dict(env_cfg.sim)}
sim_params = parse_sim_params(args, sim_params)

env = LeggedRobot(env_cfg, sim_params, args.physics_engine, args.sim_device, args.headless)

# load motion data
motion_file = f"{PROJECT_ROOT_DIR}/data/LAFAN/dance1_subject2.csv"

motion_data = torch.from_numpy(np.loadtxt(motion_file, delimiter=','))
motion_data = motion_data.to(torch.float32).to(env.device)

root_trans = motion_data[:, :3]
root_rot = motion_data[:, 3:7]
actions = motion_data[:, 7:]

root_trans[:, :2] += env.env_origins[:, :2]

N = len(root_trans)
print('total frames: ', N)

t = 0
while t < N+1:
    if t == N:
        t = 0

    # 注意：def step_animation并没有做decimation步step（只做了一步step）
    env.step_animation(actions[t], root_trans[t], root_rot[t])
    t += 1
