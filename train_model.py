import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os

# Set random seed for reproducibility
np.random.seed(42)


# Generate synthetic dataset
def create_dataset(n_samples=1000):
    """
    Create synthetic student performance dataset

    Features:
    - hours_studied:  Weekly study hours (0-40)
    - attendance:  Attendance percentage (50-100)
    - previous_score: Previous exam score (40-100)
    - assignment_score: Average assignment score (40-100)
    - sleep_hours: Average sleep per night (4-10)
    - participation: Class participation level (1-5)

    Target:
    - final_grade:  Final grade (0-100)
    """

    data = {
        'hours_studied': np.random.uniform(0, 40, n_samples),
        'attendance': np.random.uniform(50, 100, n_samples),
        'previous_score': np.random.uniform(40, 100, n_samples),
        'assignment_score': np.random.uniform(40, 100, n_samples),
        'sleep_hours': np.random.uniform(4, 10, n_samples),
        'participation': np.random.randint(1, 6, n_samples)
    }

    df = pd.DataFrame(data)

    # Create realistic final grade based on weighted features
    df['final_grade'] = (
                                0.25 * df['hours_studied'] +  # 25% weight
                                0.20 * df['attendance'] +  # 20% weight
                                0.25 * df['previous_score'] +  # 25% weight
                                0.15 * df['assignment_score'] +  # 15% weight
                                0.10 * df['sleep_hours'] * 5 +  # 10% weight (scaled)
                                0.05 * df['participation'] * 10  # 5% weight (scaled)
                        ) / 100 * 100

    # Add some random noise
    df['final_grade'] += np.random.normal(0, 3, n_samples)

    # Clip grades to 0-100 range
    df['final_grade'] = df['final_grade'].clip(0, 100)

    return df


# Create and save dataset
print("📊 Creating synthetic dataset...")
df = create_dataset(1000)

# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)
df.to_csv('data/student_data.csv', index=False)
print(f"✅ Dataset saved! Shape: {df.shape}")
print("\n📈 Dataset Statistics:")
print(df.describe())

# Split data
X = df.drop('final_grade', axis=1)
y = df['final_grade']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\n🔀 Train size: {X_train.shape[0]}, Test size: {X_test.shape[0]}")

# Train model
print("\n🤖 Training Random Forest model...")
model = RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\n📊 Model Performance:")
print(f"   Mean Absolute Error: {mae:.2f}")
print(f"   R² Score: {r2:.4f}")

# Feature importance
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print("\n🎯 Feature Importance:")
print(feature_importance)

# Save model
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/grade_predictor.pkl')
print("\n✅ Model saved successfully!")