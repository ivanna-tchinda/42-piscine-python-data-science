def all_thing_is_obj(object: any) -> int:
  ft_dict = {
    list: "List",
    tuple: "Tuple",
    set: "Set",
    dict: "Dict",
    str: "String"
  }
  match type(object):
    case type() if type(object) in ft_dict:
      print(f"{ft_dict[type(object)]}: {type(object)}")
    case _:
      print("Type not found")
  return 42