#**kwargs makes your function receive mutiple keyword arguments. 
#**kwargs treats arguments as a dictionary

def keyword_args(**kwargs):
  for k, v in kwargs.items():
    print(f'{k}: {v}')


keyword_args(word1='nunca', word2='pares', word3='de', word4='aprender')