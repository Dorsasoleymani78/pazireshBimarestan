#Dorsa soleymani
from abc import ABC,abstractclassmethod
import random
import datetime
class person(ABC):
    def __init__(self,name,family,phoneNumber) -> None:
        self.__name=name
        self.__family=family
        self.__phoneNumber=phoneNumber

    @abstractclassmethod
    def showInfo():
        pass
#--------------------------------------------------------
class doctor(person):
    def __init__(self,__name, __family, __phoneNumber,CodeDoctor,speciality ) -> None:
        super().__init__(__name, __family, __phoneNumber)
        self.CodeDoctor=self.newDoctorCode()
        self.speciality=speciality
        self.saatstart=datetime.datetime.now()
        self.saatend=datetime.datetime.now()
        self.mizanesaatworkeed=self.calcuteSaatWorked()
    
    def newDoctorCode(self):
        return random.randint(1,3000)
    
    def calcuteSaatWorked(self):
        return (self.saatend - self.saatend)
    
    def mohasebedaramad(self):
        return (self.mizanesaatworkeed*500000)

    def showInfo(self):
        print(f"name is{self.name}\tfamily is {self.family}\tphone number is {self.phoneNumber}\tkode dopctor is {self.kodeDoctor}\tspeciality is {self.speciality}")
#---------------------------------------------------------------------------------------------
class employ(person):
    def __init__(self,__name, __family, __phoneNumber ) -> None:
        super().__init__(__name, __family, __phoneNumber)
        self.Codeemploy=self.newemplyCode()
    
    def newemplyCode(self):
        return random.randint(1,3000)
    
    def showInfo(self):
        print(f"name is{self.name}\tfamily is {self.family}\tphone number is {self.phoneNumber}\t Codeemploy is{self.Codeemploy}")
#------------------------------------------------------------------------------------------
class sick(person):
    def __init__(self, __name, __family, __phoneNumber,tarikhTavalod,noeBime,tedadShabha):
        super().__init__(__name, __family, __phoneNumber)
        self.Codesick=self.newSickCode()
        self.tarilhTavalod=tarikhTavalod
        self.noeBime=noeBime
        self.tedadShabha=tedadShabha
    
    def newSickCode(self):
        return random.randint(1,3000)
    
    def showInfo(self):
        print(f"name is{self.name}\tfamily is {self.family}\tphone number is {self.phoneNumber}\t tarikh tavalod{self.tarilhTavalod}noeBime is{self.noeBime}")
#----------------------------------------------------------------------------------------
class bakhsh:
    def __init__(self,Codebakhsh,onvan,zarfiyat) :
        self.Codebakhsh=Codebakhsh
        self.onvan=onvan
        self.zarfiyat=zarfiyat
    
     
    
    def showEmptyBed(self,takht):
         
        print(f"tedad takht khali{takht}")
         
#-------------------------------------------------------------------------------------
class takht:
    def __init__(self,shomareTakht, emkanat):
        self.shomareTakht=shomareTakht
        self.emkanat=emkanat
        self.ListTakht=[]
        self.ListTakhthayeKhali=[]
        self.teadtakhtKhali=0
        self.ListTakhtpor=[]
        self.tedadTakh=0
        self.tedadTakhPor=0
        self.teadShabhayePorbodanTakht=0
        self.geymat=2000
 
    def AddListTakht(self):
        self.ListTakht.append(self.shomareTakht)   
        self.tedadTakh+=1    

    def showListtakht(self):
        list1=[ j for j in self.ListTakht]
        print("list takht ha is",list1)  

    def khalikardanTakht(self,j):
        self.ListTakhtpor.remove(j)
        self.tedadTakhPor-=1
        self.ListTakhthayeKhali.append(j)
        self.teadtakhtKhali+=1

    def TakhthayePor(self,i):
          self.ListTakhtpor.append(i)
          self.tedadTakhPor+=1

    def showListTakhthayePor(self):
        list1=[j for j in self.ListTakhtpor]
        print("list takhthaye por is",list1)

    def TakhthayeKhali(self,j):
        if self.ListTakht[j] not in self.ListTakhtpor:
          self.ListTakhthayeKhali.append(j)
          self.teadtakhtKhali = self.tedadTakh-self.tedadTakhPor
        else:
            print("dar list takhthaye por qarar darad")
    
    def showListTakhthayeKhali(self):
        list1=[j for j in self.ListTakhthayeKhali]
        print("list takhat haye khali",list1)
        print("teadtakhtKhali",self.teadtakhtKhali)

    def counttakhtFull(self):
        self.teadShabhayePorbodanTakht+=1

    def showTedadShabha(self):
        print(f"tedad shabhaye por bodan takht{self.teadShabhayePorbodanTakht}")
     
    def situationOfBed(self):
        print("good")
     
