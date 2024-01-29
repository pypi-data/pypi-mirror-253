# loadingpy

In this repository, we provide a custom made progress bar for python iterables. This library can be used as is or modified for any purposes (see licence).

## for deep learning

There is now a new progress bar available for deep learning purposes (I guess it could be leveraged for other stuff as well...). Say, you want to train a model using a dataset $D$ over $e$ epochs. Using `TrainBar`you can get a double progress bar (first for the epochs and second for the steps in the current epoch) on a single line. you can check the [test](tests/test_loadingpy.py) or this simple example:

```python
from loadingpy import TrainBar

for data in TrainBar(
        trainloader,
        num_epochs=e,
        base_str="training",
    ):
        inputs, labels = data
```

## Example
You can install with pip `pip install loadingpy` and use as follows

```python
from loadingpy import PyBar

loss = 0.0
accuracy = 0.0
for inputs, labels in PyBar(dataset, monitoring=[loss, accuracy], naming=["loss", "accuracy"], base_str="training"):
    # do whatever you please
    loss += 0.0 # update monitoring variables in place
    accuracy += 0.0 # update monitoring variables in place
```

For a more detailed exampel (in torch) check this [tutorial](https://gitlab.com/ey_datakalab/loadingpy/-/blob/main/notebooks/unit_test.ipynb). You can use a global argument in order to disable the verbatim from the loading bars as follows:

```python
from loadingpy import BarConfig

BarConfig["disable loading bar"] = True
```

## Arguments

Here is a list of the arguments and their description
| argument | description | type |
| :---: | :---: | :---: |
| iterable | python object that can be iterated over | can be a list, tuple, range, np.ndarray, torch.Tensor, dataset,... |
| monitoring | a python object (or list of python objects) that will be printed after each iteration using the following format f'{monitoring}'. IF they are updated during the loop, make sure to update inplace, in order to see the changes | an be a tensor, float or list of these |
| naming | if you want to add a descritpion prefix to the monitoring variables | str or list of str |
| total_steps | number of iterations to perform (if you set it to a lower value than the length of the iterable, then the process will stop after the given total_steps) | int |
| base_str | prefix description of the loop we are iterating over | str |
| color | which color to use for the loading bar | str |