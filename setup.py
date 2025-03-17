from setuptools import setup, find_packages

setup(
    name="my_project",  # Replace with your project name
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List dependencies here, example:
        "requests",
        "flask"
    ],
    entry_points={
        "console_scripts": [
            "my_project=app.py.main:main",  # Replace with actual entry point
        ],
    },
)
