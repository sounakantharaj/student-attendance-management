
def attendance_percentage(present, total):
    if total <= 0:
        return 0
    return (present / total) * 100


print("\nSTUDENT ATTENDANCE MANAGEMENT SYSTEM")
print("------------------------------------")

name = input("Enter student name: ")

try:
    total = int(input("Enter total classes: "))
    present = int(input("Enter classes attended: "))

    if total < 0 or present < 0 or present > total:
        print("Invalid attendance details.")
    else:
        percentage = attendance_percentage(present, total)

        print("\n--- Attendance Report ---")
        print("Student Name:", name)
        print("Total Classes:", total)
        print("Classes Attended:", present)
        print("Attendance Percentage:", round(percentage, 2), "%")

except ValueError:
    print("Please enter valid whole numbers.")
