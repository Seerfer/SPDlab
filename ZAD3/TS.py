from neh import NEHmodifications
from Johnson import Johnson

def initialize_shedule(times):
    if len(times) < 101:
        return NEHmodifications.neh_ext4(times)[0]
    else:
        return Johnson.multi_machines_Johnson(times)

def TS(times):
    schedule = initialize_shedule(times)

