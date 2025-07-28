T = int(input())
lai_suat = 0.05 
so_tien = T
for i in range(10):
    so_tien *= (1 + lai_suat)
    print(f"{so_tien:.3f}")
