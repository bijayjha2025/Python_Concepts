'''
Virtual Environment
A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages. It allows us to create isolated environments for different projects, so that you can manage dependencies and avoid conflicts between packages.
To create a virtual environment, we can use the venv module that comes with Python. We can create a virtual environment by running the following command in the terminal:
python -m venv myenv
'''

# Create a project directory with a virtual environment based on the example given above.

import os


os.makedirs("myproject", exist_ok=True)
os.chdir("myproject")
# Activate the virtual environment
# On Windows:
# myenv\Scripts\activate
# On macOS/Linux:
# source myenv/bin/activate