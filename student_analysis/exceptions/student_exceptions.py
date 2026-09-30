class StudentAnalysisError(Exception):
    pass
class StudentNotFoundError(StudentAnalysisError):
    pass

class StudentAlreadyExistsError(StudentAnalysisError):
    pass

class InvalidStudentDataError(StudentAnalysisError):
    pass

class StudentFileError(StudentAnalysisError):
    pass
