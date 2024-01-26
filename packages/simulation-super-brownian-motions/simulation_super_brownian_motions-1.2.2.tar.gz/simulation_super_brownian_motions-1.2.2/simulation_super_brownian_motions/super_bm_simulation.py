#!/usr/bin/env python3
"""

Simulations for the branching Brownian motions.

It includes functionalities to:
- Simulate the motion
- Plot the paths
- Export the data
- Generate an animation of the process

By Le Chen and Chatgpt
chenle02@gmail.com / le.chen@auburn.edu
Created at Tue 23 Jan 2024 04:50:37 PM CST

Thanks Yumin Zhong (yzz0225@auburn.edu) and Panqiu Xia (pqxia@auburn.edu) for helpful discussions.
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
import argparse
import time
from datetime import datetime
# import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter


class Branching_BM:
    def __init__(self, num_steps=301, update_steps=100, branching_prob=0.5, scale=10, seed=42):
        """
        Initialize the Super Brownian Motion simulation.

        :param num_steps: Number of steps in the simulation
        :param branching_prob: Probability of branching at each step
        :param seed: random seed
        """
        self.num_steps = num_steps
        self.update_steps = update_steps
        self.branching_prob = branching_prob
        self.seed = seed
        self.positions = [np.zeros(num_steps)]
        self.scale = scale

        # Get the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Construct the name with the timestamp
        self.name = (f'SuperBm_'
                     f'Timestamp={timestamp}_'
                     f'NumSteps={num_steps}_'
                     f'UpdateSteps={update_steps}_'
                     f'BrachingProb={branching_prob}_'
                     f'GausianScale={scale}_'
                     f'RandomSeed={seed}')

        # Initialize some state variables
        self.path_length = [num_steps]  # num_steps means the path is still alive
        self.branch_from = [0]
        self.final_length = 0
        self.num_paths = len(self.positions)

        # Set ten colors for each potential path
        self.colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'yellow', 'pink', 'brown', 'grey']

        # Set the random seed
        np.random.seed(self.seed)

    def Branch_or_Die(self, path_id, step):
        """
        Update the specified path based on the branching and dying logic.

        This method applies the branching and dying logic to the path identified by path_id at the given simulation step. It determines whether the path should branch, continue, or die.

        :param path_id: The identifier of the path to be updated.
        :param step: The current step in the simulation process.
        :return: A boolean value; True if the path is still alive after this step, False if it has died.
        """
        alive = True
        if self.path_length[path_id] != self.num_steps:  # If path is dead, skip
            alive = False
            return alive

        action = np.random.choice(['branch', 'die'], p=[self.branching_prob, 1 - self.branching_prob])

        match action:
            case 'branch':
                self.positions.append(np.copy(self.positions[path_id]))  # Branching: duplicate the path
                self.path_length.append(self.num_steps)
                self.num_paths += 1
                self.branch_from.append(step - 1)
                self.One_Step(path_id, step)
                self.One_Step(self.num_paths - 1, step)
            case 'die':
                alive = False
                self.path_length[path_id] = step  # Dying: record the path length

        return alive

    def One_Step(self, path_id, step):
        """
        Go one step for a path.
        """
        self.positions[path_id][step] = self.positions[path_id][step - 1] + np.random.normal(scale=self.scale)

    def simulate(self):
        """
        Run the simulation of the Brownian motion with branching.
        """
        for step in range(1, self.num_steps):
            for path_index in range(len(self.positions)):
                if self.path_length[path_index] == self.num_steps:  # If path is alive, update
                    if step % self.update_steps == 0:
                        self.Branch_or_Die(path_index, step)
                    else:
                        self.One_Step(path_index, step)

    def plot_paths(self):
        """
        Plot all the paths of the Brownian motions.
        """
        fig, ax = plt.subplots()

        # Determine plot limits
        max_path_length = max(self.path_length)
        min_position = min(path.min() for path in self.positions)
        max_position = max(path.max() for path in self.positions)

        # Plot each path
        for i in range(self.num_paths):
            ax.plot(range(self.branch_from[i], self.path_length[i]), self.positions[i][self.branch_from[i]:self.path_length[i]], color=self.colors[i % len(self.colors)], label=f'Path {i+1}')
            plt.draw()
            plt.pause(1)

        # Set plot limits
        ax.set_xlim(0, max_path_length)
        ax.set_ylim(min_position, max_position)

        # Set title and labels
        ax.set_title("Super Brownian Motions")
        ax.set_xlabel("Step")
        ax.set_ylabel("Position")

        # List of formats to save the plot in
        formats = ['jpeg', 'png']

        # Saving the plot in the specified formats and preparing the message for the saved plot files
        print("Sample paths have been saved as the following image files:")
        for fmt in formats:
            filename = f'{self.name}.{fmt}'
            plt.savefig(filename, format=fmt)
            print(f"* {filename}")

        plt.show()

    def export_paths(self):
        """
        Export the paths in csv file.
        """
        # Assuming self.positions is a list of lists or a list of NumPy arrays
        filename = self.name + '.csv'
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)

            # Transpose and write to CSV
            for row in zip(*self.positions):
                writer.writerow(row)

        print(f"Sample paths have been saved as the following CSV file:\n * {filename}")

    def Animation(self, dpi=150):
        """
        Generate the animation of the branching Brownian motion.
        """
        print("Generating the animation... (This may take a while)")
        fig, ax = plt.subplots()

        # Determine plot limits
        max_path_length = max(self.path_length)
        min_position = min(path.min() for path in self.positions)
        max_position = max(path.max() for path in self.positions)

        # Set plot limits
        ax.set_xlim(0, max_path_length)
        ax.set_ylim(min_position, max_position)

        # Set title and labels
        ax.set_title("Super Brownian Motions")
        ax.set_xlabel("Step")
        ax.set_ylabel("Position")

        # Initialize lines for each path
        lines = [ax.plot([], [], color=self.colors[i % len(self.colors)], label=f'Path {i+1}')[0] for i in range(self.num_paths)]

        # Animation update function
        def update(frame):
            for i, line in enumerate(lines):
                if frame < self.path_length[i]:
                    line.set_data(range(self.branch_from[i], frame), self.positions[i][self.branch_from[i]:frame])
                    # line.set_data(range(frame + 1), self.positions[i][:frame + 1])
                else:
                    line.set_data(range(self.branch_from[i], self.path_length[i]), self.positions[i][self.branch_from[i]:self.path_length[i]])
            return lines

        # update(max_path_length)
        # update(2000)
        # for i in range(2000):
        #     update(i)
        #     plt.draw()
        #     plt.pause(0.001)

        # Create the animation using FuncAnimation
        anim = FuncAnimation(fig,
                             update,
                             frames=301,
                             interval=1,
                             blit=True)

        # Save the animation using PillowWriter
        # Form the filename using the parameters
        filename = self.name + '.gif'
        anim.save(filename, writer=PillowWriter(fps=60), dpi=300)
        print(f'Animation has been saved as the following GIF file:\n* {filename}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-s', '--seed', type=int, default=42, help="Random seed (use -1 for a random seed based on current time)")
    parser.add_argument('-n', '--num-steps', type=int, default=301, help="Maximum number of steps in the simulation")
    parser.add_argument('-u', '--update-steps', type=int, default=100, help="Number of steps between each branching event")
    parser.add_argument('-p', '--branching-prob', type=float, default=0.5, help="Probability of branching at each step")
    parser.add_argument('-c', '--scale', type=float, default=10.0, help="Scale of the Brownian motion")
    parser.add_argument('-d', '--dpi', type=float, default=150, help="The dpi parameter for the animation")
    parser.add_argument('-a', '--save-animation', action='store_true', help="Save the animation as a GIF")
    args = parser.parse_args()

    # Set the random seed
    if args.seed == -1:
        # Use the current time as the random seed for true randomness
        seed = int(time.time())
    else:
        # Use the provided seed for reproducibility
        seed = args.seed

    # Create an instance of the Branching_BM class
    BM = Branching_BM(num_steps=args.num_steps,
                      update_steps=args.update_steps,
                      branching_prob=args.branching_prob,
                      scale=args.scale,
                      seed=seed)

    # Run the simulation
    BM.simulate()

    # Export the paths
    BM.export_paths()

    # Plot the paths
    BM.plot_paths()

    # Save the animation if requested
    if args.save_animation:
        BM.Animation(args.dpi)


if __name__ == "__main__":
    main()
