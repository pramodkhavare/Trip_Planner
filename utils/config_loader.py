import yaml ,os 

def load_config(config_path : str = ".confg/config.yaml"):
    with open(config_path) as file:
        config = yaml.load(file)

        return config
