<img width="613" alt="image" src="https://github.com/user-attachments/assets/06065be8-edc1-450c-aa49-c63d9d3ad4cd"># Assignment 3 Tool:

## 01. The IFC model
The Industry Foundation classes (IFC) model used for developing this script is from the course Advanced Building Design (ABD) group #2406.

We are utilizing the architecture (ARC) model to extract data from the IFC file. We aim to extract the IfcEntity to get data about IfcMaterialLayers and their corresponding quantities. The selected entity is IfcwallStandardCase, however, we believe the general idea and method can be applied to all entities within an IFC model. This tool aims to solve part of the challenge when matching material quantities from an IFC model, with environmental data such as Global Warming Potential (GWP) and life time, using Bag of Word (BoW) operations. 

## 02. Use case
The work presented for Assignment 3 has been built on the foundation of Assignments 1 and 2, with several significant modifications implemented to enhance functionality and meet time constraints.

The following list will explain the major changes in the tool:
- **Reduced scope:** the idea for the tool was initially quite broad, and in our research and in dialogue with the course responsible, we identified other examples of similar solutions. This led us to narrow our focus towards the material-matching process. Furthermore, due to our limitations when it comes to python proficiency, and the project deadline, we reduced the scope of creating a tool that is able to include all IfcEntities and calculate the environmental impact, to implement a match-operation on a single entity.

- **Simplified focus on IfcWallStandardCase**: This change is given on behalf of the limitations outlined above, we prioritized to deliver a fully functioning example of one entity rather than presenting an incomplete solution. Single entity *IfcWallStandardCase* was chosen.
  
- **User friendliness:** In order for this tool to be applicable and practical for other users, the tool should be further developed in a certain direction. In section "Further Development for this tool" we present potential improvements to increase user-friendliness and customization options.
  
- **High error rate:** With the data provided approximately one-third of the materials fail to generate any match. However, this is primarily due to the flaws in the data used. This issue is discussed in greater detail in the section *Description of the tool*.
  

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
