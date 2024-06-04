import json

lijst = []
lijst.append("JSON output from TA_JSONmethod_txt2RASE_X_trainingarticles-files")
lijst.append("JSON output from TA_JSONmethod_txt2RASE_X_trainingarticles-files")
lijst.append("JSON output from TA_JSONmethod_txt2RASE_X_trainingarticles-files")
lijst.append("JSON output from TA_JSONmethod_txt2RASE_X_trainingarticles-files")
lijst.append("JSON output from TA_JSONmethod_txt2RASE_X_trainingarticles-files")
lijst.append("JSON output from TA_JSONmethod_txt2RASE_X_trainingarticles-files")
lijst.append("JSON output from TA_JSONmethod_txt2RASE_X_trainingarticles-files")
lijst.append("JSON output from TA_JSONmethod_txt2RASE_X_trainingarticles-files")
lijst.append("JSON output from TA_JSONmethod_txt2RASE_X_trainingarticles-files")

new_json_structure = {"artikelen": lijst}

output_path = 'FILEPATH TO resultaten.json'
with open(output_path, 'w') as json_file:
    json.dump(new_json_structure, json_file, ensure_ascii=False, indent=4)

print(f"De gegevens zijn opgeslagen in {output_path}.")
