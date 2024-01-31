import json

from netbox import NetBoxClient
import pynetbox

nb = NetBoxClient(
    base_url="http://127.0.0.1:8000/", token="1dc6fa5bfcef8390dd83a261c36ed8f1551b2d6b"
)

pynb = pynetbox.api(
    'http://127.0.0.1:8000/', token='1dc6fa5bfcef8390dd83a261c36ed8f1551b2d6b'
)

# 1. List
ret = nb.dcim.sites.list(limit=3)

# 2. Filtered List
ret = nb.dcim.sites.list(region_id=43)
data = pynb.dcim.sites.filter(region_id=43)

# 3. All
ret = nb.dcim.sites.all()
data = pynb.dcim.sites.all()

# 4. Get
ret = nb.dcim.sites.get(24)
data = pynb.dcim.sites.get(24)

# 5. Create
ret = nb.dcim.sites.create(name="foo3", slug="foo3")
data = pynb.dcim.sites.create(name="foo3", slug="foo3")

# 6. Bulk Create
data = [
    {"name": "foo4", "slug": "foo4"},
    {"name": "foo5", "slug": "foo5"},
    {"name": "foo6", "slug": "foo6"},
]
ret = nb.dcim.sites.create(data)
data = pynb.dcim.sites.create(data)

# 7. Update
sites = nb.dcim.sites.filter(region_id=43).data
for site in sites:
    db.dcim.sites.update(name=site["name"] + "-test")

sites = list(pynb.dcim.sites.filter(region_id=43))
for site in sites:
    site.name = site.name + "-test"
pynb.dcim.sites.update(sites)
