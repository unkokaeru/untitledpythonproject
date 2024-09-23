#!/bin/bash -e

# This script takes care of:
# 1. Updating the version number in the pyproject.toml file
# 2. Generating a new changelog based on the commit history
# 3. Committing the changes to the git repository
# 4. Creating a new tag for the release
# 5. Building the package
# 6. Publishing the package to PyPI

# The script takes the type of version to release ('major', 'minor', or 'patch') as an argument.
# It is incompatible with pre-release versions for simplicity.

# This script requires both Poetry and git to be installed and configured on the system,
# including authentication for pushing to the remote repository and publishing to PyPI.

# Check if the git repo has any uncommitted changes
if [[ -n $(git status --porcelain) ]]; then
    echo "There are uncommitted changes in the git repository. Please commit or stash them before releasing."
    exit 1
fi

# Check if an argument was passed
if [ -z "$1" ]; then
    echo "No version type supplied. Please specify 'major', 'minor', or 'patch'."
    exit 1
fi

# Validate the argument as a version type
if [[ "$1" != "major" && "$1" != "minor" && "$1" != "patch" ]]; then
    echo "Invalid version type. Please specify 'major', 'minor', or 'patch'."
    exit 1
fi

# Get the current script's directory
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Ensure requirements.txt files are up to date
"$SCRIPT_DIR/export_requirements.sh"

# Clear the current changelog - it gets regenerated fully on each release
echo '' > CHANGELOG.md

# Update the changelog
gitchangelog > CHANGELOG.md
git add CHANGELOG.md
git commit -m "Update CHANGELOG.md"

# Get the current version number
current_version=$(poetry version -s)

# Update the version number using poetry
poetry version "$1"

# Get the new version number
new_version=$(poetry version -s)

# Update __init__.py version numbers
find source -type f -name "__init__.py" -exec sed -i "s/__version__ = \"$current_version\"/__version__ = \"$new_version\"/g" {} \;

# Update the version number in the git repo
git add .
git commit -m "Bump version: $current_version -> $new_version"

# Create a new tag and push it to the remote repository
git tag -a "v$new_version" -m "Release $new_version"

git push --follow-tags

# Build the package for PyPI
poetry build

# Publish the package to PyPI
poetry publish