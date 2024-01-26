# PyAWD: a Python acoustic wave propagation dataset using PyTorch and Devito
A package for generating a Pytorch dataset containing simulations of the acoustic wave propagation in the Marmousi velocity field. It uses the [Devito Python Library](https://www.devitoproject.org) to solve the acoustic wave PDE from various random initial conditions.

## Marmousi velocity field
The Marmousi velocity field used in the simulation is a subset of the following:
<img src="https://slideplayer.com/slide/15021598/91/images/37/Marmousi+Velocity+Model.jpg" alt="Marmousi velocity field" width="40%"/>

## Installation
The package (along with the dependencies) is accessible via [PyPI](https://pypi.org):

```bash
pip install pyawd
```

## Getting started

Basic imports:
```python
import PyAWD
from PyAWD.AcousticWaveDataset import AcousticWaveDataset
```

Let us generate a Dataset made of 10 simulations. Each simulation is run in a $250\times 250$ matrix. We store the field state every $2$ seconds and we run the simulation for $10$ seconds:

```python
dataset = AcousticWaveDataset(2, nx=250, dt=2, t=10)
```

Then we plot the first simulation:

```python
dataset.plot_item(0)
```

Which outputs the following figure:
![Example of simulation output](https://github.com/pascaltribel/PyAWD/tree/main/examples/examples/example.png)

Finally, we can generate a video of this simulation. We will use $240$ frames, so that we have a final rate of $24 fps$:

```python
dataset.generate_video(0, "example", 240)
```


This produces the following video (stored in the file `example.mp4`):

<img src="https://github.com/pascaltribel/PyAWD/tree/main/examples/example.gif" alt="Example of simulation video" width="40%"/>

## Documentation
Basic help is provided for each class and function, and is accessible via the Python `help()` function.

## Examples
Mutliple IPython notebooks are presented in the [examples](examples/) directory. If [Jupyter](https://jupyter.org) is installed, those examples can be explored by starting Jupyter:

```bash
jupyter-notebook
```

- `HeatPropagation.ipynb`: an introduction to PDE solving and simulation using Devito applied on the heat propagation
- `AcousticWaveGeneration.ipynb`: an introduction to PDE solving and simulation using Devito applied on the acoustic wave propagation
- `Marmousi.ipynb`: a visualisation of the Marmousi velocity field used in the simulations
- `GenerateAcousticWaveDataset.ipynb`: an example of dataset generation workflow
