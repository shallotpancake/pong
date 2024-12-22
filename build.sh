#!/bin/bash

# Exit on error
set -e

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to install dependencies
install_deps() {
    echo "Checking and installing dependencies..."
    
    # Check if pip is installed
    if ! command_exists pip && ! command_exists pip3; then
        echo "Error: pip is not installed. Please install Python and pip first."
        exit 1
    fi
    
    # Use pip3 if available, otherwise use pip
    PIP="pip"
    if command_exists pip3; then
        PIP="pip3"
    fi
    
    # Install required packages
    echo "Installing required packages..."
    $PIP install pygame pyinstaller
}

# Function to clean previous builds
clean_build() {
    echo "Cleaning previous builds..."
    rm -rf build dist *.spec
}

# Detect OS
OS="unknown"
case "$(uname -s)" in
    Linux*)     OS="Linux";;
    Darwin*)    OS="Mac";;
    CYGWIN*|MINGW*|MSYS*) OS="Windows";;
esac

echo "Detected OS: $OS"

# Install dependencies
install_deps

# Clean previous builds
clean_build

# Build executable
echo "Building executable for $OS..."
case "$OS" in
    "Linux"|"Mac")
        pyinstaller --onefile pong.py
        echo "Build complete! Executable is at: dist/pong"
        echo "To run: ./dist/pong"
        ;;
    "Windows")
        pyinstaller --onefile pong.py
        echo "Build complete! Executable is at: dist\pong.exe"
        echo "To run: dist\pong.exe"
        ;;
    *)
        echo "Error: Unsupported operating system"
        exit 1
        ;;
esac

# Make the executable executable on Unix-like systems
if [ "$OS" = "Linux" ] || [ "$OS" = "Mac" ]; then
    chmod +x dist/pong
fi

echo "Build process completed successfully!"