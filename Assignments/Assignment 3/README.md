<img width="613" alt="image" src="https://github.com/user-attachments/assets/06065be8-edc1-450c-aa49-c63d9d3ad4cd"># Assignment 3 Tool:

## 01. The IFC model
The IFC model used for developing this script is from the course Advanced Building Design group #2406.

We are using the model made by ARC to extract data from the ifc file. We wish to extract the ifcEntity to get data about IfcMaterialLayers and their corresponding quantities. The entitiy chosen is the walls, but we believe the overall method can be applied for all entities in an ifc model. The tool aims to solve part of the solution of matching material quantities from a model, with the materials environmental data such as GWP and life time, using Bag of Word (BoW). 

## 02. Use case
The work done for Assignment 3 has been built on top of the work from Assignments 1 and 2, although some considerable modifications has been made.

The following list will explain the major changes in the tool:
- **Less ambitious:** the idea for the tool was initially quite broad, and in our research and in dialogue with the course responsible, we found other examples of solutions where it had already been solved. This is the reasone why the focus was directed towards the matching of materials process. Furthermore, because of the limitations of our python skills, as well as the deadline, the ambition on creating a tool that can include all IfcEntities and calculate the environmental impact has been reduced to a single entity.

- **Single and simple entity IfcWallStandard**: This change is because of the limitations explained above, we would rather show a fully functioning example of one entity than a solution where half of the idea is fulfilled.
  
- **User friendly:** In order for this tool to be applicable for others and not be too time consuming, to change and to fit their own use case, the tool should be further developed in a certain direction. In section "Further Development for this tool" these ideas of user-friendliness will be presented.
  
- **High error rate:** Given the data in this example approximately 1/3 of the materials doesn't get a relevant match. However this clearly has to come from the flaws in the used data, which is described later in the section "Description of the tool"
  

### State where you found that problem
We found the environmental data from PM appendix #2406 - "LCI for LCA", this information was used to double check whether the results of our tool would be close to their list.

Whenever you're doing LCA work for buildings the data from the ifc file is not easy to match with open-source environmental data analysis tools such as LCAByg. With our idea the script should be able to withdraw quantities from the Ifc file that can then be matched with environmental data and exported to a JSON file. This JSON file can then easily be imported into an excel spreadsheet for further LCA work or imported to LCAByg and other Building LCA tools to finish the assessment.  
The problem is simply put, that sustainability experts are spending a lot of time matching the data when building an LCI and our tool could potentially be able to cut down the hours needed to do a full LCA.

In principle the imported Ifc data will be able to be matched with any environmental data that the user can provide, and therefore the user will not have to base their analysis on a static and definitve dataset, which could become obsolete in the future when new technologies and results is changing the standards.

### About the tool

We aim to be able to solve the following steps with our tool:

- [X] Importing an environmental data set. For this tool it's an excel file containaing environmental data, but it could be other environmental data repositories or EPDs, depending on the processing power and data libraries available. This is used to create the document matrix in the Bag of Word (BoW) analysis using the words in the excel rows.
- [X] Extracting IfcMaterialLayers and the quantities from an Ifc file. Then cross referencing the words within the material layers with the BoW to create new query vectors. 
- [X] Using the query vector the cosine simularity is calculated for all materials in the document matrix and the top 5 matches are suggested.
- [X] The simularity scores are then exported to a json file, where each layer in the wall is displayed. 
- [ ] Here the user has a possibility to control if it is correctly matched before potentially exporting it into a LCAx JSON format and doing the calculation.

Link to youtube video with introduction: https://youtu.be/GlpV5v2etjg

### Description of the tool

The tool is a new suggetion on how to match up environmental data and quantaties of material layers from an ifc model using BoW. 
The eaxmple that this exact tool solves is matching environmental data from a spreadsheet, which the group made, with the information available in the Ifc model on IfcWalls.
The tools effectiveness in matching words were therfore found to be limited by:  
- [ ] Words joint together by eg. "/".
- [ ] Mix in languages (Danish and English).
- [ ] Different units used eg. cm/mm/m.

The tool relies a lot on the data used to create the document matrix and the query vectors and terefore the tool is quite dependent on this. However, the tool still helps a lot in matching the materials compared to exact material matching and make quite qualified guesses. On a lot of materials and can work quite flexibly. For instance if customized mixed material layers are used. 
For a further look and explanation of the code follow this link:
https://github.com/fcBIM/gruppe38/blob/24e40fc76818ce06aff1e28525f8750ffbad8e02/Assignments/Assignment%204/Presentation%20of%20tool.pdf

### Software requirements to run this tool  

In order to be able to run this tool we expect access to the following software:
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
Extending the document matrix across multiple project or databases could result in a quite strong search ability and a more precise tool. Also, if eg. dimensions and entity type of the buildings were realated to this data, a machine learning perspective could be implemented to develop a model, which assigned/suggested materials to the building entities instead of the other way around.
