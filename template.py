import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')

project_name = "textSummarizer"
list_of_files = [
    ".github/workflows/.gitkeep",  # will be used for CI/CD Deployment
    f"src/{project_name}/__init__.py",     # for making your folder as package
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",  # Here we will write all utilities
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",  # this will be for train and test pipelines
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",  # for all model related parameters
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",  
    "research/trails.ipynb"
]

# Loop through your files and create 
for filepath in list_of_files:
    # Convert path in specific format based on your system
    filepath = Path(filepath)
    # Split folder and file from name
    filedir, filename = os.path.split(filepath)
    # Check filedir is not empty
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # exist_ok will check if folder is already there
        logging.info(f"Creating Directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
