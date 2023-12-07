def ways_to_beat_record(time, distance):
    ways = 0
    for hold_time in range(time):
        speed = hold_time
        remaining_time = time - hold_time
        total_distance = speed * remaining_time
        if total_distance > distance:
            ways += 1
    return ways


def multiply_ways(records):
    result = 1
    for record in records:
        result *= record
    return result


times = [44, 70, 70, 80]
distances = [283, 1134, 1134, 1491]

# Calculate the number of ways to beat the record for each race
records = [
    ways_to_beat_record(time, distance) for time, distance in zip(times, distances)
]

# Multiply the results together
result = multiply_ways(records)

print("The result is:", result)
