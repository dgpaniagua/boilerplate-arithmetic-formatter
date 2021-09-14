def arithmetic_arranger(problems, solve=False):

    terms1 = list()
    terms2 = list()
    signs = list()
    results = list()
    max_digits = list()
    max_term = list()

    #to many problems error:
    if len(problems) > 5:
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
    for i in range(len(problems)):
      if len(terms1[i]) > len(terms2[i]):
        max_digits.append(len(terms1[i]))
        max_term.append(len(terms1[i]))
      else:
        max_digits.append(len(terms2[i]))
        max_term.append(len(terms2[i]))
      if max_digits[i] > 4:
        return "Error: Numbers cannot be more than four digits."
      for digit in terms1[i]:
        if digit not in ["0","1","2","3","4","5","6","7","8","9"]:
          return "Error: Numbers must only contain digits."
      for digit in terms2[i]:
        if digit not in ["0","1","2","3","4","5","6","7","8","9"]:
          return "Error: Numbers must only contain digits."

    #line1 and line2 right justify
    line1 = "  " + terms1[0].rjust(max_digits[0])
    line2 = signs[0] + " " + terms2[0].rjust(max_digits[0])

    for i in range(1, len(problems)):
      line1 = line1 + "    " + "  " + terms1[i].rjust(max_digits[i])
      line2 = line2 + "    " + signs[i] + " " + terms2[i].rjust(max_digits[i])

        #solves problems if solve=True
    if solve:
      for i in range(len(problems)):
        if signs[i] == "+":
          results.append(int(terms1[i]) + int(terms2[i]))
        elif signs[i] == "-":
          results.append(int(terms1[i]) - int(terms2[i]))
        if results[i] > len(str(max_digits[i])):
          max_digits[i] = len(str(results[i]))

    #dashes
    dashes = [None] * len(problems)
    for j in range(len(problems)):
      dashes[j] = "--"
      for i in range(max_term[j]):
        dashes[j] = dashes[j] + "-"

    line3 = dashes[0]
    for i in range(1, len(problems)):
      line3 = line3 + "    " + dashes[i]

    #results
    if solve:
      if results[0] >= 0:
        line4 = "  " + str(results[0]).rjust(max_digits[0])
      else:
        line4 = " " + str(results[0]).rjust(max_digits[0])
      for i in range(1, len(problems)):
        line4 = line4 + "    " + str(results[i]).rjust(max_term[i]+2)
      arranged_problems = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    else:
      arranged_problems = line1 + "\n" + line2  + "\n" + line3

    return arranged_problems