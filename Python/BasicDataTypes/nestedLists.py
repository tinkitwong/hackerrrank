from operator import itemgetter
if __name__ == '__main__':
    records = [['Harsh', 20], ['Beria', 20], ['Varun', 19], ['Kakunami', 19], ['Vikas', 21]]
    records.sort(key=itemgetter(1))
    print(records)
    
    
    records.sort(key=itemgetter(1))
    secondLowestScore = records[0][1]
    for record in records:
        if record[1] > secondLowestScore: 
            secondLowestScore = record[1]
            break
    secondLasts = [inner for inner in records if inner[1] == secondLowestScore]
    if len(secondLasts) > 1:
        secondLasts.sort(key=itemgetter(0))
    
    
    for record in secondLasts:
        print(record[0])