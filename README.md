HAT Admin Tool
=======

Install
-------

**Ubuntu/MacOSs**
```
git clone https://github.com/HDDcoin-Network/HAT-admin-tool.git
cd HAT-admin-tool
python3 -m venv venv
. ./venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install .
```
(If you're on an M1 Mac, make sure you are running an ARM64 native python virtual environment)

**Windows Powershell**
```
git clone https://github.com/HDDcoin-Network/HAT-admin-tool.git
cd HAT-admin-tool
py -m venv venv
./venv/Scripts/activate
python -m pip install --upgrade pip setuptools wheel
pip install .
```

Lastly this requires a synced, running light wallet
