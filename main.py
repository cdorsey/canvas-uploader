import UploadFile
import UserInterface

if __name__ == '__main__':
    class_id = UserInterface.get_course()
    assign_id = UserInterface.get_assignment(class_id)
    file_name = UserInterface.get_file()

    UploadFile.upload_file(class_id, assign_id, file_name)

    print("\nAssignment submitted.")
