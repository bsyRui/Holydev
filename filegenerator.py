import os

# Base project directory
project_name = "newproject"

# Folder structure to create
folders = [
    f"{project_name}/src/api",
    f"{project_name}/src/controllers",
    f"{project_name}/src/models",
    f"{project_name}/src/middleware",
    f"{project_name}/src/services",
    f"{project_name}/src/config",
    f"{project_name}/src/utils",
    f"{project_name}/frontend/public",
    f"{project_name}/frontend/src/components",
    f"{project_name}/frontend/src/pages",
    f"{project_name}/frontend/src/services",
    f"{project_name}/database/migrations",
    f"{project_name}/tests"
]

# Files to touch
files = [
    f"{project_name}/.env",
    f"{project_name}/.gitignore",
    f"{project_name}/README.md",
    f"{project_name}/package.json",
    f"{project_name}/docker-compose.yml",
    f"{project_name}/src/server.js",
    f"{project_name}/database/schema.sql",
    f"{project_name}/database/seed.js"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created folder: {folder}")

# Create files
for file in files:
    with open(file, "w") as f:
        f.write("")
    print(f"Created file: {file}")

print("\n✅ Project structure created successfully!")
