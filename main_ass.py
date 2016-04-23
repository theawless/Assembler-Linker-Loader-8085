def main_ass(filenames):
    for filename in filenames:
        input_file = open(filename, "r")
        output_filename = "output" + filename
        output_file = open(output_filename, "w+")
        code = input_file.read()
        lines = code.split('\n')
        for line in lines:
            n = line.count(',')
            if "min" in line:
                numbers = line.split(',')
                numbers[-1] = numbers[-1][:-1]
                numbers[0] = numbers[0][4:]
                output_file.write("var r=" + numbers[0] + "\n" + "loop " + str(n) + "\n")
                for num in numbers:
                    output_file.write("if " + num + "<r" + "\n" + "r=" + num + "\n" + "endif" + "\n")
                    
                output_file.write("endloop" + "\n")
            elif "max" in line:
                numbers = line.split(',')
                numbers[-1] = numbers[-1][:-1]
                numbers[0] = numbers[0][4:]
                output_file.write("var r=" + numbers[0] + "\n" + "loop " + str(n) + "\n")
                for num in numbers:
                    output_file.write("if " + num + ">r" + "\n" + "r=" + num + "\n" + "endif" + "\n")

                output_file.write("endloop" + "\n")
            elif "add" in line:
                numbers = line.split(',')
                numbers[-1] = numbers[-1][:-1]
                numbers[0] = numbers[0][4:]
                output_file.write("var r=0" + "\n" + "loop " + n + "\n")
                for num in numbers:
                    output_file.write("r=r+" + num)
                output_file.write("endloop" + "\n")
            elif "multiply" in line:
                numbers = line.split(',')
                numbers[-1] = numbers[-1][:-1]
                numbers[0] = numbers[0][4:]
                output_file.write("var r=0" + "\n")
                for i in range(1, int(numbers[1])):
                    output_file.write("r=r+" + numbers[0] + "\n")
                output_file.write("endloop" + "\n")
        output_file.close()


main_ass({"mys.x"})
