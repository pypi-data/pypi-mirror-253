import json

from netbox import NetBoxClient

nb = NetBoxClient(
    base_url="http://127.0.0.1:8000/", token="1dc6fa5bfcef8390dd83a261c36ed8f1551b2d6b"
)


def print_response(response):
    print(f"status: {response.status_code}")
    print(response.data)


# response = nb.schema.get(format="yaml")
# print_response(response)
# response = nb.status.get()
# print_response(response)

print("")
print("1. List")
print("--------------------------------------------")
ret = nb.dcim.sites.list(limit=3)
print(json.dumps(ret.data, indent=4))
print(ret.pagination)

print("")
print("2. Filtered List")
print("--------------------------------------------")
sites = nb.dcim.sites.list(region_id="43")
print(sites)

print("")
print("3. All")
print("--------------------------------------------")
ret = nb.dcim.sites.all(limit=3)
print(json.dumps(ret.data, indent=4))
print(ret.pagination)

print("")
print("4. Get")
print("--------------------------------------------")
site = nb.dcim.sites.get(24)
print(site)

"""
print("")
print("5. Create")
print("--------------------------------------------")
ret = nb.dcim.sites.create(name="foo3", slug="foo3")
print(ret)

print("")
print("6. Bulk Create")
print("--------------------------------------------")
data = [
    {"name": "foo4", "slug": "foo4"},
    {"name": "foo5", "slug": "foo5"},
    {"name": "foo6", "slug": "foo6"},
]
ret = nb.dcim.sites.create(data)
print(ret)

print("")
print("7. Update")
print("--------------------------------------------")
ret = nb.dcim.sites.update(26, name="foo2-new", slug="foo2-new-slug")
print(ret)

print("")
print("8. Bulk Update")
print("--------------------------------------------")
data = [
    {"id": 28, "name": "foo4-new", "slug": "foo4-new"},
    {"id": 29, "name": "foo5-new", "slug": "foo5-new"},
]
ret = nb.dcim.sites.update(data)
print(ret)

print("")
print("9. Delete")
print("--------------------------------------------")
response = nb.dcim.sites.delete(37)
print_response(response)

print("")
print("10. Bulk Delete")
print("--------------------------------------------")
data = [{"id": 25}, {"id": 27}]
response = nb.dcim.sites.delete(data)
print_response(response)
"""


# print(nb.circuits.circuits.list())
# circuit = nb.circuits.circuits.get(19)
# print("")
# print(type(circuit))
# print(circuit)
# print(circuit["id"])
# import json
#
# print(json.dumps(circuit, indent=4))
# sites = nb.dcim.sites.list()
# print(json.dumps(sites, indent=4))
# nb.dcim.sites.create(name="foo2", slug="foo2")

# racks = nb.dcim.racks.list()
# print(json.dumps(racks, indent=4))
