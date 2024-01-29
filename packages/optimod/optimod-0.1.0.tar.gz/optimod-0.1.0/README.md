# Optimod

Optimod is an innovative Python package designed to streamline Python project development. It automatically scans your Python project, identifies missing modules, installs them, and generates a `requirements.txt` file. This tool is ideal for Python developers looking to automate the setup of their development environment and ensure consistency across different setups.

## Features

- **Automatic Module Detection**: Scans your Python project files to detect import statements and identifies any missing modules.
- **Module Installation**: Automatically installs the detected missing modules.
- **Requirements File Creation**: Generates a `requirements.txt` file, listing all the installed modules with their respective versions, ensuring easy replication of the environment.

## Installation

To install Optimod, simply run the following command in your terminal:

```bash
pip install optimod
```

## Usage

Using Optimod is simple and efficient. To run Optimod on your Python project, activate your virtual environment and specify the path to your project directory in the following manner:

```bash
optimod /source/to/project
```
