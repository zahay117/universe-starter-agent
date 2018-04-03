import sys
sys.path.append('/home/cis455/Desktop/gym-ras-simulation')
import cv2
from gym.spaces.box import Box
import numpy as np
import gym
from gym import spaces
import logging
import universe
from universe import vectorized
from universe.wrappers import BlockingReset, GymCoreAction, EpisodeID, Unvectorize, Vectorize, Vision, Logger
from universe import spaces as vnc_spaces
from universe.spaces.vnc_event import keycode
import time
from gym_ras_simulation.envs.ras_env import RASEnv

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
universe.configure_logging()

def create_env(env_id, port, client_id, remotes, **kwargs):
    if env_id == "ate3":
        # To-Do: command line argument to specify the scenario file
        # To-Do (Urgent): dynamically specify port number
        return RASEnv("ate3-test-scenario_config.json", local_port=port, log_steps=10,
                      docker_directory="/home/cis455/Desktop/gym-ras-simulation/docker")
    else:
        raise Exception("environment doesn't exist")