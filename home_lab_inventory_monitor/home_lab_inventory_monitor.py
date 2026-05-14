import sys
containers=["pihole","nginx","plex"]
while True:
   
    action=input("What do you want to do?: ").strip().lower()

    match action:
        case "add":
            newcontainer=input("Name of the new container: ").strip().lower()
            containers.append(newcontainer)
            print(f"{containers}")
        case "delete":
            containername=input("Write the container name: ").strip().lower()
            if containername in containers:
                containers.remove(containername)
                print(f"{containers}")
            else:
                print("The container name doesn't exists")
        case "see":
            length=len(containers)
            print(f"You have {length} actives containers: {sorted(containers)}")
        case "exit":
            sys.exit(0)
        case _:
            print("This option doesn't exists or is incorrect")