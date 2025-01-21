# Colour Changer

This is a simple Python application that allows users to change the background colour of a window using either a randomly generated colour or a user-specified hex colour code.

## Features

- Change the background colour to a random colour by clicking a button.
- Change the background colour to a user-specified hex colour code by entering the code and clicking a button.
- Displays the current colour in a label.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## Usage

1. Clone the repository or download the `colours.py` file.
2. Run the `colours.py` file using Python:

    ```sh
    python colours.py
    ```

3. A window will appear with the following elements:
    - A label displaying "Hello World".
    - A button labeled "Click for Random Colour" to change the background to a random colour.
    - An entry field to input a hex colour code.
    - A button labeled "Change Colour" to change the background to the specified colour.

## Example

!Example

## Code Overview

The main class in the application is [ColourChanger](http://_vscodecontentref_/1), which initializes the Tkinter window and its widgets. It includes methods to handle random colour generation, colour validation, and changing the background colour.

- [random_colour_change](http://_vscodecontentref_/2): Changes the background to a random colour.
- [colour_change](http://_vscodecontentref_/3): Changes the background to the user-specified colour if valid.
- [generate_random_colour](http://_vscodecontentref_/4): Generates a random hex colour code.
- [is_valid_colour](http://_vscodecontentref_/5): Validates the user-specified hex colour code.

## License

This project is licensed under the MIT License.