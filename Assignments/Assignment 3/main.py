import pandas as pd
import numpy as np
import ifcopenshell
import os
import hashlib
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the Excel file
file_path_xl = 'File_path/Excel_EPD_Data.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path_xl)
df.columns = df.columns.str.lower()
df = df.iloc[1:]
df_selected = df.iloc[:, [1, 2, 4]]


# IFC file import
name = 'File_path/Adv.BIM/CES_BLD_24_06_ARC'
model_url = name + ".ifc"

if os.path.exists(model_url):
    model = ifcopenshell.open(model_url)
else:
    raise FileNotFoundError(f"Model file {model_url} does not exist")

# Initialize wall type areas and material layers
wall_types = model.by_type("IfcWallType")
wall_type_areas = {}

# Function to calculate wall area
# OBS! Should be repaced with the standard ifc comand, when used with at newer ifc file
def calculate_wall_area(wall):
    if wall.Representation:
        for representation in wall.Representation.Representations:
            for item in representation.Items:
                if item.is_a("IfcExtrudedAreaSolid"):
                    profile = item.SweptArea
                    if profile.is_a("IfcRectangleProfileDef"):
                        width = profile.XDim
                        length = item.Depth
                        return (width * length) / 1_000_000  # Convert mm² to m²
    return 0.0

# Function to get material layers
def get_wall_type_material_layers(wall_type):
    material_layers = []
    material_relations = model.by_type("IfcRelAssociatesMaterial")
    for rel in material_relations:
        if rel.RelatingMaterial and wall_type in rel.RelatedObjects:
            material = rel.RelatingMaterial
            if material.is_a("IfcMaterialLayerSet"):
                for layer in material.MaterialLayers:
                    material_layers.append((layer.Material.Name, layer.LayerThickness))
            elif material.is_a("IfcMaterial"):
                material_layers.append((material.Name, 0))  # No thickness for single materials
    return material_layers

# Find wall types through IfcRelDefinesByType
rel_defines_by_type = model.by_type("IfcRelDefinesByType")

for relation in rel_defines_by_type:
    related_wall_type = relation.RelatingType
    if related_wall_type.is_a("IfcWallType"):
        wall_id = related_wall_type.id()
        if wall_id not in wall_type_areas:
            wall_type_areas[wall_id] = {
                'name': related_wall_type.Name,
                'area': 0.0,
                'material_layers': get_wall_type_material_layers(related_wall_type)
            }
        for wall in relation.RelatedObjects:
            wall_type_areas[wall_id]['area'] += calculate_wall_area(wall)

# Step 1: Create a Bag of Words (BoW) Document-Term Matrix from df_selected
def create_bow_matrix(df_selected):
    df_selected['combined'] = df_selected.apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
    vectorizer = CountVectorizer(lowercase=True, stop_words='english')
    bow_matrix = vectorizer.fit_transform(df_selected['combined'])
    return pd.DataFrame(bow_matrix.toarray(), columns=vectorizer.get_feature_names_out()), vectorizer

# Step 2: Generate matches and export to JSON
bow_df, vectorizer = create_bow_matrix(df_selected)

def create_query_vector_for_layer(material_layer, vectorizer):
    material, thickness = material_layer
    query_string = f"{material} {thickness}"
    query_vector = vectorizer.transform([query_string]).toarray()[0]
    return query_vector

def compute_similarity_for_layer(bow_df, query_vector):
    similarities = cosine_similarity(bow_df, query_vector.reshape(1, -1))
    return sorted(list(enumerate(similarities.flatten())), key=lambda x: x[1], reverse=True)

# Structure to hold the final results
json_data = []

# Loop through each wall type and calculate matches
for wall_type_id, data in wall_type_areas.items():
    wall_entry = {
        "wall_type": data['name'],
        "wall_id": wall_type_id,
        "area_m2": data['area'],
        "material_layers": []
    }
    for material_layer in data['material_layers']:
        material, thickness = material_layer
        query_vector = create_query_vector_for_layer(material_layer, vectorizer)
        similarity_scores = compute_similarity_for_layer(bow_df, query_vector)

        # Add matches to the structure
        matches = {f"match_{i+1}": {
            "material_name": df_selected.iloc[idx]['combined'],
            "similarity_score": round(score, 4)
        } for i, (idx, score) in enumerate(similarity_scores[:5])}

        wall_entry["material_layers"].append({
            "material_layer_chosen": material,
            "thickness_mm": thickness,
            "matches": matches
        })

    json_data.append(wall_entry)

# Step 3: Write JSON to file
json_file_name = 'wall_material_matches.json'

with open(json_file_name, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

# Step 4: Generate the hash for the JSON file
def hash_json_file(file_path, algorithm='sha256'):
    hasher = hashlib.new(algorithm)
    with open(file_path, 'rb') as file:
        hasher.update(file.read())
    return hasher.hexdigest()

# Compute the hash of the exported JSON file
json_hash = hash_json_file(json_file_name)
print(f"The SHA-256 hash of the JSON file is: {json_hash}")
