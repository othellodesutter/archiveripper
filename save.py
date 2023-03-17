def save_config(username, password):
    quote = ''
    quotes = ["'''",'"""','"',"'"]
    testing = username+password
    for q in quotes:
        if q not in testing:
            quote = q

    if quote == '':
        raise "Details can not be saved."

    with open('config.py', 'a+', ) as f:
        f.write("config={'email':" + quote + username + quote + ",'password':" + quote + password + quote + "}")

