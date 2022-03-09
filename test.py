# input file
# a,1
# b,2
# c,3

class Dummy():
  def __init__(self, name='', value=0) -> None:
      self.name = name
      self.value = value
  
  def __str__(self) -> str:
      return f'Name: {self.name}, Value: {self.value}'

def supporting_loader(f):
    with open(f) as h:
            lines = h.readlines()
            dummies = []
            for i in lines:
                name, value = i.strip("\n").split(",")
                dummy_content = {}
                dummy_content['name'] = name
                dummy_content['value'] = float(value)
                dummies.append(dummy_content)
    return dummies

def dummy_objects_creator(list_of_dicts):
  dummy_objects = []
  for dummy in list_of_dicts:
    Dummy(name=dummy['name'], value=dummy['value'])
  return dummy_objects


dict_of_dummies = supporting_loader("stations.txt")
print(dict_of_dummies)
myDummyObjects = dummy_objects_creator(dict_of_dummies)