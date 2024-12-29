from collections import defaultdict

almanac = ""
almanacs = defaultdict(list)
with open("input_long.txt", "r") as file:
    for line in file:
        if "seeds" in line:
            seeds = [int(s) for s in (line.strip().split(":")[1]).strip().split(" ")]
        elif line == "\n":
            continue
        elif "map" in line:
            almanac = line.replace("map:", "").strip()
        elif line[0] in "0123456789":
            almanacs[almanac].append(list(map(int, line.strip().split(" "))))


def get_mapped(intervals, mappings):
    mappings.sort(key=lambda x: x[1])

    for mapping in mappings:
        queue = intervals.copy()
        intervals = []

        while queue:
            intervals.extend(apply_interval(mapping, queue.pop(0)))

    return intervals


def apply_interval(mapping, interval):
    d, s, r = mapping
    m1 = s
    m2 = s + r
    x1, x2 = interval
    if m1 <= x1 <= x2 <= m2:  # m1, x1, x2, m2
        res1 = x1 + d - s
        res2 = x2 + d - s
        return [(res1, res2)]
    if m1 <= x1 < m2 <= x2:  # m1, x1, m2, x2
        res1 = x1 + d - s
        res2 = m2 + d - s
        return [(res1, res2 - 1), (m2, x2)]
    if x1 <= m1 < m2 <= x2:
        res1 = m1 + d - s
        res2 = m2 + d - s
        return [(x1, m1 - 1), (res1, res2 - 1), (m2, x2)]
    if x1 <= m1 < x2 <= m2:
        res1 = m1 + d - s
        res2 = x2 + d - s
        return [(x1, m1 - 1), (res1, res2)]

    return [(x1, x2)]


def seed_to_soil(seeds):
    return get_mapped(seeds, almanacs["seed-to-soil"])


def soil_to_fertilizer(soil):
    return get_mapped(soil, almanacs["soil-to-fertilizer"])


def fertilizer_to_water(fertilizer):
    return get_mapped(fertilizer, almanacs["fertilizer-to-water"])


def water_to_light(water):
    return get_mapped(water, almanacs["water-to-light"])


def light_to_temperature(light):
    return get_mapped(light, almanacs["light-to-temperature"])


def temperature_to_humidity(temperature):
    return get_mapped(temperature, almanacs["temperature-to-humidity"])


def humidity_to_location(humidity):
    return get_mapped(humidity, almanacs["humidity-to-location"])


locations = []
for i in range(1, len(seeds), 2):
    print("seeds", [seeds[i - 1], seeds[i - 1] + seeds[i] - 1])
    soil = seed_to_soil([(seeds[i - 1], seeds[i - 1] + seeds[i] - 1)])
    print("soil", soil)
    fertilizer = soil_to_fertilizer(soil)
    print("fertilizer", fertilizer)
    water = fertilizer_to_water(fertilizer)
    print("water", water)
    light = water_to_light(water)
    print("light", light)
    temperature = light_to_temperature(light)
    print("temperature", temperature)
    humidity = temperature_to_humidity(temperature)
    print("humidity", humidity)
    location = humidity_to_location(humidity)
    print("location", location)
    locations += location

print(len(locations))
print(sorted(locations))
print(min(locations))  # 313 045 984
