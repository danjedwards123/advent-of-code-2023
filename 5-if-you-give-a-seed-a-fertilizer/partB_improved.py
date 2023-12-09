def solution() -> int:
    answer = float("inf")

    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        mappings = ["seed_to_soil", "soil_to_fertilizer", "fertilizer_to_water", "water_to_light", "light_to_temperature", "temperature_to_humidity", "humidity_to_location"]

        seeds = lines[0].split(':')[1].split()
        seed_ranges = [(int(seeds[i]), int(seeds[i]) + int(seeds[i + 1])) for i in range(0, len(seeds), 2)]

        seed_to_soil = []
        seed_to_soil_ranges = []
        soil_to_fertilizer = []
        soil_to_fertilizer_ranges = []
        fertilizer_to_water = []
        fertilizer_to_water_ranges = []
        water_to_light = []
        water_to_light_ranges = []
        light_to_temperature = []
        light_to_temperature_ranges = []
        temperature_to_humidity = []
        temperature_to_humidity_ranges = []
        humidity_to_location = []
        humidity_to_location_ranges = []
        location_ranges = []

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


        # for each range, create new list of mappings to the level below
        # creates 1-3 new ranges, 1 if fully inside a range, 2 if split by start/end range, 3 if fully enclosing a range
        # on next row, loop through mappings and create new mappings to the level below ^
        # after complete, loop through all starting seeds of each created mapping range
        # return minimum location of these seeds

        for seed_range in seed_ranges:
          for x in seed_to_soil:
            if seed_range[0] >= x[1] and seed_range[1] < (x[1] + x[2]):
              seed_to_soil_ranges.append([x[0] + (seed_range[0] - x[1]), x[0] + (seed_range[1] - x[1])])
              break
            elif seed_range[0] < x[1] and seed_range[1] < (x[1] + x[2]) and seed_range[1] > x[1]:
              seed_to_soil_ranges.append([seed_range[0], x[1]])
              seed_to_soil_ranges.append([x[1] - x[0], seed_range[1] - x[0]])
              break
            elif seed_range[0] >= x[1] and seed_range[1] >= (x[1] + x[2]) and seed_range[0] < (x[1] + x[2]):
              seed_to_soil_ranges.append([seed_range[0] - x[0], x[1] + x[2] - x[0]])
              seed_to_soil_ranges.append([x[1] + x[2], seed_range[1]])
              break
            elif seed_range[0] < x[1] and seed_range[1] >= (x[1] + x[2]):
              seed_to_soil_ranges.append([seed_range[0], x[1]])
              seed_to_soil_ranges.append([x[1] - x[0], x[1] + x[2] - x[0]])
              seed_to_soil_ranges.append([x[1] + x[2], seed_range[1]])
              break

        for soil_range in seed_to_soil_ranges:
            for x in soil_to_fertilizer:
                if soil_range[0] >= x[1] and soil_range[1] < (x[1] + x[2]):
                    soil_to_fertilizer_ranges.append([soil_range[0] - x[0], soil_range[1] - x[0]])
                    break
                elif soil_range[0] < x[1] and soil_range[1] < (x[1] + x[2]) and soil_range[1] > x[1]:
                    soil_to_fertilizer_ranges.append([soil_range[0], x[1]])
                    soil_to_fertilizer_ranges.append([x[1] - x[0], soil_range[1] - x[0]])
                    break
                elif soil_range[0] >= x[1] and soil_range[1] >= (x[1] + x[2]) and soil_range[0] < (x[1] + x[2]):
                    soil_to_fertilizer_ranges.append([soil_range[0] - x[0], x[1] + x[2] - x[0]])
                    soil_to_fertilizer_ranges.append([x[1] + x[2], soil_range[1]])
                    break
                elif soil_range[0] < x[1] and soil_range[1] >= (x[1] + x[2]):
                    soil_to_fertilizer_ranges.append([soil_range[0], x[1]])
                    soil_to_fertilizer_ranges.append([x[1] - x[0], x[1] + x[2] - x[0]])
                    soil_to_fertilizer_ranges.append([x[1] + x[2], soil_range[1]])
                    break

        for fertilizer_range in soil_to_fertilizer_ranges:
            for x in fertilizer_to_water:
                if fertilizer_range[0] >= x[1] and fertilizer_range[1] < (x[1] + x[2]):
                    fertilizer_to_water_ranges.append([fertilizer_range[0] - x[0], fertilizer_range[1] - x[0]])
                    break
                elif fertilizer_range[0] < x[1] and fertilizer_range[1] < (x[1] + x[2]) and fertilizer_range[1] > x[1]:
                    fertilizer_to_water_ranges.append([fertilizer_range[0], x[1]])
                    fertilizer_to_water_ranges.append([x[1] - x[0], fertilizer_range[1] - x[0]])
                    break
                elif fertilizer_range[0] >= x[1] and fertilizer_range[1] >= (x[1] + x[2]) and fertilizer_range[0] < (x[1] + x[2]):
                    fertilizer_to_water_ranges.append([fertilizer_range[0] - x[0], x[1] + x[2] - x[0]])
                    fertilizer_to_water_ranges.append([x[1] + x[2], fertilizer_range[1]])
                    break
                elif fertilizer_range[0] < x[1] and fertilizer_range[1] >= (x[1] + x[2]):
                    fertilizer_to_water_ranges.append([fertilizer_range[0], x[1]])
                    fertilizer_to_water_ranges.append([x[1] - x[0], x[1] + x[2] - x[0]])
                    fertilizer_to_water_ranges.append([x[1] + x[2], fertilizer_range[1]])
                    break

        for water_range in fertilizer_to_water_ranges:
            for x in water_to_light:
                if water_range[0] >= x[1] and water_range[1] < (x[1] + x[2]):
                    water_to_light_ranges.append([water_range[0] - x[0], water_range[1] - x[0]])
                    break
                elif water_range[0] < x[1] and water_range[1] < (x[1] + x[2]) and water_range[1] > x[1]:
                    water_to_light_ranges.append([water_range[0], x[1]])
                    water_to_light_ranges.append([x[1] - x[0], water_range[1] - x[0]])
                    break
                elif water_range[0] >= x[1] and water_range[1] >= (x[1] + x[2]) and water_range[0] < (x[1] + x[2]):
                    water_to_light_ranges.append([water_range[0] - x[0], x[1] + x[2] - x[0]])
                    water_to_light_ranges.append([x[1] + x[2], water_range[1]])
                    break
                elif water_range[0] < x[1] and water_range[1] >= (x[1] + x[2]):
                    water_to_light_ranges.append([water_range[0], x[1]])
                    water_to_light_ranges.append([x[1] - x[0], x[1] + x[2] - x[0]])
                    water_to_light_ranges.append([x[1] + x[2], water_range[1]])
                    break

        for light_range in water_to_light_ranges:
            for x in light_to_temperature:
                if light_range[0] >= x[1] and light_range[1] < (x[1] + x[2]):
                    light_to_temperature_ranges.append([light_range[0] - x[0], light_range[1] - x[0]])
                    break
                elif light_range[0] < x[1] and light_range[1] < (x[1] + x[2]) and light_range[1] > x[1]:
                    light_to_temperature_ranges.append([light_range[0], x[1]])
                    light_to_temperature_ranges.append([x[1] - x[0], light_range[1] - x[0]])
                    break
                elif light_range[0] >= x[1] and light_range[1] >= (x[1] + x[2]) and light_range[0] < (x[1] + x[2]):
                    light_to_temperature_ranges.append([light_range[0] - x[0], x[1] + x[2] - x[0]])
                    light_to_temperature_ranges.append([x[1] + x[2], light_range[1]])
                    break
                elif light_range[0] < x[1] and light_range[1] >= (x[1] + x[2]):
                    light_to_temperature_ranges.append([light_range[0], x[1]])
                    light_to_temperature_ranges.append([x[1] - x[0], x[1] + x[2] - x[0]])
                    light_to_temperature_ranges.append([x[1] + x[2], light_range[1]])
                    break

        for temperature_range in light_to_temperature_ranges:
            for x in temperature_to_humidity:
                if temperature_range[0] >= x[1] and temperature_range[1] < (x[1] + x[2]):
                    temperature_to_humidity_ranges.append([temperature_range[0] - x[0], temperature_range[1] - x[0]])
                    break
                elif temperature_range[0] < x[1] and temperature_range[1] < (x[1] + x[2]) and temperature_range[1] > x[1]:
                    temperature_to_humidity_ranges.append([temperature_range[0], x[1]])
                    temperature_to_humidity_ranges.append([x[1] - x[0], temperature_range[1] - x[0]])
                    break
                elif temperature_range[0] >= x[1] and temperature_range[1] >= (x[1] + x[2]) and temperature_range[0] < (x[1] + x[2]):
                    temperature_to_humidity_ranges.append([temperature_range[0] - x[0], x[1] + x[2] - x[0]])
                    temperature_to_humidity_ranges.append([x[1] + x[2], temperature_range[1]])
                    break
                elif temperature_range[0] < x[1] and temperature_range[1] >= (x[1] + x[2]):
                    temperature_to_humidity_ranges.append([temperature_range[0], x[1]])
                    temperature_to_humidity_ranges.append([x[1] - x[0], x[1] + x[2] - x[0]])
                    temperature_to_humidity_ranges.append([x[1] + x[2], temperature_range[1]])
                    break

        for humidity_range in temperature_to_humidity_ranges:
            for x in humidity_to_location:
                if humidity_range[0] >= x[1] and humidity_range[1] < (x[1] + x[2]):
                    humidity_to_location_ranges.append([humidity_range[0] - x[0], humidity_range[1] - x[0]])
                    break
                elif humidity_range[0] < x[1] and humidity_range[1] < (x[1] + x[2]) and humidity_range[1] > x[1]:
                    humidity_to_location_ranges.append([humidity_range[0], x[1]])
                    humidity_to_location_ranges.append([x[1] - x[0], humidity_range[1] - x[0]])
                    break
                elif humidity_range[0] >= x[1] and humidity_range[1] >= (x[1] + x[2]) and humidity_range[0] < (x[1] + x[2]):
                    humidity_to_location_ranges.append([humidity_range[0] - x[0], x[1] + x[2] - x[0]])
                    humidity_to_location_ranges.append([x[1] + x[2], humidity_range[1]])
                    break
                elif humidity_range[0] < x[1] and humidity_range[1] >= (x[1] + x[2]):
                    humidity_to_location_ranges.append([humidity_range[0], x[1]])
                    humidity_to_location_ranges.append([x[1] - x[0], x[1] + x[2] - x[0]])
                    humidity_to_location_ranges.append([x[1] + x[2], humidity_range[1]])
                    break

        seeds_to_test = [x[0] for x in humidity_to_location_ranges]

        print(seeds_to_test)

        for seed in seeds_to_test:
            running_location = int(seed)
            for soil in seed_to_soil:
                if running_location > soil[1] and running_location < (soil[1] + soil[2]):
                    running_location = running_location - soil[1] + soil[0]
                    break
            for fertilizer in soil_to_fertilizer:
                if running_location > fertilizer[1] and running_location < (fertilizer[1] + fertilizer[2]):
                    running_location = running_location - fertilizer[1] + fertilizer[0]
                    break
            for water in fertilizer_to_water:
                if running_location > water[1] and running_location < (water[1] + water[2]):
                    running_location = running_location - water[1] + water[0]
                    break
            for light in water_to_light:
                if running_location > light[1] and running_location < (light[1] + light[2]):
                    running_location = running_location - light[1] + light[0]
                    break
            for temperature in light_to_temperature:
                if running_location > temperature[1] and running_location < (temperature[1] + temperature[2]):
                    running_location = running_location - temperature[1] + temperature[0]
                    break
            for humidity in temperature_to_humidity:
                if running_location > humidity[1] and running_location < (humidity[1] + humidity[2]):
                    running_location = running_location - humidity[1] + humidity[0]
                    break
            for location in humidity_to_location:
                if running_location > location[1] and running_location < (location[1] + location[2]):
                    running_location = running_location - location[1] + location[0]
                    break
            answer = min(answer, running_location)

    return answer

if __name__ == '__main__':
    print(solution())