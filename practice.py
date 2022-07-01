


class House:
    def __init__(self,location,HouseType,SaleType,HousePrice,CompleteYear) :
        self.l = location
        self.HT = HouseType
        self.ST= SaleType
        self.HP=HousePrice
        self.CY= CompleteYear

    def ShowDetail(self):
        print(self.l,self.HT,self.HP,self.CY)




houses=[]
house1=House("강남","아파트","매매","10억","2002년")
house2=House("여의도","빌라","전세","3억","2021년")
house3=House("역곡","오피스텔","월세","500/ 50","2019")
houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0} 개의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.ShowDetail()
