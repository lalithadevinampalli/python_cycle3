list = ['1','2','3','3','4','2','1']
frequency = {}
for item in list:
    if (item in frequency):
        frequency[item] += 1
    else:
        frequency[item] = 1

for key, value in frequency.items():
    print("% s -> % d" % (key, value))
                    
        
