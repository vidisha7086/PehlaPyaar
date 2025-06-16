import os
#import pathlib as Path
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')

Project_Name = "textSummarizer"

List_of_files=['.github/workflows/gitkeep.py',
               f'src/{Project_Name}/__init__.py',
               f'src/{Project_Name}/entity/__init__.py',
               f'src/{Project_Name}/components/__init__.py'
               f'src/{Project_Name}/utils/__init__.py',
               f'src/{Project_Name}/utils/common.py',
               f'src/{Project_Name}/config/__init__.py',
               f'src/{Project_Name}/config/configuration.py',
               f'src/{Project_Name}/pipeline/__init__.py',
               f'src/{Project_Name}/logging/__init__.py',
               f'src/{Project_Name}/constants/__init__.py',
               'params.yaml',
               'config/config.yaml',
               'main.py',
               'setup.py',
               'Dockerfile',
               'requirement.txt',
               'research/stage1.ipynb'
               ]

for filepath in List_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    #os.makedirs(filedir)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"the file directory{filedir} and filename{filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"file is empty{filepath}")
            #os.makedirs(filedir)
        
    else:
        logging.info(f"file already exists {filename}")
