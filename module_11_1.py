import requests
import pandas as pd
import matplotlib.pyplot as plt

# Ваш ключ доступа
access_key = '25d9e4c6-ac93-4338-8419-acff733d0fb9'

# Список городов и их координаты
cities = {
    "Moscow": {"lat": 55.7558, "lon": 37.6173},
    "Saint Petersburg": {"lat": 59.9343, "lon": 30.3351},
    "Kazan": {"lat": 55.7961, "lon": 49.1064}
}

# Заголовки запроса
headers = {
    'X-Yandex-Weather-Key': access_key
}

# Сохранение данных о погоде
weather_data = []

# Получаем данные для каждого города
for city, coords in cities.items():
    url = 'https://api.weather.yandex.ru/v2/forecast'
    params = {
        'lat': coords["lat"],
        'lon': coords["lon"],
        'lang': 'ru_RU',
        'limit': 7,  # Прогноз на 7 дней
        'hours': False,  # Не включать данные по часам
        'extra': False  # Не включать дополнительные данные
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        for forecast in data["forecasts"]:
            date = forecast["date"]
            temp = forecast["parts"]["day"]["temp_avg"]
            weather_data.append({
                "city": city,
                "date": date,
                "temperature": temp
            })
    else:
        print(f"Ошибка при получении данных для города {city}: {response.status_code}")

# Создаем DataFrame
df = pd.DataFrame(weather_data)

# Выводим данные
print(df)

# Вычисляем среднюю температуру для каждого города
average_temperatures = df.groupby("city")["temperature"].mean()
print("\nСредняя температура за последние 7 дней:")
print(average_temperatures)

# Визуализация данных
plt.figure(figsize=(10, 6))
for city in cities.keys():
    city_data = df[df["city"] == city]
    plt.plot(city_data["date"], city_data["temperature"], marker="o", label=city)

plt.xlabel("Дата")
plt.ylabel("Температура (°C)")
plt.title("Изменение температуры за последние 7 дней")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

# Сохраняем график
plt.savefig("temperature_change_yandex.png")

# Показываем график
plt.show()
