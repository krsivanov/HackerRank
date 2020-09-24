the_class = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())  
        the_class.append([name,score])

    
sorted_class = sorted(the_class, key= lambda x: (x[1], x[0] ))
result = []
while True:
    counter = 0
    if sorted_class[counter][1]==sorted_class[counter+1][1]:
        counter+=1
        continue
    else:
        counter+=1
        if sorted_class[counter][1]== sorted_class[counter+1][1]:
            result.append(sorted_class[counter][0])
            result.append(sorted_class[counter+1][0])
            counter +=1
            break
        else:
            counter+=1
            result.append(sorted_class[counter][0])
            break

[print(x) for x in result]
