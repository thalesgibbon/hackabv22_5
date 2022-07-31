import json


def generate_score(driver_id):
    f = open(f'exports/{driver_id}/partners_trips.json')
    data = json.load(f)

    if data['count'] > 3500:
        score = 100
    elif data['count'] > 2500:
        score = 90
    elif data['count'] > 1500:
        score = 60
    else:
        score = 30
    return score
