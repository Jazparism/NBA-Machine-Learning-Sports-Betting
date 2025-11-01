import sqlite3

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split

"""
Logistic Regression Over/Under Model Training Script

This script trains a Logistic Regression model for predicting NBA game over/under outcomes.

Model Details:
- Algorithm: Logistic Regression (scikit-learn)
- Objective: Multi-class classification (Under/Push/Over)
- Features: Team statistics + over/under line
- Dataset: 2012-23 seasons

IMPORTANT: This model is NOT currently integrated into the prediction pipeline (main.py).
It exists as an experimental/alternative approach but is not used by the Flask app or 
command-line predictions. To use this model, additional integration work would be needed
in the src/Predict/ directory.

See MODELS.md for detailed documentation.
"""

dataset = "dataset_2012-23"
con = sqlite3.connect("../../Data/dataset.sqlite")
data = pd.read_sql_query(f"select * from \"{dataset}\"", con, index_col="index")
con.close()

OU = data['OU-Cover']
total = data['OU']
data.drop(['Score', 'Home-Team-Win', 'TEAM_NAME', 'Date', 'TEAM_NAME.1', 'Date.1', 'OU-Cover', 'OU'], axis=1,
          inplace=True)

data['OU'] = np.asarray(total)
data = data.values
data = data.astype(float)

X_train, X_test, y_train, y_test = train_test_split(data, OU, test_size=0.1, random_state=42)

model = LogisticRegression()

# Train the model on the training data
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Generate a classification report
report = classification_report(y_test, y_pred)

# Print the results
print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(report)
