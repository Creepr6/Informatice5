def yiq(rgb):
    y = '{:.4f}'.format(0,299 * rgb[0] + 0,587 * rgb[1] + 0,114 * rgb[2])
    i = '{:.4f}'.format(0,5960 * rgb[0] -0,274 * rgb[1] -0,322 * rgb[2])
    q = '{:.4f}'.format(0,2110 * rgb[0] -0,523 * rgb[1] + 0,312 * rgb[2])

    return y, i, q

print(yiq((12,12,512)))
