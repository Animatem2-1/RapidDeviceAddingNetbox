import modelsDB


def device_database(dname, dmodel, duList):
    dmodel = dmodel.format()
    if dname== "po" or dname == "pm" or dname == "pp":
        dname = dname.upper() + "/"
        dmodel = "panel"
        fileAppend = open("netbox.txt", "a")
        for x in duList:
            fileAppend.write("\r"+dname+x+","+dmodel+","+x)
        fileAppend.close()

    else:
        dmodel = modelsDB.models[dmodel]
        #if modelsDB.models["shortname"] == dmodel: dmodel = modelsDB.model1["fullname"]






    
