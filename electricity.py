def total_calc(bill_amount,total_perc):
    total=bill_amount*(1+0.001*total_perc)
    print(f"your amount is${total}")
total_calc(150,20)