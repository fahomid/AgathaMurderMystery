# Murder Mystery Solver - Who Killed Agatha?

Someone in Dreadsbury Mansion killed Aunt Agatha. Agatha, the butler, and Charles live in Dreadsbury Mansion, and are the only ones to live there. A killer always hates and is no richer than his victim. Charles hates no one that Agatha hates. Agatha hates everybody except the butler. The butler hates everyone not richer than Aunt Agatha. The butler hates everyone whom Agatha hates. No one hates everyone. Who killed Agatha?

---

## Solution in Python

This Python script solves a murder mystery using Constraint Satisfaction Problem (CSP) techniques. The problem involves determining the killer, the victim, relationships of hate, and wealth relations among three people: Agatha, Butler, and Charles.

### How to Run

To run the script, follow these steps:

1. Ensure you have Python installed on your machine.
2. Install the `python-constraint` library. You can install it using the following command:
    ```
    pip install python-constraint
    ```
3. Run the `script.py` python code.

### Code Explanation

- The script uses the `python-constraint` library to define a CSP problem.
- Variables are defined for the people (Agatha, Butler, Charles) and their wealth status (0: poorest, 1: richer, 2: richest).
- Additional variables represent the killer and the victim.
- Constraints are added to model relationships such as hatred and wealth comparisons.
- The script then solves the CSP problem and prints all possible solutions.

### Result

The script outputs various solutions to the murder mystery, including the killer, the victim, who hates whom, and wealth relations. Each solution represents a consistent scenario satisfying the defined constraints.

### Example Output

| Killer   | Victim   | Hates       | Richer      |
|----------|----------|-------------|-------------|
| Charles  | Charles  | 1 1 1       | 0 0 1       |
|          |          | 1 1 1       | 0 0 1       |
|          |          | 1 1 1       | 1 1 0       |

The output provides information about the killer, victim, who hates whom, and wealth relations for each possible solution.

---
