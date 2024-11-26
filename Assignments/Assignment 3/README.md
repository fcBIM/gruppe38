# Assignment 3 Tool:

## 01. The IFC model
The IFC model used for developing this script is from the course Advanced Building Design course group #2406.

We are using the ARC IFC to extract data from an ifcEntity to get data about MaterialLayers and their corresponding quantities. The entitiy  has been walls in our eample, but we belive the overall method can be apllied for most entities. The tool aims to solve part of the sollution of matching material quantities from a model, with the materials environmental data such as GWP and life time using Bag of Word (BoW). 


## 02. Assignment 3 - use case analysis :
The work done for Assignment 3 has been built on top of the work provided in Assignments 1 and 2, although some considerable modifications has been made.

The following list will explain some major changes for the tool:
- **Less ambitious:** the tool was initially quite broad. and in our research and in dialouge with the course responible, we found other solutions to already have been solved and directed our focus on matching. Because of the limitations of our python skills as well as the deadline set by the course responsible, the ambition on creating a tool that can include all IfcEntities and calculate the environmental impact has been reduced to a single entity.

- **Single and simple entity IfcWallStandard**: This change is because of the limitations explained above, we would rather show a completed example of one entity than half a solution for all entities.
  
- **User friendly:** In order for this tool to be applicable for others and not be too time consuming, to change, to fit their own use case, an explanation in section "Further Development for this tool" will be presented.
  

### State where you found that problem
We found the environmental data from PM appendix #2406 and used that information to double check whether the results of our tool are close to the list they've done with the LCI for LCA.  
Whenever you're doing LCA work for buildings the data from the ifc file is not easy to match with the open-source environmental data analysis tools such as LCAByg. With this idea the script will be able to withdraw quantities from the Ifc file that will be matched with environmental data and exported to a JSON file. This JSON file can then easily be imported into an excel spreadsheet for further LCA work or imported to LCAByg and other Building LCA tools.  
The problem is simply that sustainability experts are spending a lot of time matching the data when building an LCI and our tool will potentially be able to cut down the hours needed to do a full LCA.

In principle the imported Ifc data will be able to be matched with any environmental data that the user can provide, and therefore the user will not have to base their analysis on a static and definitve dataset, which could become obsolete in the future when new technologies and results are found.

### About the tool

We aim to be able to solve the following steps with our tool:

- [ ] Importing an environmental data set. For this tool it's an excel file containaing environmental data, but it could be other environmental data repositories or EPDs, depending on th processing power and data libraries available. This is used to create the document matrix in the BoW analysis using the words in the excel rows.
- [ ] Extracting MaterialLayers and the quantities from an Ifc file. Then cross referencing the words with in hte material layers with the BoW to create some new query vectors. 
- [ ] Using the query vector the cosine simularity is calculated for all materials in the document matrix and the top 5 are suggested.
- [ ] The simularity scores are the eported to a json file, where each layer in the wall is displayed. 
- [ ] Here the user has a possibility to control if it is correctly matched before potentially eporting it into a LCAx JSON format and doing the calculation (We have not made a script for this last part) 

### Description of the tool

The tool is a new suggetion on how to match up environmental data and quantaties of material layers from an ifc model using Bag of Words (BoW). 
The eaxmple that this exact tool solves is matching env. data from a spreadsheet, which the group made, with the information available in the ifcmodel on walls.
The tools effectiveness in matching words were therfore found to be limited by:  
- [ ] Words joint together by eg. "/".
- [ ] Mix in languages (Danish and English).
- [ ] Different units used eg. cm/mm/m.

The tool relies a lot on the data used to create the document matrix and the query vectors and terefore the tool is quite dependend on this. However the tool, still helps a lot in matching the materials compared to exact material matching and make quite qualified guesses. On a lot of materials and can work quite flexibly. For instance if costumized mixed material layers are used. 

### Software requirements to run this tool  

In order to be able to run this tool we expect the following software to be required:  
1. [X] Python 3.10-12 (needed to run the script)
2. [X] IfcOpenShell (for ifc work)
3. [X] Numpy (for matrix work)
4. [X] Pandas (for JSON work)
5. [X] (Microsoft package - Excel (used as environmental data file, could be any software))

   
### Advanced Building Design

When it comes to usability in the course "Advanced Building Design", we propose that this tool could be used both in the early design stage (A) and during the end when the total environmental cost of the building needs to be calculated (D).

For the early design stage, the disciplines such as ARC and STR, could use this tool to initially figure out how much of an impact a certain material choice is going to have. They could for example propose scenarios with different material choices, and then the rest of the team would have a more clear idea on the impacts that these choice will have later in the design phase.

For the total environmental cost of the building the disciplines such as PM and ARC could use our tool to create a JSON file where the LCI is basically done automatically which will provide them time to consider which environmental data they need and which stages of the building needs to be included.

We would also propose that a new discipline for the Advanced Building Course is created, a so-called sustainability analyst, that could potentially provide the abovementioned work.  
With such a discipline we would argue that the overall design of the building would include more thoughts on the environmental impact, ultimately reducing the GWP and meeting the Building Regulations requirements of a max CO2 emission of 12 kgCO2eq/m2/year. But potentially even meeting the Reduction Roadmap's ambitions to reduce the impact even more in trying to meet the Planetary Boundaries.

On a higher level, it is hopefully  a tool that brings more awareness to, what information is included in the model.



## 03. Further development for this tool:




For this tool to be more user-friendly it is proposed that an implementation of two things happens.  
1. The ability to choose whether the output of the Ifc quantity should be stated as an area or a volume.  
   - This will secure that the match of Ifc data and Environmental data is using the same unit.
3. The ability to choose whether to match "x" (IfcMaterialLayer) or "y" (IfcMaterialLayer) to "a" (environmental unit) or "b" (environmental unit).  
   - With this implementation the user is now able to match the data by clicking on chosen (by the script) names. This will give the tool a higher accuracy in matching the correct data.
   
4. it would also be interesting to look if weightening of the different categories would lead to more precise results. 


On another level: 
Extending the dookument matrix across multiple project or databases could result in a quite strong search abillity and a more precise tool. Also, if eg. dimensions and entity type of the buildings were realated to this data, a macine leaning perspective could be to develop a model, which assigned/suggested materials to the building entities.


## 04. An IDS:
Produce an IDS to check that the model can be run by your tool.

