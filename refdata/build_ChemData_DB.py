from tinydb import TinyDB, Query
import os
import json

with open('Config.json') as json_config_file:
    config = json.load(json_config_file)

filename = config["rootdir"] + config["ChemDataDB"]["filename"]

if os.path.exists(filename):
    print("Removing:"+filename)
    os.remove(filename)

density_data_list =[
{"chemicalName":"acetic acid","tempurature":"25","density":"1049","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"acetone","tempurature":"25","density":"784.6","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"acetonitrile","tempurature":"20","density":"782","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"ethanol","tempurature":"25","density":"785.1","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"methanol","tempurature":"25","density":"786.5","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"propyl alcohol","tempurature":"25","density":"800.0","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"ammonia","tempurature":"25","density":"823.5","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"aniline","tempurature":"25","density":"1019","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"benzene","tempurature":"25","density":"873.8","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"bromine","tempurature":"25","density":"3120","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"butyric acid","tempurature":"20","density":"959","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"butane","tempurature":"25","density":"599","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"n-butyl acetate","tempurature":"20","density":"880","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"n-butyl alcohol","tempurature":"20","density":"810","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"phenol at 15C","tempurature":"15","density":"956","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"carbon disulfide","tempurature":"25","density":"1261","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"carbon tetrachloride","tempurature":"25","density":"1584","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"castor oil","tempurature":"25","density":"956.1","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"chloride","tempurature":"25","density":"1560","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"chlorobenzene","tempurature":"20","density":"1106","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"chloroform at 20C","tempurature":"20","density":"1489","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"chloroform","tempurature":"25","density":"1465","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"coconut oil","tempurature":"15","density":"924","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"cotton seed oil","tempurature":"15","density":"926","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"cresol","tempurature":"25","density":"1024","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"creosote","tempurature":"15","density":"1067","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"cyclohexane","tempurature":"20","density":"779","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"cyclopentane","tempurature":"20","density":"745","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"diethyl ether","tempurature":"20","density":"714","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"o-dichlorobenzene","tempurature":"20","density":"1306","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"dichloromethane at 20C","tempurature":"20","density":"1326","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"diethylene glycol","tempurature":"15","density":"1120","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"dichloromethane","tempurature":"20","density":"1326","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"dimethyl acetamide","tempurature":"20","density":"942","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"n,n-dimethylformamide","tempurature":"20","density":"949","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"dimethyl sulfoxide","tempurature":"20","density":"1100","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"ethane","tempurature":"-89","density":"570","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"ether","tempurature":"25","density":"713.5","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"ethylamine","tempurature":"16","density":"681","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"ethyl acetate","tempurature":"20","density":"901","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"ethanol at 20C","tempurature":"20","density":"789","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"ethyl ether","tempurature":"20","density":"713","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"ethylene dichloride","tempurature":"20","density":"1253","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"ethylene glycol","tempurature":"25","density":"1097","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"trichlorofluoromethane refrigerant r-11","tempurature":"25","density":"1476","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"dichlorodifluoromethane refrigerant r-12","tempurature":"25","density":"1311","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"chlorodifluoromethane refrigerant r-22","tempurature":"25","density":"1194","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"formaldehyde","tempurature":"45","density":"812","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"formic acid 10 percent concentration","tempurature":"20","density":"1025","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"formic acid 80 precent concentration","tempurature":"20","density":"1221","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"furan","tempurature":"25","density":"1416","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"furforol","tempurature":"25","density":"1155","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"glycerine","tempurature":"25","density":"1259","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"glycerol","tempurature":"25","density":"1126","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"heating oil","tempurature":"20","density":"920","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"heptane","tempurature":"25","density":"679.5","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"hexane","tempurature":"25","density":"654.8","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"hexanol","tempurature":"25","density":"811","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"hexene","tempurature":"25","density":"671","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"hydrazine","tempurature":"25","density":"795","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"ionene","tempurature":"25","density":"932","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"isobutyl alcohol","tempurature":"20","density":"802","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"iso-octane","tempurature":"20","density":"692","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"isopropyl alcohol","tempurature":"20","density":"785","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"isopropyl myristate","tempurature":"20","density":"853","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"linolenic acid","tempurature":"25","density":"897","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"linseed oil","tempurature":"25","density":"929.1","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"machine oil","tempurature":"20","density":"910","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"mercury","tempurature":"25","density":"13590","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"methane","tempurature":"-164","density":"465","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"methanol at 20C","tempurature":"20","density":"791","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"methyl isoamyl ketone","tempurature":"20","density":"888","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"methyl isobutyl ketone","tempurature":"20","density":"801","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"methyl n-propyl ketone","tempurature":"20","density":"808","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"methyl t-butyl ether","tempurature":"20","density":"741","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"n-methylpyrrolidone","tempurature":"20","density":"1030","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"methyl ethyl ketone","tempurature":"20","density":"805","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"milk","tempurature":"15","density":"1020","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"naphtha","tempurature":"15","density":"665","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"wood naphtha, wood","tempurature":"25","density":"960","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"napthalene","tempurature":"25","density":"820","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"nitric acid","tempurature":"0","density":"1560","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"ocimene","tempurature":"25","density":"798","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"octane","tempurature":"15","density":"698.6","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"oil of resin","tempurature":"20","density":"940","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"oil of turpentine","tempurature":"20","density":"870","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"oil, lubricating","tempurature":"20","density":"900","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"olive oil","tempurature":"20","density":"920","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"oxygen (liquid)","tempurature":"-183","density":"1140","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"paraffin","tempurature":"","density":"800","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"palmitic acid","tempurature":"25","density":"851","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"pentane at 20C","tempurature":"20","density":"626","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"pentane","tempurature":"25","density":"625","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"perchlor ethylene","tempurature":"20","density":"1620","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"petroleum ether","tempurature":"20","density":"640","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"phenol","tempurature":"25","density":"1072","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"phosgene","tempurature":"0","density":"1378","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"phytadiene","tempurature":"25","density":"823","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"pinene","tempurature":"25","density":"857","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"propane","tempurature":"-40","density":"493.5","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"propane, r-290","tempurature":"25","density":"494","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"propanol","tempurature":"25","density":"804","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"propylenearbonate","tempurature":"20","density":"1201","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"propylene","tempurature":"25","density":"514.4","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"propylene glycol","tempurature":"25","density":"965.3","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"pyridine","tempurature":"25","density":"979","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"pyrrole","tempurature":"25","density":"966","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"rape seed oil","tempurature":"20","density":"920","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"resorcinol","tempurature":"25","density":"1269","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"rosin oil","tempurature":"15","density":"980","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"sea water","tempurature":"25","density":"1025","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"silane","tempurature":"25","density":"718","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"silicone oil","tempurature":"25","density":"965","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"sodium hydroxide (caustic soda)","tempurature":"15","density":"1250","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"sorbaldehyde","tempurature":"25","density":"895","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"soya bean oil","tempurature":"15","density":"926","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"stearic acid","tempurature":"25","density":"891","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"sulfuric acid 95 percent concentration","tempurature":"20","density":"1839","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"sulfurus acid","tempurature":"-20","density":"1490","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"sugar solution 68 brix","tempurature":"15","density":"1338","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"sunflower oil","tempurature":"20","density":"920","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"styrene","tempurature":"25","density":"903","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"terpinene","tempurature":"25","density":"847","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"tetrahydrofuran","tempurature":"20","density":"888","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"toluene","tempurature":"20","density":"867","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"trichlor ethylene","tempurature":"20","density":"1470","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"triethylamine","tempurature":"20","density":"728","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"trifluoroacetic acid","tempurature":"20","density":"1489","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"turpentine","tempurature":"25","density":"868.2","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"heavy water","tempurature":"11.6","density":"1105","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"pure water","tempurature":"4","density":"1000","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"whale oil","tempurature":"15","density":"925","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"o-xylene","tempurature":"20","density":"880","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"duplicate","tempurature":"20","density":"880","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
{"chemicalName":"duplicate","tempurature":"20","density":"880","units":"kg/m3","source":"https://www.engineeringtoolbox.com/liquids-densities-d_743.html"},
]

unique_compounds = []
for datum in density_data_list:
    density=datum.pop("density")
    chemicalName = datum["chemicalName"]
    if chemicalName in unique_compounds:
        if chemicalName == "duplicate":
            # I keep one duplicate in there for testing
            continue
        print("error:" + chemicalName + " already in db")
        exit()
    else:
        unique_compounds.append(chemicalName)
    digits = len(density)
    if ("." in density):
        digits -=1
    datum["value"] = str(round(float(density)/float(1000),digits))
    datum["property"] = "density"
    datum["units"] = "g/mL"
    #print(datum)

CV_db = TinyDB(filename)

CV_db.insert_multiple(density_data_list)

print("File:"+filename+" created with "+str(len(CV_db))+" items")
