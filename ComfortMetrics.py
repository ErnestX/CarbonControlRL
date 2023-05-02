COMFORT_RANGE_HIGH = 30
COMFORT_RANGE_LOW = 20
EXP_FACTOR = 1.0

def calcComfortMetric(temperature, month, day, hour):
    if temperature < COMFORT_RANGE_LOW:
        return pow((temperature - COMFORT_RANGE_LOW), EXP_FACTOR)
    elif temperature > COMFORT_RANGE_HIGH:
        return pow((COMFORT_RANGE_HIGH - temperature), EXP_FACTOR)
    else:
        return 0.001 # always give a small positive reward?
    
