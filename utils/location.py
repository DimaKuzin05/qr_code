import requests


def get_address(lat, lon):
    url = "https://nominatim.openstreetmap.org/reverse"

    params = {
        "lat": lat,
        "lon": lon,
        "format": "json"
    }

    headers = {
        "User-Agent": "qr-bot"
    }

    try:
        r = requests.get(url, params=params, headers=headers, timeout=10)
        data = r.json()

        address = data.get("address", {})

        city = address.get("city") or address.get("town") or address.get("village")
        country = address.get("country")

        if not city and not country:
            return "Адрес не найден"

        text = "Ваше местоположение:\n"
        if city:
            text += f"Город: {city}\n"
        if country:
            text += f"Страна: {country}"

        return text

    except Exception:
        return "Ошибка определения адреса"