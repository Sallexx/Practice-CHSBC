import datetime

################################################################
def printTimeStamp(name):									  ##
 print('Автор програми: ' + name)							  ##
 print('Час компіляції: ' + str(datetime.datetime.now()))	  ##
 printTimeStamp('Beliaev and Pereviznyk')			          ##
################################################################
now = datetime.datetime.now() # Час
time = int(now.year)  # Рік
time = 2000
TextTime = str(time) # Число в строку
n1 = time % 400 # Якщо націло ділиться - Високосний	
n2 = time % 4   # З решти всі роки, що діляться на 4, є високосними.
n3 = time % 100 # З решти всі роки, що діляться на 100 – невисокосні.


# Якщо False - цей рік націло не ділиться 
# Якщо True  - цей рік ділиться без остачі

print(n1)
print(n2)
print(n3)

# Високосний рік
if n1 == 0 :
	print('Данний рік високосний: '+ TextTime)
elif n3 == 0 :
	print('Данний рік  не високосний: ' + TextTime) 
elif n2 == 0 :
	print('Данний рік високосний: '+ TextTime)
else :
	print('Данний рік  не високосний: ' + TextTime)





# Задача №17
# Високосні роки визначаються за наступними правилами:
# • Будь-який рік, що націло ділиться на 400, високосний.
# • З решти всі роки, що діляться на 100 – невисокосні.
# • З решти всі роки, що діляться на 4, є високосними.
# • Всі інші - невисокосні.
# Напишіть програму, яка зчитує рік та виводить повідомлення
# про те, чи є цей рік високосним.



