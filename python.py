def predict_weather(T, H, w):
    w = (0.5 * (T ** 2)) - (0.2 * H) + (0.1 * w) - 15
    if w > 300:
        return "sunny"
    elif 200 <= w <= 300:
        return "rainy"
    else:
        return "unknown"

# Example usage
temperature = 25 # Celsius
humidity = 80 # Percentage
wind = 10 # km/h
weather_condition = predict_weather(temperature, humidity, wind)
print(f"The predicted weather condition is {weather_condition}.")
