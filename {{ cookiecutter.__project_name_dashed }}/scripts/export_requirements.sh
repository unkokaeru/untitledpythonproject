#!/bin/bash

# This script takes care of exporting the project requirements to requirements.txt files
# for different groups defined in the pyproject.toml file.

# Ensure the poetry lock file is up to date
echo "Making sure lock file is up to date..."
if ! poetry lock; then
    echo "Failed to update the lock file. Aborting."
    exit 3
fi

# Check if there are changes to commit
if [[ -n $(git status --porcelain) ]]; then
    echo "Committing changes to the lock file..."
    git add poetry.lock
    git commit -m "chore: update lock file"
else
    echo "No changes to commit for the lock file."
fi

# Export the base project requirements poetry into requirements.txt format.
echo "Exporting main requirements..."
if ! poetry export --format=requirements.txt \
    --only="main" \
    --without-hashes \
    --output="requirements.txt"; then
    echo "Failed to export main requirements. Aborting."
    exit 4
fi

# Define the extra group dependencies
declare -a arr=("dev" "types" "test" "docs" "release")

for group in "${arr[@]}"
do
    echo "Exporting $group requirements..."
    if ! poetry export --format=requirements.txt \
        --without-hashes \
        --only="$group" \
        --output="requirements-$group.txt"; then
        echo "Failed to export $group requirements. Aborting."
        exit 4
    fi
done

echo "All requirements exported."

if [[ -n $(git status --porcelain) ]]; then
    git add "requirements*.txt"
    git commit -m "chore: update requirement files"
else
    echo "No changes to commit for requirements files."
fi

return 0  # Success but don't exit the script, as it is sourced by another script