"""Pytest configuration for the tools/ directory.

The modules under tools/ are standalone scripts, not an installed package, so
tests import them by bare name (e.g. `from fetch_model_data import ...`).
Putting this directory on sys.path here, once, lets every test module in
tools/ do that without each one repeating its own sys.path.insert boilerplate.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
