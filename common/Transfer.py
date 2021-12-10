import yaml

#
# def URLTransfer(locator, set, m):
#     f = open(locator)
#     content = yaml.load(f)
#     return content[set][m]['http']['path']
#
#
# def ParamTransfer(locator, set, m, n):
#     f = open(locator)
#     content = yaml.load(f)
#     return content[set][m]['http']['prameters'][n]


def URLTransfer(locator, set, m):
    f = open(locator)
    content = yaml.load(f)
    return content[set][m]['http']['path']


def ParamTransfer(locator, set, m, n):
    f = open(locator)
    content = yaml.load(f)
    return content[set][m]['http']['prameters'][n]