the_class = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())  
        the_class.append([name,score])

    
sorted_class = sorted(the_class, key= lambda x: (x[1], x[0] ))
result = []
counter = 0
while True:
    if sorted_class[counter][1]==sorted_class[counter+1][1]:
        counter+=1
        continue
    else:
        counter+=1
        if counter+1==len(sorted_class):
            result.append(sorted_class[counter][0])
            break
        else:
            if sorted_class[counter][1]== sorted_class[counter+1][1]:
                result.append(sorted_class[counter][0])
                result.append(sorted_class[counter+1][0])
                counter +=1
                break
            else:
                result.append(sorted_class[counter][0])
                break

[print(x) for x in result]


# tests 
# 4
# Prashant
# 32
# Pallavi
# 36
# Dheeraj
# 39
# Shivam
# 40


# 4
# Rachel
# -50
# Mawer
# -50
# Sheen
# -50
# Shaheen
# 51
