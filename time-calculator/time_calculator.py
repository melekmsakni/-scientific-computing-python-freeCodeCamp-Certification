     
def add_time(start,duration,dy=""):
  #extractiong data and preparing it 
    l=start.split(":")
    h1=int(l[0])
    zone=l[1].split()[1]
    min1=int(l[1].split()[0])
    
    l=duration.split(":")
    h2=int(l[0])
    min2=int(l[1])
    
    
    #calculating the global hours and all the minutes
    hourS=h1+h2
    minS=min1+min2
    addedHours=0
    minutes=0
    if(minS>59):
        addedHours=int(minS/60)
        minutes=int(minS % 60)
        minS=minutes
    hourS=hourS+addedHours
    
    days=0
  #getting number of days
    if hourS>=24:
        days=hourS/24
      #this conversion is done so that if it is float number 
      #it returns the ceil of this number
        days=days*10
        days=int(days)
        days=days/10
        if (days>float(int(days))):
            days=int(float(int(days)))+1
            days=int(days)
        
    n=0
  #formating the hours to 12-hours format
    while(hourS>12):
        hourS=hourS-12
        n=n+1
    zone1=zone
    if(n%2 != 0):
        if(zone=="PM"):
            zone="AM"
        else:
            zone="PM"
    #treating the particular case of the hour being 12:00
    if (hourS==12):
        if(zone=="PM"):
            zone="AM"
        else:
            zone="PM"
    #other particual case (transition between today and tommorow)
    if(n==1 and zone1=="PM" and zone=="AM"):
        days=1


  #finding the correspanding day depanding on the giving day
    s=0
    week=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day=dy
    if day!="":
        countDays=days%7
        #finding the day by geeting the rest of the division by 7 than counting from this day to the countDays
        for i in week:
            
            if i==day.lower():
                index=week.index(i)
                
                s=index
                while(countDays>0):
                    
                    if(s==len(week)-1):
                        s=0
                    else:
                        s=s+1
                    countDays=countDays-1
                break
    day=week[s].capitalize()
 
    #formating to print the string and return ir correctly 
    if minS <10:
        minS="0"+str(minS)
    else:
        minS=str(minS)
        
    
    time=str(hourS)+":"+minS+" "+zone
    
    if days==1.0:
        ch=" (next day)"
    elif days==0:
        ch=""
    else:
        ch=" ("+str(days)+" days later)"
    ch1=""
    if(dy!=""):
        ch1=", "+str(day)
    new_time=time+ch1+ch

  
    return new_time

    
   

                    
        
    


