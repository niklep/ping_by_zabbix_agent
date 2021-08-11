set first_path=%cd%
echo %first_path%

chdir icmplib-3.0
echo %cd%

python setup.py install

chdir %first_path%

copy ".\zabbix_agentd.conf.d\pingas.conf" "C:\Program Files\Zabbix Agent\zabbix_agentd.conf.d\pingas.conf"
copy ".\zabbix_agentd.conf.d\pingas_targets.txt" "C:\Program Files\Zabbix Agent\zabbix_agentd.conf.d\pingas_targets.txt"

mkdir "C:\Program Files\Zabbix Agent\scripts"

copy ".\scripts\pingas.py" "C:\Program Files\Zabbix Agent\scripts\pingas.py"
copy ".\scripts\pingas_discovery.py" "C:\Program Files\Zabbix Agent\scripts\pingas_discovery.py"

distr\x64\fart "C:\Program Files\Zabbix Agent\zabbix_agentd.conf" "# Timeout=3" "Timeout=30"
distr\x64\fart "C:\Program Files\Zabbix Agent\zabbix_agentd.conf" "zabbix_agentd.conf.d\\" "zabbix_agentd.conf.d\*.conf"
