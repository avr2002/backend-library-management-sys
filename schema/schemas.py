def individual_serial(student) -> dict:
    return {
        'id': str(student['_id']),
        'name': student['name'],
        'age': student['age'],
        'address': student['address']
    }


def list_serial(students) -> list:
    return [individual_serial(student) for student in students]
