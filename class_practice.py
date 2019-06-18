# Enter your code here. Read input from STDIN. Print output to STDOUT

n = {
    "report": [
        { "enrollment": "rit2011001", "name": "Julia",  "subject" : [ {"code": "DSA","grade": "A" } ] }

        ,{"enrollment": "rit2011020", "name": "Samantha", "subject": [ {"code": "COM", "grade": "B"},{ "code": "DSA", "grade": "A"} ] } ]
}

dict = {}
report_value = n['report']
for i in range(len(report_value)):
    for j in range(len(report_value[i]['subject'])):
        student_list = []
        student_list.append(report_value[i]['subject'][j]['code'])
        student_list.append(report_value[i]['subject'][j]['grade'])
        student_list.append(report_value[i]['enrollment'])
        student_list.append(report_value[i]['name'])
        dict[i + j] = student_list

a = sorted(dict.values())

for i in a:
    for n in i:
        print(n,' ', end="")
    print()
