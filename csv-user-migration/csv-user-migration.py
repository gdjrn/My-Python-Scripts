import csv

rows = ['username', 'role', 'email', "status"]
with open("old_users.csv", "r") as f_csv:
      total_data = csv.DictReader(f_csv)
      my_data = list(total_data) 
      with open("migrate_users.csv", "w", newline="", encoding="utf-8") as f_csv2:
        with open("migrate_failed.log", "w", newline="", encoding="utf-8") as log:
            writer = csv.DictWriter(f_csv2, fieldnames=rows)
            writer.writeheader()
            for row in my_data:
                hostname=row["username"]
                if row["status"] == "active":
                    if "@" in row["email"]:
                        if row["role"] == "admin":   
                            row["role"] = "super_user"
                        writer.writerow(row)  
                    else:
                        log.write(f"ERROR: {hostname} is corrupt!\n")
                
                
            

                
