Group 38 - Analyst

Focus area: Group 38 - Sustainability and materials

Claim from the PM report: 
IFCRoof in ARC-model has a total of the following squaremeters: 1479m^2 

Source of claim: 
file CES_BLD_24_06_PM_Appendix.pdf p. 5 Appendix b LCI for LCA 


Description of your script:
The script is inspired by Basic Example 2, that extracts the total beam length from the IFC file.
- As described in the claim, the roof has a total area of 1479m^2. Instead of looking for the length of the IfcElementQuantity of a beam
the script aims to sort through all IfcRoof elements and calculate the total area in the IFC model investigated.
In folder "rules" -> "SubmissionA1.py" there will be a step-by-step explanation of the script.
