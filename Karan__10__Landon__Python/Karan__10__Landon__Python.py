def subSplit(sub, equation):
    again=True
    while again:
        again=False
        for i in range(0,len(equation)):
            if equation[i]==sub and equation[i-1:i+2]!=" "+sub+" ":
                again=True
                equation = equation[:i] + " " + sub + " " + equation[i+1:]
    return equation

#problem = input("What is the equation: ")
problem = "2+3+7-246*(426%5)"
problem = subSplit("+", problem)
problem = subSplit("-", problem)
problem = subSplit("*", problem)
problem = subSplit("/", problem)
problem = subSplit("^", problem)
problem = subSplit("%", problem)
problem = subSplit("(", problem)
problem = subSplit(")", problem)
equations = problem.split()
print(problem)
print(equations)