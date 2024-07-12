# Guess Car

## Project Overview
**Guess Car** is a car brand detection project utilizing Faster R-CNN to identify car brands in real-time. The model is optimized for live feed and mobile compatibility, ensuring seamless performance across various devices. This project also recognizes various features of the car to enhance detection accuracy.

## Installation and Setup

### Prerequisites
1. Install [Anaconda 1.4](https://www.anaconda.com/products/distribution)
2. Install [CUDA v.8.0](https://developer.nvidia.com/cuda-80-ga2-download-archive)
3. Install [cuDNN v.6.0](https://developer.nvidia.com/rdp/cudnn-archive)
4. Ensure Python 3.7 is installed

### Setting Up the Environment
1. Download the environment setup files from the provided link:
   [Environment Download Link](https://drive.google.com/file/d/1OIS6zaiJRvfAccsNvjejcXHRolit1TQ5/view?usp=sharing)

2. Extract the downloaded folder to your desired location.

3. Open Anaconda Prompt and navigate to the extracted folder.

4. Create and activate the environment:
   ```bash
   conda env create -f environment.yml
   conda activate <environment_name>
   ```

5. Enter the Python interactive mode:
   ```bash
   python
   ```

6. Open the project directory:
   ```python
   import os
   os.chdir('path_to_proj2')
   ```

### Setting Up Mobile Compatibility
1. Install [DroidCam](https://play.google.com/store/apps/details?id=com.dev47apps.droidcam) from the Play Store on your mobile device.

2. Alternatively, you can use [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam) by following similar steps to set up the camera.

## Running the Project
1. Ensure the environment is activated.
2. Run the detection script:
   ```bash
   python detect.py
   ```

3. Follow the on-screen instructions to set up the live feed from your mobile device using DroidCam or IP Webcam.

## Usage
The model will start detecting car brands and their features in real-time. Make sure your mobile device is positioned correctly to capture the car images for accurate detection.

## Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.

## Contact
For any queries or support, please contact [Your Email].

---

Ensure you replace placeholder texts like `<environment_name>` and `path_to_proj2` with the actual names/paths used in your setup.
8. You can also use IPwebcam by following the same steps for droid camera
