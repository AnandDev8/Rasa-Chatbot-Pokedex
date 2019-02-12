from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

def train_core(domain='domain.yml',model_path='./models/dialog',train_data='./data/stories.md'):
	agent=Agent(domain,policies=[MemoizationPolicy(),KerasPolicy(batch_size=50,epochs=250,max_history=3)])
	data=agent.load_data(train_data)
	agent.train(data)
	agent.persist(model_path)
	return agent

if __name__=="__main__":
	train_core()
