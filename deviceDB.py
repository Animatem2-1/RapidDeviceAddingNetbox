import modelsDB


def device_database(dname, dmodel, duList):
    dmodel = dmodel.format()
    if dname== "po" or dname == "pm" or dname == "pp":
        dname = dname.upper() + "/"
        fileAppend = open("netbox.txt", "a")
        for u in duList:
            #                       name,device_role,tenant,manufacturer,device_type,status,rack,position,face,site
            fileAppend.write("\r" + dname + u + "," + dmodel + "," + u)
        fileAppend.close()

    else:
        dmodel = modelsDB.models[dmodel]
        brand = ""
        if dmodel[0] == "W":
            brand = "Cisco"
        elif dmodel[1] == "D":
            brand = "Moxa"
        elif dmodel[0:1] == "EX" or dmodel[0] == "M" or dmodel[0] == "S":
            brand = "Juniper"
        else:
            brand = ""
        fileAppend = open("netbox.txt", "a")
        for u in duList:
            fileAppend.write("\r" + dname + "," + "ZHS" + "," + dmodel + "," + u + "," + brand)
        fileAppend.close()
