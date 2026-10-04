student_name = input("Enter your name : ")
python_score = float(input("Enter your Python score : "))
english_score = float(input("Enter your English score : "))
maths_score = float(input("Enter your Maths score : "))

average = python_score + english_score + maths_score / 3



print(f"""
========================================
          STUDENT RESULT
========================================

          Student: {student_name}

Python:       {python_score}
English:      {english_score}
Mathematics:  {maths_score}
----------------------------------------
Average:      {average}
========================================

      """)