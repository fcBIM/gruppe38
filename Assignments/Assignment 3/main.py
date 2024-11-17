
import json
import ifcopenshell
import os
import time
import uuid

#IFC file import is taken from https://github.com/timmcginley/
'''
    load the IFC file
'''
name = '/Users/fredemollegaard/Desktop/Adv.BIM/CES_BLD_24_06_ARC'

model_url = name+".ifc"
start_time = time.time()

if (os.path.exists(model_url)):
    model = ifcopenshell.open(model_url)
    print("\n\tFile    : {}.ifc".format(name))
    print("\tLoad    : {:.2f}s".format(float(time.time() - start_time)))

    #start_time = time.time()
    #print("\tConvert : {:.4f}s".format(float(time.time() - start_time)))

else:
    print("\nERROR: please check your model folder : " +model_url+" does not exist")




# Retrieve all wall types in the IFC file
wall_types = model.by_type("IfcWallType")

# If you want to get individual wall instances (e.g., IfcWall)
walls = model.by_type("IfcWall")

# Print out the names or IDs of all wall types
print("Wall Types in IFC File:")
for wall_type in wall_types:
    print(f"Wall Type Name: {wall_type.Name}, ID: {wall_type.id()}")

# Optional: Print information for individual wall instances
print("\nIndividual Wall Instances in IFC File:")
for wall in walls:
    print(f"Wall Name: {wall.Name}, ID: {wall.id()}")

    



