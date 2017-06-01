#num_array = []
#num = input("Enter number of days:")
#print 'Enter temperature in celsius: '
#for i in range(1,num+1):
#    n = input("Enter temperature for day "+str(i)+" :")
#    num_array.append(n)
#print 'temperature in celsius for last 7 days of Mumbai: ',num_array

#fahrenheit = (celsius * 1.8) + 32
num_array = [10,20,30,40,33,30,7]
def convert(num_array):
    #num_array_new = [x*33.8 for x in num_array]
    num_array_new = [(x * 1.8) + 32 for x in num_array]
    return num_array_new

output = convert(num_array)
#print 'temperature in fahrenheit for last 7 days of Mumbai: ',output
print output
