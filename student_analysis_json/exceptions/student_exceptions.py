class StudentNotFoundError(Exception):
    def __init__(self, message: str = "Student not found") -> None:
        super().__init__(message)


class StudentAlreadyExistsError(Exception):
    def __init__(self, message: str = "Student already exists") -> None:
        super().__init__(message)


class InvalidStudentDataError(Exception):
    def __init__(self, message: str = "Invalid student data") -> None:
        super().__init__(message)


class StudentMarksNotFoundError(Exception):
    def __init__(self, message: str = "Marks not found for student") -> None:
        super().__init__(message)


class NoMarksAvailableError(Exception):
    def __init__(self, message: str = "No marks are available for analysis") -> None:
        super().__init__(message)
