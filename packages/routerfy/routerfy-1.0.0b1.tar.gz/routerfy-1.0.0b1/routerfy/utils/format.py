def pascalify(text: str):
    final_text = text
    chars = ["_", "-", " "]
    
    for char in chars:
        final_text = "".join([part[0].upper()+part[1:] for part in final_text.split(char)])

    return final_text

def python_class_to_AWS_type(python_class: type):
    if python_class == dict:
        return "object"
    if python_class == list:
        return "array"
    if python_class == str:
        return "string"
    if python_class == bool:
        return "boolean"
    if python_class == float:
        return "number"
    if python_class == int:
        return "integer"
    
    return "null"