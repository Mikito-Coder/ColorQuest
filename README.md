---

#  ColorQuest 🎨

ColorQuest is an innovative computer vision project designed to detect and track specific colors in real-time using a webcam feed. Utilizing the powerful OpenCV library alongside Python, ColorQuest turns complex image processing tasks into an engaging and interactive user experience. Whether for educational purposes, hobbyist projects, or integration into larger systems, ColorQuest adds a splash of color to the world of computer vision.

## 🚀 Features

- 📹 Real-time color detection and tracking with webcam support.
- 🎨 Utilizes HSV color space for accurate color recognition.
- 🌟 Dynamically calculates HSV ranges for targeted color detection.
- 🖼️ Implements bounding boxes to highlight detected colors.
- 🔧 Modular code design for easy customization and extension.

## 🛠 Getting Started

### Prerequisites

Ensure you have Python 3.x installed on your system. You'll also need to install OpenCV and Pillow (PIL) libraries. All necessary dependencies are listed in `requirements.txt`.

### Installation

1. 🐑 Clone the repository:
   ```sh
   git clone https://github.com/yourusername/ColorQuest.git
   ```
2. 📂 Navigate to the project directory:
   ```sh
   cd ColorQuest
   ```
3. 📦 Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

### Usage

🚀 Run `Original.py` to start color detection:
```sh
python Original.py
```
🌈 Position a color object in front of your webcam. ColorQuest currently targets the color yellow by default but can be easily reconfigured to detect your colors of choice.

🔚 To exit the application, press 'q' while the application window is active.

## ⚙ Configuration

To change the target color, edit the `Original.py` file and modify the `Blue` or `Yellow` variables to your desired BGR color values. Then, adjust the `get_limits` function call accordingly.

## 🤝 Contributing

Contributions to ColorQuest are welcome! 🎉 Feel free to fork the repository, make your changes, and submit pull requests. If you have suggestions or encounter issues, don't hesitate to open an issue in the GitHub repository.

## 📜 License

ColorQuest is released under the MIT License. See the `LICENSE` file for more information.

## 🙏 Acknowledgments

- Big thanks to the OpenCV community for their comprehensive documentation and resources.
- Appreciation to all project contributors and the open-source community for their continuous support.

---
