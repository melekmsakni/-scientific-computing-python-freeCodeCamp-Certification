class Category:
    def __init__(self,BudgetCategory):
        
        self.ledger=[]
        self.BudgetCategory=BudgetCategory
        self.balance=0
    
    def __str__(self):
        
        
        stars=int((30-len(self.BudgetCategory))/2)*'*'
        title=stars+self.BudgetCategory.capitalize()+stars+'\n'
        line=""
        for i in self.ledger:
          
            amount=str(format(i["amount"], '.6f'))[:6]
            desc=i["description"][:23]
            space =30-(len(desc)+len(amount))
            line=line+desc+" "*space+amount+"\n"
        
        total="Total: "+str(self.balance)
            
        all=title+line+total
        
        
        return all
    
    
    
    
    
    def deposit(self,amount,description=""):
        newDeposit={"amount": amount, "description": description}
        self.ledger.append(newDeposit)
        self.balance=self.balance+amount
        
    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            newWidthraw={"amount": -amount, "description": description}
            self.ledger.append(newWidthraw)
            self.balance=self.balance-amount
            
            return True
        else:
            return False
            
            
            
    def get_balance(self):
        return self.balance
    
    
    def transfer(self,amount,receiver):
        if self.check_funds(amount):
            ch="Transfer to "+receiver.BudgetCategory
            self.withdraw(amount,ch)
            
            ch="Transfer from "+self.BudgetCategory
            receiver.deposit(amount,ch)
            
            return True
        else:
            return False
        
    
    
    def check_funds(self,amount):
        if amount<=self.balance:
            return True
        else:
            return False
        





def create_spend_chart(categories):
    l=[]
    moyenne=0
    for i in categories:
        sommeLedger=0
        for g in i.ledger:
            if(g['amount']<0):
                sommeLedger=sommeLedger+g['amount']
        l.append(sommeLedger)
        moyenne=sommeLedger+moyenne
    moyenne=-moyenne
    
    for i in l:
       l[l.index(i)] =int((-i/moyenne)*100)
        
    
    line="Percentage spent by category\n"
    chart=""
    for value in reversed(range(0, 101, 10)):
        chart =chart+ str(value).rjust(3) + '|'
        for percent in l:
            if percent >= value:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"
        
    line=line+chart
    bar=4*" "+"-"*((len(l)*2)+len(l)+1)
    line=line+bar+'\n'
    
    t=[]
    for i in categories:
        
        t.append(i.BudgetCategory.capitalize())
        
    
    
    g=[]
    for i in t :
        g.append(len(i))
    
    maxim=max(g)
    
    b=""
    for i in range(maxim):
        b=b+" "*5
        for a in t:
            if(i<=len(a)-1  ):
                
                if t.index(a)==len(t)-1:
                    
                    
                    b=b+a[i]
                else:
                    
                    
                    b=b+a[i]+"  "
            else:
                b=b+" "+"  "
            
        
        if (i==maxim-1):
          b=b+"  "
        else:
          b=b+"  "+'\n'
          
          
                    
        
      
      
    line=line+b
    return line
    
            
        
        
        

    

        
    
    
    
    
    
