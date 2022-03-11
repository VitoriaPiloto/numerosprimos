continua='S'
while continua in ('S','s'):
  base = input('Insira a base: ')
  base=int(base)
  limite = input('Insira o limite: ')
  limite = int(limite)
  primos=[]
  i=base
  try:
    if (limite>100000) or (base>limite) or (base<10):
      print('Base', base, 'e limite', limite, ': ERRO' )
      continua='n'
    else:
      if (base==limite): 
        print('Base %d e Limite %d: VAZIO'%(base,limite))
        continua='n'
      else: 
        print('Base',base,'e Limite',limite,': ', end="")
        for i in range(base, limite+1):  
            for j in range(2,i): 
              if(i % j==0): 
                break
            else: 
              primos.append(i)
                
        for primos in primos : 
          primos_str = str(primos)
          print(primos_str, end=", ")
          i += 1
    
        continua=input('\nPara nova execução (S,s): ')
        
  except ValueError: 
    print('Base %d e Limite %d: ERRO'%(base,limite))
    continua='n'
  
  except TypeError:
    print('Base %d e Limite %d: ERRO'%(base,limite))
    continua='n'
