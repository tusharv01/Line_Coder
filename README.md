# ITT305 Programming Assignment 1 - Line Coding Encoder and Scrambler

## Overview

This project involves implementing a Line Coding Encoder and Scrambler with a digital data generator. The assignment includes the generation of a random data sequence, encoding using various line coding schemes (NRZ-L, NRZ-I, Manchester, Differential Manchester, AMI), and optional scrambling using B8ZS or HDB3. The code also identifies the longest palindromic sequence in the generated data.

## Line Encoder GUI

This is a Line Encoder GUI implemented using PySimpleGUI, Matplotlib, and NumPy. It provides an interface for encoding and decoding various line encoding schemes.

### Features:

- Initialize random input data.
- Enter custom input data.
- Encode and decode data using various line encoding schemes.
- Display the encoded and decoded data.
- Plot graphs for input, encoded, and decoded data.

### Line Encoding Schemes:

1. Polar NRZ-L
2. Polar NRZ-I
3. Manchester
4. Polar RZ
5. AMI
6. Scrambling AMI B8ZS (Bipolar with 8 zero substitution)
7. Differential Manchester
8. Scrambling AMI HBD3 (High-Density Bipolar 3 Zeros)
9. PCM (Pulse Code Modulation)
10. Delta Modulation

### How to Use:

1. Launch the GUI.
2. Initialize random input or enter custom input.
3. Encode the data using a selected encoding scheme.
4. Optionally, decode the encoded data.
5. Visualize the input, encoded, and decoded data using the "Show Graph" button.

### Examples:

#### Initializing the Input:
![Screenshot from 2023-11-13 05-31-08](https://github.com/tusharv01/Line_Coder/assets/93588934/ffa2e9bd-d089-4aee-ad16-da1e8eab8dcf)


#### Entering scheme Input:
![Screenshot from 2023-11-13 05-30-04](https://github.com/tusharv01/Line_Coder/assets/93588934/6ccc855f-f37f-4b98-887c-ac198e7ecc6f)


#### Encoding and Decoding:
![Screenshot from 2023-11-13 05-30-18](https://github.com/tusharv01/Line_Coder/assets/93588934/4aa74ebf-a226-4635-aad3-b853ca512400)


## How to Run the Code

1. Ensure you have Python installed on your machine.
2. Clone the repository:

    ```bash
    git clone https://github.com/tusharv01/Line_Coder.git
    ```

3. Navigate to the project directory:

    ```bash
    cd Line_Coder
    ```

4. Run the main program:

    ```bash
    python LineEncoder.py
    ```

    or using the LineEncoder.ipynb file:

    ```bash
    jupyter notebook
    ```

    Navigate to the .ipynb file and run the cells.

5. Follow the on-screen prompts to input preferences for data generation, encoding, and scrambling.

**THANK YOU!**
