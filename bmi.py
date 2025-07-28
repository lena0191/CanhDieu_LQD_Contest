w = float(input())
h = float(input())
bmi = w / (h ** 2)
if bmi < 18.5:
    print("Thieu can")
elif bmi <= 22.9:
    print("Binh thuong")
else:
    print("Thua can")
