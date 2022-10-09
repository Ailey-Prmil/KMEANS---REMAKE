import pygame
from random import randint
from math import sqrt
from sklearn.cluster import KMeans
import elbow_algorithm_graph # import self-made library

def group_points ():
    point_group = [[] for i in range (len(clusters))] # list of K sub-lists to store which points in each cluster

    for i in range (len(labels)) : # append the points into each group (cluster)
        point_group[labels[i]].append(points[i]) # point_group = [[point1,point2],[point3,point4]]
        # point1,point2 belongs to cluster 0
        # point3,4 belongs to cluster 1
        #each point is a list [x,y]

    return (point_group)

def save_errors ():
    global labels,clusters, grp_distances
    error_list=[]
    for i in range (1,11):
        K= i
        kmeans = KMeans(n_clusters=K).fit (points)
        labels = kmeans.predict(points)
        clusters = kmeans.cluster_centers_
        point_group = group_points()
        grp_distances = group_point_distance(point_group)
        error = calculate_error()
        error_list.append(error)
    return(error_list)
    
def distance (K): # need to know the distance between all the points and each cluster
    distances = [[] for i in range (K)] # each element is a list contain distances of each cluster

    for j in range (len(points)): 
        for i in range (len(clusters)): 
            x = (points[j][0]-clusters[i][0])**2 
            y = (points[j][1]-clusters[i][1])**2
            distance = sqrt(x+y) # distance = squareroot [(x-x0)^2+(y-y0)^2]
            distances[i].append(distance)
    return (distances)
def draw_rectangle (color,x,y,width,height):
    return (pygame.draw.rect(screen,color,(x,y,width,height))) 
def distance_compare ():# to mark all the point with labels
    labels = []
    # gan label cho tung diem :
    for i in range (len (points)): # distance each point with all clusters so as to find cluster closest to point
        lst_distance_each =  [distances[num][i] for num in range (len(distances))]
        dis_nearest_clus = min(lst_distance_each) # the nearest cluster
        labels.append (lst_distance_each.index(dis_nearest_clus))
    return (labels)
def cluster_update ():# to update the positions of clusters
    new_clusters = []
    
    for p in range (len(point_group)): 
        try:
            points_x = [point_group[p][num][0] for num in range (len(point_group[p]))] # list x value of a group point
            points_y = [point_group[p][num][1] for num in range (len(point_group[p]))] # list y value of a group point
            average_x = sum(points_x)/len(point_group[p])
            average_y = sum(points_y)/len(point_group[p])
            new_clusters.append([average_x,average_y])
        except ZeroDivisionError:
            new_clusters.append (clusters[p]) # if there is no point in cluster, the cluster will remains
  
    return (new_clusters)
def calculate_error (): 
    error = 0  # error is calculated by the sum of distance between clusters and their labelled points
    for i in (grp_distances):
        error += sum(i)
    return (int(error))
def group_point_distance (p_grp):
    grp_distances = [[] for i in range (len(p_grp))] # distance between points in the group
    for grp_index in range (len(p_grp)): 
        for point in p_grp[grp_index]:
            x = (point[0]-clusters[grp_index][0])**2 
            y = (point[1]-clusters[grp_index][1])**2
            distance = sqrt(x+y) # distance = squareroot [(x-x0)^2+(y-y0)^2]
            grp_distances[grp_index].append(distance)
    return (grp_distances)           
# draw all the constant interface
if (True): # all  variable and early structure
    pygame.init()
    screen = pygame.display.set_mode((1000,700))
    title = pygame.display.set_caption ("Kmeans visualization")
    clock = pygame.time.Clock()
    running = True
    BACKGROUND = (47,79,79)
    COLOURED_LINE = (230,230,250)
    BACKGROUND_PANEL = (176,224,230)
    COLOURED_BUTTON =(255,160,122)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    BUTTON_ALGO_COLOR = (255,255,102)
    RED = (255,0,0)
    font = pygame.font.SysFont("FNT",50)
    small_font = pygame.font.SysFont("FNT",20)
    text_plus = font.render("+",True,BLACK)
    txt_minus = font.render("-",True,BLACK)
    txt_run = font.render ("RUN",True,BLACK)
    txt_random = font.render("RANDOM",True,BLACK)
    txt_Algo = font.render ("ALGORITHM",True,BLACK)
    txt_Reset = font.render ("RESET",True,BLACK)
    txt_Graph = font.render ("GRAPH",True,BLACK)
    COLORS = []
    points = []
    clusters =[]
    labels = []
    K = 0
    error = 0
    error_list = []
    reset = False

while (len(COLORS) <15):  # random color for clusters
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    color = (r,g,b)
    if (color not in COLORS) and (color!= BACKGROUND_PANEL): # make sure ko trung
        COLORS.append(color)

