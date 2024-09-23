#Formalities:
# Group 38 - Sustainability and materials

#Claim: Layers of contruction
#Actual example: Terrain in ARC-model has the following constructions: Concrete 900mm, reinforcement steeel, screed layer, insulation (presure resistant)

#Source of claim: file CES_BLD_24_06_PM_Appendix.pdf p. 5 Appendix b LCI for LCA 

# The script isionspired by Basic Exampel 2 that gets the total beam lengt. 

# Make sure ifcopenshell and model is imported.
#import ifcopenshell
#model = ifcopenshell.open('/Users/fredemollegaard/Desktop/Adv.BIM/CES_BLD_24_06_ARC.ifc')

#import ifcopenshell
#Importer model:
#model = ifcopenshell.open('/Users/fredemollegaard/Desktop/Adv.BIM/CES_BLD_24_06_ARC.ifc')
#model = ifcopenshell.open('/Users/fredemollegaard/Desktop/Adv.BIM/CES_BLD_24_06_STR.ifc')

def roofArea(model):
    #Making sure the value of property doesn't change if run multiple times
    total_roof_area = 0

    #Firsrst we define the part of the building we're looking into.
    for entity in model.by_type("IfcRoof"):
    

        #Secondly we get sort throught the properties of the defined building part and define the property we'll look into.
        for relDefinesByProperties in entity.IsDefinedBy:
            for prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
                
                if prop.Name == 'Area':
                    #add the area to the total area
                    total_roof_area += prop.NominalValue.wrappedValue

    #Then we print the value of the property
    result = print(f"\n The roof in the arc model has n area of {total_roof_area} square meters")
    return result
