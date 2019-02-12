from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Interpreter

def train_nlu(data,configs,domain_dir):
	train_data=load_data(data)
	trainer=Trainer(config.load(configs))
	trainer.train(train_data)
	model_directory=trainer.persist(domain_dir,fixed_model_name='pokedex')

def run_nlu():
	interpreter=Interpreter.load('./models/nlu/default/pokedex')
	print(interpreter.parse(u'tell me about charmander'))

if __name__=="__main__":
	#train_nlu('./data/data.json','config.json','./models/nlu')
	run_nlu()
