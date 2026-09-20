def main():
    while True:
        date = input("Date: ")
        try:
            if "/" in date:
                m, d, y = date.split("/")
                m, d, y = int(m), int(d), int(y)

                if 0 < m <= 12 and 0 <= d <= 31: # Verificar se está entre os 31 dias e os 12 meses
                    date = outdated(y,m,d)

                    if date != None: # Se a data atualizada não for none
                        print(date)
                        break

            elif ", " in date: #
                m, d, y = date.split(" ")
                d = d.replace(",", "")
                d, y = int(d), int(y)

                if 0 <= d <= 31 and m.isalpha(): # Verificar se está dentro dos 31 dias e se o mes é uma string
                    date = outdated(y,m,d)

                    if date != None: # Se a data atualizada não for none
                        print(date)
                        break
        except:
            pass

def outdated(year, month, day):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    if month in months:
        month = months.index(month) + 1 # Contar em que posição está o month na lista months e somar mais 1 porque a contagem começa no zero
        return f"{year}-{month:02}-{day:02}" # return data atualizada
    else:
        return f"{year}-{month:02}-{day:02}" # return data atualizada

main()