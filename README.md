# The great TRP: Neural Networks Visualization & Analysis
This repository contains the work produced for our tutored research project, carried over the Fall semester of the 2017/2018 university year, for the IPCV Master 2.
The project consisted in two main parts:
- The development of a library that would allow its users to visualize the decision boundaries of an input neural network.
- A comparative study of deep neural networks and shallow neural networks: our instinct tends to tell us that a deeper network will generally perform better than a shallower network for the same number of neurons. Experimentally, we tried to see if that instinct was right or not.

## Pear, a visualization library
To fulfill the first part of the project, we wrote a Python library, Pear, that can be found in the `pear` directory. Downloading this directory, you can locally install Pear by doing:
```
cd pear
pip3 install .
```
Pear will soon be available on PyPI as well.
Pear can only take TensorFlow files as inputs. Networks created with any other frameworks will not be read by Pear (sorry). Specificities of the input files will later be described.

Moreover, to make the library easy to use for people who are not necessarily familiar with coding, we build a Graphical User Interface that wraps it up. The GUI can be found in `GUI` directory. To run it, just do: 
```
python3 main.py
```
An executable (hopefully cross-platform) will soon be available.

## Comparison between deep and shallow networks: a story of depth
For this comparison, we ran networks with different layers and different number of parameters and tried, from the results, to get insights as to which type of network tends to perform better. (spoilers: it seems to be the deeper ones)

The results of those runs can be found in the `Results` directory.
