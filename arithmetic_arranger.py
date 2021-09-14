def arithmetic_arranger(problems, solve=False):

    terms1 = list()
    terms2 = list()
    signs = list()
    results = list()
    max_digits = list()
    max_term = list()

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
      max_term.append(max([len(terms1[i]), len(terms2[i])]))
      #error conditions:
      if max_digits[i] > 4:
        return "Error: Numbers cannot be more than four digits."
      if (not terms1[i].isdigit()) or (not terms2[i].isdigit()):
        return "Error: Numbers must only contain digits."

    #line1 and line2 right justify
    #line1 = "  " + terms1[0].rjust(max_digits[0])
    #line2 = signs[0] + " " + terms2[0].rjust(max_digits[0])
    line1 = ""
    line2 = ""
    for i in range(problems_len):
      if i==0:
        line1 = "  " + terms1[i].rjust(max_digits[i])
        line2 = signs[i] + " " + terms2[i].rjust(max_digits[i])
      else:
        line1 = line1 + "    " + "  " + terms1[i].rjust(max_digits[i])
        line2 = line2 + "    " + signs[i] + " " + terms2[i].rjust(max_digits[i])

    #solves problems if solve=True
    if solve:
      for i in range(problems_len):
        if signs[i] == "+":
          results.append(int(terms1[i]) + int(terms2[i]))
        else:
          results.append(int(terms1[i]) - int(terms2[i]))
        if results[i] > len(str(max_digits[i])):
          max_digits[i] = len(str(results[i]))

    #dashes
    dashes = [None] * problems_len
    for j in range(problems_len):
      dashes[j] = "--"
      for i in range(max_term[j]):
        dashes[j] = dashes[j] + "-"

    line3 = dashes[0]
    for i in range(1, problems_len):
      line3 = line3 + "    " + dashes[i]

    #results
    if solve:
      if results[0] >= 0:
        line4 = "  " + str(results[0]).rjust(max_digits[0])
      else:
        line4 = " " + str(results[0]).rjust(max_digits[0])
      for i in range(1, problems_len):
        line4 = line4 + "    " + str(results[i]).rjust(max_term[i]+2)
      arranged_problems = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    else:
      arranged_problems = line1 + "\n" + line2  + "\n" + line3

    return arranged_problems