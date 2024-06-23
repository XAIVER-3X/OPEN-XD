import os
import sys
import time

try:
    import requests
except ImportError:
    pass

try:
    from FBTools import Start
except ImportError:
    print('FB Tool Installing....✓')

logo = '''
\x1b[1;92m
▬ \x1b[1;92m███████ ██    ██ ██   ██  █████        \x1b[33;1m▬▬▬▬▬▬▬▬▬\x1b[1;92m
▬ \x1b[1;92m██      ██    ██ ██   ██ ██   ██      \x1b[33;1m█ V : 0.1 █\x1b[1;92m
▬ \x1b[1;92m███████ ██    ██ ███████ ███████ 
▬ \x1b[1;92m     ██ ██    ██ ██   ██ ██   ██ 
▬ \x1b[1;92m███████  ██████  ██   ██ ██   ██ 
▬\x1b[1;92m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\x1b[1;37m
'''

print(logo)
user = input('\x1b[1;92mEnter Your User Name:')

def main():
    BotActions()

a = 'os_start_placeholder'
b = 'Jiku'
b_2 = 'suha'
c = 'alexa'
c_2 = 'jiku'
d = 'os_input_placeholder'

key = b + a + c + d
key2 = b_2 + a + c_2 + d

def not_permission():
    print(logo)
    print(f'\x1b[1;92mYour Name {user}')
    print(f'\x1b[1;92mYour Key :- {key2}')
    print(key)
    print('\x1b[1;92mYou need Permission For use that Tool\x1b[1;92m')
    print('\x1b[1;92mIt is a Free Tool and Pro Can ignore That Tool\x1b[1;92m')
    os.system(key2)
    time.sleep(1)
    os.system(key2)
    time.sleep(1)

def apruve():
    pass

apruve()

def Login():
    email = input('\x1b[1m \x1b[0;37m[^]𝖨𝗇𝗉𝗎𝗍 𝖸𝗈𝗎𝗋 𝖤𝗆𝖺𝗂𝗅: \x1b[0;37m  ')
    password = input('\x1b[1;30m[^]𝖨𝗇𝗉𝗎𝗍 𝖸𝗈𝗎𝗋 𝖯𝖺𝗌𝗌𝗐𝗈𝗋𝖽: \x1b[1;30m ')

    FB = Start(email, password)
    FB.system()

def BotActions():
    print(os.NULL)
    print(logo)
    print(' Username', user)
    print('▬\x1b[1;92m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\x1b[1;37m')

    choice = input('\x1b[1;34m[A] Comment on a post\n\x1b[1;35m[B] Share a post\n\x1b[1;35m[0] Exit\nChoose an option: ')

    if choice in ('A', 'a', '1'):
        CommentOnPost()
    elif choice in ('B', 'b', '2'):
        SharePost()
    elif choice in ('0', 'exit', ''):
        print('Exit Done...✅')
        sys.exit()
    else:
        print('Invalid choice')
        BotActions()

def CommentOnPost():
    post = input('Input Post ID: ')
    comt = input('Write Comment: ')
    loop = int(input('How Many: '))

    for _ in range(loop):
        comment_response = FB.comment(post=post, text=comt)
        print(comment_response)
        print(' Comment Done✅')
        print('404')

    os.system('CommentToPost')
    print(logo)
    return CommentOnPost()

def SharePost():
    link = input('Input Post Link: ')
    share_response = FB.share(link=link)
    print(share_response)

if __name__ == '__main__':
    Login()
    main()
