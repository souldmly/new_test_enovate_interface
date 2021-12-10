import yaml


def urlTransfer(url, set, count):
    f = open(url)
    content = yaml.load(f)
    return content[set][count]['http']['path']

print(urlTransfer(r'E:\自动化\new_enovate_interface_auto\config\env_config.yml', 'tests', 0))