def Calculator(str):
    for char in str:
        # Para arreglar: con otra funcion dentro, recorrer el string, si hay ( o + o - o * o / devolver True, sino devolver False, y si esta funcion devuelve False, que Calculator(str) devuelva str
        if char == '+':
            splitted = str.split("+")
            return Calculator(splitted[0]) + Calculator(splitted[1])
        if char == '-':
            splitted = str.split("-")
            return Calculator(splitted[0]) - Calculator(splitted[1])
        if char == '(':
            for char in str[str.find(char) : len(char) - 1 : 1] :
                tmp = 0
                if char == '(':
                    tmp += 1
            substrStart = str.find(char)
            for char in str[str.find(char) : len(char) - 1 : 1] :
                count = 0 
                if char == ')':
                    count += 1
                    if count == tmp:
                        substrEnd = str.find(char)
                        return str[substrStart:substrEnd]                        
            # Algoritmo acá: fijarse cuantos "(" hay hasta que se termina el string, guardar ese numero "n" y cortar el string al n-esimo "(" que aparezca, retornar Calculator(strNueva) siendo strNueva el pedazo recien cortado
        if char == '*':
            splitted = str.split("*")
            return Calculator(splitted[0]) * Calculator(splitted[1])
        if char == '/':
            splitted = str.split("/")
            return Calculator(splitted[0]) / Calculator(splitted[1])
        else:
            return str
