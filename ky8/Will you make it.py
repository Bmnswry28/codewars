def zero_fuel(distance_to_pump, mpg, fuel_left):
    possible = mpg * fuel_left

    if distance_to_pump <= possible:
        return True
    else:
        return False