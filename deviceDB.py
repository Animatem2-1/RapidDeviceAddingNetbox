import modelsDB


def device_database(dname, dmodel, duList, drack, dsite):
    dmodel = dmodel.format()
    if dname== "po" or dname == "pm" or dname == "pp":
        dname = dname.upper() + "/"
        if dname == "PO/" or dname == "PM/":
            dmodel = modelsDB.models[dname]
        fileAppend = open("netbox.txt", "a")
        for u in duList:
            #                       name,device_role,tenant,manufacturer(brand),device_type(dmodel),status,position,face,rack,site
            fileAppend.write("\r" + dname + u +","+ "Passive infrastructure" + "," + "ZHS" + "," + "Generic" + "," + dmodel + "," + "Active" + "," + u + "," + "Front" + "," + drack + "," + dsite)
        fileAppend.close()

    else:
        dmodel = modelsDB.models[dmodel]
        brand = ""
        if dmodel[0] == "W":
            brand = "Cisco"
        elif dmodel[1] == "D":
            brand = "Moxa"
        elif dmodel[1] == "X" or dmodel[0] == "M" or dmodel[0] == "S":
            brand = "Juniper"
        else:
            brand = ""
        fileAppend = open("netbox.txt", "a")
        for u in duList:
            fileAppend.write("\r" + dname + "," + "ZHS" + "," + dmodel + "," + u + "," + brand)
        fileAppend.close()
