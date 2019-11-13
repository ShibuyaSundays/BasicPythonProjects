class Employee:
    def __init__(self, name, x1, y1, x2, y2):
        self.name = name
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)
        self.total = abs(((int(x1)-int(x2)))*(int(y1)-int(y2)))
        self.contested = 0
def main():
    input_file = open("Office.txt", "r")
    file_lines = input_file.readlines()
    line_skip = 0
    for num, lines in enumerate(file_lines):
        if line_skip > 0:
            line_skip -= 1
            continue
        office_dim = file_lines[num].split()
        office_size = int(office_dim[0]) * int(office_dim[1])
        print("Total Office Space in Square Feet:", office_size)
        employee_count = int(file_lines[num + 1])
        employees = []
        table = [[0]*int(office_dim[1]) for j in range(int(office_dim[0]))]
        for i in range(employee_count):
            employee_info = file_lines[num + 2 + i].split()
            employees.append(Employee(employee_info[0], employee_info[1], employee_info[2], employee_info[3],\
            employee_info[4]))
        for employee in employees:
            for i in range(employee.x1, employee.x2):
                for j in range(employee.y1, employee.y2):
                    table[i][j] += 1
        empty_count = 0
        contest_count = 0
        for i in range(int(office_dim[0])):
            for j in range(int(office_dim[1])):
                if table[i][j] == 0:
                    empty_count += 1
                if table[i][j] > 1:
                    contest_count += 1
        print("Unallocated Space:", empty_count)
        print("Contested Space:", contest_count)
        for employee in employees:
            for i in range(employee.x1, employee.x2):
                for j in range(employee.y1, employee.y2):
                    if table[i][j] > 1:
                        employee.contested += 1
            print(employee.name, employee.total - employee.contested)
        line_skip = employee_count + 1

main()
