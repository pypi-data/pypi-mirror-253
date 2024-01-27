# Prusek-Spheroid

Prusek-Spheroid is a Python package designed for spheroid segmentation based on provided microscope images. This package provides an easy-to-use interface and functionalities that are essential for determination of properties and characteristics of the spheroids.

## Installation

### Installing Python

#### For Windows:

1. **Download Python** from [python.org](https://python.org).
2. **Run the downloaded installer**. Ensure to check the "Add Python to PATH" option.
3. **Verify the installation** by opening CMD and typing `python --version`.

#### For MacOS/Linux:

1. **Check if Python is installed** by typing `python3 --version` in the terminal. If not installed:
   - On MacOS: Install via Homebrew with `brew install python3`.
   - On Linux: Install using `sudo apt-get install python3`.
2. **Verify the installation** by typing `python3 --version` in the terminal.

### Installing Miniconda

1. **Download Miniconda** from the [official Miniconda website](https://docs.conda.io/en/latest/miniconda.html).
2. **Install Miniconda** and follow the on-screen instructions.
3. **Verify the installation** by opening a new terminal or CMD and typing `conda list`.

### Creating a Virtual Environment and Installing Prusek-Spheroid

1. **Create a virtual environment** using Miniconda: `conda create -n myenv python=3.x`.
2. **Activate the virtual environment**: `conda activate myenv` (Windows) or `source activate myenv` (MacOS/Linux).
3. **Install the Prusek-Spheroid package**: `pip install prusek_spheroid`.

## Running the Package

To use the package, first ensure it is up to date: `pip install --upgrade prusek_spheroid`

then run the program using the command: `python -m prusek_spheroid.GUI`

## User Guide for Prusek-Spheroid GUI

Prusek-Spheroid is a sophisticated Python package equipped with a user-friendly graphical interface (GUI) that facilitates image segmentation and optimization tasks. This guide provides an overview of the GUI functionalities and how to use them effectively.

### Key Features

1. **File Selection**: Users can easily select image files or datasets for processing. This feature allows you to work with your preferred data seamlessly.

2. **Progress Windows**: The GUI includes dedicated windows displaying the ongoing progress of image processing and optimization tasks, keeping you informed every step of the way.

3. **Segmentation Parameters**: Customize your segmentation process with adjustable parameters. These settings allow you to fine-tune the segmentation to suit your specific needs.

4. **Optimization Tools**: Enhance the accuracy of your segmentation with built-in optimization algorithms based on the well-known Gradient descent algorithm. These tools are designed to improve the outcome of your image processing tasks.

### Using the GUI

The Prusek-Spheroid GUI is designed to be intuitive, providing a range of functionalities for effective image segmentation. Here’s a detailed overview of the key elements:

1. **Loading Addresses Buttons**: These buttons are used for selecting and loading the directories where your data is stored. You can easily navigate and choose the required folders that contain your image files.

2. **Project Name Field**: Here, you enter the name of your project. This name will be used for organizing and saving the results in a structured manner.

3. **Output Folder Selection**: After processing, the results will be saved in the selected output folder. This feature allows you to specify where you want the segmented images and other outputs to be stored.

4. **Method Selection Dropdown**: This dropdown menu lets you choose the segmentation method. The GUI includes various methods like Sauvola, Niblack, etc. Notably, Sauvola and Niblack methods are often considered the best choices due to their effectiveness in image segmentation.

5. **Gradient Descent Parameters**: These parameters are crucial for the Gradient Descent algorithm. They typically include settings like learning rate, number of iterations, and delta. It's generally recommended not to alter these parameters unless you have specific requirements or understanding of the algorithm.

6. **Other Settings Checkboxes**: This section contains various checkboxes for additional settings. These settings might include options for inner contours, specific algorithmic adjustments, or other advanced configurations.

7. **'I Already Know the Parameters' Checkbox**: If you have pre-determined parameters from a previous Gradient Descent project, you can use this checkbox. It's useful when you want to segment images using already optimized parameters without going through the Gradient Descent process again.

### Additional Information

- The GUI is structured to facilitate both beginners and advanced users in the field of image processing.
- Each feature and button is designed to provide maximum control over the segmentation process, ensuring that users can tailor the process to their specific data and requirements.
- Regular updates and feedback from users are encouraged to continuously improve the functionality and user experience.

For detailed explanations of the segmentation methods and Gradient Descent algorithm, refer to the technical documentation provided with the package.

If you encounter any issues or need further assistance, please feel free to reach out to prusemic@fjfi.cvut.cz


## Support 

For any issues or queries, contact me at: prusemic@fjfi.cvut.cz