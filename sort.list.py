


#exercice : trier la liste des valeurs entre 0 et 100 par ordre croissant ou décroissant

#paramètres de la fonction : lista et ordem

#ordem=1 signifie décroissant

#ordem!=1 signifie croissant

#########################################################

lista=[31,32,21,33,34,1,90,5,7,9,0,89,34.1,32,91,100]


#debut

def sort(lista,ordem=1):

    a=0

    lista_local=lista.copy()        #on copie la liste à l'intérieur de la fonction 

    lista_final=[]                  #  liste vide


    if ordem ==1:                  #  ordre décroissante

        #loop variable a, debut

        while a<len(lista_local):  # on fixe le premier terme de la local_list
            
            #loop variable b, debut
            # 
            # cette boucle calcule le maximum de la local_list ainsi que sa position

            b=0

            posicao_max=0

            max=0

            while b < len(lista_local):

                if lista_local[b]>max:

                    max=lista_local[b]

                    posicao_max=b

                b=b+1

            #fin loop b

            lista_final.append(max)      # colocamos este maximo em lista_final

            lista_local[posicao_max]=0   # trocamos o valor maximo por 0 em lista_local   
            
            a=a+1                        # e voltamos a calcular o proximo maximo da lista_local

        #fim do loop em a  

        #quando o contador 'a' percorrer toda a lista,ela estara organizada em ordem decrescente.

    else:#ordem crescente

        while a<len(lista_local):#fixamos o  primeiro termo da lista_local.

            #inicio do loop em b.este loop calcula o minimo da lista_local assim como sua posicao
            
            b=0

            posicao_min=0

            min=100

            while b<len(lista_local):

                if lista_local[b]<min:

                    min=lista_local[b]

                    posicao_min=b

                b=b+1

            #fim do loop em b

            lista_final.append(min)         #  colocamos este mainimo em lista_final

            lista_local[posicao_min]=100    #  trocamos o valor minimo por 100 em lista_local   
            
            a=a+1                           #  e voltamos a calcular o proximo minimo da lista_local
          
        #quando o contador 'a' percorrer toda a lista,ela estara organizada em ordem crescente.

    return lista_final 

print(sort(lista,2))  #imprimir a lista organizada de acordo com e escolha do parametro ordem 

#fim da funcao
 
    
         
        

      





