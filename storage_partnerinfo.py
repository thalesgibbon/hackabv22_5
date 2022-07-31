import json
import os
import uber_lib


def storage_partnerinfo(driver_id):
    direxport = f'exports/{driver_id}/'
    os.makedirs(direxport)

    partners_me = uber_lib.get_partners_me()
    out_file = open(direxport + "partners_me.json", "w")
    json.dump(partners_me, out_file)

    partners_payments = uber_lib.get_partners_payments()
    out_file = open(direxport + "partners_payments.json", "w")
    json.dump(partners_payments, out_file)

    partners_trips = uber_lib.get_partners_trips()
    out_file = open(direxport + "partners_trips.json", "w")
    json.dump(partners_trips, out_file)

    print('export feito com sucesso')


if __name__ == "__main__":
    storage_partnerinfo('ID001')
    storage_partnerinfo('ID002')
    storage_partnerinfo('ID003')
