from typing import Iterator, Optional
from util import *
from dataclasses import dataclass


@dataclass
class Packet:
    data: str
    version: int
    subpackets: "list[Packet]"
    value: Optional[int]


def parse_packet(packet: str) -> Packet:
    version = int(packet[0:3], 2)
    type_id = int(packet[3:6], 2)
    if type_id == 4:
        idx = 6
        literal = ""
        while idx + 5 <= len(packet):
            group = packet[idx : idx + 5]
            literal += group[1:]
            if group[0] == "0":
                break
            idx += 5
        literal = int(literal, 2)
        return Packet(packet[0 : idx + 5], version, [], literal)
    else:
        subpackets = []
        length_type_id = int(packet[6], 2)
        if length_type_id == 0:
            total_length = int(packet[7:22], 2)
            idx = 22
            curr_length = 0
            while curr_length < total_length:
                subpacket = parse_packet(packet[idx:])
                subpackets.append(subpacket)

                idx += len(subpacket.data)
                curr_length += len(subpacket.data)
            packet = Packet(packet[0:idx], version, subpackets, None)
        else:
            # length_type_id == 1
            num_subpackets = int(packet[7:18], 2)
            idx = 18
            for _ in range(num_subpackets):
                subpacket = parse_packet(packet[idx:])
                subpackets.append(subpacket)

                idx += len(subpacket.data)
            packet = Packet(packet[0:idx], version, subpackets, None)
    if type_id == 0:
        packet.value = sum(subpacket.value for subpacket in packet.subpackets)
    elif type_id == 1:
        packet.value = 1
        for subpacket in packet.subpackets:
            packet.value *= subpacket.value
    elif type_id == 2:
        packet.value = min(subpacket.value for subpacket in packet.subpackets)
    elif type_id == 3:
        packet.value = max(subpacket.value for subpacket in packet.subpackets)
    elif type_id == 5:
        packet.value = (
            1 if packet.subpackets[0].value > packet.subpackets[1].value else 0
        )
    elif type_id == 6:
        packet.value = (
            1 if packet.subpackets[0].value < packet.subpackets[1].value else 0
        )
    elif type_id == 7:
        packet.value = (
            1 if packet.subpackets[0].value == packet.subpackets[1].value else 0
        )
    return packet


def get_total_version(packet: Packet) -> int:
    return packet.version + sum(
        get_total_version(subpacket) for subpacket in packet.subpackets
    )


def solve(input: Optional[str]) -> Iterator[any]:
    data = bin(int(input, 16))[2:]
    while len(data) % 4 != 0:
        data = "0" + data

    packet = parse_packet(data)
    yield get_total_version(packet)
    yield packet.value
