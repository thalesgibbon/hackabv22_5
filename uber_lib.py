import json


def get_mockfile(name):
    f = open(f'mockfiles/{name}')
    return json.load(f)


def get_partner_me():
    return get_mockfile('partners_me.json')


def get_partner_payments():
    return get_mockfile('partners_me.json')


def get_partner_trips():
    return get_mockfile('partners_me.json')
