<h1 align="center">Facial Recognition Attendance System using Python</h1>

<p align="center">
  Building an Advanced Facial Recognition Attendance System with Python
</p>

---

## 🚀 Introduction

Welcome to the Facial Recognition Attendance System project! This project demonstrates the power of Python in creating a robust facial recognition system. It leverages convolutional neural networks (CNN), support vector machines (SVM), hierarchical Gaussian models (HGO), and more to achieve accurate facial identification.

To dive into this project, make sure you have the following prerequisites:

- A computer with a webcam.
- A Python environment with the required dependencies.
- Libraries used: cmake, dlib, cvzone, face_recognition, os, pickle, cv2, firebase_admin, and more.
- Recommended: Set up a dedicated virtual environment for this project.

Once you have the essentials ready, you can start by following these steps:

1. **Clone the Repository**: Clone this project's repository from GitHub.

2. **Install Dependencies**: Run `pip install -r libraries-required.txt` to install the necessary dependencies.

3. **Setup Firebase**: Configure a Firebase real-time database and storage. Add unique IDs for each student manually or through a .csv file in the `AddDataToDatabase` file. Add corresponding student images named according to their unique IDs in the `images` folder. Generate encodings using the `EncodeGenerator.py` file.

4. **Run the System**: Execute the `main.py` file to initiate the webcam or other devices for facial recognition.

Feel free to experiment with various hyperparameters, model architectures, and training techniques to enhance the accuracy of your facial recognition system. You can also consider exploring different datasets and incorporating additional features such as age or gender estimation.

Best of luck with your project! If you encounter any queries or concerns, consult the documentation or create an issue on the GitHub repository.

---

## 🤝 Contributions

We welcome contributions from the community! If you'd like to enhance FinancialFlow, feel free to submit issues and pull requests.
