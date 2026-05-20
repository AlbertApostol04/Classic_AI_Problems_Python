def functioneaza(m,n,stare):
  if m >= len(stare) or n >= len(stare) :
    return False
  if m < 0 or n < 0 :
    return False

  return True

def succesor(stare):
  pos=[]
  lin=0
  col=0

  for i in range(len(stare)):
    for j in range(len(stare)):
      if stare[i][j] == 0:
        lin=i
        col=j


  if(functioneaza(lin-1,col,stare)) :
    pos.append((lin-1,col,stare))

  if(functioneaza(lin+1,col,stare)) :
    pos.append((lin+1,col,stare))

  if(functioneaza(lin,col+1,stare)) :
    pos.append((lin,col+1,stare))

  if(functioneaza(lin,col-1,stare)) :
    pos.append((lin,col-1,stare))

  vec=[]
  orig=[r[:] for r in stare]
  for i in pos :
    orig[i[0]][i[1]], orig[lin][col]=orig[lin][col], orig[i[0]][i[1]]
    vec.append(orig)
    orig=[r[:] for r in stare]


  return vec

def obiectiv(stare) :
  if stare == [[1,2,3],[4,5,6],[7,8,0]]:
    return True

  return False

def tuplificare(stare):

  return tuple((tuple(r) for r in stare))

def detuplificare(stare):
  return [list(r) for r in stare]

def BFS(start):

  frontiera=[]
  frontiera.append(start)
  vizitate=[]
  contor=0
  start_tuplu=tuplificare(start)

  parinte={start_tuplu: None}

  while 0 < len(frontiera) :
    contor=contor+1

    u=frontiera.pop(0)

    if obiectiv(u) :
      drum=[]
      u_tuplu=tuplificare(u)
      x=u_tuplu
      cost=0
      while( x != None ) :
        cost=cost+1
        drum.append(detuplificare(x))
        x=parinte[x]

      drum.reverse()
      return drum, cost, contor

    vizitate.append(u)

    for i in succesor(u) :
      if i not in frontiera and i not in vizitate :
        frontiera.append(i)
        u_tuplu=tuplificare(u)
        i_tuplu=tuplificare(i)
        parinte[i_tuplu]=u_tuplu

  return None, 0, contor


def h(stare) :
  gresite=0
  obiectiv=[[1,2,3],[4,5,6],[7,8,0]]
  for i in range(len(stare)):
    for j in range(len(stare)):
      if stare[i][j] != 0 and stare[i][j] != obiectiv[i][j] :
        gresite=gresite+1

  return gresite


def A_stea(start):

  frontiera=[]
  frontiera.append(start)
  vizitate=[]
  start_tuplu=tuplificare(start)
  contor=0

  g={start_tuplu: 0 }
  parinte={start_tuplu: None }

  while 0 <  len(frontiera) :
    contor=contor+1
    indice_fav=0
    stare_fav=frontiera[0]
    stare_fav_tuplu=tuplificare(stare_fav)
    f_fav=g[stare_fav_tuplu]+h(stare_fav)

    i=1

    while i < len(frontiera) :
      x=frontiera[i]
      x_tuplu=tuplificare(x)
      f_x=g[x_tuplu] + h(x)

      if f_x < f_fav :
        f_fav=f_x
        stare_fav=frontiera[i]
        indice_fav=i
      i=i+1

    u=frontiera.pop(indice_fav)

    if obiectiv(u) :
      drum=[]
      u_tuplu=tuplificare(u)
      x=u_tuplu


      while x != None :
        drum.append(detuplificare(x))
        x=parinte[x]
      drum.reverse()
      return drum, g[u_tuplu], contor

    vizitate.append(u)

    for i in succesor(u) :
      i_tuplu=tuplificare(i)
      u_tuplu1=tuplificare(u)
      g_nou=g[u_tuplu1]+1
      if i_tuplu not in g or g_nou < g[i_tuplu]:
        g[i_tuplu]=g_nou
        parinte[i_tuplu]=u_tuplu1

        if i not in vizitate and i not in frontiera :
          frontiera.append(i)


  return None, 0, contor

start=[[1,0,3],
       [5,2,6],
       [4,7,8]]

drum1, cost1, contor1 = A_stea(start)
drum2, cost2, contor2 = BFS(start)



print("Cautare A*:")
for i in drum1 :
  for j in i :
    print(j)
  print("_____")
print("Costul folosind A*:",cost1)
print("Numarul de note expandate folsind A*:",contor1)

print("\n","***********","\n")



print("Cautare BFS:")
for i in drum2 :
  for j in i :
    print(j)
  print("_____")

print("Costul folosind BFS",cost2)
print("Numarul de noduri expandate prin BFS:", contor2)
