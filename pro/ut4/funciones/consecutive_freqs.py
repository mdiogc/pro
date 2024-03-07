# ************************************
# FRECUENCIA DE ELEMENTOS CONSECUTIVOS
# ************************************


def cfreq(input_list, output_format=False):

    frequency_dict = {}
    previous_element = None
    for element in input_list:
        if element == previous_element:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
        previous_element = element

    if not output_format:
        return list(frequency_dict.items())
    else:
        return ', '.join([f"{key}:{value}" for key, value in frequency_dict.items()])
