
def compareTriplets(alice,bob):
    
    score=[]
    alice_score=0
    bob_score=0
   
    try:
        #contains 3 integers and number of item is equal
        if (len(alice)!=len(bob) and len(alice)!=3):
            raise ValueError("challenge is the triplet!")
        
        for i in range(len(alice)):
           
            #Constraints
            if (0<alice[i]<101 and 0<bob[i]<101)==0:
                raise ValueError("The constraint will be 1<= alice[i] <=100 or 1<= bob[i] <=100")
                
            if alice[i]>bob[i]:
                alice_score+=1
                #print(alice_score)
            elif alice[i]<bob[i]:
                bob_score+=1
                #print(bob_score)
                
        #adds an item to the score list
        score.append(alice_score)
        score.append(bob_score)
        #print(score)
    
    except TypeError:
        print("Not a valid choice!")
        
    #Alice's score is in the first position, and Bob's score is in the second.
    return score


print(compareTriplets([71,28,30],[99,16,8]))
        
            
            
        
        
        
    
    
        
        
    
    
    
    
    
    
    

