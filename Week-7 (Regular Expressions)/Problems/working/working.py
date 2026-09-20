import re

def main():
  print(convert(input("Hours: ")))

def convert(time):
    timetable = {
        "h12": {
            12: 0
        },
        "h24": {
            1: 13,
            2: 14,
            3: 15,
            4: 16,
            5: 17,
            6: 18,
            7: 19,
            8: 20,
            9: 21,
            10: 22,
            11: 23
        }
    }
    try:
        sh = "([1-9]|1[0-2])"
        sm = "([0-5][0-9])"
        t = re.search("^({})((:)({}))? (AM to ({})((:)({}))? PM|PM to ({})((:)({}))? AM)$".format(sh, sm, sh, sm, sh, sm), time)
        # ↓↓↓
        if t.group(8) != None:
            if t.group(12) != None:
                a, p = int(t.group(1)), int(t.group(8))
                amh = timetable["h12"].get(a, a)
                pmh = timetable["h24"].get(p, p)
                amm = t.group(5)
                pmm = t.group(12)
                return f"{amh:02}:{amm} to {pmh:02}:{pmm}"

            else:
                a, p = int(t.group(1)), int(t.group(8))
                amh = timetable["h12"].get(a, a)
                pmh = timetable["h24"].get(p, p)
                return f"{amh:02}:00 to {pmh:02}:00"

        else:
            if t.group(18) != None:
                a, p = int(t.group(14)), int(t.group(1))
                amh = timetable["h12"].get(a, a)
                pmh = timetable["h24"].get(p, p)
                pmm = t.group(5)
                amm = t.group(18)
                return f"{pmh:02}:{pmm} to {amh:02}:{amm}"
            else:
                a, p = int(t.group(14)), int(t.group(1))
                amh = timetable["h12"].get(a, a)
                pmh = timetable["h24"].get(p, p)
                return f"{pmh:02}:00 to {amh:02}:00"

    except:
        raise ValueError

if __name__ == "__main__":
    main()

'''
AM to PM without (:00)
AM = 1 or 2
PM = 8 or 9

AM to PM with (:00)
AM = 1 or 2 : 5 or 6
PM = 8 or 9 : 12 or 13

PM to AM without (:00)
AM = 1 or 2
PM = 14 or 15

PM to AM with (:00)
AM = 1 or 2 : 5 or 6
PM = 14 or 15 : 18 or 19
'''