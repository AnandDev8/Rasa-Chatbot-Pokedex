#story 1
* greet
  - utter_greet
* goodbye
  - utter_goodbye
#story 2
* greet
  - utter_greet
* pokemon_search{"pokemon":"bulbasaur"}
  - slot{"pokemon":"bulbasaur"}
  - action_know
  - slot{"pokemon":"bulbasaur"}
* goodbye
  - utter_goodbye
#story 3
* pokemon_search{"pokemon":"charmander"}
  - slot{"pokemon":"charmander"}
  - action_know
  - slot{"pokemon":"charmander"}
* goodbye
  - utter_goodbye

#story 4
* greet
  - utter_greet
* pokemon_search{"pokemon":"squirtle"}
  - slot{"pokemon":"squirtle"}
  - action_know
  - slot{"pokemon":"squirtle"}
* goodbye
  - utter_goodbye

#story 5
* greet
  - utter_greet
* pokemon_search{"pokemon":"blastoise"}
  - slot{"pokemon":"blastoise"}
  - action_know
  - slot{"pokemon":"blastoise"}
* pokemon_search{"pokemon":"butterfree"}
  - slot{"pokemon":"butterfree"}
  - action_know
  - slot{"pokemon":"butterfree"}
* pokemon_search{"pokemon":"pidgey"}
  - slot{"pokemon":"pidgey"}
  - action_know
  - slot{"pokemon":"pidgey"}
* goodbye
  - utter_goodbye





