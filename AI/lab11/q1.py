districts = [
    "kachchh", "banaskantha", "patan", "mehsana", "sabarkantha",
    "gandhinagar", "ahmedabad", "surendranagar", "rajkot", "jamnagar",
    "porbandar", "junagadh", "amreli", "bhavnagar", "anand",
    "kheda", "panchmahal", "dahod", "vadodara", "bharuch",
    "narmada", "surat", "navsari", "valsad", "dangs"
]
n = len(districts)
adj_matrix = [[0]*n for _ in range(n)]

def connect(a, b):
    i = districts.index(a)
    j = districts.index(b)
    adj_matrix[i][j] = 1
    adj_matrix[j][i] = 1

#kachchh borders
connect("kachchh", "banaskantha")
connect("kachchh", "patan")
connect("kachchh", "surendranagar")
connect("kachchh", "jamnagar")

#banaskantha borders
connect("banaskantha", "patan")
connect("banaskantha", "mehsana")
connect("banaskantha", "sabarkantha")

#patan borders
connect("patan", "mehsana")
connect("patan", "surendranagar")

#mehsana borders
connect("mehsana", "sabarkantha")
connect("mehsana", "gandhinagar")
connect("mehsana", "ahmedabad")
connect("mehsana", "surendranagar")

#sabarkantha borders
connect("sabarkantha", "gandhinagar")
connect("sabarkantha", "ahmedabad")
connect("sabarkantha", "kheda")
connect("sabarkantha", "anand")
connect("sabarkantha", "panchmahal")

#gandhinagar
connect("gandhinagar", "ahmedabad")

#ahmedabad borders
connect("ahmedabad", "surendranagar")
connect("ahmedabad", "kheda")
connect("ahmedabad", "anand")

#surendranagar borders
connect("surendranagar", "rajkot")
connect("surendranagar", "bhavnagar")
connect("surendranagar", "amreli")

#rajkot borders
connect("rajkot", "jamnagar")
connect("rajkot", "porbandar")
connect("rajkot", "junagadh")
connect("rajkot", "amreli")

#jamnagar borders
connect("jamnagar", "porbandar")

#porbandar borders
connect("porbandar", "junagadh")

#junagadh borders
connect("junagadh", "amreli")

#amreli borders
connect("amreli", "bhavnagar")

#bhavnagar borders
connect("bhavnagar", "anand")
connect("bhavnagar", "bharuch")

#anand borders
connect("anand", "kheda")
connect("anand", "vadodara")
connect("anand", "bharuch")

#kheda borders
connect("kheda", "vadodara")
connect("kheda", "panchmahal")

#panchmahal borders
connect("panchmahal", "vadodara")
connect("panchmahal", "dahod")

#dahod borders
connect("dahod", "vadodara")

#vadodara borders
connect("vadodara", "bharuch")
connect("vadodara", "narmada")

#bharuch borders
connect("bharuch", "narmada")
connect("bharuch", "surat")

#narmada borders
connect("narmada", "surat")
connect("narmada", "dangs")

#surat borders
connect("surat", "navsari")
connect("surat", "dangs")

#navsari borders
connect("navsari", "valsad")
connect("navsari", "dangs")

#valsad borders
connect("valsad", "dangs")


def safe(v, c, col):
    for i in range(n):
        if adj_matrix[v][i] == 1 and col[i] == c:
            return False
    return True

def backtrack(v, m, col):
    if v == n:
        return True
    for c in range(1, m+1):
        if safe(v, c, col):
            col[v] = c
            if backtrack(v+1, m, col):
                return True
            col[v] = 0
    return False

def min_colors():
    for m in range(1, 5):
        col = [0]*n
        if backtrack(0, m, col):
            return m, col
    return None, None

m, res = min_colors()
if res:
    names = ["", "red", "green", "blue", "yellow"]
    print("minimum colors =", m)
    for i in range(n):
        print(districts[i], "->", names[res[i]])
else:
    print("no solution")