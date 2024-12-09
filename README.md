# AutoClicker and Keypress Automation (with userdefined mouse click location)

This script automates keypresses and **mouse clicks at a userdefined place** at the display. It's designed to simulate the press of two customizable keys (key1 and key2) for random periods, followed by a mouse click at a place selected by the person. The script may be toggled on and off by the use of the "`~`" key.

## Features

- Automates the input of  keys (`key1` and `key2`) with random periods.
- Simulates mouse clicks at a position selected by way of the user.
- The script may be paused and resumed with the "`~`" key.
- Customizable to in shape distinctive keypresses or use cases.

## Requirements

Before running the script, you want to install the subsequent dependencies:

- `pyautogui` for automating keypresses and mouse clicks.
- `pynput` for listening to keyboard and mouse events.

## How to Use

1. **Run the Script:**
   - When you run the script, it'll ask you to click anywhere on the display to set the place where the mouse click on will occur.

2. **Customize the Keys:**
   - To trade the keys that the script presses, you could adjust the `key1` and `key2` variables at the start of the script. For example:
   
     ```python
     key1 = 'a'  # Set the first key to press
     key2 = 's'  # Set the second key to press
     ```
   
     Replace `'a'` and `'s'` with the keys you want the script to press.

3. **Toggle Autoclicker:**
   - Once the script is up and running, it's going to press the keys you place (`key1` and `key2`) for random periods, followed through a mouse click at the vicinity you selected.
   - You can toggle the autoclicker on and off by using pressing the "`~`" key on your keyboard.

4. **Stop script:**
   - To stop the script, just press `Ctrl + C` in terminal or close the terminal window.

## Code customization

You can edit the following variables to change the script's behavior.

- `key1` and `key2`: Keys that the script simulates pressing.
- `duration_key1` and `duration_key2`: The length of time each key is held. Currently, the script keeps each key for 0.4 to 0.75 seconds, but you can adjust the range by changing the values. `random.uniform(0.4, 0.75)`

For example:

``` python
Duration_key1 = Random.uniform(0.5, 1.0) # Adjust retention time key1
Duration_key2 = Random.uniform(0.5, 1.0) # Adjust key2 retention time
```

## Troubleshooting

- **Error: `pyautogui` or `pynput` is not installed:**  
  Make sure you have installed both libraries.

- **Error: Mouse click position not set:**  
  You must click anywhere on the screen when prompted to set the mouse click position before automatic clicking can be performed.

## License

This project is open source and available under the MIT license.

---
