class AdmissionForm:
    def printData(self):
        print(f"Name is {self.name}")

        print(f'Course is {self.course}')

applicant = AdmissionForm()
applicant.name="shubhangi"
applicant.course="Human Resource Management"
applicant.printData()





# class AdmissionForm:
#     def __init__(self,name,course):
#         self.name =name
#         self.course=course
#     def __repr__(self):
#         return repr("name is"+self.name+"course"+self.course)
# applicant = AdmissionForm("shubhangi","human resource management")
#
# print(applicant)
# repr(applicant)
