# MineSweeper
## CSC 481 - Knowledge Based Systems at Cal Poly - taught by Dr. Rodrigo Canaan
[![PyPI](https://img.shields.io/pypi/v/minesweeper.svg?maxAge=2592000)](https://github.com/duguyue100/minesweeper)
[![PyPI](https://img.shields.io/pypi/pyversions/minesweeper.svg?maxAge=2592000)](https://github.com/duguyue100/minesweeper)

[![Build Status](https://travis-ci.org/duguyue100/minesweeper.svg?branch=master)](https://travis-ci.org/duguyue100/minesweeper)
[![Build status](https://ci.appveyor.com/api/projects/status/p8xuedefg61yia02?svg=true)](https://ci.appveyor.com/project/duguyue100/minesweeper)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8ad343ff420a42ba9130c822fa154557)](https://www.codacy.com/app/duguyue100/minesweeper?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=duguyue100/minesweeper&amp;utm_campaign=Badge_Grade)
[![license](https://img.shields.io/github/license/duguyue100/minesweeper.svg?maxAge=2592000)](https://raw.githubusercontent.com/duguyue100/minesweeper/master/LICENSE)

A python Minesweeper implementation with interfaces for machine learning.

## How to Install

To download the necessary dependencies, run the following command:

pip install requirements.txt

## How to Run

To run the machine learning solvers, walk through the jupyter notebook found at minesweeper_solver.ipynb. This notebook goes through extracting datasets, training models as well as simulating games. To see a visual simulation of the minesweeper solver, run ms-gui.py and subsequently run the notebook runGui.ipynb. You will see a popup game appear with the solver making moves every 0.5 seconds. 

## The Minesweeper game

The minesweeper interface is implemented in the minesweeper_game folder. It contains scripts to run the game through command line, a python interface or through tcp ip. It is based off the implementation here: https://github.com/duguyue100/minesweeper

## Machine Learning approach to solve Minesweeper

The machine learning implementation is explored in minesweeper_solver.ipynb. We implemented several feature extraction methods to derive datasets. We then train and tune decision tree models to solve the minesweeper game. Once we train the machine learning models, we simulate them over hundreds of games to see how effective they are. The analytics are presented at the bottom. 

### Methods

The first method we explored is a basic feature extractor, which simply uses the minesweeper grid as a feature map. The second feature extractor expands on this by taking the minesweeper grid and deriving an indicator of how likely it is a bomb. The last methods uses a probability map to calculate the actual likelihood the square is a bomb. We use these feature extractors to collect large datasets to train the decision trees. When simulating the model in a minesweeper game, we run every potential move through the decision tree and let the model decide which move is least likely a bomb. 

## Algorithmic approach to solve Minesweeper

The algorithmic approach to solve minesweeper is implemented in minesweeper_solver. This solution is based off the implementation from https://github.com/JohnnyDeuss/minesweeper-solver. 

### How it works
This solver uses two approaches in sequence to solve the problem. The first approach is the very basic counting approach, where the number of known mines next to a number is subtracted from that number. If the reduced number is 0, then all unopened neighbors are opened. If the reduced number is equal to the number of unopened neighbors, then all those neighbors are flagged. This simple approach is run first because it efficiently deals with trivial cases, reducing the cost of running the second approach, not only by solving trivial squares but also by potentially breaking up the boundary into disconnected components.

The second approach is more expensive and can compute the exact probability of all unknown squares in the boundary. The steps this approach takes are as follows:

Divide the unknown boundary into disconnected components.
Divide the components into areas, each area is a group of squares to which the same constraints apply, i.e. two squares that are both next to only the same 1 and 3. Thinking in constrained areas rather than individual cells allows for massive performance improvements in the CLP step, because we don't care about the exact assignment of mines, just about the amount in an area.
Use constraint programming to find all valid models assigning a number of mines to each area.
Combine model counts and probabilities of each area into aggregated counts and probabilities for the component.
Combine the components and again aggregate the model counts and probabilities, then weigh the probabilities by the model counts.
For more detail, please reference the code and the more elaborate explanation in the comments of minesweeper_solver/solver.py.



## Images and Videos

Images containing analytics can be found in the /images folder.
Videos of simulating the game with agents can be found in the /videos folder.
