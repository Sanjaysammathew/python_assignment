class StudentAnalysisError(Exception):
	"""Base exception for expected student analysis errors."""


class StudentNotFoundError(StudentAnalysisError):
	"""Raised when a requested student ID is not in the student records."""
