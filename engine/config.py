config = {}

def read_config():
    with open('config.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace('\n', '')
            if line[0] == ';':
                continue
            comment_idx = 0
            values = line.split('=')
            config[values[0]] = values[1]

def get_param_value(param_name: str) -> str:
    return config[param_name]