#! /bin/bash
conda activate ds_env
conda install -c anaconda ipykernel
conda install -c anaconda ipywidgets
python -m ipykernel install --user --name ds_env --display-name "Python (ds_env)"