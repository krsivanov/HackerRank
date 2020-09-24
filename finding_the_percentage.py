if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

result = 0
if query_name in student_marks:
    for x in range(len(student_marks[query_name])):
        result += student_marks[query_name][x]
        avg_rslt = result/len(student_marks[query_name])
print(f"{avg_rslt:.2f}")
