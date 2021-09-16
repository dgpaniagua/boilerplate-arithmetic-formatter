def arithmetic_arranger(problems, solve=False):

    #variables declarations
    terms1 = list()
    terms2 = list()
    signs = list()
    results = list()
    max_digits = list()
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    #too many problems error:
    problems_len = len(problems)
    if problems_len > 5:
      return "Error: Too many problems."

    #parses the problems
    for problem in problems:
      terms1.append(problem.split()[0])
      signs.append(problem.split()[1])
      terms2.append(problem.split()[2])

    #operator error:
    for sign in signs:
      if sign not in ["+","-"]:
        return "Error: Operator must be '+' or '-'."
    
    #search for the term with the maximum number of digits
    for i in range(problems_len):
      max_digits.append(max([len(terms1[i]), len(terms2[i])]))
      #maximum digits error:
      if max_digits[i] > 4:
        return "Error: Numbers cannot be more than four digits."
      #only digits error
      if (not terms1[i].isdigit()) or (not terms2[i].isdigit()):
        return "Error: Numbers must only contain digits."

    #line1, line2 and line3
    dashes = [None] * problems_len
    for i in range(problems_len):
      whitespace = "" if i==0 else "    "
      line1 = line1 + whitespace + "  " + terms1[i].rjust(max_digits[i])
      line2 = line2 + whitespace + signs[i] + " " + terms2[i].rjust(max_digits[i])
      dashes[i] = "--"
      for j in range(max_digits[i]):
        dashes[i] = dashes[i] + "-"
      line3 = line3 + whitespace + dashes[i]

    #solves problems if solve=True and create line 4
      if solve:
        results.append((int(terms1[i]) + int(terms2[i])) if signs[i] == "+" else int(terms1[i]) - int(terms2[i]))
        if i==0:
          whitespace = "  " if results[i] >= 0 else  " "
          justify = 0
        else:
          justify = 2
        line4 = line4 + whitespace + str(results[i]).rjust(max_digits[i]+ justify)

      arranged_problems = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 if solve else line1 + "\n" + line2  + "\n" + line3

    return arranged_problems