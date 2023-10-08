class Project4:
    def __init__(self):
        self.fb = 0
        self.gb = 0
        self.dis = 0
        self.n1 = [None] * 30
        self.c1 = [0] * 30
        self.q1 = [0] * 30
        self.x = 0
        self.flag = False

    def main(self):
        print("\f                                                         THE BETTLE HOUSE")
        print("                                                         MALLAPUR,HYDERABAD")
        print("**********************************************************************************************************************************************")

        ans = "yes"
        while ans.lower() == "yes":
            print("WHICH DISH DO YOU WANT TO HAVE ")
            print("1-STARTERS")
            print("2-MAIN COURSE")
            print("3-DESSERTS")
            print("4-BEVERAGES")
            print("5-YOUR ORDERS")
            print("6-BILL")
            ch = int(input("ENTER YOUR OPTION: "))

            if ch == 1:
                self.sta()
            elif ch == 2:
                self.mai()
            elif ch == 3:
                self.des()
            elif ch == 4:
                self.bev()
            elif ch == 5:
                self.order()
            elif ch == 6:
                self.bill()
            else:
                print("INVALID")

            ans = input("ANY MORE TRANSACTIONS (YES/NO): ").lower()

        if not self.flag:
            print("Pay the bill")
            self.bill()

    def sta(self):
        bill = 0
        n = ["CHINESE STARTERS", "ITALIAN STARTERS"]
        for i in range(2):
            print(f"{i + 1}-{n[i]}")
        ch = int(input("ENTER YOUR CHOICE AND 0 FOR MENU: "))
        if ch == 0:
            self.main()
        else:
            if ch == 1:
                self.chi()
            elif ch == 2:
                self.ita()
            else:
                print("INVALID")

    def mai(self):
        bill = 0
        n = ["BIRYANIS", "NOODLES & RICE", "INDIAN BREADS", "CURRIES"]
        for i in range(4):
            print(f"{i + 1}-{n[i]}")
        ch = int(input("ENTER YOUR CHOICE AND 0 FOR MENU: "))
        if ch == 0:
            self.main()
        else:
            if ch == 1:
                self.bir()
            elif ch == 2:
                self.noo()
            elif ch == 3:
                self.ind()
            elif ch == 4:
                self.cur()
            else:
                print("INVALID")

    def des(self):
        bill = 0
        n = ["ICE CREAMS", "PASTRIES"]
        for i in range(2):
            print(f"{i + 1}-{n[i]}")
        ch = int(input("ENTER YOUR CHOICE AND 0 FOR MENU: "))
        if ch == 0:
            self.main()
        else:
            if ch == 1:
                self.ice()
            elif ch == 2:
                self.pas()
            else:
                print("INVALID")

    def bev(self):
        bill = 0
        n = ["SOFT DRINKS", "HARD DRINKS", "JUICES", "MILKSHAKES"]
        for i in range(4):
            print(f"{i + 1}-{n[i]}")
        ch = int(input("ENTER YOUR CHOICE AND 0 FOR MENU: "))
        if ch == 0:
            self.main()
        else:
            if ch == 1:
                self.soft()
            elif ch == 2:
                self.hard()
            elif ch == 3:
                self.jui()
            elif ch == 4:
                self.milk()
            else:
                print("INVALID")

    def order(self):
        print("YOUR ORDERS")
        print("ITEMS                       COST PER UNIT  QUANTITY  TOTAL COST ")
        for i in range(self.x):
            print(f"{self.n1[i]}\t{self.c1[i]}            {self.q1[i]}         {self.c1[i] * self.q1[i]}")
        print(f"TOTAL BILL-  {self.fb}")

    def bill(self):
        print("\f")
        self.flag = True
        gst = self.fb * 0.21
        st = self.fb * 0.05
        print(f"TOTAL BILL-  {self.fb}")
        s = ""
        print("MODE OF PAYMENT")
        print("1.CASH")
        print("2.CREDIT CARD")
        print("3.DEBIT CARD")
        self.gb = self.fb
        ch = int(input())
        if ch == 1:
            s = input("DO U HAVE ANY COUPONS(YES/NO): ")
            if s.lower() == "yes":
                self.cou()
        elif ch == 2:
            self.cardc()
        elif ch == 3:
            self.cardd()
        else:
            print("INVALID")
        self.gb = self.gb + st + gst - self.dis
        print("                             THE BETTLE HOUSE                           ")
        print("                             MALLAPUR,HYDERABAD")
        print("                             YOUR BILL")
        print("    YOUR ORDERS")
        print("    ITEMS                       COST PER UNIT  QUANTITY  TOTAL COST ")
        for i in range(self.x):
            print(f"    {self.n1[i]}\t  {self.c1[i]}               {self.q1[i]}           {self.c1[i] * self.q1[i]}")
        print(f"    TOTAL BILL-  {self.fb}")
        print(f"    TAXES-       {gst + st}")
        print(f"    DISCOUNT-    {self.dis}")
        print("                -------")
        print(f"    GRAND BILL-  {self.gb}")
        print("                -------")
        print("    THANK YOU")
        print("    VISIT AGAIN")
        print("\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606\u2606")
        exit(0)

    def cou(self):
        if self.fb >= 5000:
            s = input("ENTER YOUR COUPON: ")
            if s == "JUMBO" or s == "jumbo":
                self.dis = self.fb * 0.15
            else:
                print("INVALID")
        elif self.fb >= 3000:
            s = input("ENTER YOUR COUPON: ")
            if s == "MEDIUM" or s == "medium":
                self.dis = self.fb * 0.1
            else:
                print("INVALID")
        elif self.fb >= 1000:
            s = input("ENTER YOUR COUPON: ")
            if s == "SMALL" or s == "small":
                self.dis = self.fb * 0.05
            else:
                print("INVALID")
        else:
            print("NO DISCOUNT FOR THE PARTICULAR BILL")

    def cardc(self):
        print("PAYMENT THROUGH CREDIT CARD")
        print("ENTER CARD NUMBER: ")
        s = input()
        if len(s) != 16:
            print("INVALID CARD NUMBER")
            return
        print("ENTER CVV NUMBER: ")
        s = input()
        if len(s) != 3:
            print("INVALID CVV NUMBER")
            return
        print("ENTER EXPIRY DATE: ")
        s = input()
        if len(s) != 5:
            print("INVALID EXPIRY DATE")
            return

    def cardd(self):
        print("PAYMENT THROUGH DEBIT CARD")
        print("ENTER CARD NUMBER: ")
        s = input()
        if len(s) != 16:
            print("INVALID CARD NUMBER")
            return
        print("ENTER CVV NUMBER: ")
        s = input()
        if len(s) != 3:
            print("INVALID CVV NUMBER")
            return
        print("ENTER EXPIRY DATE: ")
        s = input()
        if len(s) != 5:
            print("INVALID EXPIRY DATE")
            return

    def bir(self):
        bill = 0
        n = ["CHICKEN BIRYANI", "MUTTON BIRYANI"]
        for i in range(2):
            print(f"{i + 1}-{n[i]}")
        ch = int(input("ENTER YOUR CHOICE AND 0 FOR MENU: "))
        if ch == 0:
            self.mai()
        else:
            if ch == 1:
                bill = 250
            elif ch == 2:
                bill = 300
            else:
                print("INVALID")
            self.qua(n[ch - 1], bill)

    def noo(self):
        bill = 0
        n = ["VEG NOODLES", "EGG NOODLES", "VEG FRIED RICE", "EGG FRIED RICE"]
        for i in range(4):
            print(f"{i + 1}-{n[i]}")
        ch = int(input("ENTER YOUR CHOICE AND 0 FOR MENU: "))
        if ch == 0:
            self.mai()
        else:
            if ch == 1:
                bill = 150
            elif ch == 2:
                bill = 180
            elif ch == 3:
                bill = 160
            elif ch == 4:
                bill = 190
            else:
                print("INVALID")
            self.qua(n[ch - 1], bill)

    def ind(self):
        bill = 0
        n = ["ROTI", "NAN", "PULKA", "KULCHA"]
        for i in range(4):
            print(f"{i + 1}-{n[i]}")
        ch = int(input("ENTER YOUR CHOICE AND 0 FOR MENU: "))
        if ch == 0:
            self.mai()
        else:
            if ch == 1:
                bill = 10
            elif ch == 2:
                bill = 20
            elif ch == 3:
                bill = 15
            elif ch == 4:
                bill = 25
            else:
                print("INVALID")
            self.qua(n[ch - 1], bill)

    def cur(self):
        bill = 0
        n = ["VEG CURRY", "CHICKEN CURRY", "MUTTON CURRY"]
        for i in range(3):
            print(f"{i + 1}-{n[i]}")
        ch = int(input("ENTER YOUR CHOICE AND 0 FOR MENU: "))
        if ch == 0:
            self.mai()
        else:
            if ch == 1:
                bill = 150
            elif ch == 2:
                bill = 200
            elif ch == 3:
                bill = 250
            else:
                print("INVALID")
            self.qua(n[ch - 1], bill)

    def soft(self):
        bill = 0
        n = ["PEPSI", "COCA COLA", "MIRINDA", "SPRITE"]
        for i in range(4):
            print(f"{i + 1}-{n[i]}")
        ch = int(input("ENTER YOUR CHOICE AND 0 FOR MENU: "))
        if ch == 0:
            self.bev()
        else:
            if ch == 1:
                bill = 30
            elif ch == 2:
                bill = 30
            elif ch == 3:
                bill = 30
            elif ch == 4:
                bill = 30
            else:
                print("INVALID")
            self.qua(n[ch - 1], bill)

    def hard(self):
        bill = 0
        n = ["KINGFISHER", "OLD MONK", "ROYAL STAG", "MAGIC MOMENTS"]
        for i in range(4):
            print(f"{i + 1}-{n[i]}")
        ch = int(input("ENTER YOUR CHOICE AND 0 FOR MENU: "))
        if ch == 0:
            self.bev()
        else:
            if ch == 1:
                bill = 180
            elif ch == 2:
                bill = 150
            elif ch == 3:
                bill = 160
            elif ch == 4:
                bill = 200
            else:
                print("INVALID")
            self.qua(n[ch - 1], bill)

    def jui(self):
        bill = 0
        n = ["ORANGE", "MANGO", "APPLE", "PINEAPPLE"]
        for i in range(4):
            print(f"{i + 1}-{n[i]}")
        ch = int(input("ENTER YOUR CHOICE AND 0 FOR MENU: "))
        if ch == 0:
            self.bev()
        else:
            if ch == 1:
                bill = 40
            elif ch == 2:
                bill = 50
            elif ch == 3:
                bill = 45
            elif ch == 4:
                bill = 45
            else:
                print("INVALID")
            self.qua(n[ch - 1], bill)

    def milk(self):
        bill = 0
        n = ["VANILLA", "STRAWBERRY", "CHOCOLATE", "BUTTERSCOTCH"]
        for i in range(4):
            print(f"{i + 1}-{n[i]}")
        ch = int(input("ENTER YOUR CHOICE AND 0 FOR MENU: "))
        if ch == 0:
            self.bev()
        else:
            if ch == 1:
                bill = 60
            elif ch == 2:
                bill = 70
            elif ch == 3:
                bill = 65
            elif ch == 4:
                bill = 65
            else:
                print("INVALID")
            self.qua(n[ch - 1], bill)

    def chi(self):
        bill = 0
        n = ["CHILLI CHICKEN", "MANCHURIA"]
        for i in range(2):
            print(f"{i + 1}-{n[i]}")
        ch = int(input("ENTER YOUR CHOICE AND 0 FOR MENU: "))
        if ch == 0:
            self.sta()
        else:
            if ch == 1:
                self.q(n[ch - 1], 180)
            elif ch == 2:
                self.q(n[ch - 1], 160)
            else:
                print("INVALID")

    def ita(self):
        bill = 0
        n = ["PASTA", "GARLIC BREAD"]
        for i in range(2):
            print(f"{i + 1}-{n[i]}")
        ch = int(input("ENTER YOUR CHOICE AND 0 FOR MENU: "))
        if ch == 0:
            self.sta()
        else:
            if ch == 1:
                self.q(n[ch - 1], 150)
            elif ch == 2:
                self.q(n[ch - 1], 100)
            else:
                print("INVALID")

    def ice(self):
        bill = 0
        n = ["CHOCOLATE", "VANILLA", "STRAWBERRY", "BUTTERSCOTCH"]
        for i in range(4):
            print(f"{i + 1}-{n[i]}")
        ch = int(input("ENTER YOUR CHOICE AND 0 FOR MENU: "))
        if ch == 0:
            self.des()
        else:
            if ch == 1:
                self.q(n[ch - 1], 40)
            elif ch == 2:
                self.q(n[ch - 1], 30)
            elif ch == 3:
                self.q(n[ch - 1], 35)
            elif ch == 4:
                self.q(n[ch - 1], 35)
            else:
                print("INVALID")

    def pas(self):
        bill = 0
        n = ["PINEAPPLE", "BLACKFOREST", "BUTTERSCOTCH"]
        for i in range(3):
            print(f"{i + 1}-{n[i]}")
        ch = int(input("ENTER YOUR CHOICE AND 0 FOR MENU: "))
        if ch == 0:
            self.des()
        else:
            if ch == 1:
                self.q(n[ch - 1], 120)
            elif ch == 2:
                self.q(n[ch - 1], 150)
            elif ch == 3:
                self.q(n[ch - 1], 130)
            else:
                print("INVALID")

    def qua(self, s, bill):
        print(f"ENTER QUANTITY OF {s}: ")
        self.q1[self.x] = int(input())
        self.n1[self.x] = s
        self.c1[self.x] = bill
        self.x += 1
        self.fb += bill * self.q1[self.x - 1]

    def q(self, s, bill):
        print(f"ENTER QUANTITY OF {s}: ")
        self.q1[self.x] = int(input())
        self.n1[self.x] = s
        self.c1[self.x] = bill
        self.x += 1
        self.fb += bill

proj = Project4()
proj.main()
