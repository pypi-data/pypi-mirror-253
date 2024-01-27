# Super Brownian Motion Simulation

![Super Brownian Motion](./examples/branching_brownian_motion_500_0.5_1.0_12.gif)

## Introduction

This Python script simulates super Brownian Motion (SBm), a stochastic process
where particles move randomly and branch under certain conditions. The script
offers functionalities to simulate the motion, plot the paths, save the images,
export the data, and generate an animation of the process in the gif format.

* Currently, all paths will branch or die after every fixed number of steps (default 100). More flexibility will be added in the future.

## Requirements
- Python 3
- NumPy
- Matplotlib

## Installation
Ensure you have Python 3 installed. You can install the required packages using pip:
```bash
pip install git+https://github.com/yourusername/mypackage.git
```
or from [pypi](https://pypi.org/project/simulation-super-brownian-motions/) 
```bash
pip install simulation-super-brownian-motions
```

## Usage
### Command line
To run the simulation with default parameters, simply execute the script:
```bash
SuperBm --help
```

#### Command Line Arguments
You can customize the simulation using the following command line arguments:
- `-s` or `--seed`: Random seed (default: 42), set to `-1` for random seed based on current time (for random outcome)
- `-n` or `--num-steps`: Number of steps in the simulation (default: 301)
- `-u` or `--update-steps`: Number of steps between branching events (default: 100)
- `-p` or `--branching-prob`: Probability of branching at each step (default: 0.5)
- `-c` or `--scale`: Scale of the Brownian motion (default: 10.0)
- `-d` or `--dpi`: DPI parameter for the animation (default: 150)
- `-a` or `--save-animation`: Save the animation as a GIF

#### Example
```bash
SuperBm --num-steps 500 --branching-prob 0.7 --scale 15
```
This command runs the simulation with 500 steps, a branching probability of 0.7, a Brownian motion scale of 15, and with default values for the other parameters. The animation won't be saved as a GIF.

If you want the animation, run the following command:
```bash
SuperBm --num-steps 500 --branching-prob 0.7 --scale 15 --save-animation
```

### Output
- The script will plot the paths of the Brownian motion.
- Paths will be exported as a CSV file.
- The plot will be saved as files in both PNG and JPET formats.
- With additional argument `-a` or `--save-animation`, the script will generate an animation of the process and save it as a GIF file.

## Within Python as a Module
You can use the script within Python as a module. The following example shows how to run the simulation with default parameters:
```python
import simulation_super_brownian_motions.super_bm_simulation as sbm

# Create an instance of the class
instance = sbm.Branching_BM()

# Use the instance and its methods
instance.simulate()
instance.plot_paths()
```

## Contributing

Contributions to this project are welcome! Please feel free to submit pull
requests or open issues to discuss potential improvements or features.

## Acknowledgments

Thanks for helpful discussions with Yumin Zhong and Panqiu Xia from Auburn University.

## License

* [MIT](./LICENSE)
