import json
import polars as pl
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


# Step 1: Data Loading and Preprocessing
def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return pl.DataFrame(data)


def preprocess_data(df):
    # Features remain the same
    features = ['high_price', 'low_price', 'average_price']
    high_price_target = 'high_price_target'
    low_price_target = 'low_price_target'

    df = df.drop_nulls(subset=features + [high_price_target, low_price_target])
    x = df.select(features)
    y_high = df.select([high_price_target]).to_series()
    y_low = df.select([low_price_target]).to_series()
    return x.to_pandas(), y_high.to_pandas(), y_low.to_pandas()


# Step 2: Feature Engineering (if necessary)
# For simplicity, we will not add extra features in this example.

# Step 3: Model Training
def train_model(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')

    return model


# Step 4: Model Evaluation
# The evaluation is done during training using mean squared error.

# Step 5: Predictions
def make_predictions(model, new_data):
    return model.predict(new_data)


file_path = 'data.json'
df = load_data_from_json(file_path)
x, y_high, y_low = preprocess_data(df)

# Train models
model_high = train_model(x, y_high)
model_low = train_model(x, y_low)

# Making predictions on new data
# new_data should be a DataFrame with the same structure as the training features
new_data = pl.DataFrame({
    'high_price': [120, 250],
    'low_price': [100, 200],
    'average_price': [110, 225]
}).to_pandas()

# Predict high and low prices
predicted_highs = make_predictions(model_high, new_data)
predicted_lows = make_predictions(model_low, new_data)

print("Predicted Highs:", predicted_highs)
print("Predicted Lows:", predicted_lows)
