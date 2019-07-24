def setup():
    size(1000,1000)
    background(18,148,255)
    
    # mytank = range(5)
    # for jordin in mytank:
    #     fish(random(1000),random(1000),random(50,100),random(40,50))
    numFish = 5
    fishX = [] #x coordinates
    for jordin in range(numFish):
        fishX.append(random(1000))
    fishY = [] #y coordinates
    for jordin in range(numFish):
        fishY.append(random(1000))
    for x in range(numFish): #draws fish
        fish(fishX[x],fishY[x],50,100)
    
    
    
def fish(x,y,fish_width,fish_height):
    fish_width = random(80,100)
    fish_height = random(20,30)        
    noStroke()
    fill(random(255),random(255),random(255))
    ellipse(x,y,fish_width,fish_height)
    triangle(x+fish_width/2, y, x+(fish_width/2)+15, y-15,x+(fish_width/2)+15, y+15)
