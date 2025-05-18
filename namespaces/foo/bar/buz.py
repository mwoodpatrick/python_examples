if __name__ == "__main__":
    print(f'The script {__name__} is being run directly.')
else:
    print(f'The script {__name__} is being imported as a module.')

def func(z):
    print(f'In {__name__} Called with arg {z}')

