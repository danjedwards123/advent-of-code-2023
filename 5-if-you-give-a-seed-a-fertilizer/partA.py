def solution() -> int:
    answer = float("inf")

    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        mappings = ["seed_to_soil", "soil_to_fertilizer", "fertilizer_to_water", "water_to_light", "light_to_temperature", "temperature_to_humidity", "humidity_to_location"]

        seeds = lines[0].split(':')[1].split()

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

        for seed in seeds:
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