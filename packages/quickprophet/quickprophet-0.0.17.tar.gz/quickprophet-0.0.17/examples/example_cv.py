from quickprophet.models import BatchCOVIDLogisticProphet, generate_cutoffs

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Function to generate synthetic time series data
def generate_synthetic_data(start_date, end_date, freq='D'):
    date_range = pd.date_range(start=start_date, end=end_date, freq=freq)
    n = len(date_range)

    # Generate random data for the time series
    np.random.seed(42)
    y = np.cumsum(np.random.normal(size=n))

    # Create a DataFrame with 'ds' (date) and 'y' (target variable)
    data = pd.DataFrame({'ds': date_range, 'y': y})

    # Add some additional predictors for demonstration purposes
    data['extra_predictor_1'] = np.random.rand(n)
    data['extra_predictor_2'] = np.random.rand(n)

    # Create a column for grouping (for this example, a simple binary grouping)
    data['group_column_name'] = np.random.choice([0, 1], size=n)

    return data

# Generate synthetic data
start_date = datetime(2020, 1, 1)
end_date = datetime(2022, 1, 1)
synthetic_data = generate_synthetic_data(start_date, end_date)

# Instantiate the BatchCOVIDLogisticProphet model
model = BatchCOVIDLogisticProphet(group_cols=['group_column_name'])

# Cross-validation parameters
cutoffs = generate_cutoffs(synthetic_data, horizon='30 days', initial='365 days', step='180 days')
param_grid = {
    'changepoint_prior_scale': [0.001, 0.01, 0.1, 0.5],
    'seasonality_prior_scale': [0.01, 0.1, 1.0, 10.0],
    'holidays_prior_scale': [0.01, 0.1, 1.0, 10.0]
}

# Perform cross-validation to find the best model
model.cv(synthetic_data, param_grid=param_grid, cutoffs=cutoffs)

# Access the best parameters found during cross-validation
best_params = model.best_params

# Now you can use the best parameters to fit the final model
model.fit(synthetic_data)

# Perform predictions for a specified number of periods into the future
forecasts = model.predict(periods=365 * 2)

# Display the forecast results
print(forecasts.head())

