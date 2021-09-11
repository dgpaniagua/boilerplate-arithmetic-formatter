def arithmetic_arranger(problems, solve=False):

    terms1 = list()
    terms2 = list()
    signs = list()
    results = list()
    max_digits = list()
    top_max = list()
    

    #parses the problems
    for problem in problems:
      terms1.append(problem.split()[0])
      signs.append(problem.split()[1])
      terms2.append(problem.split()[2])
    
    #search for the term with the maximum number of digits
    for i in range(len(problems)):
      if len(terms1[i]) > len(terms2[i]):
        max_digits.append(len(terms1[i]))
        top_max.append(True)
      else:
        max_digits.append(len(terms2[i]))
        top_max.append(False)

    #solves problems if solve=True
    if solve:
      for i in range(len(problems)):
        if signs[i] == "+":
          results.append(int(terms1[i]) + int(terms2[i]))
        elif signs[i] == "-":
          results.append(int(terms1[i]) - int(terms2[i]))

    #line1 and line2 right justify
    line1 = "  " + terms1[0].rjust(max_digits[0])
    line2 = signs[0] + " " + terms2[0].rjust(max_digits[0])

    for i in range(1, len(problems)):
      line1 = line1 + "    " + "  " + terms1[i].rjust(max_digits[i])
      line2 = line2 + "    " + signs[i] + " " + terms2[i].rjust(max_digits[i])

    #dashes
    dashes = [None] * len(problems)
    for j in range(len(problems)):
      dashes[j] = "--"
      for i in range(max_digits[j]):
        dashes[j] = dashes[j] + "-"
        
    line3 = dashes[0]
    for i in range(1, len(problems)):
      line3 = line3 + "    " + dashes[i]

    arranged_problems = line1 + "\n" +line2 + "\n" + line3

    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))