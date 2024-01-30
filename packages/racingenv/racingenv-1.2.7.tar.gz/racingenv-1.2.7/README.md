# RacingEnv
A simple 2D racing environment using `gymnasium`

## Installation

Requirements `python 3.8+`, `C++17 compiler`

Package requirements:
- `scikit-build-core >=0.4.3`
- `nanobind >=1.3.2`
- `gymnasium>=0.26.0`
- `pygame>=2.1.0`
- `numpy>=1.19`

## Registered Environments

The package registers three environments

1. `racingenv/Racing-v1`
2. `racingenv/Racing-features-v1`
3. `racingenv/Racing-pixels-v1`

## Environment Arguments

The environment can be customized using the following kwargs:

1. render_mode
   - human
   - rgb_array
   - debug
   - agent
2. obs_type (this should only be specified when using `racingenv/Racing-v1`)
   - pixels
   - features
3. resolution, a tuple of the form `(width, height)` (Note that, when training the agent on pixels, the resolution will affect the observation returned by the environment)
4. pyhsics_settings, a dictionary containing the physics settings (a more details below)
5. map, path to a map file (again more details below)

## Feature Space

The environment defines the following features (Shape 37x1):
- Agent x-position `[0.0, 1.0]`
- Agent y-position `[0.0, 1.0]`
- Agent normalized x-direction `[-1.0, 1.0]`
- Agent normalized y-direction `[-1.0, 1.0]`
- Distance to the inner bound of the next checkpoint or MAX_RAY_LENGTH `[0.0, 1.0]`
- Normalized x-direction to the inner bound of the next checkpoint `[-1.0, 1.0]`
- Normalized y-direction to the inner bound of the next checkpoint `[-1.0, 1.0]`
- Distance to the outer bound of the next checkpoint or MAX_RAY_LENGTH `[0.0, 1.0]`
- Normalized x-direction to the outer bound of the next checkpoint `[-1.0, 1.0]`
- Normalized y-direction to the outer bound of the next checkpoint `[-1.0, 1.0]`
- Agent forward velocity `[-1.0, 1.0]`
- Agent angular velocity `[-1.0, 1.0]`
- Agent lateral velocity `[-1.0, 1.0]`
- For each of the 8 rays
  - Distance to the intersection or MAX_RAY_LENGTH if no intersection occurred `[0.0, 1.0]`
  - x-position of the intersection or the furthest point that could be an intersection `[0.0, 1.0]`
  - y-position of the intersection or the furthest point that could be an intersection `[0.0, 1.0]`

## Pixel Space

Image scaled down to 64x64 as `np.array`. (Shape 12288x1)

## Rewards

On the track there are several checkpoints that can only be taken in order, 
passing a checkpoint gives the agent a one time reward of 1.0. 
Hitting a wall gives the agent a reward of -1.0. Should the agent ever come to a complete
standstill the environment will truncate.

## Physics settings

There are several physics settings that can be customized by passing a dictionary when creating the environment,
which needs to specify all the keys below:

- max_velocity, the maximum possible forwards or backwards velocity of the agent
- acceleration, the acceleration applied by the forward and backward action
- drag, drag applied every frame the agent is not accelerating
- max_lateral_velocity, maximum velocity in the lateral direction (aka. drift)
- lateral_acceleration, acceleration in lateral direction
- lateral_drag, drag applied in the lateral direction
- angular_velocity, strength of the agents steering
- drift_threshold, minimum lateral velocity needed to drift

## Custom maps

In progress

## Rendering Modes

The environment supports 4 rendering modes

### Human

Implements human rendering, additionally a resolution tuple (width, height) maybe be passed when creating the environment via `resolution=(width, height)`.\
![human](https://github.com/laurenzlevi/RacingEnv/assets/72398071/a9d6e013-53e4-4315-bb76-3009827f909f)


### RGB_Array

Renders the same frame as in human mode, but the resolution is fixed to be 800 by 600, additionally `render()` returns the frame as `np.array` instead of blitting it onto the screen.

### Agent

Renders the game in the same way the agent "sees" it.
![agent](https://github.com/laurenzlevi/RacingEnv/assets/72398071/fcef8f33-55e2-4310-a304-456c7bf2c67a)

### Debug

Human rendering with additional debug information.
![debug](https://github.com/laurenzlevi/RacingEnv/assets/72398071/65a30f5f-ce82-49ae-aa67-f979c40be352)

## Credits

The AE86 sprite has been created by [u/cropmania](https://www.reddit.com/user/cropmania/).\
This environment was created as part of the Fachprojekt [Applied Deep Reinforcement Learning](https://ai.cs.tu-dortmund.de/teaching/bsc-fachprojekte/applied-deep-reinforcement-learning/) at TU-Dortmund.