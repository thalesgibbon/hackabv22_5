import json

# TODO
# apos adquirir volume de + 50 mil dados de motoristas de uber,
# subir os dados no vertex e criar o modelo de machine learning para bons motoristas
# solicitamos o access token para uber, porem nao recebemos a tempo do hackathon


def generate_score(driver_id):
    f = open(f'exports/{driver_id}/partners_me.json')
    data = json.load(f)

    if data['rating'] > 4:
        score = 100
    elif data['rating'] > 3:
        score = 90
    elif data['rating'] > 2:
        score = 60
    else:
        score = 30
    return score
