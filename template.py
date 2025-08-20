import os
import sys
import logging
import pathlib 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'HOUSE_PRICE_PREDICTIONS'

list_of_files = [
    'notebook/EDA.ipynb',
    'notebook/Evaluation.ipynb',
    'notebook/Trainer.ipynb',
    
    'src/components/__init__.py',
    'src/components/data_ingestion.py',
    'src/components/data_transformation.py',
    'src/components/model_trainer.py',
    
    'src/pipeline/__init__.py',
    'src/pipeline/predict_pipeline.py',
    'src/pipeline/train_pipeline.py',
    
    'src/templates/index.html',
    'src/templates/home.html',
    
    'src/__init__.py',
    'src/exception.py',
    'src/logger.py',
    'src/utils.py',
    
    '.gitignore',
    'app.py',
    'application.py',
    'README.md',
    'requirements.txt',
    'setup.py',
    
]

for file_path in list_of_files:
    file_path = pathlib.Path(file_path)
    file_dir, file_name = os.path.split(file_path)
    
    if(file_dir):
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f'Creating directory; {file_dir} for file: {file_name}')
        
    if(not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
            logging.info(f'creating empty file: {file_path}')
            
    else:
        logging.info(f'{file_name} Already exists!')
