def clip_input(input, min, max):
    if input > max:
        return max
    elif input < min:
        return min
    return input