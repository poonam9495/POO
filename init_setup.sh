echo [$(date)]: "START"

echo [$(date)]: "creating env with python" 

conda create --prefix ./env python -y

echo [$(date)]: "activating the environment" 

source activate ./env

echo [$(date)]: "installing the dev requirements" 

pip install -r requirements.txt

echo [$(date)]: "END" 