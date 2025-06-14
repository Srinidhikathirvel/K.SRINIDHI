🔄 Flowchart of the Quiz Game

+--------------------------+
|  Start quiz_game()      |
+-----------+--------------+
            |
            v
+--------------------------+
|  Initialize score = 0   |
+-----------+--------------+
            |
            v
+--------------------------+
|  For each question in   |
|  the questions list     |
+-----------+--------------+
            |
            v
+--------------------------+
|  Call ask_question()    |
+-----------+--------------+
            |
            v
+--------------------------+
|  Display question        |
|  and options             |
+-----------+--------------+
            |
            v
+--------------------------+
|  Get user input (1-4)   |
+-----------+--------------+
            |
            v
+-----------------------------+
|  Is input valid and correct?|
+----+--------------------+---+
     |                    |
    Yes                  No
     |                    |
     v                    v
+---------+        +------------------------+
| Print   |        | Print "Wrong answer"   |
| "Correct"        | and correct option     |
+----+----+        +------------------------+
     |                    |
     v                    v
+--------------------------+
|  Return True or False   |
+-----------+--------------+
            |
            v
+--------------------------+
|  If True, increment     |
|  score by 1             |
+-----------+--------------+
            |
            v
+--------------------------+
|  Next question?         |
+-----------+--------------+
            |
            v
+--------------------------+
|  End of loop            |
+-----------+--------------+
            |
            v
+--------------------------+
|  Print final score      |
+-----------+--------------+
            |
            v
+--------------------------+
|         End             |
+--------------------------+


---

🧠 Explanation of the Code

1. Function ask_question()

Displays the question and options.

Takes user input (1 to 4).

Checks if the answer is correct.

Handles invalid input (non-integer or out-of-range).

Returns True for correct, False otherwise.



2. Function quiz_game()

Initializes the score.

Holds a list of questions (each is a dictionary with question, options, and answer).

Loops through the questions and calls ask_question() for each.

Increments the score if the answer is correct.

Displays final score after all question.
