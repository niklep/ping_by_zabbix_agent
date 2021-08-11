# -*- coding: utf-8 -*-
"""
Script for icmp checks by zabbix agent
"""

from icmplib import ping
import sys

def packetloss(target, count, interval, timeout, payload_size):
    packetloss = ping(target, int(count), int(interval), int(timeout), payload_size=int(payload_size))
    return packetloss


if __name__ == "__main__":

    if (len(sys.argv) < 6):
        print("You must set arguments: target, count, interval, timeout, payload_size")
        exit(1)
    result = packetloss(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    json_result = {
        "min_rtt": result.min_rtt,
        "avg_rtt": result.avg_rtt,
        "max_rtt": result.max_rtt,
        "packet_loss": int(result.packet_loss*100),
        "jitter": result.jitter
    }
    str_json = str(json_result).replace('\'', '\"')
    print(str_json)
