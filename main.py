romano = "XVII"

romano_arabigo = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}

def append_conversions(romano):
    total = 0
    for i in romano:
        total += romano_arabigo[i]
    print(total)

append_conversions(romano)



