
c_t=3 
m_t=3 

alegeri=[(1,0),(2,0),(0,1),(0,2),(1,1)]

def valid(m_st,c_st):

  if m_st < 0 or m_st > m_t or c_st < 0 or c_st > c_t :
    return False


  if m_st < c_st and m_st != 0:
    return False

  m_dr=m_t-m_st
  c_dr=c_t-c_st

  if m_dr!=0 and m_dr<c_dr:
    return False

  return True


def functioneaza(stare):
  return valid(stare[0],stare[1])


def succesor(stare):
  M=stare[0]
  C=stare[1]
  B=stare[2]

  pos=[] #urmatoarele alegeri posibile

  i = 0
  while i < len(alegeri) :

    m=alegeri[i][0]
    c=alegeri[i][1]

    if B == 0 :
      if M-m < 0 or C-c < 0 :
        i=i+1
        continue
      if M-m < C-c and M-m != 0 :
        i=i+1
        continue

      if functioneaza((M-m,C-c)):
        pos.append((M-m,C-c,1-B))

    else :
      x=m_t-M
      y=c_t-C

      if x - m< 0 or y-c < 0:
        i=i+1
        continue

      if x-m < y-c and x-m != 0 :
        i=i+1
        continue

      if functioneaza((M+m,C+c)) :
        pos.append((M+m,C+c,1-B))

    i=i+1

  return pos

def obiectiv(stare):
  if stare[0] == 0 and stare[1] == 0 and stare[2] == 1:
    return True

  return False

def afisare_frumoasa(stare) :
  m_st=stare[0]
  c_st=stare[1]
  b=stare[2]
  m_dr=3-m_st
  c_dr=3-c_st

  if b == 0 :
    return(f"🏝️{m_st}M_{c_st}C🏝️🛶≈≈≈≈≈≈≈≈🏝️{m_dr}M_{c_dr}C🏝️")
  else:
    return(f"🏝️{m_st}M_{c_st}C🏝️≈≈≈≈≈≈≈≈🛶🏝️{m_dr}M_{c_dr}C🏝️")


def h(stare) :
  M=stare[0]
  C=stare[1]
  T=M+C
  return (T+1)//2

#Cautare neinformata

def BFS(start):
  contor=0
  frontiera=[]
  vizitat=[]
  parinte={start:None}
  cost=0
  frontiera.append(start)

  while len(frontiera) > 0:
    n=frontiera.pop(0)
    contor=contor+1

    if obiectiv(n):

      drum=[]
      cost=0
      while n != None :
        cost=cost+1
        drum.append(n)
        n=parinte[n]
      drum.reverse()

      return drum, cost, contor

    vec=succesor(n)
    vizitat.append(n)

    for i in vec :
      if i in vizitat :
        continue
      else :
        vizitat.append(i)
        parinte[i]=n
        frontiera.append(i)

  return None, 0, contor


#Cautare informata

def A_stelat(start):
  frontiera=[]
  vizitate=[]
  parinte={start: None}
  g={start: 0}
  contor=0

  frontiera.append(start)

  while len(frontiera) !=0 :
    contor=contor+1
    best_indice=0
    best_stare=frontiera[0]
    best_f=g[best_stare]+h(best_stare)

    i=1

    while i < len(frontiera) :
      s=frontiera[i]
      f_s=g[s]+h(s)
      if f_s < best_f :
        best_f=f_s
        best_stare=frontiera[i]
        best_indice=i
      i=i+1

    u=frontiera.pop(best_indice)

    if obiectiv(u) :
      drum=[]
      x=u
      while x!= None :
        drum.append(x)
        x=parinte[x]

      drum.reverse()
      return drum,g[u], contor

    vizitate.append(u)

    vec=succesor(u)

    for v in vec :
      g_nou=g[u]+1
      if v not in g or g_nou < g[v]:
        g[v]=g_nou
        parinte[v]=u

      if v not in vizitate and v not in frontiera :
        frontiera.append(v)


  return None, 0, contor



start=(m_t,c_t,0)

drum1,cost1, contor1=BFS(start)
drum2, cost2, contor2=A_stelat(start)

print("Cautare neinformata:","\n")
for i in drum1 :
  print(i,":  ",afisare_frumoasa(i))

print("Numarul de noduri expandate de BFS:",contor1)
print("Costul lui BFS:",cost1-1)#cost1-1 reprezinta numarul de mutari, cost1 reprezinta numarul de stari

print("\n","\n","\n","Cautare informata:","\n")

for i in drum2 :
  print(i,":  ",afisare_frumoasa(i))

print("Numarul de noduri expandate de A*:", contor2)
print("Costul lui A*:",cost2)
