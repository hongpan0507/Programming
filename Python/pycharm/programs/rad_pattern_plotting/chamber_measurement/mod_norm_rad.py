def norm_rad(rad_h=[], rad_v=[]):
    # # find max and normalize
    if max(rad_h) >= max(rad_v):
        temp_max = max(rad_h)
        for i in range(0, len(rad_h)):
            rad_h[i] = rad_h[i] - temp_max
            rad_v[i] = rad_v[i] - temp_max
    else:
        temp_max = max(rad_v)
        for i in range(0, len(rad_h)):
            rad_h[i] = rad_h[i] - temp_max
            rad_v[i] = rad_v[i] - temp_max

    return rad_h, rad_v
