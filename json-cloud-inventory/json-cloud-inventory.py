import json
with open("cloud_inventory.json", "r") as file:
    data_total = json.load(file)
    with open("storage_alert.log", "w") as log:
        for info in data_total:
            hostname=info["hostname"]
            total_storage=sum(info["disks"])
            if info["region"] == "eu-west" and total_storage > 250:
                log.write(f"ALERTA: {hostname} supera el límite en eu-west\n")

