while True:
    print("         Send Instruction")
    print("bKash")
    print("1 Send money")
    print("2 Send money to non bKash")
    print("3 Mobile Recharge")
    print("4 Payment")
    print("5 CashOut")
    print("6 PayBill")
    print("7 Microfinace")
    print("8 Download bKashApp")
    print("9 MybKash")
    print("10 ResetPin")
    print("0 Back")
    v=int(input())
    if v==1:
       
        print("         Send Instruction")
        while True:
            print("Enter '0' to back")
            bkashNumber=int(input("Enter Receiver bKash Account No: "))
            if len(str(bkashNumber))>11:
                print("There are some invalide input")
            elif bkashNumber==0:
                break
            else:
                print("         Send Instruction")
                while True:
                    print("Enter '0' to back")
                    amount=int(input("Enter amount: "))
                    if amount==0:
                        break
                    elif amount>20000:
                        print("invalid amount")
                    else:
                        print("         Send Instruction")
                        while True:
                            print("Enter '0' to back")
                            pin=int(input("Enter pin: "))
                            if pin==0:
                                break
                            elif pin>9999:
                               print("invalid amount")
                               
                            else:
                                print(f"successfully send the money {amount} BDT to the {bkashNumber} account ")
                                break
    elif v==0:
        continue