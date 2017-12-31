# Automatically generates an almost unique RGB code
def color_generation(index):
    red = 0
    green = 0
    blue = 0
    for i in range(0, index + 1):
        if i % 3 == 0:
            red += 50
            
        elif i % 3 == 1:
            green += 50
            
        else:
            blue += 50

        if i > 0 and red == blue and blue == green:
            if i % 3 == 0:
                blue -= 75
                
            elif i % 3 == 1:
                red += 65
                
            else:
                green -= 55
                
    return [red % 255, green % 255, blue % 255]

if __name__ == "__main__": 
    tmp = []

    for i in range(0, 160):
        color = color_generation(i)
        tmp.append(color)
        print(color)

        for x in range(0, len(tmp) -1):
            if tmp[x] == color:
                print("Color already generated! \o/")
                break


        
