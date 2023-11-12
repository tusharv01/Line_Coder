# Line_Coder
"Line Encoder generates digital signals with encoding options like NRZ-L, NRZ-I, Manchester, and more. User-friendly interface for signal manipulation and visualization."

# ITT305 Programming Assignment 1 - Line Coding Encoder and Scrambler

## Overview

This project involves implementing a Line Coding Encoder and Scrambler with a digital data generator. The assignment includes the generation of a random data sequence, encoding using various line coding schemes (NRZ-L, NRZ-I, Manchester, Differential Manchester, AMI), and optional scrambling using B8ZS or HDB3. The code also identifies the longest palindromic sequence in the generated data.

# Line Encoder GUI

This is a Line Encoder GUI implemented using PySimpleGUI, Matplotlib, and NumPy. It provides an interface for encoding and decoding various line encoding schemes.

## How to Run

1. Install the required libraries:
   ```bash
   pip install PySimpleGUI matplotlib numpy
  

Features:
Initialize random input data.
Enter custom input data.
Encode and decode data using various line encoding schemes.
Display the encoded and decoded data.
Plot graphs for input, encoded, and decoded data.
Line Encoding Schemes
Polar NRZ-L
Polar NRZ-I
Manchester
Polar RZ
AMI
Scrambling AMI B8ZS (Bipolar with 8 zero substitution)
Differential Manchester
Scrambling AMI HBD3 (High-Density Bipolar 3 Zeros)
PCM (Pulse Code Modulation)
Delta Modulation


**How to Use**
Launch the GUI.
Initialize random input or enter custom input.
Encode the data using a selected encoding scheme.
Optionally, decode the encoded data.
Visualize the input, encoded, and decoded data using the "Show Graph" button.
Examples
Initializing Random Input
Random Input

Entering Custom Input
Custom Input

Encoding and Decoding

## How to Run the Code

1. Ensure you have Python installed on your machine.
2. Clone the repository:

    ```
   https://github.com/tusharv01/Line_Coder.git
    ```

3. Navigate to the project directory:

    ```
    cd Line_Coder
    ```

4. Run the main program:

    ```
    python LineEncoder.py
    or using the LineEncoder.ipynb file run the program using juptyer notebook and dialog box opens on which you can operate.
    To run an iPython Notebook (.ipynb file), you typically use a Jupyter Notebook server.```


## Here's a step-by-step guide:
Using Jupyter Notebook (Local Installation):
Install Jupyter Notebook:
If you don't have Jupyter Notebook installed, you can install it using:

```pip install notebook```
Navigate to the Directory Containing the .ipynb File:
Open a terminal, navigate to the directory where your .ipynb file is located.

Start Jupyter Notebook Server:
Run the following command in the terminal:

```jupyter notebook```
This will open a new tab in your default web browser with the Jupyter Notebook dashboard.

Access the Notebook:
In the Jupyter Notebook dashboard, you will see a list of files in the current directory. Click on the .ipynb file you want to run.

Run Cells:
Once the notebook is open, you can run individual cells by selecting a cell and clicking the "Run" button or using the keyboard shortcut (usually Shift + Enter).



5. Follow the on-screen prompts to input preferences for data generation, encoding, and scrambling.

   ------------THANK YOU--------------





