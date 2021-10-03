import datetime

stockitem = {
    'Soap': 12345 ,
    'Book': 1234567
}
class Stock:
    def __init__(self, name, price, stockitem, date, company):
        self.name = name
        self.price = price
        self.date = date
        self.company = company
        self.stockitem = stockitem



    def check_item(self, name):
        for i in range(len(ls)):
            if ls[i].name == name:
                return i


    def sale(self):
        n = int(input("How many products to sale: "))
        total = 0
        for j in range(n):
            name = input("Enter Product name : ")
            stockitem = int(input("Enter stockitem: "))
            card_number = int(input('Enter the  card_number'))

            i = obj.check_item(name)
            if i and ls[i].stockitem >= stockitem:
                ls[i].stockitem -= stockitem
                if ls[i].stockitem < 5:
                    print("Low Stock! Low Stock! Order Placed")
                    obj.place_order(name, ls[i].stockitem + 10)
                print("....AkshayShop....")
                print(datetime.date.today())
                print("Product Name  | stockitem  | Cost $")
                print(ls[i].name, end=" ")
                print(stockitem, end=" ")
                print(ls[i].price * stockitem)
                total += ls[i].price * stockitem
                print("\n")
                print("Total Cost----->", "$" + total)
            else:
                print("Product out of stock or not enough stockitem")



    def purchase(self):
        name = input("Enter Product name: ")
        date = datetime.date.today()
        i = obj.check_item(name)
        if i:
            ls[i].stockitem += int(input("Enter stockitem: "))
            ls[i].price = int(input("Enter product price: "))
            ls[i].date = date
            ls[i].company = self.company
        else:
            stockitem = int(input("Enter stock item: "))
            price = int(input("Enter product price: "))
            ob = Stock(name, price, stockitem, date, self.company)
            ls.append(ob)



    def luhn_checksum(card_number):
        def digits_of(n):

            return [int(d) for d in str(n)]


        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return checksum % 10

    print('Valid') if luhn_checksum("4532015112830366") == 0 else print('Invalid')

    def Cvv_Checksum(CVV):
         def digits_of(n):

             return [int(C) for C  in str(n) ]




    def place_order(self, name,stockitem,company,card_number):
        return name, stockitem , company,card_number



    def print_products(self):
        def __repr__(self):
            return str(self.name) + str(self.price) + str(self.stockitem) + str(self.date) + str(self.company)+str(self.card_number) +str(self.CVV)

        return __repr__



    def demo(self):
        print("Welcome To AkshayShop")
        print("choose an option below")
        print("\n1.Enter a Product\n2.Make a sale \n3.See all Products\n6.Exit")
        option = int(input("Enter the option here:"))
        print("\nEnter the card_number")
        print('\nEnter the cvv code')


        while True:

            if option == 1:
                obj.purchase()
            elif option == 2:
                obj.sale()
            elif option == 3:
                obj.print_products()
                break
            elif option == 4:
                obj.luhn_checksum()
            elif option == 5:
                obj.Cvv_Checksum()

            else:
                print("Enter a valid input!")


ls = []

obj = Stock('', 0, 0, 0 , '')
obj.demo()