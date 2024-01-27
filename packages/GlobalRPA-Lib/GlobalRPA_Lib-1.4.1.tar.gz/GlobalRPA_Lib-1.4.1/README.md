# RPA Library Documentation

## Folder Structure

The RPA Library follows a simplified structure with modules directly in the main directory. The current structure is as follows:

### 1. GlobalEmail

- **File Name:** `GlobalEmail.py`
- **Description:** Contains functionalities related to email automation.

### 2. GlobalFiles

- **File Name:** `GlobalFiles.py`
- **Description:** Includes file-related automation capabilities.

### 3. GlobalTables

- **File Name:** `GlobalTables.py`
- **Description:** Includes table-related automation capabilities.

### 4. GlobalUi

- **File Name:** `GlobalUi.py`
- **Description:** Houses functionalities for UI automation.

This new structure aims for simplicity, with all modules directly accessible in the main directory.

## Global Environment

- **Virtual Environment for the RPA Library:** `env_global_rpa_lib`

## Installation Instructions

To install dependencies for each module, use the respective virtual environments. For example, for the `email` module:

```bash
pip install -r email/requirements.txt
```

Repeat the same process for the file and selector modules.

## Global RPA Library

To install global dependencies for the entire RPA Library, you can use the provided `env_global_rpa_lib` virtual environment. Run the following command:

```bash
pip install -r env_global_rpa_lib/requirements.txt
```

## Usage

After installing the required dependencies, you can use the RPA Library modules in your Python script as follows:
```bash
pip install GlobalRPA-Lib
```

```python
from GlobalRPA_Lib import GlobalEmail, GlobalFiles, GlobalTables, GlobalUi
```