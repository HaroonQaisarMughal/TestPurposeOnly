def get_student_result(student_id: str) -> dict:
    """Retrieves fictional academic results for a given student ID.
    
    Args:
        student_id: The unique identifier for the student (e.g., 'STU-101').
        
    Returns:
        A dictionary containing the student's name, grade, major, GPA, and status,
        or an error message if the ID is not found.
    """
    # Fictional database stored in a simple Python dictionary
    mock_database = {
        "STU-101": {
            "name": "Amina Al-Balushi",
            "major": "Computer Science",
            "gpa": 3.85,
            "status": "Honor Roll",
            "completed_credits": 90,
        },
        "STU-102": {
            "name": "Marcus Vance",
            "major": "Mechanical Engineering",
            "gpa": 3.10,
            "status": "In Good Standing",
            "completed_credits": 64,
        },
        "STU-103": {
            "name": "Elena Rostova",
            "major": "Data Analytics",
            "gpa": 3.92,
            "status": "Honor Roll",
            "completed_credits": 110,
        },
    }

    # Normalize ID to prevent casing mismatches
    normalized_id = student_id.strip().upper()

    # Safely retrieve data or return a deterministic fallback
    if normalized_id in mock_database:
        return {
            "success": True,
            "student_id": normalized_id,
            "data": mock_database[normalized_id],
        }
    
    return {
        "success": False,
        "student_id": normalized_id,
        "error": f"Student ID '{student_id}' not found in the records.",
    }


# Demonstration of execution:
if __name__ == "__main__":
    # Test valid student
    result_valid = get_student_result("STU-101")
    print("Found Record:", result_valid)

    # Test unknown student
    result_invalid = get_student_result("STU-999")
    print("Missing Record:", result_invalid)