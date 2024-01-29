from gymnasium.envs.registration import register
from collision.collision import CollisionHandler

import os

resource_dir = os.path.dirname(os.path.realpath(__file__)) + '/'

register(
     id="racingenv/Racing-v1",
     entry_point="racingenv.env:RacingEnv",
)

register(
     id="racingenv/Racing-features-v1",
     entry_point="racingenv.env:RacingEnv",
     kwargs={
          "obs_type": "features"
     }
)

register(
     id="racingenv/Racing-pixels-v1",
     entry_point="racingenv.env:RacingEnv",
     kwargs={
          "obs_type": "pixels",
          "normalize_images": False
     }
)

register(
     id="racingenv/Racing-normalized-v1",
     entry_point="racingenv.env:RacingEnv",
     kwargs={
          "obs_type": "pixels",
          "normalize_images": True
     }
)
