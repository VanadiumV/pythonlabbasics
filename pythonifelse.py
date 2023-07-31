"""

n = int(input())
if n % 2:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
    """
#Like this: n = int(input().strip()) Instead of just coding: n = int(input()) I know . strip() returns a copy of the string in which all chars have been stripped from the beginning and the end of the string.

if __name__ == '__main__':
    n = int(input().strip())
    if n%2 or 6 <= n <= 20:
        print('Weird')
    else:
        print('Not Weird') 