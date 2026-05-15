from sklearn.ensemble import IsolationForest
import numpy as np

# Sample network traffic data
# [packets, duration, failed_logins]
data = np.array([
    [50, 10, 0],
    [45, 12, 0],
    [500, 2, 10],
    [55, 11, 0],
    [600, 1, 15]
])

# Train model
model = IsolationForest(contamination=0.2)

model.fit(data)

# Predict anomalies
predictions = model.predict(data)

print("Traffic Analysis Results:\n")

for i, result in enumerate(predictions):
    if result == -1:
        print(f"Record {i+1}: Suspicious Activity Detected")
    else:
        print(f"Record {i+1}: Normal Traffic")
