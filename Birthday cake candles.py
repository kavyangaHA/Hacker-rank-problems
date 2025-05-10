def birthdayCakeCandles(candles):
    a=candles[0]
    total=0
    for x in range(len(candles)):
        if a<candles[x]:
            a=candles[x]
    for x in candles:
        if a==x:
            total=total+1
    return(total)
