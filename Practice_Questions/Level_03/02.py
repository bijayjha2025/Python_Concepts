# Input price and calculate and calculate total bill

price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))

totalBill = price * quantity
discount = 0.1 * totalBill #10% discount

billAfterDiscount = totalBill - discount
print(f"The total bill before discount is: NPR {totalBill:.2f}")
print(f"The discount amount is: NPR {discount:.2f}")
print(f"The total bill after discount is: NPR {billAfterDiscount:.2f}")