def RandomString(strLength = 5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(strLength))