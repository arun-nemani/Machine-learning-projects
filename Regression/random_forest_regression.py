# Random Forest Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
Y = dataset.iloc[:, -1].values

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting the Random forest regression model to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=100,random_state=0)
regressor.fit(X, Y)

# Calculate R^2 and adjusted R^2
def calculateRSquared(y_orig, y_pred, X):
    Resid = sum((y_orig - y_pred)**2)
    Total = sum((y_orig - np.mean(y_orig))**2)
    R_squared = 1 - (float(Resid))/Total
    R_squared_adjusted = 1 - (1-R_squared)*(len(y_orig)-1)/(len(y_orig)-X.shape[1]-1)
    return R_squared, R_squared_adjusted

# Predicting a new result
Y_pred = regressor.predict(6.5)
# Visualizing the random forest tree results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, Y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (Random forest regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()