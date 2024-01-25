import struct
from collections import defaultdict


def write_pmu(twix_scan: dict, filename: str):
    pmu_end = b'\xFF\xFF\xFF\xFF'
    if 'pmu' in twix_scan and 'raw' in twix_scan['pmu']:
        with open(filename, 'wb') as fid:
            for pmu in twix_scan['pmu']['raw']:
                fid.write(pmu)
    else:
        raise ValueError('No PMU data found in twix scan')


def read_pmu(filename: str):
    pmu_end = b'\xFF\xFF\xFF\xFF'
    with open(filename, 'rb') as fid:
        data = fid.read()
    data = data.split(pmu_end)
    phys = _process_pmu(data)
    return phys


def _process_pmu(data):
    names = {0: 'ecg1', 1: 'ecg2', 2: 'ecg3', 3: 'ecg4', 4: 'pulse', 5: 'resp1', 6: 'resp2', 7: 'resp3', 8: 'ecg5', 9: 'ecg6', 10: 'ecg6'}
    pmu_end = b'\xFF\xFF\xFF\xFF'
    out = defaultdict(list)
    learn = defaultdict(list)
    for mdb in data:
        if len(mdb) < 60:
            continue

        packet_id = mdb[4:mdb.find(b'\x00', 4)].decode('ascii')
        is_learn = packet_id == 'PMULearnPhase'

        pmu_data = mdb[60:]
        index = pmu_data.find(pmu_end)
        index = index + 4 if index > 0 else -1
        pmu_data = pmu_data[0:index]
        timestamp1, timestamp2, packet_nr, duration, dummy = struct.unpack('<IIIHH', pmu_data[0:16])
        pos = 16
        while pos + 8 < len(pmu_data):
            magic, period = struct.unpack('<II', pmu_data[pos:pos + 8])
            pos += 8
            signal_length = int(duration / period) * 4
            if pos+signal_length >= len(pmu_data):
                break

            phys = struct.unpack('<{}I'.format(int(signal_length/4)),  pmu_data[pos:pos+signal_length])
            pos += signal_length
            name = names.get(magic)
            if name:
                if is_learn:
                    learn[name].extend(phys)
                else:
                    out[name].extend(phys)

    out['learn'] = learn
    out['raw'] = data
    return dict(out)
