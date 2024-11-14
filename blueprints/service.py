def check_email(data):
    sentences = data['sentences']
    new_sen = ""
    for i in sentences:
        new_sen += i
    new_sen.replace('.',' ')

    if "hostage" in new_sen:
        return "hostage"
    elif"explos" in new_sen:
        return "explos"
    else:
        return

def c(sentens):
    n = sentens.split(' ')
    for i in n:
        if i.lower() in ['hostage', 'explos']:
            return True
    return False


def change_senteness(data):
    sentences = data['sentences']
    new_sen = ""
    for i in sentences:
        new_sen += i
    n = new_sen.split('.')
    n.pop()
    for i in range(len(n)):
        if c(n[i]):
            tmp=n[i]
            n[i] = n[0]
            n[0] = tmp

    data['sentences'] = n
    return data
