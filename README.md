# bootcamp_tejas_pandya

# Bootcamp Repository
## Folder Structure
- **homework/** → All homework contributions will be submitted here.
- **project/** → All project contributions will be submitted here.
- **class_materials/** → Local storage for class materials. Never pushed to
GitHub.

## Homework Folder Rules
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Include all required files for grading.
## Project Folder Rules
- Keep project files organized and clearly named.

## Data Storage
- **Folder Structure:**
    - data/raw
    - data/processed
- **Formats used and why?**
    - CSV:
        1. human-readable
        2. file size is large compared to Parquet
        3. use-case: basic and better for small to medium data size
    - Parquet:
        1. faster loading and reading time
        2. file size is very small compared to CSV
        3. use-case: for storing large scale data

## env Variables
- raw and processed data paths are stored in .env, making it more portable and secured
- api_keys are also stored in the .env file
- .env.example file is stored in the repo for easy replication of .env file