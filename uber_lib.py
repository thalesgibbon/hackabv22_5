import json


def get_mockfile(name):
    f = open(f'mockfiles/{name}')
    return json.load(f)


def get_partners_me():
    return get_mockfile('partners_me.json')


def get_partners_payments():
    return get_mockfile('partners_payments.json')


def get_partners_trips():
    return get_mockfile('partners_trips.json')
