#!/bin/bash -e

# This script takes care of:
# 1. Updating the version numbers across the project
# 2. Update requirements and their files across the project
# 3. Generating a new changelog based on the commit history
# 4. Committing the changes to the git repository
# 5. Creating a new tag for the release
# 6. Building the package
# 7. Publishing the package to PyPI

# The script takes the type of version to release ('major', 'minor', or 'patch') as an argument.
# It is incompatible with pre-release versions for simplicity.

# This script requires both Poetry and git to be installed and configured on the system,
# including authentication for pushing to the remote repository and publishing to PyPI.

# Error codes:
# 1 - Uncommitted changes in the git repository
# 2 - Invalid version type
# 3 - Failed to update the lock file
# 4 - Failed to export requirements
# 5 - Failed to pull the latest changes from the remote repository

# Check if the git repo has any uncommitted changes
if [[ -n $(git status --porcelain) ]]; then
    echo "There are uncommitted changes in the git repository. Please commit or stash them before releasing."
    exit 1
fi

# Check if an argument was passed
if [ -z "$1" ]; then
    echo "No version type supplied. Please specify 'major', 'minor', or 'patch'."
    exit 2
fi

# Validate the argument as a version type
if [[ "$1" != "major" && "$1" != "minor" && "$1" != "patch" ]]; then
    echo "Invalid version type. Please specify 'major', 'minor', or 'patch'."
    exit 2
fi

# Get the current script's directory
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Update requirements and their files
echo "Updating requirements and their files..."
poetry update
source "$SCRIPT_DIR/export_requirements.sh"
echo "Requirements and their files updated successfully."

# Clear the current changelog - it gets regenerated fully on each release
echo '' > CHANGELOG.md

# Update the changelog
echo "Generating a new changelog..."
gitchangelog > CHANGELOG.md
git add CHANGELOG.md
git commit -m "chore: update changelog"
echo "Changelog generated successfully."

# Get the current version number
current_version=$(poetry version -s)

# Update the version number using poetry
poetry version "$1"

# Get the new version number
new_version=$(poetry version -s)

# Update __init__.py version numbers
echo "Updating __init__.py version numbers to $new_version..."
find source -type f -name "__init__.py" -exec sed -i "s/__version__ = \"$current_version\"/__version__ = \"$new_version\"/g" {} \;
echo "__init__.py version numbers updated successfully."

# Update the version number in the git repo
echo "Committing version bump to the git repository..."
git add .
git commit -m "chore: bump version from $current_version to $new_version"
echo "Version bump committed successfully."

# Pull the latest changes from the remote repository
git config pull.rebase true  # Ensure that the pull is a rebase
echo "Pulling the latest changes from the remote repository..."
if ! git pull origin main; then
    echo "Failed to pull the latest changes from the remote repository."
    exit 5
fi

# Create a new tag and push it to the remote repository
echo "Creating a new tag for the release..."
git tag -a "v$new_version" -m "Release $new_version"
echo "Pushing the new tag to the remote repository..."
git push --follow-tags
echo "Release $new_version created successfully."

# Build the package for PyPI
echo "Building the package..."
poetry build
echo "Package built successfully."

# Publish the package to PyPI
echo "Publishing the package to PyPI..."
poetry publish
echo "Package published to PyPI successfully."