# 🎓 Student Grade Predictor

A beautiful and interactive machine learning web application that predicts student final grades based on multiple performance metrics.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![scikit-learn](https://img.shields.io/badge/sklearn-1.4.0-orange.svg)
![Gradio](https://img.shields.io/badge/Gradio-4.19.2-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🌟 Live Demo

**[Try it live on Hugging Face Spaces!](#)** _(Replace with your actual URL)_

## 📸 Screenshots

_Add screenshots of your app here_

## 🎯 Features

- ✨ **Beautiful UI** - Modern, gradient-styled interface with Gradio
- 🤖 **ML-Powered** - Random Forest Regression model (R² > 0.98)
- 📊 **Real-time Predictions** - Instant grade predictions
- 🎨 **Visual Feedback** - Color-coded results with personalized messages
- 📱 **Responsive Design** - Works on desktop and mobile
- 🔧 **Easy to Use** - Simple sliders and dropdowns

## 📊 Dataset

The model is trained on a **synthetic dataset** of 1,000 student records with the following features: 

| Feature | Description | Range |
|---------|-------------|-------|
| 📚 Hours Studied | Weekly study hours | 0-40 |
| ✅ Attendance | Class attendance percentage | 50-100% |
| 📊 Previous Score | Previous exam score | 40-100 |
| 📄 Assignment Score | Average assignment score | 40-100 |
| 😴 Sleep Hours | Average nightly sleep | 4-10 hours |
| 🙋 Participation | Class participation level | 1-5 |

**Target Variable:** Final Grade (0-100)

## 🧠 Model Details

- **Algorithm:** Random Forest Regressor
- **Training Samples:** 800 (80% split)
- **Test Samples:** 200 (20% split)
- **Performance Metrics:**
  - Mean Absolute Error (MAE): ~2.34
  - R² Score: ~0.9856

### Feature Importance

```
1. Hours Studied: 25%
2. Previous Score: 25%
3. Attendance: 20%
4. Assignment Score: 15%
5. Sleep Hours: 10%
6. Class Participation: 5%
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/student-grade-predictor.git
   cd student-grade-predictor
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the model**
   ```bash
   python train_model.py
   ```

5. **Run the app**
   ```bash
   python app.py
   ```

6. **Open in browser**
   - Go to http://127.0.0.1:7860

## 📁 Project Structure

```
student-grade-predictor/
│
├── data/
│   └── student_data.csv          # Generated synthetic dataset
│
├── models/
│   └── grade_predictor.pkl       # Trained ML model
│
├── app. py                         # Gradio web application
├── train_model.py                 # Model training script
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
├── SETUP.md                       # Installation guide
└── DEPLOYMENT.md                  # Deployment guide
```

## 🎨 UI Features

- **Interactive Sliders** - Easy input adjustment
- **Dropdown Menus** - Participation level selection
- **Real-time Prediction** - Instant results
- **Color-coded Output** - Visual grade indicators
- **Example Inputs** - Pre-filled sample students
- **Responsive Design** - Mobile-friendly interface

## 📚 How It Works

1. **Input:** User enters 6 performance metrics
2. **Processing:** Features are passed to the trained Random Forest model
3. **Prediction:** Model predicts final grade (0-100)
4. **Output:** Display prediction with color-coded message

## 🎯 Grade Scale

| Grade | Range | Message |
|-------|-------|---------|
| 🌟 Outstanding | 90-100 | Excellent performance!  |
| 🎉 Great | 80-89 | Very good work! |
| 👍 Good | 70-79 | Keep it up! |
| 📚 Fair | 60-69 | More study needed |
| ⚠️ Poor | 0-59 | Needs improvement |

## 🔧 Technologies Used

- **Python 3.8+** - Programming language
- **scikit-learn** - Machine learning library
- **Gradio** - Web UI framework
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Joblib** - Model serialization

## 🌐 Deployment

This app can be deployed to: 

- **Hugging Face Spaces** (Recommended) - See [DEPLOYMENT.md](DEPLOYMENT.md)
- **Streamlit Cloud**
- **Railway**
- **Heroku**
- **AWS/GCP/Azure**

## 📈 Future Improvements

- [ ] Add data visualization dashboard
- [ ] Include study tips based on predictions
- [ ] Compare with class average
- [ ] Historical tracking for multiple predictions
- [ ] Export prediction reports as PDF
- [ ] Add more ML models for comparison

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- LinkedIn: [Your Profile](#)

## 🙏 Acknowledgments

- Gradio team for the amazing UI framework
- scikit-learn community
- Hugging Face for free hosting

## 📧 Contact

Have questions?  Feel free to reach out! 

- Email: your.email@example.com
- Twitter: [@yourhandle](#)

---

<div align="center">
  Made with ❤️ and Python
  
  ⭐ Star this repo if you found it helpful! 
</div>