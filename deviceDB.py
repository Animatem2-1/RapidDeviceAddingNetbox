import modelsDB


def device_database(dname, dmodel, du):
    dmodel = dmodel.format()
    if dname== "po" or dname == "pm" or dname == "pp":
        dname = dname.upper() + "/" + du
        dmodel = "panel"
    else:
        dmodel = modelsDB.models[dmodel]
        #if modelsDB.models["shortname"] == dmodel: dmodel = modelsDB.model1["fullname"]





    fileAppend = open("netbox.txt", "a")
    fileAppend.write("\r"+dname+","+dmodel+","+du)
    fileAppend.close()
