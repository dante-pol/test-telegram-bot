from __future__ import annotations

storage_recipes = None

class Recipe:

    count = 0
    
    def __init__(self, id, name, description, ingredients, complexity, type_cuisine) -> None:
        self.__id = id
        self.__name = name
        self.__description = description
        self.__ingredients = ingredients
        self.__complexity = complexity
        self.__type_cuisine = type_cuisine

        Recipe.count += 1

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
    def get_description(self):
        return self.__description
    
    def get_ingredients(self):
        return self.__ingredients
    
    def get_complexity(self):
        return self.__complexity
    
    def get_type_cuisine(self):
        return self.__type_cuisine
    
def provide_recipe_of_id(id: int) -> (Recipe | None):
    global storage_recipes
    
    if id <= 0:
        return None
    
    if storage_recipes == None:
        provide_all_recipes()
    
    for item in storage_recipes:
        if item.get_id() == id:
            return item
        
    return None

def provide_all_recipes() -> tuple:
    global storage_recipes

    if storage_recipes != None:
        return storage_recipes

    datas = __load()
    dataset = __process_raw_data(datas)
    recipes = __convert_to_recipes(dataset)

    storage_recipes = recipes

    return tuple(recipes)

def __process_raw_data(datas: str, split_char="|") -> list:
    datas = datas.split('\n')

    datas = datas[1::]

    dataset = []

    for item in datas:
        if item == '': continue

        raw_resicipe = item.split(split_char)

        raw_resicipe[0] = int(raw_resicipe[0])
        raw_resicipe[4] = int(raw_resicipe[4])

        dataset.append(raw_resicipe)

    return dataset

def __convert_to_recipes(dataset: list) -> list:
    recipes = []

    for raw_recipe in dataset:
        recipe = Recipe(*raw_recipe)
        recipes.append(recipe)

    return recipes

def __save(datas: any) -> None: pass

def __load(path="datas/recipe_book.csv", type="r", encoding="utf-8") -> str:
    with open(path, type, encoding=encoding) as file:
        datas = file.read()
    
    return datas