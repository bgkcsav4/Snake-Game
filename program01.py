import images


def generate_image (image: list, position_general: [int,int], length:int):
    
    green_list = []
    grey_list = []
    pg = position_general
    
    
    for i in range(len(pg)-length,len(pg)):
        green_list.append(pg[i])
    for i in range(0,len(pg)-length):
        grey_list.append(pg[i])
      
    for i in grey_list:
        x=i[0]
        y=i[1]
        image[y][x] = (128,128,128)        
    for i in green_list:
        x=i[0]
        y=i[1]
        image[y][x] = (0,255,0)
               
    return image
def generate_lists (img: str):
    image = images.load(img)
    food_array = []
    obstacle_array = []
    
    for i,valuei in enumerate(image):
        for j, valuej in enumerate(valuei):
            if valuej == (255,128,0):
                cor = [j,i]
                food_array.append(cor)
            if valuej == (255,0,0):
                cor = [j,i]
                obstacle_array.append(cor)
  
    return image, food_array, obstacle_array
def change_N(position_head: list, image:list):
    
    if position_head[1] == 0:
        position_head[1] = len(image) - 1
    else:    
        position_head[1] -= 1  
        
    return position_head[0], position_head[1]
def change_S(position_head: list, image:list):
    if position_head[1] == len(image) - 1:
        position_head[1] = 0
    else:
        position_head[1] +=1
    
    return position_head[0], position_head[1]
def change_E(position_head: list, image:list):
    if position_head[0] == len(image[0])-1:
        position_head[0] = 0
    else:
        position_head[0] +=1    
        
    return position_head[0], position_head[1]
def change_W(position_head: list, image:list):
    if position_head[0] == 0:
        position_head[0] = len(image[0]) - 1
    else:
        position_head[0] -=1  
    return position_head[0], position_head[1]
def change_NW(position_head: list, image:list):
    if position_head[1] == 0:
        position_head[1] = len(image) - 1
    else:
        position_head[1] -=1
    if position_head[0] == 0:
        position_head[0] = len(image[0]) - 1    
    else:
        position_head[0] -=1   
        
    return position_head[0], position_head[1]
def change_NE(position_head: list, image:list):
    if position_head[1] == 0:
        position_head[1] = len(image) - 1
    else:
        position_head[1] -=1  
                    
    if position_head[0] == len(image[0])-1:
        position_head[0] = 0
    else:    
        position_head[0] +=1 

    return position_head[0], position_head[1]
def change_SW(position_head: list, image:list):
    if position_head[1] == len(image) - 1:
        position_head[1] = 0
    else: 
        position_head[1] +=1   
                    
    if position_head[0] == 0:
        position_head[0] = len(image[0]) - 1    
    else:    
        position_head[0] -=1

    return position_head[0], position_head[1]
def change_SE(position_head: list, image:list):
    if position_head[1] == len(image) - 1:
        position_head[1] = 0
    else:   
        position_head[1] +=1 
                    
    if position_head[0] == len(image[0])-1:
        position_head[0] = 0    
    else:
        position_head[0] +=1 
                                     

    return position_head[0], position_head[1]



def generate_snake(start_img: str, position: list[int, int],
                   commands: str, out_img: str) -> int:

    length = 1
    image, food_array, obstacle_array = (generate_lists(start_img))
    
    position_head = position
    position_general = []
    position_general.append([position_head[0], position_head[1]])

    for each in commands.split():
        
        if each == "N":
                position_head[0],position_head[1] = change_N(position_head,image)
        elif each == "S":
                position_head[0],position_head[1] = change_S(position_head,image)
        elif each == "E":
                position_head[0],position_head[1] = change_E(position_head,image)            
        elif each == "W":            
                position_head[0],position_head[1] = change_W(position_head,image)  
        elif each ==  "NW":
                if ([(position_head[0] - 1), position_head[1]]) and ([position_head[0], position_head[1]-1]) in position_general[len(position_general)-length:-1]:
                    break             
                position_head[0],position_head[1] = change_NW(position_head,image)               
        elif each ==  "NE":
                if ([(position_head[0] + 1), position_head[1]]) and ([position_head[0], position_head[1]-1]) in position_general[len(position_general)-length:-1]:
                    break 
                position_head[0],position_head[1] = change_NE(position_head,image) 
        elif each ==  "SW":
                if ([(position_head[0] - 1), position_head[1]]) in position_general[len(position_general)-length:-1]  and  ([position_head[0], position_head[1]+1]) in position_general[len(position_general)-length:-1]:                    
                    break 
                position_head[0],position_head[1] = change_SW(position_head,image) 
        elif each ==  "SE":
                if ([(position_head[0] + 1), position_head[1]]) and ([position_head[0], position_head[1]+1]) in position_general[len(position_general)-length:-1]:
                    break
                position_head[0],position_head[1] = change_SE(position_head,image) 
                
                
        if ([position_head[0], position_head[1]] in obstacle_array) or ([position_head[0], position_head[1]]) in position_general[len(position_general)-length:-1]:
            break
        
        
        position_general.append([position_head[0], position_head[1]])
        
        if [position_head[0], position_head[1]] in food_array:
            length += 1
            food_array.remove([position_head[0], position_head[1]])

    images.save(generate_image(image,position_general,length),out_img)
        
    return length

