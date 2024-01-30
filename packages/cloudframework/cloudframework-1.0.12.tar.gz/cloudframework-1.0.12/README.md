# appengine-python-core-3.9

CloudFramework for Appengine using python language.

## REQUIREMENTS:

1. Install Python3: https://cloud.google.com/python/docs/setup#installing_python
2. Add to your path: /usr/local/opt/python@3.9/libexec/bin
3. Verify version

Example for MAC environment
```
# Add path of python
echo 'export PATH="/usr/local/opt/python@3.9/libexec/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# verify version
python --version
[Python 3.11.5]

pip --version
[pip 23.3.2]
```

## Creating you development environment

Create your working directory
```
mkdir your-python-project
cd your-python-project
```

Create a virtual environment. It will create a 'env' folder where your libraries will be stored.
```
python -m venv env
source env/bin/activate
# execute 'deactivate' to exit the virtual environment
```

install cloudframework library
```
pip install cloudframework
```

copy the basic files to start working with your APIs developed in python
```
cp env/lib/python3.11/site-packages/cloudframework/python-dist/main.py .
```

Now you have the following structure of files:
```
 - main.py           (main file to run your project)
 - config.json       (cloudframework config file. Intially empty
 - requirements.txt  (packages required when you deploy)
 - api/hello.py      (example of your first API Hellow world)
```

### Running you development environment
Be sure you have activated your virtual environment: `source env/bin/activate`
```
python main.py
# now you can go to: http://localhost:8080/hello
```
