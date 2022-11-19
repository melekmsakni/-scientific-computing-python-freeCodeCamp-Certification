def arithmetic_arranger(problems,calc=False):
  
    if (len(problems)>5):
        return "Error: Too many problems."
    r=[]
  #initilizing the lines and treating the cases
    line1=""
    line2=""
    line3=""
    line4=""
    for i in problems:
        l=i.split()
        if (not(l[0].isdigit()) or not(l[2].isdigit()) ):
          return "Error: Numbers must only contain digits."
        if (l[1] not in ['+','-']):
          return "Error: Operator must be '+' or '-'."
        if (len(l[0])>4 or len(l[2])>4 ):
          return "Error: Numbers cannot be more than four digits.";
          #calculate numbers and put the result in a list 
        if(l[1]=='+'):
          r.append(str(int(l[0])+int(l[2])))
        else:
          r.append(str(int(l[0])-int(l[2])))
        dif=abs(len(l[0])-len(l[2]))
        a=len(l[0])
        b=len(l[2])
        toRight=0
        #printing the first line of the operation so we must 
        #figure out wish is the bigger digit so that we can allign them correctly 
        if (a-dif<b-dif):
          toRight=dif
        if (problems.index(i)==len(problems)-1):
            
            line1=line1+" "*2 +toRight*" "+l[0]+"\n"
        else:
        
            line1=line1+" "*2 +toRight*" "+l[0]+" "*4

          #creating the second line 
    for i in problems:
        l=i.split()
        dif=abs(len(l[0])-len(l[2]))
        a=len(l[0])
        b=len(l[2])
        toRight=0
        if (a-dif>b-dif):
          toRight=dif
        if (problems.index(i)==len(problems)-1):
            line2=line2+l[1]+" " +toRight*" "+l[2]+"\n"
        else:
            line2=line2+l[1]+" " +toRight*" "+l[2]+" "*4
    uo=[]
  #creating the third line whish is the "*"
    for i in problems:
        l=i.split()
        p=max(len(l[0]),len(l[2]))
        if (problems.index(i)==len(problems)-1):
            line3=line3+(2+p)*"-"
        else:
            line3=line3+ (2+p)*"-"+" "*4
        uo.append(2+p)
      #printing results in case the value calc is True
    if(calc==True):
        line3=line3+"\n"
    
        for i in range(len(problems)):
            s=uo[i]-len(r[i])
            if (i== len(problems)-1):
                line4=line4+ s*" "+r[i]
            else:
                line4=line4+ s*" "+r[i]+" "*4
                
        arranged_problems=line1+line2+line3+line4
    else:
        arranged_problems=line1+line2+line3
   
    return arranged_problems
  