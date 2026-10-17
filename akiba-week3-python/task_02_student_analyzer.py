students = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67}
]

def score_validation(students):
    students_result = []
    
    for student in students:
        score = student["score"]
        if score < 0:
            return "invalid score"
        elif score > 100:
            return "score must be under 100"
        else:
            students_result.append(score)
            
    return students_result

def avg_score(students):
    scores =  score_validation(students)
    
    if isinstance(scores, str): 
        return scores
    
    total = 0
    for score in scores: 
        total += score
    
    avg = total / len(scores)
    return avg

def calculate_grade(students):
    result = []
    for student in students:
        score = student["score"]
        
        if score >= 90:
            result.append("A")
          
        elif score >= 80:
            result.append("B")
           
        elif score >= 70:
            result.append("C")
          
        elif score >= 60:
            result.append("D")
           
        else:
            result.append("F")
    
    return result

def scores_degree(students):
    highest = students[0]["score"]
    smallest = students[0]["score"]
    for student in students:
        score = student["score"]
        if score > highest:
            highest = score
    
        if score < smallest:
            smallest = score
            
   
    return highest, smallest

def count_passed_failed(students):
    pass_count = 0
    fail_count = 0
    
    for student in students:
        score = student["score"]
        
        if score >= 50:
            pass_count += 1
        elif score < 50:
            fail_count += 1
       
    return pass_count,fail_count


def generate_report(students):
    validation_result = score_validation(students) 
    
    if isinstance(validation_result, str):
        print(validation_result)
        return
    
    average = avg_score(students)
    highest, lowest = scores_degree(students)
    passed, failed = count_passed_failed(students)
    grades = calculate_grade(students)
    
    
    print("\n========== STUDENT PERFORMANCE REPORT ==========\n")
    
    print(f"{'Name':<12}{'Score':<10}{'Grade':<10}")
    print("-" * 32)
    for index, student in enumerate(students):
        name = student["name"]
        score = student["score"]
        grade = grades[index]
        print(f"{name:<12}{score:<10}{grade:<10}")



    print("\n============== CLASS STATISTICS ==============")
    print(f"Class Average:    {average}")
    print(f"Highest Score:    {highest}")
    print(f"Lowest Score:     {lowest}")
    print(f"Students Passed:  {passed}")
    print(f"Students Failed:  {failed}")
    print("=" * 48)


score_validation(students)
avg_score(students)
scores_degree(students)
count_passed_failed(students)
calculate_grade(students)
generate_report(students)