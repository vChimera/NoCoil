# NoCoil

## Description

This is a private recoil script/macro that is designed to control recoil in all games.

This script utilizes the `keyboard` library to simulate mouse movement on Windows platforms.

## Features

- **Customizable Speed**: The movement speed can be adjusted by changing pressing the F1 key to increase strength and the F2 key to decrease strength.
- **Easy Start/Stop Mechanism**: The script is enabled when the user presses the F3 key and when the F3 key is pressed again the script is disabled.
- **Lightweight**: Runs in the background without requiring any game modifications.

### Install Required Libraries

To install the required libraries (`pywin32`, `keyboard`, `pyqt5`), you can use `pip`:

```bash
pip install pywin32, keyboard, pyqt5
```

## Usage

1. **Run the Script**: Execute the script in your terminal or IDE or use the run.bat file. The script will create a overlay at the top left of your screen.
   
   ```bash
   python NoCoil.py
   ```

2. **Start NoCoil**: Press F3 to enabled the script and then press F1 to increase the strength (it starts with 0 strength). Once the script is fully enabled simply hold down on the left mouse button and the cursor will move.

3. **Stop NoCoil**: Either release the left mouse button or simply press F3 to fully deactivate the script.

4. **Adjust Speed**: To adjust the recoil speed, simply press F1 to increase and F2 to decrease.

## Important Notes

- **Platform**: This script is specifically designed for Windows. If you are using another OS, you may need to modify the code to simulate mouse events.
- **Legal Considerations**: Make sure you are not violating any game rules or terms of service by using automation scripts like this.
