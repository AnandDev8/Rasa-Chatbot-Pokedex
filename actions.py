from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests

class KnowPokemon(Action):
	def name(self):
		return "action_know"
	def run(self,dispatcher,tracker,domain):
		name=tracker.get_slot('pokemon').lower()
		if not name:
			response="Sorry it seems there is no such pokemon :("
			name="Sorry"
		elif name:
			requester=requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(name))
			req_json=requester.json()
			pokemon_name=req_json['forms'][0]['name'].upper()
			pokemon_attack=req_json['abilities'][0]['ability']['name']
			pokemon_height=req_json['height']
			pokemon_type=req_json['types'][0]['type']['name']
			pokemon_weight=req_json['weight']
			response="Pokedex Information\n________________\n*Pokemon Name:{}\n*Type:{}\n*Height:{}\n*Weight:{}\n*Attack:{}\nThank You".format(pokemon_name,pokemon_type,pokemon_height,pokemon_weight,pokemon_attack)
		dispatcher.utter_message(response)
		return [SlotSet('pokemon',name)]
