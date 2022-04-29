from datetime import datetime
from SearchAlgorithms import AEstrela
from TaxiDriver import TaxiDriver
import gym

env = gym.make("Taxi-v3").env

def test1():
  current_state = env.reset()
  current_state = env.encode(3, 3, 2, 0)
  env.render()
  inicio = datetime.now()
  result = TaxiDriver(env.desc, env.decode(current_state))
  fim = datetime.now()
  print("")
  print("=======================================")
  print("Teste 1")
  print(f"Tempo de resolucao: {fim-inicio}")
  assert result.path()[-1] == 5
  
def test2():
  current_state = env.reset()
  current_state = env.encode(3, 2, 2, 1)
  env.render()
  inicio = datetime.now()
  result = TaxiDriver(env.desc, env.decode(current_state))
  fim = datetime.now()
  print("")
  print("=======================================")
  print("Teste 2")
  print(f"Tempo de resolucao: {fim-inicio}")
  assert result.path()[-1] == 5
  
def test3():
  current_state = env.reset()
  current_state = env.encode(1, 3, 2, 1)
  env.render()
  inicio = datetime.now()
  result = TaxiDriver(env.desc, env.decode(current_state))
  fim = datetime.now()
  print("")
  print("=======================================")
  print("Teste 3")
  print(f"Tempo de resolucao: {fim-inicio}")
  assert result.path()[-1] == 5
  
def test4():
  current_state = env.reset()
  current_state = env.encode(2, 2, 2, 3)
  env.render()
  inicio = datetime.now()
  result = TaxiDriver(env.desc, env.decode(current_state))
  fim = datetime.now()
  print("")
  print("=======================================")
  print("Teste 4")
  print(f"Tempo de resolucao: {fim-inicio}")
  assert result.path()[-1] == 5
  
def test5():
  current_state = env.reset()
  current_state = env.encode(0, 3, 2, 0)
  env.render()
  inicio = datetime.now()
  result = TaxiDriver(env.desc, env.decode(current_state))
  fim = datetime.now()
  print("")
  print("=======================================")
  print("Teste 5")
  print(f"Tempo de resolucao: {fim-inicio}")
  assert result.path()[-1] == 5