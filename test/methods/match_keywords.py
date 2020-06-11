def check(content, keywords):
    content = content.lower()
    for i in range(len(keywords)):
        keywords[i] = keywords[i].lower()
    for keyword in keywords:
        if(content.find(keyword) == -1):
            return False
    return True

