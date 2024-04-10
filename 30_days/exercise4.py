salary = float( input( "Enter yoour salary amount in KSH:" ))

def calculate_basic_needs():
    basic_amount = salary * 0.5
    return salary * 0.5
def calculate_wants():
    balance_50 = float(salary - basic_amount)
    wants = 0.3 * balance_50
    return wants
def calculate_savings():
    saving = (salary - (balance_50 + wants))
    return saving

basic_amount = basic_amount = salary * 0.5
balance_50 = float(salary - basic_amount)
wants =  0.3 * balance_50
saving = (salary - (balance_50 + wants))

result = print("Based on the 50/30/20 Rule the basic needs should be: ", calculate_basic_needs())
result = print("Based on the 50/30/20 Rule the Wants amount should be: ", calculate_wants())
result = print("Based on the 50/30/20 Rule your savings should be: ", calculate_savings())