

def dateGenerator(numdays): # generate N days until now, eg [20151231, 20151230]
    base = datetime.datetime.today()
    date_list = [base - datetime.timedelta(days=x) for x in range(0, numdays)]
    for i in range(len(date_list)): date_list[i] = date_list[i].strftime("%Y%m%d")
    return set(date_list)

def unify_word(word): # went -> go, apples -> apple, BIG -> big
    # try: word = en.verb.present(word) # unify tense
    # except: pass
    # try: word = en.noun.singular(word) # unify noun
    # except: pass
    return word.lower()
