import json
import polars as pl
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


# Data Loading and Preprocessing
def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return pl.DataFrame(data)


def preprocess_data(df):
    features = ['high_price', 'low_price', 'average_price']
    high_price_target = 'high_price_target'
    low_price_target = 'low_price_target'

    df = df.drop_nulls(subset=features + [high_price_target, low_price_target])
    x = df.select(features)
    y_high = df.select([high_price_target]).to_series()
    y_low = df.select([low_price_target]).to_series()
    return x.to_pandas(), y_high.to_pandas(), y_low.to_pandas()


#possible fix

#def preprocess_data(df):
    # Sort the DataFrame by 'id' and 'timestamp'
#    df = df.sort(by=['id', 'timestamp'])

    # Create target variables by shifting prices
#    df = df.with_columns([
#        pl.col('high_price').shift(-1).alias('high_price_target'),
#        pl.col('low_price').shift(-1).alias('low_price_target')
#    ])
#
#    # Filter out the last entries where targets are null
#    df = df.drop_nulls(subset=['high_price_target', 'low_price_target'])
#
#    features = ['high_price', 'low_price']
#    x = df.select(features).to_pandas()
#    y_high = df.select('high_price_target').to_pandas().values.ravel()
#    y_low = df.select('low_price_target').to_pandas().values.ravel()
#
#    return x, y_high, y_low
#


# Model Training
def train_model(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')

    return model


# Model Evaluation and prediction making
def make_predictions(model, new_data):
    return model.predict(new_data)


file_path = 'output/aggregated_item_prices.csv'
df = load_data(file_path)
x, y_high, y_low = preprocess_data(df)

# Train models
model_high = train_model(x, y_high)
model_low = train_model(x, y_low)

# Predictions on new data
new_data = pl.DataFrame({
    'high_price': [120, 250],
    'low_price': [100, 200],
    'average_price': [110, 225]
}).to_pandas()

# High and low price predictions
predicted_highs = make_predictions(model_high, new_data)
predicted_lows = make_predictions(model_low, new_data)

print("Predicted Highs:", predicted_highs)
print("Predicted Lows:", predicted_lows)
