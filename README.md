# bout-forge
 Easily organize fencers and teams for fencing tournaments, optimizing fencer placement based on preferences and skill levels

## Set the project's Python venv
To get your project to correctly resolve (import) installed python packages while using the flexibility of Pyenv, Poetry, and VS Code, follow these steps:
1. `pyenv install 3.12.1`
1. `pyenv global 3.12.1`
1. `poetry env use "$(pyenv which python)"`
1. Select the correct Python interpreter (VS Code)
    1. `Ctrl + Shift + P`, `"Python: Select Interpreter"`
    3. Click the refresh icon if the Poetry venv for the Python version isn't showing.
    3. Select the **Poetry** venv for the appropriate Python version. Do not select any Pyenv options, your packages will not resolve correctly!
    - If your package `import`s, (e.g. `import pandas`), produce the warning that they can't resolve from source (can't find the package's install location in the targeted venv), simply change the Python interpreter to anything else, then change it back. This force updates the package resolution paths and should fix the issue. Sometimes the paths can get stuck incorrectly pointing to the Pyenv venv. 
1. [Poetry docs](https://python-poetry.org/docs/managing-environments#managing-environments) if you experience problems.
