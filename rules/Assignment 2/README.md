# Formalities
41934 Advanced Building Information Modeling 2024
We are group 38 and the focus area is Sustainability and materials. Our main objective is to be an analyst and develop a tool to help with a fuller LCA of a building.   
In terms of programming skills we answered this to the following question:  
#### I am confident coding in Python.  
we chose:  
- [x] Disagree.   
<br /> As we are fairly new but are interested in improving this skill.

### The chosen building 
We chose the #2406 building from last years Advanced Building Design course because it seems like the model have all the required data that we need in order for us to develop a relevant tool for our choice of use case.  
Claim is that the building will emit 6,74 kgC02eq/m2/year, and the claim is from the ARC report: BEATS -> CO2 -> 6,74 kgC02eq./m2/yr.  
The source of claim is from the file [#2406 ARC Report](https://github.com/fcBIM/gruppe38/blob/809fada3f66e063b730dfc2ff6c38421f6afafb6/rules/Assignment%202/files/CES_BLD_24_06_ARC.pdf) page 5.  
# Use Case
The use case for our work is going to be matching relevant IfcEntities with corresponding environmental data such as GWP of certain materials.  
By extracting the relevant entities and the underlying IfcMaterial or IfcMaterialLayer we want to match environmental data with that material. After a potential match the tool should now create a file (JSON) with all the matched data and the corresponding GWP score. Finally, we want to sum up the total GWP score of an IfcEntity in the BIM model to get a insights on the overall impact the entity and in the end the building will have on the environment.  
Preferably this tool will be able to match all materials in the building with a corresponding environmental score, but realistically with the limited time we have, it will print a list of some entities in the BIM model. This score could then be checked by calculating the amount from the #2406 report: [#2406 PM Appendix](https://github.com/fcBIM/gruppe38/blob/bfc0fecdb650550fa5acecadf90a5e590b67155d/rules/Assignment%202/files/CES_BLD_24_06_PM_Appendix.pdf) p. 2.

The claims will be checked after a complete interdisciplinary BIM model have been made, data such as entities and material choices would be needed for a complete LCA of the building. If we instead are looking for a specific part of the design of the building it will be specified further. 

The tool would be used for the design and post build phase, as the tool has a potential to guide with the maintenance choices of the built building.

The BIM purpose si to Gather, analyse and communicate the potential environmental impact of the specific materials as well as a full LCA of the building.

[Preliminary BPMN diagram](https://github.com/fcBIM/gruppe38/blob/2469687baea8ea2ae0baedddbf63d1b55d766b13/rules/Assignment%202/IMG/PreliminaryBPMN.png)

A2d: Scope the use case
From the ‘whole use case’ identify where a new script / function / tool is needed. Highlight this in your BPMN diagram. Show this clearly in a new SVG diagram. You may wish to change the SVG diagram, you can use inkscape for this task.
A2f: Information Requirements
Identify what information you need to extract from the model

Where is this in IFC?

Is it in the model?

Do you know how to get it in ifcOpenShell?


# Tool Idea  
Describe in words your idea for your own OpenBIM ifcOpenShell Tool in Python.

### Potential value  
- Facilitate a smooth and coordinated collaboration between designers and sustainability engineers
- Enable a more environmental friendly design process.
- Potential to reduce the design phase.
- Reduces documentation phase.


Produce a BPMN diagram to summarise your idea. Save this in a folder in your repository along with an SVG of the disagram and embed the SVG in the Markdown as an image.

A2f: Information Requirements
Identify what information you need to extract from the model

Where is this in IFC?

Is it in the model?

Do you know how to get it in ifcOpenShell?


# Software requirements to run this tool  

In order to be able to run this tool we expect the following softwares to be required:  
1. LCAByg
2. Microsoft package - Excel
3. IfcOpenShell
4. Python 3.10-12
