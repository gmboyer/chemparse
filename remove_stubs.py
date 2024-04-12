import os

def main():
    ROOT = './chemparse'
    for root, _, files in os.walk(ROOT):
        for file in files:
            if file.lower().endswith('.pyi'):
                print(f'removing {root}/{file}')
                os.remove(f"{root}/{file}")


if __name__ == '__main__':
    main()