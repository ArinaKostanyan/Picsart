# code

for_dict = {}
args = {}
with open("enun.l", "rt") as f:
    for line in f:
        lst = []
        lst = line.split()

        if len(lst) < 3:

            if "get" in line:
                var = lst[1]
                value = float(input("enter an item "))
                args[var] = value
                print(var, "is", value)

            if "print" in line:
                var = lst[1]
                args[var] = value
                print(var, "is", value)

        if len(lst) == 3:
            values = args.values()
            values_list = list(values)
            var1 = values_list[0]
            var2 = values_list[1]
            if "plus" in line:
                p = var1 + var2
                print(p)
            if 'sub' in line:
                p = var1 - var2
                print(p)
            if 'multiply' in line:
                p = var1 * var2
                print(p)
            if 'divide' in line:
                p = var1 // var2
                print(p)

        elif '(' and ')' in line:
            par1 = lst.index('(')
            par2 = lst.index(')')

            compex = lst[par1 + 1:par2]

            var1 = compex[0]
            var2 = compex[2]

            values = args.values()
            values_list = list(values)
            val1 = values_list[0]
            val2 = values_list[1]

            if "plus" == compex[1]:
                p = val1 + val2

            if 'sub' == compex[1]:
                p = val1 - val2

            if 'multiply' in line:
                p = val1 * val2

            if 'divide' in line:
                p = val1 / val2

            args.update({"pat": p})

            # for j in range(par1,par2+1):
            #   lst.pop(0)
            if par1 != 0:
                t = False
                var = lst[0]
                args[var] = value

            else:
                var = lst[6]
                # args[var] = value
                t = True

            value = args[var]

            if t == False:
                if "sub" == lst[1]:
                    p = value - p

                if "divide" == lst[1]:
                    p = value / p
            else:
                if "sub" == lst[5]:
                    p = p - value
                if "divide" == lst[5]:
                    p = p / value

            if "plus" in lst:
                p = p + value

            if 'multiply' in lst:
                p = p * value
            print(p)
        if lst[0] == 'if':
            if lst[2] == '>':
                if lst[1] > lst[3]:
                    print(True)
                else:
                    print(False)
            if lst[2] == '<':
                if lst[1] < lst[3]:
                    print(True)
                else:
                    print(False)
            if lst[2] == '==':
                if lst[1] == lst[3]:
                    print(True)
                else:
                    print(False)
            if lst[2] == '>=':
                if lst[1] >= lst[3]:
                    print(True)
                else:
                    print(False)
            if lst[2] == '<=':
                if lst[1] <= lst[3]:
                    print(True)
                else:
                    print(False)

        if lst[0] == "for" and lst[1] == "i":

            for i in range(2, 7, 2):

                if lst[i].isalpha():
                    for_dict[lst[i]] = args[lst[i]]
                else:
                    for_dict[lst[i]] = int(lst[i])
            values_ = for_dict.values()
            for_lst = list(values_)

            a = int(for_lst[0])
            b = int(for_lst[1])
            c = int(for_lst[2])

        if lst[0] == "for:":
            for i in range(a, b, c):
                if lst[1] == "print":
                    if lst[2] in args:
                        print(args[lst[2]])
                    elif lst[2] == "i":
                        print(i)

