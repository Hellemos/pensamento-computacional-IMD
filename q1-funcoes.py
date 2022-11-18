from datetime import datetime, timedelta, time

def calcularonda(h, m, s):
    t1 = time(h, m, s)
    print(t1)
    #somar 1h ao tempo inicial
    h *= 60
    h += 60
    h = h // 60
    #t1 = time(h,m,s)
    #print(t1)
    r3 = timedelta(hours=h,minutes=m,seconds=s)
    r3 = datetime(h,m,s)
    print(r3.strftime("%H:%M:%S %Z"))
    
    
def calcularonda2(h,m,s):
    #somar 2h10m30s ao tempo inicial
    h *= 60
    h += 120
    h = h // 60
    m *= 60
    m += 600
    m = m // 60
    s += 30
    t1 = time(h,m,s)
    print(t1)

def calcularonda3(h,m,s):
    #somar 4h40m50s ao tempo inicial
    h *= 60
    h += 240
    h = h // 60
    m *= 60
    m += 2500
    m = m // 60
    s = (s + 50)-60
    t1 = time(h,m,s)
    print(t1)

def calcularonda4(h,m,s):
    #somar 12h05m5s ao tempo inicial
    h *= 60
    h += 720
    h = h // 60
    m *= 60
    m += 300
    m = m // 60
    s = (s + 5)
    t1 = time(h,m,s)
    print(t1)
      

hora = int(input())
minuto = int(input())
segundo = int(input())
calcularonda(hora,minuto,segundo)
calcularonda2(hora,minuto,segundo)
calcularonda3(hora,minuto,segundo)
calcularonda4(hora,minuto,segundo)
