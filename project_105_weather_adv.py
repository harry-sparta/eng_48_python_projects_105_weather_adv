# Game codes-------------------------------------------------------------------------------------
weather = {'sunny': 'take your shorts!',
            'stormy': 'take rain coat!',
            'rainy': 'take your umbrella!',
            'rainy&stormy': 'stay home!'}

current_weather = input('enter weather condition (sunny, stormy, rainy, rainy&stormy):    ')
current_weather_format = current_weather.strip().lower()

while current_weather_format not in weather:
    print('sorry I didn\'t quite catch that. Try again.')
    current_weather = input('enter weather condition (sunny, stormy, rainy, rainy&stormy):    ')
    current_weather_format = current_weather.strip().lower()
print(weather[current_weather_format])