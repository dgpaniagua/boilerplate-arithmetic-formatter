def arithmetic_arranger(problems, solve=False):

    terms1 = list()
    terms2 = list()
    signs = list()
    results = list()

    for problem in problems:
      terms1.append(problem.split()[0])
      signs.append(problem.split()[1])
      terms2.append(problem.split()[2])

    if solve:
      for i in range(len(problems)):
        if signs[i] == "+":
          results.append(int(terms1[i]) + int(terms2[i]))
        elif signs[i] == "-":
          results.append(int(terms1[i]) - int(terms2[i]))

    arranged_problems = [terms1, signs, terms2, results]

    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))