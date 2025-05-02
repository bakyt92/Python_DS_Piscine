import math
import inspect

def NULL_not_found(object: any)-> int:
    previous_frame = inspect.currentframe().f_back
    object_name = None

    for name, value in previous_frame.f_locals.items():
        if isinstance(object, float) and math.isnan(object):
            if isinstance(value, float) and math.isnan(value):
                object_name = name
                break
        elif object is value and name != "object":
            object_name = name
            break
    if object is None:
        print(f"Nothing: None", type(object))
    elif isinstance(object, float) and math.isnan(object):
        print(f"{object_name}: nan", type(object))
    elif object == 0:
        print(f"{object_name}: {object}", type(object))
    elif isinstance(object, str) and object == '':
        print(f"{object_name}: {object}", type(object))
    elif isinstance(object, bool):
        print(f"{object_name}: {object}", type(object))
    else:
        print("Type not found")
        return 1
    return 0
    