def solution() -> int:
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        mappings = ["seed_to_soil", "soil_to_fertilizer", "fertilizer_to_water", "water_to_light", "light_to_temperature", "temperature_to_humidity", "humidity_to_location"]

        seeds = lines[0].split(':')[1].split()
        seed_ranges = [(int(seeds[i]), int(seeds[i + 1])) for i in range(0, len(seeds), 2)]

        seed_to_soil = []
        soil_to_fertilizer = []
        fertilizer_to_water = []
        water_to_light = []
        light_to_temperature = []
        temperature_to_humidity = []
        humidity_to_location = []

        i = 0
        j = 0
        while i < len(lines):
            if len(lines[i]) == 0:
                i += 2
                while i < len(lines) and len(lines[i]) > 0:
                    mapping = [int(x) for x in lines[i].split()]
                    if mappings[j] == "seed_to_soil":
                        seed_to_soil.append(mapping)
                    elif mappings[j] == "soil_to_fertilizer":
                        soil_to_fertilizer.append(mapping)
                    elif mappings[j] == "fertilizer_to_water":
                        fertilizer_to_water.append(mapping)
                    elif mappings[j] == "water_to_light":
                        water_to_light.append(mapping)
                    elif mappings[j] == "light_to_temperature":
                        light_to_temperature.append(mapping)
                    elif mappings[j] == "temperature_to_humidity":
                        temperature_to_humidity.append(mapping)
                    elif mappings[j] == "humidity_to_location":
                        humidity_to_location.append(mapping)
                    i += 1
                j += 1
            else:
                i += 1

        location = min([x[0] for x in humidity_to_location])

        while True:
            running_location = location
            for humidity in humidity_to_location:
                if running_location >= humidity[0] and running_location < (humidity[0] + humidity[2]):
                    running_location = running_location - humidity[0] + humidity[1]
                    break
            for temperature in temperature_to_humidity:
                if running_location >= temperature[0] and running_location < (temperature[0] + temperature[2]):
                    running_location = running_location - temperature[0] + temperature[1]
                    break
            for light in light_to_temperature:
                if running_location >= light[0] and running_location < (light[0] + light[2]):
                    running_location = running_location - light[0] + light[1]
                    break
            for water in water_to_light:
                if running_location >= water[0] and running_location < (water[0] + water[2]):
                    running_location = running_location - water[0] + water[1]
                    break
            for fertilizer in fertilizer_to_water:
                if running_location >= fertilizer[0] and running_location < (fertilizer[0] + fertilizer[2]):
                    running_location = running_location - fertilizer[0] + fertilizer[1]
                    break
            for soil in soil_to_fertilizer:
                if running_location >= soil[0] and running_location < (soil[0] + soil[2]):
                    running_location = running_location - soil[0] + soil[1]
                    break
            for seed in seed_to_soil:
                if running_location >= seed[0] and running_location < (seed[0] + seed[2]):
                    running_location = running_location - seed[0] + seed[1]
                    break
            for seed in seed_ranges:
                if running_location >= seed[0] and running_location < (seed[0] + seed[1]):
                    return location
            location += 1

    return -1


if __name__ == '__main__':
    print(solution())