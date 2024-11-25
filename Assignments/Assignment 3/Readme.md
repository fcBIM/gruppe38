# Assignment 3 Tool:

## 01 The IFC model
The IFC model used for developing this script is from the course Advanced Building Design course group #2406.
We are using the ARC IFC file in order to find alle the IfcEntities' MaterialLayers and their corresponding quantities. These findings will be matched with the environmental data provided by group #2406 PM appendix B to both fact check their results as well as having an easy access to environmental data for our tool.

## 02 Explanation on this markdown file:
The work done for Assignment 3 has been built on top of the work provided in Assignments 1 and 2, although some considerable modifications has been made.

The following list will explain some major changes for the tool:
- **Less ambitious:** Because of the limitations of our python skills as well as the deadline set by the course responsible, the ambition on creating a tool that can include all IfcEntities and calculate the environmental impact has been reduced to a single entity.
- **Describe entity once chosen** Single and simple entity such as internal wall (if there are multiple layers in a single material layer, then we can't match the correct data to the layer). This change is because of the limitations explained above.
- **User friendly:** In order for this tool to be applicable for others and not be too time consuming, to change, to fit their own use case, an explanation in section "Further Development for this tool" will be presented.
    
### About the tool

We aim to be able to solve the following steps with our tool:
- [ ] Extracting MaterialLayers and the quantities from an Ifc file
- [X] Importing an environmental data set. For this tool it's an excel file containaing EPD's but it could be other environmental data repositories.
- [ ] Creating a defined matrix for both step 1 and 2.
- [ ] Predefine search queues for the tool to match up the Ifc data with Environmental data
- [ ] Calculate the impact per MaterialLayer
- [ ] Be able to do it for all IfcEntities in an Ifc file  

## State where you found that problem
We found the environmental data from PM appendix #2406 and used that information to double check whether the results of our tool are close to the list they've done with the LCI for LCA.  
Whenever you're doing LCA work for buildings the data from the ifc file is not easy to match with the open-source environmental data analysis tools such as LCAByg. With this idea the script will be able to withdraw quantities from the Ifc file that will be matched with environmental data and exported to a JSON file. This JSON file can then easily be imported into an excel spreadsheet for further LCA work or imported to LCAByg and other Building LCA tools.  
The problem is simply that sustainability experts are spending a lot of time matching the data when building an LCI and our tool will potentially be able to cut down the hours needed to do a full LCA.

In principle the imported Ifc data will be able to be matched with any environmental data that the user can provide, and therefore the user will not have to base their analysis on a static and definitve dataset, which could become obsolete in the future when new technologies and results are found.


## Description of the tool

instructions to run the tool.

### Advanced Building Design

When it comes to usability in the course "Advanced Building Design", we propose that this tool could be used both in the early design stage (A) and during the end when the total environmental cost of the building needs to be calculated (D).
For the early design stage, the disciplines such as ARC and STR, could use this tool to initially figure out how much of an impact a certain material choice is going to have. They could for example propose scenarios with different material choices, and then the rest of the team would have a more clear idea on the impacts that these choice will have later in the design phase.
For the total environmental cost of the building the disciplines such as PM and ARC could use our tool to create a JSON file where the LCI is basically done automatically which will provide them time to consider which environmental data they need and which stages of the building needs to be included.
We would also propose that a new discipline for the Advanced Building Course is created, a so-called sustainability analyst, that could potentially provide the abovementioned work.  
With such a discipline we would argue that the overall design of the building would include more thoughts on the environmental impact, ultimately reducing the GWP and meeting the Building Regulations requirements of a max CO2 emission of 12 kgCO2eq/m2/year. But potentially even meeting the Reduction Roadmap's ambitions to reduce the impact even more in trying to meet the Planetary Boundaries.

## Software requirements to run this tool  

In order to be able to run this tool we expect the following software to be required:  
1. [X] Python 3.10-12 (needed to run the script)
2. [X] Microsoft package - Excel (used as environmental data file, could be any software)
3. [X] IfcOpenShell (for ifc work)
4. [X] Numpy (for matrix work)
5. [X] Pandas (for JSON work)

### Further development for this tool:

Ability to implement a "decision tree" if it's a wall = m2 if it's a 

## 03 An IDS:
Produce an IDS to check that the model can be run by your tool.

