# Your localhost IP address is 127.0.0.1. The process of defanging basically surrounds all the dots with brackets. The end result is 127[.]0[.]0[.]1. Easy!


def defanging_ip(adress: str) -> str:
    splitted_adress = adress.split('.')
    return '[.]'.join(splitted_adress)


print(defanging_ip("192.168.172.1"))