import math



Player = 'X'
AI ='0'

def stare_initiala():
  return [' ']*9

def afisare_frumoasa(stare) :
  print("\n   C1  C2 C3")
  print(f"L1  {stare[0]} | {stare[1]} | {stare[2]}")
  print("   ---+---+---")
  print(f"L2  {stare[3]} | {stare[4]} | {stare[5]}")
  print("   ---+---+---")
  print(f"L3  {stare[6]} | {stare[7]} | {stare[8]}")
  print("\n")

def verificare(stare) :
  combinatii=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

  for comb in combinatii :
    x1 = comb[0]
    x2= comb[1]
    x3 = comb[2]

    if stare[x1] == stare[x3] == stare[x2] and stare[x1] != ' ' :
      return stare[x1]

  if ' ' not in stare :
    return 'Remiza'

  return False

def succesori(stare, player) :
  pos= []
  for i in range(9) :
    if stare[i] == ' ':
      stare_n= stare[:]
      stare_n[i] =  player
      pos.append(stare_n)

  return pos

def evaluare(stare) :
  rezultat = verificare(stare)
  if rezultat==AI:
    return 10
  elif rezultat == Player :
    return -10
  else :
    return 0

def max_val(stare, costuri, alfa, beta):
  rezultat = verificare(stare)


  if rezultat:
      return evaluare(stare)

  stare_t=tuple(stare)
  if stare_t in costuri :
      return costuri[stare_t]

  v=-math.inf
  for succesor in succesori(stare, AI) :
    v=max(v,min_val(succesor,costuri,alfa,beta))
    if v >= beta:
      return v
    alfa=max(alfa,v)


  costuri[stare_t]=v
  return v


def min_val(stare, costuri, alfa, beta):

  rezultat = verificare(stare)

  if rezultat :
    return evaluare(stare)


  stare_t=tuple(stare)
  if stare_t in costuri:
    return costuri[stare_t]

  v=math.inf

  for succesor in succesori(stare, Player) :
    v=min(v,max_val(succesor,costuri,alfa,beta))
    if v <=alfa:
      return v

    beta=min(beta,v)

  costuri[stare_t]=v
  return v

def best_miscare(stare, costuri) :
  best_val = -math.inf
  best_miscare= None
  mutari_pos=[]
  for i in range(9):
    if stare[i] == ' ':
      stare_copie = stare[:]
      stare_copie[i] = AI
      mutari_pos.append(stare_copie)

  for mutare in mutari_pos:
    val = min_val(mutare, costuri,-math.inf, math.inf)
    if val > best_val:
      best_val=val
      best_miscare = mutare


  return best_miscare


def joaca_jocul():
  stare_actuala= stare_initiala()
  costuri={}

  print("Jocul X si 0")
  print("Introdu coordonatele sub forma urmatoare : lini coloana(De exemplu: 1 1)")
  afisare_frumoasa(stare_actuala)

  while True:

    while True :
      intrare = input(f"Mutarea ta (linie coloana):")

      parti=intrare.split()

      if len(parti) !=2 :
        print("Formatul este gresit! Introdu doua numere cu spatiu intre ele")
        continue

      if not parti[0].isdigit() or not parti[1].isdigit():
                print("Eroare: Trebuie sa introduci numere intregi pozitive!")
                continue

      linie = int(parti[0])
      coloana = int(parti[1])

      if not (1 <= linie<= 3 and 1 <= coloana<=3):
        print("Coordonatele trebuie sa fie intre 1 si 3!")
        continue

      x=(linie-1)*3+(coloana-1)

      if stare_actuala[x]== ' ':
        stare_actuala[x] = Player
        break
      else:
        print("Pozitie ocupata!Incearca din nou")

    afisare_frumoasa(stare_actuala)

    rezultat= verificare(stare_actuala)

    if rezultat:
      print(f"Joc terminat! Castigator :{rezultat}")
      break

    print("AI-ul se gandeste...")

    stare_noua=best_miscare(stare_actuala, costuri)
    if stare_noua :
      stare_actuala = stare_noua

    else:
      print("Eroare:Ai-ul nu a gasit mutari!")
      break

    afisare_frumoasa(stare_actuala)

    rezultat =verificare(stare_actuala)

    if rezultat:
      print(f"Joc terminat!Castigator:{rezultat}")
      break

joaca_jocul()
