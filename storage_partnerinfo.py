import json
import os
import uber_lib


def storage_partnerinfo(driver_id):
    direxport = f'exports/{driver_id}/'
    os.makedirs(direxport)

    partner_me = uber_lib.get_partner_me()
    out_file = open(direxport + "partner_me.json", "w")
    json.dump(partner_me, out_file)

    partner_payments = uber_lib.get_partner_payments()
    out_file = open(direxport + "partner_payments.json", "w")
    json.dump(partner_payments, out_file)

    partner_trips = uber_lib.get_partner_trips()
    out_file = open(direxport + "partner_trips.json", "w")
    json.dump(partner_trips, out_file)

    print('export feito com sucesso')
