# Pong Game

A simple Pong game implementation in Python.

## Running from Source

### Prerequisites
- Python 3.x
- pip (Python package manager)
- Pygame (`pip install pygame`)

### Running
```bash
python pong.py
```

## Building Executables

PyInstaller can be used to create standalone executables. **Important**: You must build the executable on the target platform you want to run it on.

### Prerequisites
- Python 3.x
- pip (Python package manager)
- PyInstaller (`pip install pyinstaller`)
- Pygame (`pip install pygame`)

### Building Instructions

The process is the same for all platforms, but must be run on the target platform:

```bash
# On Linux/macOS:
pyinstaller --onefile pong.py

# On Windows (run in Command Prompt):
pyinstaller --onefile pong.py
```

The executable will be created in the `dist` directory:
- Linux: `dist/pong`
- macOS: `dist/pong`
- Windows: `dist\pong.exe`

### Platform-Specific Notes

1. **Windows**:
   - Build must be done on a Windows system
   - Run the command in Command Prompt or PowerShell
   - Resulting executable will have `.exe` extension

2. **Linux**:
   - Build must be done on a Linux system
   - Resulting executable has no extension

3. **macOS**:
   - Build must be done on a macOS system
   - Resulting executable has no extension
   - You may need to allow the app in Security & Privacy settings
