import string
import random
if __name__ == '__main__':
    sp=('@/.-=$&^*+|:~')
    s = string.digits + string.ascii_letters + sp
    c = list(s)
    while True:
        try:
            l = int(input('Enter the length of the password : '))
            break
        except:
            print('Please enter an integer number ')
    b=random.sample(c,l)
    print(f'Here\'s Your Generated Password : {"".join(b)}')