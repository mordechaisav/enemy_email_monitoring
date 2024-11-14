def analyze_email(content):
    lines = content['sentences']
    combined_text = ""
    for line in lines:
        combined_text += line
    combined_text.replace('.', ' ')

    if "hostage" in combined_text:
        return "hostage"
    elif "explos" in combined_text:
        return "explos"
    else:
        return

def contains_keywords(phrase):
    words = phrase.split(' ')
    for word in words:
        if word.lower() in ['hostage', 'explos']:
            return True
    return False

def reorder_sentences(content):
    lines = content['sentences']
    combined_text = ""
    for line in lines:
        combined_text += line
    parts = combined_text.split('.')
    parts.pop()
    for i in range(len(parts)):
        if contains_keywords(parts[i]):
            temp = parts[i]
            parts[i] = parts[0]
            parts[0] = temp

    content['sentences'] = parts
    return content
