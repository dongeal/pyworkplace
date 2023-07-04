# class Stair():
#     def __init__(self, _stair_number) -> None:
#         self.stair_number = _stair_number

#     def case(self):
#         if self.stair_number == 1 :
#             return 1
#         elif self.stair_number == 2 :
#             return 2
#         elif self.stair_number == 3 :
#             return 4
#         else:
#             return Stair(self.stair_number -1).case() + \
#                    Stair(self.stair_number -2).case() + \
#                    Stair(self.stair_number -3).case()

#     def answer(self):
#         print(stair.case())
       

# while True:
#     in_number = input("계단의 수:")
#     if in_number.isdigit():
#         stair_number = int(in_number)
#         if stair_number == 0:
#                 break
#         else:
#             stair = Stair(stair_number)
#             stair.answer()
      
fact = lambda x  : x+10

print(fact(4))
