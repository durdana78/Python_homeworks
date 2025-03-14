from bs4 import BeautifulSoup

with open('weather.html', 'r', encoding = 'utf-8') as html_file :
    content = html_file.read()
    #print(content)

    soup = BeautifulSoup(content,'lxml')
    infos = soup.find_all('td')
    for i in range (0,len(infos), 3) :
        print(f"On {infos[i].text}, it is {infos[i + 1].text} and {infos[i + 2].text} ")

    highest_temp = int(infos[1].text.split('°')[0])

    for i in range (0, len(infos), 3)  :
        temp = int(infos[i + 1].text.split('°')[0])
        if highest_temp < temp :
            highest_temp = temp

    print(f"The highest temperature is {highest_temp}°C") 

    for i in range (0, len(infos), 3) :
        condition = infos[i + 2].text
        if condition == "Sunny" :
            print(f"On {infos[i].text}, it is {infos[i + 2].text}")   
    

    total_temp = 0
    for i in range (0, len(infos), 3) :
        temp = int(infos[i + 1].text.split('°')[0])
        total_temp += temp
    avg_temp = total_temp / (len(infos) // 3)
    print(f"The average temperature is {avg_temp}°C")


