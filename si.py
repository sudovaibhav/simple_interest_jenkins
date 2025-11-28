import sys
if len(sys.argv) == 4:
    script_name = sys.argv[0]
    principal = sys.argv[1]
    rate_of_interest = sys.argv[2]
    time = sys.argv[3]
else:
    script_name = sys.argv[0]
    principal = 10000
    rate_of_interest = 10
    time = 3
    print("Invalid input using default values.")
    simple_interest = (principal * time * rate_of_interest) / 100
    print(f"Principal amount: {principal}\nRate of interest: {rate_of_interest}\nTime in years: {time}\nSimple interest : {simple_interest}")
    