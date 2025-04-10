python -m venv ./venv
source ./venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
ipython kernel install --user --name=venv
