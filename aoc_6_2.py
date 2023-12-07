def ways_to_beat_record(time, distance):
    ways = 0
    for hold_time in range(time):
        speed = hold_time
        remaining_time = time - hold_time
        total_distance = speed * remaining_time
        if total_distance > distance:
            ways += 1
    return ways


time = 44707080
distance = 283113411341491

# Calculate the number of ways to beat the record
records = ways_to_beat_record(time, distance)

print("The result is:", records)
