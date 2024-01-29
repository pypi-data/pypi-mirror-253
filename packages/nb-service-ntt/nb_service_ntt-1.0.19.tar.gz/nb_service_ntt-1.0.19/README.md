# Netbox Nbservice
[Netbox](https://github.com/netbox-community/netbox) Plugin for ITSM service mapping.

## Compatibility

This plugin in compatible with [NetBox](https://netbox.readthedocs.org/) 3.7.
Tested in versions: 3.7.1

## Installation

Add the following line to /opt/netbox/local_requirements.txt with
```
nb-service-ntt
```

Enable the plugin in /opt/netbox/netbox/netbox/configuration.py:
```
PLUGINS = ['nb_service_ntt']
```

Runs /opt/netbox/upgrade.sh

```
sudo /opt/netbox/upgrade.sh
```