import os
from pathlib import Path

package_name="Thyroid Disease Detection"

list_of_files=[
    "github/workflows/.gitkeep",
    f"src/{package_name}/__pycache__",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/pipelines/Training_model.py"
    f"src/{package_name}/components/data_ingestion.py",
    f"src/{package_name}/components/application_logging",
    f"src/{package_name}/components/Training_logs",
    f"src/{package_name}/components/Best_model_finder",
    f"src/{package_name}/components/Data_preprocessing",
    f"src/{package_name}/components/Prediction_Logs",
    f"src/{package_name}/components/File_operations",
    f"src/{package_name}/components/Complete_notebook",
    f"src/{package_name}/pipelines/__init__.py",
    f"src/{package_name}/pipelines/training_pipeline.py",
    f"src/{package_name}/pipelines/prediction_pipeline.py",
    f"src/{package_name}/logger.py",
    f"src/{package_name}/",
    "procfile",
    
    "notebooks/research.ipynb",
    "notebooks/data/.gitkeep",
    "requirements.txt",
    "Input_filesfromUser"
    "Prediction_FilefromDB"
    "SchemaFiles"
    "SerializedModels"
    "Models"
    "Preprocessing_data"
    "app.py"
    "PredictFromModel.py"
    "init_setup.sh",
    "Encodelpickle"
    "CassandraOperations"
    
]


# here will create a directory

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    """ how exist_ok works:if "directory" already exists, 
    os.makedirs() will not raise an error, and it will do nothing. 
    If "my_directory" doesn't exist, it will create the directory.
    """
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
    else:
        print("file already exists")

# here will use the file handling