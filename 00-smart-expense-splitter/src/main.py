from services.expense_split_service import (
	split_expense,
	final_bill,
	display_receipt)

print("===== Smart Expense Splitter =====\n")

# starter function
def main():
	# taking inputs
	# trip/event name
	print("Enter trip/event name : ",end="")
	trip_name = input()

	# total amount of bill
	print("Enter total bill amount : ",end="")
	total_bill_amt = float(input())

	# total number of peoples
	print("Enter number of people : ",end="")
	total_people = int(input())

	# discount percentage
	print("Enter discount percentage : ",end="")
	discount_percentage = float(input())

	# service charge percentage
	print("Enter service charge percentage : ",end="")
	service_charge_percentage = float(input())

	# calculate final bill amount
	final_bill_amount = final_bill(total_bill_amt, discount_percentage, service_charge_percentage)

	# calculating final amount each person should contribute
	# calling split_expense from expense_split_service
	amount_per_person = split_expense(final_bill_amount, total_people)

	
	# printing receipt
	# calling display_receipt from expense_split_service
	display_receipt(trip_name, total_bill_amt, discount_percentage, service_charge_percentage, final_bill_amount, amount_per_person)


# starter
if __name__ == "__main__":
	# calling main()
	main()