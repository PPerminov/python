def longest_number(longitude):
    stri=1
    a=2
    while (a<longitude):
        stri*=10
        a+=1
    return stri

ab=0
while ab < 1:
    longest_number(1000000)
    ab+=1
# with open('num','w') as file:
#     file.write(longest_number(100000000))
