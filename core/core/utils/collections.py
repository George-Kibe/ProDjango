def deep_update(base_dict, update_with):
    # iterate over each item in the new dict(Update_with)
    for key, value in update_with.items():
        # if the value is a dict
        if isinstance(value, dict):
            base_dict_value = base_dict.get(key)
            # if the original value is also a dict then run through this same function
            if isinstance(base_dict_value, dict):
                deep_update(base_dict_value, value)
            # if the original value is not a dictionary
            else:
                base_dict[key] = value
        # if the new name is not a dictionary
        else:
            base_dict[key] = value
    return base_dict
