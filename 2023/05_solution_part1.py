# this approach works for part 1 but is completely useless for part 2
# because of large and many numbers

input_file = "05_input.txt"

with open(input_file) as f:
    raw = f.read().split("\n\n")

    
# get seeds
seeds_raw = [entry for entry in raw if "seeds" in entry]
seeds = seeds_raw[0].split(' ')[1:]
seeds = [int(seed) for seed in seeds]

# generate steps
step_names = ['seed-to-soil',
              'soil-to-fertilizer',
              'fertilizer-to-water',
              'water-to-light',
              'light-to-temperature',
              'temperature-to-humidity',
              'humidity-to-location']

all_steps = []

for step_name in step_names:
    steps_raw = [entry for entry in raw if step_name in entry]
    converters_raw = steps_raw[0].split('\n')[1:]
    converters_digitized = [[int(inner_item) for inner_item in item.split(' ')] for item in converters_raw]
    
    converters_by_step = []
    for converter_digitized in converters_digitized:
        converter = {'dst': range(converter_digitized[0], converter_digitized[0]+converter_digitized[2]),
                     'src': range(converter_digitized[1], converter_digitized[1]+converter_digitized[2])}
        converters_by_step.append(converter)
    
    all_steps.append({'step': step_name, 'converters': converters_by_step})

#%%

def convert_input_to_output(number, converters):
    result = number

    for converter in converters:
        try:
            index = converter['src'].index(number)
            result = converter['dst'][index]
        except ValueError:
            pass
        
    return result
    
#%%

outputs = []

min_output = 9999999999999999

for i in range(0, len(seeds), 2):
    for seed in range(seeds[i], seeds[i]+seeds[i+1]):
        input_ = seed
        for step in all_steps:
            output = convert_input_to_output(input_, step['converters'])
            input_ = output
        # print(f'{seed=} --> {output=}')
        min_output=min(output, min_output)
        #outputs.append(output)
    print(f"tuple {i=}")
        
#print(f'{min(outputs)=}')
print(f'{min_output=}')
