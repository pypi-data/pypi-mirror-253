import json
from netbox import NetBoxClient

nb = NetBoxClient(
    base_url="http://127.0.0.1:8000/", token="1dc6fa5bfcef8390dd83a261c36ed8f1551b2d6b"
)

# 1. List (paginated)
ret = nb.dcim.sites.list(limit=3)

# 2. Filtered List
ret = nb.dcim.sites.list(region_id="43")

# 3. All
ret = nb.dcim.sites.all()

# 4. Get
ret = nb.dcim.sites.get(24)

# 5. Create
ret = nb.dcim.sites.create(name="foo3", slug="foo3")

# 6. Bulk Create
data = [
    {"name": "foo4", "slug": "foo4"},
    {"name": "foo5", "slug": "foo5"},
    {"name": "foo6", "slug": "foo6"},
]
ret = nb.dcim.sites.create(data)

# 7. Update
ret = nb.dcim.sites.update(26, name="foo2-new", slug="foo2-new-slug")

# 8. Bulk Update
data = [
    {"id": 28, "name": "foo4-new", "slug": "foo4-new"},
    {"id": 29, "name": "foo5-new", "slug": "foo5-new"},
]
ret = nb.dcim.sites.update(data)

# 9. Delete
ret = nb.dcim.sites.delete(37)

# 10. Bulk Delete
data = [{"id": 25}, {"id": 27}]
ret = nb.dcim.sites.delete(data)
