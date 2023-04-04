import os

directories = [
    os.path.join("data", "raw"),
    os.path.join("data","processed"),
    "notebooks",
    "saved_models",
    "src"
]

for dirs in directories:
    os.makedirs(dirs, exist_ok=True)
    with open(os.path.join(dirs, ".gitkeep"), "w") as f:
        pass

files =  [ 
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py")
]

for fil in files:
    with open(fil, "w") as f:
        pass