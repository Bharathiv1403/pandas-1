import pandas

data = {
    "Day": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Visitors": [18, 26, 18, 18, 9, 9, 20, 30, 16, 24],
    "Bounce_Rate": [77.27, 74.07, 73.68, 65, 90, 70, 72, 62.16, 81.25, 72],
}

df = pandas.DataFrame(data)
print(df)