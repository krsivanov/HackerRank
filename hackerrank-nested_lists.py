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
    if sorted_class[0][counter]==sorted_class[0][counter+1]:
        counter += 1
        continue
    else:
        if sorted_class[0][counter]== sorted_class[0][counter+1]:
            result.append(sorted_class[0][counter])
            result.append(sorted_class[0][counter+1])
            counter +=1
            continue
        else:
            result.append(sorted_class[0][counter])
            break


print(result)
