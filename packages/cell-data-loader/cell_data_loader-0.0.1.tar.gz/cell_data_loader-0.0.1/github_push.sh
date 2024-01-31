#!/bin/bash

#git init
git add README.md example_numpy.py example_torch.py src tests requirements.txt
git commit -m "First commit"
git branch -M main
git remote add origin https://github.com/mleming/CellDataLoader.git
git push -u origin main
