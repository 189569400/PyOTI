## Installation for Linux

Virtualenv (recommended):
```bash
# install/setup virtual environment
python3 -m pip install virtualenv
mkdir ~/python-venv && cd ~/python-venv
python3 -m venv pyoti
source ~/python-venv/pyoti/bin/activate
# clone PyOTI repository and copy sample keys file
git clone https://github.com/RH-ISAC/PyOTI ~/PyOTI
cd ~/PyOTI
cp examples/keys.py.sample examples/keys.py
# make sure to fill in your API secrets!
vim examples/keys.py
# install requirements and PyOTI library
python3 -m pip install -r requirements.txt
python3 -m pip install .
```
No virtualenv:
```bash
# clone PyOTI repository and copy sample keys file
git clone https://github.com/RH-ISAC/PyOTI ~/PyOTI
cd ~/PyOTI
cp examples/keys.py.sample examples/keys.py
# make sure to fill in your API secrets!
vim examples/keys.py
# install requirements and PyOTI library
python3 -m pip install -r requirements.txt
python3 -m pip install .
```
## Updating

Virtualenv:
```bash
# activate virtual environment
source ~/python-venv/pyoti/bin/activate
# pull PyOTI repository
cd ~/PyOTI
git pull
bash update_keys.sh 
# make sure to fill in your updated API secrets!
vim examples/keys.py
# make sure requirements and PyOTI library are updated
python3 -m pip install -r requirements.txt
python3 -m pip install .
```
No virtualenv:
```bash
# pull PyOTI repository
cd ~/PyOTI
git pull
bash update_keys.sh 
# make sure to fill in your updated API secrets!
vim examples/keys.py
# make sure requirements and PyOTI library are updated
python3 -m pip install -r requirements.txt
python3 -m pip install .
```