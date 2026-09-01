# Grading scale dictionary mapping letter grades to grade points
GRADE_POINTS = {
    'A+': 4.0, 'A': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D': 1.0,
    'F': 0.0
}

def calculate_sgpa():
    print("=== SGPA Calculator ===")

    while True:
        try:
            num_courses = int(input("Enter the total number of courses: "))
            if num_courses > 0:
                break
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    courses = []
    total_credit_hours = 0
    total_grade_points = 0.0

    print("\n--- Enter Course Details ---")
    for i in range(1, num_courses + 1):
        print(f"\nCourse {i}:")
        course_name = input("  Course Name/Code: ").strip()
        if not course_name:
            course_name = f"Course {i}"

        # Get Credit Hours
        while True:
            try:
                credit_hours = float(input("  Credit Hours (e.g., 3 or 4): "))
                if credit_hours > 0:
                    break
                print("  Credit hours must be greater than 0.")
            except ValueError:
                print("  Invalid input! Enter a valid number for credit hours.")

        # Get Grade
        while True:
            grade = input("  Grade obtained (e.g., A, B+, C): ").strip().upper()
            if grade in GRADE_POINTS:
                break
            print(f"  Invalid grade! Valid options: {', '.join(GRADE_POINTS.keys())}")

        grade_point = GRADE_POINTS[grade]
        course_points = credit_hours * grade_point

        total_credit_hours += credit_hours
        total_grade_points += course_points

        courses.append({
            'name': course_name,
            'credits': credit_hours,
            'grade': grade,
            'point_val': grade_point,
            'total_points': course_points
        })

    sgpa = total_grade_points / total_credit_hours if total_credit_hours > 0 else 0.0

    # Display Breakdown
    print("\n" + "=" * 60)
    print(f"{'Course':<25} | {'Credits':<8} | {'Grade':<6} | {'Points':<8}")
    print("=" * 60)
    for c in courses:
        print(f"{c['name']:<25} | {c['credits']:<8.1f} | {c['grade']:<6} | {c['total_points']:<8.2f}")
    print("=" * 60)

    print(f"Total Credit Hours : {total_credit_hours:.1f}")
    print(f"Total Quality Points: {total_grade_points:.2f}")
    print(f"Final SGPA         : {sgpa:.2f}")
    print("=" * 60)

if __name__ == "__main__":
    calculate_sgpa()