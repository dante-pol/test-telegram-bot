def create_formatter_recipe(*args):
    return Formatter(*args)


class Formatter:
    
    def __init__(self, *args) -> None:
        self.__recipes = args

    def get_head(self):
        if len(self.__recipes) == 0: return "error 404: Datas not found"
        
        head = ""
        for recipe in self.__recipes:
            head += f"{recipe.get_id()}. {recipe.get_name()}\n"
        return head
    
    def get_full(self):
        if len(self.__recipes) == 0: return "error 404: Datas not found"
        
        head = ""
        for recipe in self.__recipes:
            head += f"*{recipe.get_id()}.{recipe.get_name()}* 🤟"

        body = ""
        for recipe in self.__recipes:
            body += f"""
*Описание:* {recipe.get_description()}\n
*Ингредиенты:* {recipe.get_ingredients()}\n
*Сложность приготовления:* {recipe.get_complexity()}\n
*Вид кухни:* {recipe.get_type_cuisine()}
"""
        return f"{head}\n{body}"

