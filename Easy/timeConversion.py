def timeConversion(hr,min,sec,type):
    if type=="MP":
        if hr=="12":
            pass
        else:
            hr=str(int(hr)+12)
    else:
        if hr=="12":
            hr="00"
    return(hr+":"+min+":"+sec)    

date_12=input()
hr=date_12[:2]
min=date_12[3:5]
sec=date_12[6:8]
type=date_12[-1:-3:-1]
print(timeConversion(hr,min,sec,type))
