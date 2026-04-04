weather = {"temperature": 34.2, "wind speed": 20.4,
           "rainfall": 10, "UV": 10, "pressure": 1004,
           "humidity": 0.65}

def fire_risk():
    t = weather["temperature"]
    w = weather["wind speed"]
    r = weather["rainfall"]
    h = weather["humidity"]
    return (t + w - r) / h
weather["fire rating"] = fire_risk()

def fire_rating():
    risk = weather["fire rating"]
    if risk < 0:
        return "Very Low"
    elif risk < 25:
        return "Low"
    elif risk < 50:
        return "Moderate"
    elif risk < 75:
        return "High"
    elif risk < 100:
        return "Very High"
    else:
        return "Extreme"
print(fire_rating())



