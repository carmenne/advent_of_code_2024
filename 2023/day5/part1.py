from collections import defaultdict

almanac = ""
almanacs = defaultdict(list)
with open("input_long.txt", "r") as file:
    for line in file:
        if "seeds" in line:
            seeds=[int(s) for s in (line.strip().split(":")[1]).strip().split(" ")]
        elif line == "\n":
            continue
        elif "map" in line:
            almanac = line.replace("map:", "").strip()
        elif line[0] in "0123456789":
            almanacs[almanac].append(list(map(int,line.strip().split(" "))))

def get_mapped(number, mappings):

    for mapping in mappings:
        destination = mapping[0]
        source = mapping[1]
        range = mapping[2]
        if source <= number < source + range:
            mapped = number + destination - source
            return mapped
    return number


def seed_to_soil(seed):
    return get_mapped(seed, almanacs["seed-to-soil"])

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
for seed in seeds:
    soil = seed_to_soil(seed)
    fertilizer = soil_to_fertilizer(soil)
    print("soil", fertilizer)
    fertilizer = soil_to_fertilizer(soil)
    print("fertilizer", fertilizer)
    water = fertilizer_to_water(fertilizer)
    print("water", water)
    light = water_to_light(water)
    temperature = light_to_temperature(light)
    humidity = temperature_to_humidity(temperature)
    location = humidity_to_location(humidity)
    locations.append(location)

print(min(locations)) # 313045984
