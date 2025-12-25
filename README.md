# 🎓 Student Grade Predictor

A beautiful and interactive machine learning web application that predicts student final grades based on multiple performance metrics.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![scikit-learn](https://img.shields.io/badge/sklearn-1.4.0-orange.svg)
![Gradio](https://img.shields.io/badge/Gradio-4.19.2-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🌟 Live Demo

https://huggingface.co/spaces/Jamshed18/student-grade-predictor

## 🎯 Features

- ✨ **Beautiful UI** - Modern, gradient-styled interface with Gradio
- 🤖 **ML-Powered** - Random Forest Regression model (R² > 0.98)
- 📊 **Real-time Predictions** - Instant grade predictions
- 🎨 **Visual Feedback** - Color-coded results with personalized messages
- 📱 **Responsive Design** - Works on desktop and mobile
- 🔧 **Easy to Use** - Simple sliders and dropdowns

## 📊 Dataset

The model is trained on a **synthetic dataset** of 1,000 student records with the following features: 

## 🧠 Model Details

- **Algorithm:** Random Forest Regressor
- **Training Samples:** 800 (80% split)
- **Test Samples:** 200 (20% split)
- **Performance Metrics:**
  - Mean Absolute Error (MAE): ~2.34
  - R² Score: ~0.9856



## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/JamshedAli18/student-grade-predictor.git
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

