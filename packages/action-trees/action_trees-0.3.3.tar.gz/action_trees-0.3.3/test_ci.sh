#!/bin/bash

# Function to run pytest
run_pytest() {
    gitlab-runner exec docker pytest
}

# Function to run pages
run_pages() {
    gitlab-runner exec docker pages
}

run_package() {
    gitlab-runner exec docker package
}

# Check if an argument is provided
if [ "$#" -eq 1 ]; then
    # Run specific test based on the argument
    if [ "$1" == "pytest" ]; then
        run_pytest
    elif [ "$1" == "pages" ]; then
        run_pages
    elif [ "$1" == "package" ]; then
        run_package
    else
        echo "Invalid argument: $1. Valid arguments are 'pytest' or 'pages'."
        exit 1
    fi
else
    # If no argument is provided, run all tests
    run_pytest
    run_pages
    run_package
fi
