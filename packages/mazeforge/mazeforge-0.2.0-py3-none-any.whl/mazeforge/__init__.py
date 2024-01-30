"""
    MazeForge
    =========

    Provides
      1. Generation of mazes
      2. Solving of mazes
      3. Visualisation of mazes

    Contact
      - oskar.meyenburg@gmail.com

    More information
      - https://pypi.org/project/mazeforge/
      - https://github.com/oskarmeyenburg/mazeforge
"""
from .maze import generate, Maze

__version__ = "0.2.0"
__all__ = ['generate', "Maze"]
