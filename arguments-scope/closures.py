def print_msg(msg:str):
  #This is the outer enclosing function

  def printer():
    print(msg)

  return printer #returns the nested function

another = print_msg('Holi boli') #Stores the reference to the function in a variable
another() #This is the actual execution of the function


#Another closure

def echo(n:int):
  """Returns the inner echo function."""

  #Define the inner echo
  def inner_echo(word:str):
    echo_word = n * word 
    return echo_word

  return inner_echo #Returns the nested function


twice = echo(2) #Referencing the function with 2 
thrice = echo(3) #Referencing the function with 3

print(twice('Holi '), thrice('UwU ')) #Actuallly executing