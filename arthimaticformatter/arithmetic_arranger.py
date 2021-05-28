def arithmetic_arranger(problems, sol=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    firstLine = ""
    secondLine = ""
    thirdLine = ""
    if sol:
        fourthLine = ""

    for i in range(len(problems)):
        prob = problems[i].split()

        if prob[1] == "+" or prob[1] == "-":

            length = max(len(prob[0]), len(prob[2])) + 2

            if (length - 2) > 4:
                return "Error: Numbers cannot be more than four digits."

            try:
                if prob[1] == "+":
                    answer = int(prob[0]) + int(prob[2])
                else:
                    answer = int(prob[0]) - int(prob[2])
            except:
                return "Error: Numbers must only contain digits."

            remLen1 = length - len(prob[0])
            remLen2 = length - len(prob[2]) - 1

            if sol:
                remLen4 = length - len(str(answer))

                fourthLine += (" " * remLen4) + str(answer)

            firstLine += (" " * remLen1) + prob[0]
            secondLine += prob[1] + (" " * remLen2) + prob[2]
            thirdLine += "-" * length

            if i != len(problems) - 1:
                firstLine += "    "
                secondLine += "    "
                thirdLine += "    "
                if sol:
                    fourthLine += "    "

        else:
            return "Error: Operator must be '+' or '-'."

    return firstLine + "\n" + secondLine + "\n" + thirdLine + ("\n" + fourthLine if sol else "")