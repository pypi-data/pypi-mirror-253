def dict_by_request(responce_list, univocal_keys):
    responce_dict = dict()
    for cont in responce_list:
        chiave = tuple(cont[k] for k in univocal_keys)
        responce_dict[chiave] = cont
    return responce_dict


def order_by_request(params_list, responce_list, univocal_keys):
    responce_dict = dict_by_request(responce_list, univocal_keys)
    response_content = [None for _ in range(len(params_list))]
    for i, ele in enumerate(params_list):
        chiave = tuple(ele[k] for k in univocal_keys)
        if chiave in responce_dict:
            response_content[i] = responce_dict[chiave]
        else:
            response_content[i] = None
    return response_content