while running:
    if (reset) : # when we press RESET, every thing need to be like original
        points = []
        clusters =[]
        labels = []
        K = 0
        error = 0
        COLORS = []
        while (len(COLORS) <15):  # random color for clusters
            r=randint(0,255)
            g=randint(0,255)
            b=randint(0,255)
            color = (r,g,b)
            not_allowed = [BACKGROUND_PANEL,WHITE]
            if (color not in COLORS) and (color not in not_allowed): # make sure ko trung
                COLORS.append(color)
    reset = False
    mouse_x, mouse_y = pygame.mouse.get_pos() # get position of mouse
    
    clock.tick(60)# 60 frames per second
    screen.fill(BACKGROUND)
    #draw interface (should use function)
    if (True): # draw all buttons and structure
        #draw panel
        draw_rectangle(COLOURED_LINE,30,30,600,500)
        draw_rectangle(BACKGROUND_PANEL,35,35,590,490) 
        #draw Kbutton +
        draw_rectangle(COLOURED_BUTTON,710,60,50,50) 
        screen.blit(text_plus,(725,65)) # position between the button
        #draw button K-
        draw_rectangle(COLOURED_BUTTON,810,60,50,50) 
        screen.blit(txt_minus,(830,65))#pos between the minus button
        #draw K=?
        txt_K = font.render ("K: {}".format(K),True,WHITE ) # K need to change value
        screen.blit(txt_K,(750,130))
        #draw button RUN
        draw_rectangle(COLOURED_BUTTON,710,200,150,60) 
        screen.blit(txt_run,(750,215))
        #draw button RANDOM
        draw_rectangle(COLOURED_BUTTON,680,300,210,60) 
        screen.blit(txt_random,(705,315))
        # Write Error
        txt_error = font.render("ERROR : {}".format(error),True,WHITE )
        screen.blit(txt_error,(680,390))
        #Draw Algorithm button
        draw_rectangle(BUTTON_ALGO_COLOR,660,450,250,60)
        screen.blit(txt_Algo,(685,465))    
        #Draw Button Reset
        draw_rectangle(COLOURED_BUTTON,700,550,170,60)
        screen.blit (txt_Reset,(730,565))
        #Draw Graph Button 
        draw_rectangle(COLOURED_BUTTON,270,550,170,60)
        screen.blit (txt_Graph,(290,565))

    for i in range (len(points)): # draw points
        pygame.draw.circle (screen,BLACK,(points[i][0]+35,points[i][1]+35),3)      
        pygame.draw.circle (screen,WHITE,(points[i][0]+35,points[i][1]+35),2)

    #draw mouse position when mouse in panel
    if (40<mouse_x<625)and (40<mouse_y<525):
        txt_m_pos = small_font.render("({}:{})".format(mouse_x-35,mouse_y-35),True,BLACK)
        screen.blit(txt_m_pos,(mouse_x+10,mouse_y))
    
    if(len(labels)!=0): ### only when every points have their label, thís code could run
        for i in range(len(points)): 
            pygame.draw.circle (screen,COLORS[labels[i]],(points[i][0]+35,points[i][1]+35),3)

    # draw K random clusters
   
    for i in range (len(clusters)):
        pygame.draw.circle (screen,COLORS[i],(clusters[i][0]+35,clusters[i][1]+35),6)
    #end draw interface(should use function)
    distances = distance(len(clusters))  
    for event in pygame.event.get(): # how to interact with users

        if (event.type==pygame.QUIT):
            running=False
### Interact with MOUSE
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (35<mouse_x<625)and (35<mouse_y<525): # when draw points
                labels = [] # when we want more points, every other points should have no labels
                point = [mouse_x-35,mouse_y-35]
                points.append ( point)

            if (750>mouse_x>700) and (60<mouse_y<110):# when press K+
                if (K<15):
                    K+=1
                
            if (800<mouse_x<850) and (60<mouse_y<110):# when press K-
                if (K>0):
                    K-=1
               
            if (670<mouse_x<880) and (300<mouse_y<360):# when press RANDOM
                clusters = []
                labels = []      
                error = 0
                for i in range (K) :
                    random_point = [randint(0,590),randint(0,490)]
                    clusters.append(random_point)

            if (700<mouse_x<850) and (200<mouse_y<260):# when press RUN

                if (len(clusters)==0): # if there is no cluster (K=0)
                    continue
                 # calculate all distances between points and each cluster
                labels = distance_compare() # list of label of all points (label is index of cluster)
                point_group = group_points()
                grp_distances = group_point_distance(point_group)
                error = calculate_error()
                clusters = cluster_update()

            if (650<mouse_x<900) and (450<mouse_y<510): # press ALGORITHM button
                if (K == 0) :
                    continue
                kmeans = KMeans(n_clusters=K).fit (points)
                labels = kmeans.predict(points)
                clusters = kmeans.cluster_centers_
                point_group = group_points()
                grp_distances = group_point_distance(point_group)
                error = calculate_error()
                
                
            if (690<mouse_x<860) and (550<mouse_y<610): # press RESET button
                reset = True

            if (270<mouse_x<440) and (550<mouse_y<610): # press GRAPH
                error_list = save_errors()
                elbow_algorithm_graph.line_graph(error_list)
                K=0
                clusters=[]
                labels = []
      
    pygame.display.flip ()

pygame.quit()

