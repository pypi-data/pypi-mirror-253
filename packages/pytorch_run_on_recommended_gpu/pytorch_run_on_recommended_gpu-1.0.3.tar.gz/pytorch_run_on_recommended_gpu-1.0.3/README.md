# pytorch_run_on_recommended_gpu

A lightweight script that interactively updates `CUDA_VISIBLE_DEVICES` for pytorch
## Install

`pip install pytorch_run_on_recommended_cuda`

## Usage from CLI

Perform a dry run

`pytorch_run_on_recommended_cuda`


Run a script and select a GPU manually

`pytorch_run_on_recommended_cuda <path_to_script>`



Run a script from the next available GPU

`pytorch_run_on_recommended_cuda --select * <path_to_script>`


Run a script from the next two available GPUs

`pytorch_run_on_recommended_cuda --select ** <path_to_script>`


Run a script from GPU ids 6 and 7

`pytorch_run_on_recommended_cuda --select 6 7 <path_to_script>`


## Usage from .py file
```python
import os
from pytorch_run_on_recommended_gpu.run_on_recommended_gpu import get_cuda_environ_vars as get_vars

os.environ.update(get_vars('*')
print(get_vars('*')))
import torch # Import torch after you have updated the vars.
```