import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Define the data
X = np.array([2.3, 1.8, 3.2, 2.9, 4.5, 3.8, 2.5, 3.0, 4.0, 4.2]).reshape(-1, 1)
Y = np.array([4.5, 3.7, 5.1, 4.8, 6.2, 5.7, 4.2, 5.0, 5.9, 6.3])

# Initialize the linear regression model
model = LinearRegression()

# Train the model
model.fit(X, Y)

# Predict Y for the given X values
predicted_Y = model.predict(X)

# Visualize the results
plt.scatter(X, Y, color='blue', label='Actual Data')
plt.plot(X, predicted_Y, color='red', linewidth=2, label='Predicted Line')
plt.xlabel('Sensor Reading (X)')
plt.ylabel('Actuator Response (Y)')
plt.title('Sensor vs. Actuator Relationship')
plt.legend()
plt.show()