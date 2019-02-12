from rasa_core.agent import Agent
from rasa_core import config
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.run import serve_application
import rasa_core

def pokedex_bot(serve_forever=True):
	interpreter=RasaNLUInterpreter('./models/nlu/default/pokedex')
	action_endpoint=EndpointConfig(url="http://localhost:5055/webhook")
	agent=Agent.load('./models/dialog',interpreter=interpreter,action_endpoint=action_endpoint)
	rasa_core.run.serve_application(agent,channel='cmdline')
	return agent

if __name__=="__main__":
	pokedex_bot()
