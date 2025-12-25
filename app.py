import gradio as gr
import joblib
import numpy as np
import pandas as pd

# Load the trained model
model = joblib.load('models/grade_predictor.pkl')


def get_grade_message(grade):
    """Return a friendly message based on grade"""
    if grade >= 90:
        return "🌟 Outstanding!  Excellent performance!"
    elif grade >= 80:
        return "🎉 Great job! Very good work!"
    elif grade >= 70:
        return "👍 Good effort! Keep it up!"
    elif grade >= 60:
        return "📚 Fair.  More study needed."
    else:
        return "⚠️ Needs significant improvement."


def get_grade_color(grade):
    """Return color based on grade"""
    if grade >= 90:
        return "#22c55e"
    elif grade >= 80:
        return "#3b82f6"
    elif grade >= 70:
        return "#f59e0b"
    elif grade >= 60:
        return "#ef4444"
    else:
        return "#991b1b"


def predict_grade(hours_studied, attendance, previous_score,
                  assignment_score, sleep_hours, participation):
    """Predict student's final grade"""
    input_data = pd.DataFrame({
        'hours_studied': [hours_studied],
        'attendance': [attendance],
        'previous_score': [previous_score],
        'assignment_score': [assignment_score],
        'sleep_hours': [sleep_hours],
        'participation': [participation]
    })

    predicted_grade = model.predict(input_data)[0]
    predicted_grade = np.clip(predicted_grade, 0, 100)

    message = get_grade_message(predicted_grade)
    color = get_grade_color(predicted_grade)

    result_html = f"""
    <div style="text-align: center; padding: 20px; border-radius: 10px; 
                background:  linear-gradient(135deg, {color}22, {color}44);">
        <h2 style="color: {color}; margin-bottom: 10px;">
            Predicted Final Grade
        </h2>
        <h1 style="color: {color}; font-size: 4em; margin: 20px 0;">
            {predicted_grade:.1f}%
        </h1>
        <p style="font-size: 1.3em; color: #333; font-weight: 500;">
            {message}
        </p>
    </div>
    """

    return result_html


custom_css = """
#title {
    text-align: center;
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 2.5em;
    font-weight: bold;
    margin-bottom: 10px;
}
"""

with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
        <h1 id="title">🎓 Student Grade Predictor</h1>
        <p style="text-align: center; font-size: 1.1em; color: #666;">
            Predict your final grade based on study habits, attendance, and performance metrics. <br>
            Powered by Machine Learning 🤖
        </p>
    """)

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 📝 Student Performance Metrics")

            hours_studied = gr.Slider(0, 40, 20, step=0.5,
                                      label="📚 Hours Studied (per week)",
                                      info="Weekly study hours including homework and revision")

            attendance = gr.Slider(50, 100, 85, step=1,
                                   label="✅ Attendance (%)",
                                   info="Class attendance percentage")

            previous_score = gr.Slider(40, 100, 75, step=1,
                                       label="📊 Previous Exam Score",
                                       info="Score from previous examination (0-100)")

            assignment_score = gr.Slider(40, 100, 80, step=1,
                                         label="📄 Assignment Score",
                                         info="Average score on assignments (0-100)")

            sleep_hours = gr.Slider(4, 10, 7, step=0.5,
                                    label="😴 Sleep Hours (per night)",
                                    info="Average hours of sleep per night")

            participation = gr.Dropdown([1, 2, 3, 4, 5], value=3,
                                        label="🙋 Class Participation Level",
                                        info="1 = Very Low, 5 = Very High")

            predict_btn = gr.Button("🔮 Predict My Grade", variant="primary", size="lg")

        with gr.Column(scale=1):
            gr.Markdown("### 🎯 Prediction Result")
            output = gr.HTML("""
                <div style="text-align: center; padding: 40px; border:  2px dashed #ccc; border-radius: 10px;">
                    <p style="color: #999; font-size: 1.2em;">
                        👈 Enter your details and click "Predict My Grade"
                    </p>
                </div>
            """)

    gr.Markdown("""
        ---
        ### 📖 How It Works
        This predictor uses a **Random Forest Regression** model trained on 1,000 synthetic student records.

        **Feature Weights:** 📚 Study Hours:  25% | 📊 Previous Score: 25% | ✅ Attendance: 20% | 
        📄 Assignments: 15% | 😴 Sleep: 10% | 🙋 Participation: 5%
    """)

    predict_btn.click(
        fn=predict_grade,
        inputs=[hours_studied, attendance, previous_score, assignment_score, sleep_hours, participation],
        outputs=output
    )

    gr.Examples(
        examples=[[30, 95, 85, 90, 8, 5], [15, 75, 70, 75, 7, 3], [5, 60, 50, 55, 5, 2]],
        inputs=[hours_studied, attendance, previous_score, assignment_score, sleep_hours, participation],
        label="📋 Example Students"
    )

if __name__ == "__main__":
    demo.launch()