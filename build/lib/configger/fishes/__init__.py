import os

splited_path = os.path.realpath(__file__).split('\\')[:-1]
fish_path = '\\'.join(splited_path)

fish_json_name = "fish.json"
fish_json_path = os.path.join(fish_path, fish_json_name)
