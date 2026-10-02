import json
m = json.load(open("target/manifest.json"))
for k, v in m["nodes"].items():
    if k.startswith("test."):
        print(k.split(".")[2], "| sev:", v["config"].get("severity"), "| tags:", v["config"].get("tags"),
              "| meta:", v["config"].get("meta"), "| desc:", v.get("description"))