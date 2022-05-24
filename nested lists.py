if __name__ == '__main__':
    names=[]
    scores=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)


    ar = list(set(sorted(scores)))
    ar = sorted(list(set(ar)))
    key =ar[1]
    final=[]
    for i in range(len(scores)):
        if scores[i]==key:
            final.append(names[i])
    final = sorted(final)
    for i in range(len(final)):
        print(final[i])
