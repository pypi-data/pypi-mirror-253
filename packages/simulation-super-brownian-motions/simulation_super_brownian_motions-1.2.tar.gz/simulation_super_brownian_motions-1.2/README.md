# Super Brownian Motion Simulation

![Super Brownian Motion](./examples/branching_brownian_motion_500_0.5_1.0_12.gif)


## Introduction

This Python script simulates super Brownian Motion (SBm) in R, a stochastic
process where particles move randomly and branch under certain conditions. The
script offers functionalities to simulate the motion, plot the paths, export
the data, and generate an animation of the process.

* Currently, all paths will update every 100 steps. More flexibility will be added in the future.
* At each 100 steps, each path will branch to two or die with the prescribed probability.

## Requirements
- Python 3
- NumPy
- Matplotlib

## Installation
Ensure you have Python 3 installed. You can install the required packages using pip:
```bash
pip install git+https://github.com/yourusername/mypackage.git
```
or
```bash
pip install simulation-super-brownian-motions
```

## Usage
To run the simulation with default parameters, simply execute the script:
```bash
SuperBm --help
```

### Command Line Arguments
You can customize the simulation using the following command line arguments:
- `-s` or `--seed`: Random seed (default: 42)
- `-n` or `--num-steps`: Number of steps in the simulation (default: 301)
- `-p` or `--branching-prob`: Probability of branching at each step (default: 0.5)
- `-c` or `--scale`: Scale of the Brownian motion (default: 10.0)
- `-d` or `--dpi`: DPI parameter for the animation (default: 150)
- `--save-animation`: Save the animation as a GIF

### Example
```bash
SuperBm --num-steps 500 --branching-prob 0.7 --scale 15
```
This command runs the simulation with 500 steps, a branching probability of 0.7, a Brownian motion scale of 15, and with default values for the other parameters. The animation won't be saved as a GIF.

If you want the animation, run the following command:
```bash
SuperBm --num-steps 500 --branching-prob 0.7 --scale 15 --save-animation
```

## Output
- The script will plot the paths of the Brownian motion.
- Paths will be exported as a CSV file named `positions_transposed.csv`.
- With additional argument `--save-animation`, the script will generate an animation of the process and save it as a GIF file.

## Contributing

Contributions to this project are welcome! Please feel free to submit pull
requests or open issues to discuss potential improvements or features.

## Acknowledgments

Thanks for helpful discussions with Yumin Zhong and Panqiu Xia from Auburn University.

## License

* [MIT](./LICENSE)
