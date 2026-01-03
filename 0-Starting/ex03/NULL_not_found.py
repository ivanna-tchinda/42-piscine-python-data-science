def NULL_not_found(object: any) -> int:
  ft_dict = {
    None: "Nothing",
    float("NaN"): "Garlic",
    0: "Zero",
    "": "Empty",
    False: "Fake"
  }
  match object:
    case None | float("NaN") | 0 | "" | False:
      print(f"{ft_dict[object]}: {type(object)}")
      return 0
    case _:
      print("Type not found")
      return 1