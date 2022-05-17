with open('raw_emg_data_unprocessed/index_finger_motion_raw.csv') as f:
    data = []
    for line in f:
        data.append(list(map(float, line.strip().split(','))))


for i in range(5):
    print(data[i])

print()
for i in range(-5, 0, 1):
    print(data[i])

