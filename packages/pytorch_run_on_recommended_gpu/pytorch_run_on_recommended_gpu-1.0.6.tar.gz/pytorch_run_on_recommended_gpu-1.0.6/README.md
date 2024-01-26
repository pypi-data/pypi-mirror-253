# pytorch_run_on_recommended_gpu

A lightweight script that interactively updates `CUDA_VISIBLE_DEVICES` for pytorch
## Install

`pip install pytorch_run_on_recommended_gpu`

## Usage from CLI

Perform a dry run

`pytorch_run_on_recommended_gpu`


Run a script and select a GPU manually

`pytorch_run_on_recommended_gpu <path_to_script>`



Run a script from the next available GPU

`pytorch_run_on_recommended_gpu --select * <path_to_script>`


Run a script from the next two available GPUs

`pytorch_run_on_recommended_gpu --select ** <path_to_script>`


Run a script from GPU ids 6 and 7

`pytorch_run_on_recommended_gpu --select 6 7 <path_to_script>`


## Usage from .py file
```python
import os
from pytorch_run_on_recommended_gpu.run_on_recommended_gpu import get_cuda_environ_vars as get_vars

os.environ.update(get_vars('*')
print(get_vars('*')))
import torch # Import torch after you have updated the vars.
```

## How it looks like

```
### Recommended gpus on this machine (descending order) ###
  ID  Card name                Util    Mem free  Cuda              User(s)
----  --------------------  -------  ----------  ----------------  ---------
   4  Tesla V100-SXM3-32GB      0 %   31889 MiB  11.8 (470.82.01)
   3  Tesla V100-SXM3-32GB      0 %   31887 MiB  11.8 (470.82.01)
   5  Tesla V100-SXM3-32GB      0 %   31737 MiB  11.8 (470.82.01)
   2  Tesla V100-SXM3-32GB      0 %   31341 MiB  11.8 (470.82.01)
   0  Tesla V100-SXM3-32GB      0 %   31263 MiB  11.8 (470.82.01)
   1  Tesla V100-SXM3-32GB      0 %   31038 MiB  11.8 (470.82.01)
  11  Tesla V100-SXM3-32GB      0 %   23012 MiB  11.8 (470.82.01)
   7  Tesla V100-SXM3-32GB      0 %   15481 MiB  11.8 (470.82.01)
  10  Tesla V100-SXM3-32GB     21 %    1025 MiB  11.8 (470.82.01)
   6  Tesla V100-SXM3-32GB     50 %   29296 MiB  11.8 (470.82.01)
   8  Tesla V100-SXM3-32GB     50 %   28988 MiB  11.8 (470.82.01)
   9  Tesla V100-SXM3-32GB     51 %   28988 MiB  11.8 (470.82.01)
  15  Tesla V100-SXM3-32GB   ! 99 %   22636 MiB  11.8 (470.82.01)
  13  Tesla V100-SXM3-32GB   ! 99 %   21441 MiB  11.8 (470.82.01)
  14  Tesla V100-SXM3-32GB  ! 100 %   22610 MiB  11.8 (470.82.01)
  12  Tesla V100-SXM3-32GB  ! 100 %   22141 MiB  11.8 (470.82.01)

Which GPUs shall be used? Give stars or ids. Input=* [ENTER]
```