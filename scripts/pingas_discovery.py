# -*- coding: utf-8 -*-
"""
Script for Zabbix discovery of pingas targets
link to github:
https://...............................................................
"""
import os
import json

if __name__ == "__main__":

    targets_file_name = os.path.join("C:", os.sep, "Program Files", "Zabbix Agent", "zabbix_agentd.conf.d", "pingas_targets.txt")
    with open(targets_file_name, encoding="utf-8") as f:
        targets = f.read().splitlines()

    data = [{"{#TARGET}": target} for target in targets]
    print(json.dumps({"data": data}, indent=4))
