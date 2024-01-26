from setuptools import setup, find_packages

# Function to read the list of dependencies from requirements.txt
def read_requirements():
    with open('./requirements.txt') as req:
        return req.read().splitlines()


# Function to read the README file
def read_readme():
    with open('README.md', 'r') as readme:
        return readme.read()

setup(
    name='codara-model-trainer',
    version='2.0.0',
    packages=find_packages(),
    description="OpenAI Model Trainer and Formatter",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
)
