"""Constants for NextDNS integration."""
from datetime import timedelta

ATTR_DNSSEC = "dnssec"
ATTR_ENCRYPTION = "encryption"
ATTR_IP_VERSIONS = "ip_versions"
ATTR_PROTOCOLS = "protocols"
ATTR_STATUS = "status"

CONF_PROFILE_ID = "profile_id"
CONF_PROFILE_NAME = "profile_name"

UPDATE_INTERVAL_ANALYTICS = timedelta(minutes=10)

DOMAIN = "nextdns"
