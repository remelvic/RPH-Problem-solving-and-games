def read_classification_from_file(classification_file):
    """
    Reads emails
    :param: classification_file reads all emails
    :return: a dictionary that contains SPAM or OK and email names
    """
    diction = {}
    with open(classification_file, 'r', encoding='utf-8') as f:
        for line in f:
            key, value = line.rstrip().split(' ')
            diction[key] = value
    return diction
