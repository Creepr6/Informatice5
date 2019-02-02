def yiq(rgb):
    #
    y = 0,299 * rgb[0] + 0,587 * rgb[1] + 0,114 * rgb[2]
    i = 0,5960 * rgb[0] -0,274 * rgb[1] -0,322* rgb[2]
    q = 0,2110 * rgb[0] -0,523 * rgb[1] + 0,312 * rgb[2]

    return round(y, 4), round(i, 4), round(q, 4)

print(yiq((12,12,12))) 
