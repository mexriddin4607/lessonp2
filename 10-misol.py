matn = input ("Biror bir matn kiritining ")
max_matn = matn.split()
max_matns = max_matn[0]


for i in max_matn:
    if len(i) > len(max_matns):
        max_matns = i
print("Bu matnda ichida eng uzun suz : ")
print(max_matns)