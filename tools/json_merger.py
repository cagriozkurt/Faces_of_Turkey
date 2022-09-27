import os
import json

directory = "output"

master_dict = {"players": []}

for filename in os.listdir(directory):
    dirf = os.path.join(directory, filename)
    if os.path.isfile(dirf):
        with open(dirf) as f_r:
            json_dict = json.load(f_r)
            for single_dict in json_dict["players"]:
                master_dict["players"].append(single_dict)

with open("final.json", "w") as f_w:
    json.dump(master_dict, f_w, ensure_ascii=False, indent=4)
