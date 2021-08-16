from pyfiglet import Figlet
import os
import qrcode


def show_list():
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i])


def show_menu():
    print('1- Add Product')
    print('2- Edit Product')
    print('3- Delete Product')
    print('4- Search')
    print('5- Show List')
    print('6- qrcode')
    print('7- Buy')
    print('8- Exit')


def add_product():
    print('*******Add Product*******')
    name = input('Enter name of product :')

    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['name'] == name:
            print('*****This product exists*****')
            break

    else:
        id = str(int(PRODUCTS[len(PRODUCTS) - 1]['id']) + 1)
        price = input('enter price : ')
        count = input('enter count : ')
        PRODUCTS.append({'id': id, 'name': name, 'price': price, 'count': count})


def edit_Product():
    show_list()
    print('*******Edit Product*******')
    id = input('enter product ID that you want to edit : ')

    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id'] == id:
            PRODUCTS[i]['name'] = input('Enter new name: ')
            PRODUCTS[i]['price'] = input('Enter new price: ')
            PRODUCTS[i]['count'] = input('Enter new count: ')
            break
    else:
        print('this product ID is not exists in the store')


def search_name():
    print("****Search Name****")
    name = input('Enter name of product: ')
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['name'] == name:
            print('****This product is exist****')
            print(PRODUCTS[i])
            break

    else:
        print("This product is not exist")


def delete_product():
    show_list()
    print("****Delete Product****")
    id = input('Enter product ID that you want to delete from database: ')
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id'] == id:
            del PRODUCTS[i]
            print("Selected Id has been deleted")
            break

    else:
        print('This product ID is not exist')


def save_qrcode():
    show_list()
    print("****save_qrcode****")
    id = input('Enter product ID that you want to save informations as QRcode : ')
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id'] == id:
            inf = 'id:' + PRODUCTS[i]['id'] + '-name:' + PRODUCTS[i]['name'] + '-price:' + PRODUCTS[i][
                'price'] + '-count:' + PRODUCTS[i]['count']
            path = os.path.join('QRcode/QRcode-' + PRODUCTS[i]['id'] + '.png')
            img = qrcode.make(inf)
            img.save(path)
            print("Qrcode created")
            break
    else:
        print("This product ID is not exist")


def buy():
    show_list()
    print("****shopping****")
    Shopping_cart = []
    total_amount = 0
    total_count = 0
    while True:
        id = input("Enter product ID: ")
        for i in range(len(PRODUCTS)):
            if PRODUCTS[i]['id'] == id:
                num_product = int(input("Enter number of product that you want: "))
                if num_product > int(PRODUCTS[i]['count']):
                    print("No inventory")
                else:
                    PRODUCTS[i]['count'] = int(PRODUCTS[i]['count']) - num_product
                    total_amount += int(PRODUCTS[i]['price']) * num_product
                    total_count += num_product
                    Shopping_cart.append(
                        'id:' + id + ' , name:' + PRODUCTS[i]['name'] + ' , count:' + str(num_product) + ' , price:' +
                        PRODUCTS[i]['price'] + ' , Total price:' + str(int(PRODUCTS[i]['price']) * num_product))
                break
        else:
            print("This product ID is not avalabel")

        contin = input("If you want to continue shopping ٍEnter 'y' : ")
        if contin == 'y':
            continue
        else:
            Shopping_cart.append('total amount:' + str(total_amount) + ', total count:' + str(total_count))
            print('******factor*****')
            for i in range(len(Shopping_cart)):
                print(Shopping_cart[i] + '\n')
            break


def exit():
    data_file = open('databese.txt', 'w')
    for i, product in enumerate(PRODUCTS):
        data_file.write(
            str(product['id']) + ',' + product['name'] + ',' + str(product['price']) + ',' + str(product['count']))
        if i != len(PRODUCTS) - 1:
            data_file.write('\n')
    data_file.close()


def load():
    print('Loading...')
    data_file = open('databese.txt', 'r')
    data = data_file.read()
    products_list = data.split('\n')
    for i in range(len(products_list)):
        product_info = products_list[i].split(',')
        mydict = {}
        mydict['id'] = product_info[0]
        mydict['name'] = product_info[1]
        mydict['price'] = product_info[2]
        mydict['count'] = product_info[3]
        PRODUCTS.append(mydict)
    print('Welcome')


PRODUCTS = []
load()

f = Figlet(font='standard')
print(f.renderText('Store'))

while True:
    show_menu()
    choice = int(input('please choose an action: '))

    if choice == 1:
        add_product()

    elif choice == 2:
        edit_Product()

    elif choice == 3:
        delete_product()

    elif choice == 4:
        search_name()

    elif choice == 5:
        show_list()

    elif choice == 6:
        save_qrcode()

    elif choice == 7:
        buy()

    elif choice == 8:
        exit()
        break

    count = input("If you want to continue enter 'y' : ")
    if count == 'y':
        continue
    else:
        exit()
        break

