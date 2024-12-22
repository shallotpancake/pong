# Pong Game

A simple Pong game implementation in Python.

## Building Executables

You can create standalone executables for different platforms using PyInstaller.

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Installation
```bash
pip install pyinstaller
```

### Building Instructions

1. For Linux:
```bash
pyinstaller --onefile pong.py
```

2. For Windows:
```bash
pyinstaller --onefile pong.py
```

3. For macOS:
```bash
pyinstaller --onefile pong.py
```

The executable will be created in the `dist` directory. Note that you should build on each target platform for best compatibility.

## Running the Game

### From Source
```bash
python pong.py
```

### From Executable
Simply run the executable file created in the `dist` directory:
- Linux/macOS: `./dist/pong`
- Windows: `dist\pong.exe`
