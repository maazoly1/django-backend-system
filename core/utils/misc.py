import yaml

def yaml_coerce(value):
    # convert string dict value to a proper python dict

    if isinstance(value, str):
        # Conversion is usefull because sometimes we need to stringify settings in docker file
        return yaml.load(f'dummy: {value}', loader=yaml.SafeLoader)['dummy']
    
    return value