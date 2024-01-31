import json
from netbox import NetBoxClient

nb = NetBoxClient(
    base_url="http://127.0.0.1:8000/", token="bd316de5adff1f3cd1d2e28bb0a326ff72d0b318"
)

ret = nb.dcim.sites.all()
print(json.dumps(ret.data, indent=4))

b_terminations = [
    {
      "object_type": "dcim.interface",
      "object_id": 1639
    }
]

ret = nb.dcim.cables.update(133, b_terminations=b_terminations)
print(ret)
