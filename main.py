continua='S'
while continua in ('S','s'):
  base = input('Insira a base: ')
  base=int(base)
  limite = input('Insira o limite: ')
  limite = int(limite)
  primos=[]
  i=base
  
  if (limite>100000) or (base>limite) or (base<10):
    print('Base', base, 'e limite', limite, ': ERRO' )
  else:
    if (base==limite): 
      print('Base %d e Limite %d: VAZIO'%(base,limite))
    else:
      print('Base',base,'e Limite',limite,': ', end="")
      for i in range(base, limite+1): 
              if i>10: 
                for j in range(2,i): 
                    if(i % j==0): 
                        break
                else: 
                    primos.append(i) 
      for primos in primos : 
        primos_str = str(primos)
        print(primos_str, end=", ")
        i += 1;
      #except: 
            #print('Base %d e Limite %d: ERRO'%(base,limite))
      
  continua=input('\nPara nova execução (S,s): ')

