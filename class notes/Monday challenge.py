def sum_int_value(obj):
    sum=0
    
    for item in obj:
       if type(obj[item])==int:
           sum +=obj[item]
    print(sum)
sum_int_value(obj)