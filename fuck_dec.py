import time

def dec():
    text = input('Enter Your Text : ')
    aa = text.split()
    a = []
    code = True

    if code:
        for word in aa:
            if len(word) >= 3:
                newword = word[3:-3]
                newword = newword[1] + None + newword[0]
                a.append(newword)
    else:
        a.append(word[-1])

    print('Working...')
    time.sleep(1)
    print('Your decrypt Text: ' + ' '.join(a))

if __name__ == '__main__':
    dec()