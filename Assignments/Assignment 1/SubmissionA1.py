#Formalities:
#Group 38 - Sustainability and materials, Claim: Total area of roof in the model.

#Claim is from the PM report: IFCRoof in ARC-model has the following square meter: 1479m^2, source of claim: file CES_BLD_24_06_PM_Appendix.pdf p. 5 Appendix b LCI for LCA 

# The script is inspired by Basic Example 2, that extracts the total beam length from the IFC file. 



# Make sure IfcOpenShell and model is imported.
#import ifcopenshell
#model = ifcopenshell.open('/Users/fredemollegaard/Desktop/Adv.BIM/CES_BLD_24_06_ARC.ifc')

#import ifcopenshell
#Import the correct IFC model:
#model = ifcopenshell.open('/Users/fredemollegaard/Desktop/Adv.BIM/CES_BLD_24_06_ARC.ifc')
#model = ifcopenshell.open('/Users/fredemollegaard/Desktop/Adv.BIM/CES_BLD_24_06_STR.ifc')

def roofArea(model):
    #Making sure the value of property doesn't change if run multiple times
    total_roof_area = 0

    #First we define the element we are interested in. For this case the object type IFCRoof.
    for entity in model.by_type("IfcRoof"):
    

        #Secondly we define the relation between the object type's different IfcElementQuantities and sort through to find the Area.
        for relDefinesByProperties in entity.IsDefinedBy:
            for prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
                
                if prop.Name == 'Area':
                    #Thirdly we ask it to calculate the total area of all the specified object types - IfcRoof.
                    total_roof_area += prop.NominalValue.wrappedValue

    #Fourthly, and last, we print the desired value and add a short descriptive text, for the reader to have a clear indication of what has been printed.
    result = print(f"\n The roof in the arc model has an area of {total_roof_area} square meters")
    return result
