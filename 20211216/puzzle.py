#%%
import csv
import numpy as np

bin_dict = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


with open("input.csv", "r") as f:
    reader = csv.reader(f, delimiter="\n")
    for i, line in enumerate(reader):
        hex = line[0]

binary = "".join([bin_dict[i] for i in hex])


def parse_literals(packet):
    end = False
    i = 0
    bits = []
    while not end:
        bit, packet = packet[:5], packet[5:]
        bits.append(bit[1:])
        if bit[0] == "0":
            end = True
        i += 1
    return bits, packet


def packet_parse(packet):
    version, packet = int(int(packet[:3], base=2)), packet[3:]
    type_id, packet = int(int(packet[:3], base=2)), packet[3:]

    if type_id == 4:
        literals, packet = parse_literals(packet)
        return (
            {
                "version": version,
                "type_id": type_id,
                "literals": literals,
                "value": int("".join(literals), base=2),
            },
            packet,
        )
    elif int(packet) == 0:
        return None, ""
    else:
        length_type_id = int(packet[0])
        packets = []
        if length_type_id == 0:
            packets_length_max, packet = int(packet[1:16], 2), packet[16:]
            subpacket, packet = packet[:packets_length_max], packet[packets_length_max:]
            while subpacket:
                _p, subpacket = packet_parse(subpacket)
                packets.append(_p)
        else:
            packets_num_max, packet = int(packet[1:12], 2), packet[12:]
            for i in range(packets_num_max):
                _p, packet = packet_parse(packet)
                packets.append(_p)
        return (
            {"version": version, "type_id": type_id, "subpackets": packets,},
            packet,
        )


all_packets = {}
while len(binary):
    all_packets, binary = packet_parse(binary)
    if len(binary) == 0:
        break
    if int(binary) == 0:
        break


def version_sum(packet):
    if "subpackets" in packet:
        return packet["version"] + sum([version_sum(p) for p in packet["subpackets"]])
    else:
        return packet["version"]


def value(packet):
    if packet["type_id"] == 4:
        return packet["value"]
    elif packet["type_id"] == 0:
        return sum([value(i) for i in packet["subpackets"]])
    elif packet["type_id"] == 1:
        x = 1
        for i in packet["subpackets"]:
            x = x * value(i)
        return x
    elif packet["type_id"] == 2:
        return min([value(i) for i in packet["subpackets"]])
    elif packet["type_id"] == 3:
        return max([value(i) for i in packet["subpackets"]])
    elif packet["type_id"] == 5:
        return (
            1 if value(packet["subpackets"][0]) > value(packet["subpackets"][1]) else 0
        )
    elif packet["type_id"] == 6:
        return (
            1 if value(packet["subpackets"][0]) < value(packet["subpackets"][1]) else 0
        )
    elif packet["type_id"] == 7:
        return (
            1 if value(packet["subpackets"][0]) == value(packet["subpackets"][1]) else 0
        )


print(value(all_packets))
# print(version_sum(all_packets))
# all_packets