#--------------------------------------------------------------------------------------
class paziresh():
    def __init__(self) -> None:

        self.Codebimar=self.Addbimar(sick)
        self.CodeKarmand=self.addCodekarmand(employ)
        self.CodeBakhsh=self.addCodeBakhsh(bakhsh)
        self.shomareTakht=self.addShomareTakht(takht)
        self.CodeDoctor=self.addCodeDoctor(doctor)
        self.ListTozihat=[]
        self.TarikhPaziresh=datetime.date.today()
        self.tarikhTarkhis=datetime.date.today()
        self.hazinehayejanebi=0
        self.ListHazineyebimarestan={}
    
    def addShomareTakht(self,takht):
        self.shomareTakh=takht
        
    def addCodeDoctor(self,doctor):
         self.CodeDoctor=doctor

    def Addbimar(self,sick):
        self.Codebimar=sick

    def addCodekarmand(self,employ):
        self.CodeKarmand=employ

    def addCodeBakhsh(self,bakhsh):
         self.CodeBakhsh=bakhsh
    
    def AddTypeOfsickness(self,typeSickness):
           self.ListTozihat.append(typeSickness)
           
    def showTypeOfsickness(self):
        for typeSickness in self.ListTozihat:
            print(f"noe bimari is{typeSickness}")

    def masrafAlkol(self):
        self.hazinehayejanebi+=2000
        self.showpazireshInfo()
    
    def kharidLebas(self):
        self.hazinehayejanebi+=30000
        self.showpazireshInfo()
    
    def calcutehazineyeBimarestan(self,sick):
         
        self.ListHazineyebimarestan["hazineye Har shab"]=sick*70000
        self.ListHazineyebimarestan["hazinehaye janebi"]=self.hazinehayejanebi
        self.showpazireshInfo()

    def showHazinehayeBimarestan(self):
        print(self.ListHazineyebimarestan)
        sum=0
        for value in self.ListHazineyebimarestan.values():
            sum+=value
        return sum

    def showpazireshInfo(self):
        
        print("********************************")
         
        print("codebimar is:",self.Codebimar)
        print("code karmand is :",self.CodeKarmand)
        print("code bakhsh is",self.CodeBakhsh)
        print("shomare takhat is",self.shomareTakh) 
        print("code doctor is ",self.CodeDoctor)

        print(f"tarikhpaziresh is{self.TarikhPaziresh}")
        print(f"tarikh tarkhis{self.tarikhTarkhis}")
        print(f"mablage kole hazinehayejanebi{self.hazinehayejanebi}")
        self.showTypeOfsickness()
        
        print("mablage kol bimarestan is",self.showHazinehayeBimarestan())
        print("*******************************")
        
    
#---------------------------------
doctor1=doctor("ali","soleymani",9,12,"kalp")
employ1=employ("mahsa","soleymani",99)
sick1=sick("dorsa","soleymani",12,1378,"osgol",5)
sick2=sick("dorsa","soleymani",12,1378,"osgol",6)
bakhsh1=bakhsh(6,"kalp",20)
takht1=takht(1,"daraye behtarin emkanat")
paziresh1=paziresh()
 
paziresh1.Addbimar(sick1.Codesick)
paziresh1.addCodekarmand(employ1.Codeemploy)
paziresh1.addCodeBakhsh(bakhsh1.Codebakhsh)
paziresh1.addCodeDoctor(doctor1.CodeDoctor)
paziresh1.addShomareTakht(takht1.shomareTakht)
paziresh1.showpazireshInfo()

bakhsh1.showEmptyBed(takht1.tedadTakh)
 
paziresh1.AddTypeOfsickness("bimari galbi")
paziresh1.kharidLebas()
paziresh1.masrafAlkol()
 
paziresh1.calcutehazineyeBimarestan(sick1.tedadShabha)

takht2=takht(2,"daraye behtarin emkanat")
takht3=takht(3,"daraye behtarin emkanat")
takht4=takht(4,"daraye behtarin emkanat")
takht1.AddListTakht()
takht2.AddListTakht()
takht3.AddListTakht()
takht2.showListtakht()
takht1.TakhthayePor(1)
takht1.TakhthayePor(2)
takht1.TakhthayePor(3)
takht1.showListTakhthayePor()
takht1.khalikardanTakht(3)
takht1.showListTakhthayeKhali()
takht1.showListTakhthayePor()


 
 

