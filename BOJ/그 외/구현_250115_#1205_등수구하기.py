def rank_scores(N,new_score,P,scores):
    if N==P and scores[-1]>=new_score:
        return -1
    position=0

    while position<N and scores[position]>new_score:
        position+=1
    if N<P or new_score > scores[-1]:
        rank=position+1
        return rank
    
    return -1


N,new_score,P=map(int,input().split())
if N>0:
    scores=list(map(int,input().split()))
else:
    scores=[]


result = rank_scores(N,new_score,P,scores)
print(result)