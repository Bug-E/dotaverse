import dota2api
import json

KEY = '37F66E0B4E7C37C33BD7F034E72D4DDB'
api = dota2api.Initialise(KEY)
items = api.get_game_items()
with open('items.txt', 'w') as itemfile:
	json.dump(items, itemfile)
heroes = api.get_heroes()
with open('heroes.txt', 'w') as herofile:
	json.dump(heroes, herofile)

