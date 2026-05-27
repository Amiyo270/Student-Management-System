class StudentDatabase:
    __student_list = []

    @classmethod
    def add_student(cls, student_obj):
        """Class method to insert a Student object into the student list."""
        cls.__student_list.append(student_obj)

    @classmethod
    def get_all_students(cls):
        """Helper method to access the private student list."""
        return cls.__student_list


class Student:
    def __init__(self, student_id, name, department, is_enrolled=True):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        
        StudentDatabase.add_student(self)

    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def is_enrolled(self):
        return self.__is_enrolled

    def enroll_student(self):
        if self.__is_enrolled:
            print(f"Error: Student {self.__name} (ID: {self.__student_id}) is already enrolled.")
        else:
            self.__is_enrolled = True
            print(f"Success: {self.__name} has been successfully enrolled.")

    def drop_student(self):
        if not self.__is_enrolled:
            print(f"Error: Student {self.__name} (ID: {self.__student_id}) is already marked as dropped/not enrolled.")
        else:
            self.__is_enrolled = False
            print(f"Success: {self.__name} has been dropped from the system.")

    def view_student_info(self):
        status = "Enrolled" if self.__is_enrolled else "Dropped"
        print(f"ID: {self.__student_id} | Name: {self.__name} | Department: {self.__department} | Status: {status}")


s1 = Student("S101", "Amiyo Bushon Chakraborty", "Computer Science", True)
s2 = Student("S102", "Diya Anower", "Electrical Engineering", False)
s3 = Student("S103", "Priyo pal", "Mechanical Engineering", True)
s4 = Student("S104", "Niloy Das", "English", True)


def find_student_by_id(student_id):
    """Searches the database and returns the student object if found."""
    for student in StudentDatabase.get_all_students():
        if student.get_student_id() == student_id:
            return student
    return None


def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        print("-" * 33)

        if choice == "1":
            students = StudentDatabase.get_all_students()
            if not students:
                print("No students found in the database.")
            else:
                print("\nAll Student Records:")
                for student in students:
                    student.view_student_info()

        elif choice == "2":
            student_id = input("Enter Student ID to enroll: ").strip()
            student = find_student_by_id(student_id)
            
            if student is None:
                print(f"Error: Student ID '{student_id}' does not exist.")
            else:
                student.enroll_student()

        elif choice == "3":
            student_id = input("Enter Student ID to drop: ").strip()
            student = find_student_by_id(student_id)
            
            if student is None:
                print(f"Error: Student ID '{student_id}' does not exist.")
            else:
                student.drop_student()

        elif choice == "4":
            print("Exiting system. Goodbye!")
            break
            
        else:
            print("Invalid selection. Please choose a valid option (1-4).")

if __name__ == "__main__":
    main()