def breakingRecords(scores):
    # Write your code here
    maxi=scores[0]
    mini=scores[0]
    maxcount =0
    mincount=0
    for i in range(len(scores)):
        if(scores[i]>maxi):
            maxi = scores[i]
            maxcount+=1
        if(scores[i]<mini):
            mini = scores[i]
            mincount+=1
    return [maxcount, mincount]