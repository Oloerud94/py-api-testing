def create_user_data(name = None, job = None):
    data = {}
    if name:
        data['name'] = name
    if job:
        data['job'] = job
    return data


def create_user_data_payload(input_dict):
    return {
        'name':input_dict.get('name'),
        'job':input_dict.get('job'),
    }
