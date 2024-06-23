import time

def enc():
    text = input('Enter Your Text : ')
    aa = text.split()
    a = []
    code = True

    if code:
        for word in aa:
            if len(word) >= 3:
                r1 = 'pjs'
                r2 = 'kso'
                r3 = 'lsk'

                newword = r1[-1] + word[:-1] + r1[-1] + None + r2 + r3
                a.append(newword)
    else:
        a.append(word[-1])

    print('Working...')
    time.sleep(1)
    print('Your encrypted Text: ' + ' '.join(a))

if __name__ == '__main__':
    enc()