#imports random module
from random import randint


women_dict = {'Kampala':['Mary', 'Judith', 'Flavia', 'Peace', 'Gracious', 'Rachel'],
                          'Gulu':['Eunice', 'Janet', 'Daniela', 'Esther', 'Joan', 'Winnie'], 
                           'Mbale':['Assumpta', 'Esther', 'Barbara'],
                          'Lira':['Gina', 'Vicky', 'Albright']}
# Calling the main functions depending on weather first visit or second visit            
print"1: First Time Visit "
print "2: Subsequent Visit"

w= int(raw_input("Choose kind of visit: "))

if w == 1:
    '''This is for first time visiting'''
    #A dictionary with the number of women per area got from the database
    #or another source
    women_number_dict = {'Kampala':6, 'Gulu':6, 'Mbale':3, 'Lira':3}

    #A dictionary showing the workers available
    #will be got later from the database
    workers_list =['Paul', 'Dan', 'Amali', 'Deo', 'Charles',
                   'Patricia', 'Samuel', 'Arnold', 'Jackie', 'Patience',
                   'Derrick', 'Maria', 'Mary', 'Chantal', 'Peace',
                   'Emma', 'Janet']

    #A list of all the areas to be visited as from the database
    area_list = ['Kampala','Gulu','Mbale','Lira']

    #A function to get the number of women in a particular area
    def add_num_of_women(area):
        num_of_women = women_number_dict[area]
        return num_of_women

    #A function get the total number of women in all the areas
    def total_num_of_women():
        total_num_of_women = 0
        
        for area in area_list:
            total_num_of_women += women_number_dict[area]
        return total_num_of_women

    #A function to get the area of a particular location from the database
    def add_area(area):
        #A dictionary showing the different locations and their areas
        area_dict = {'Kampala': 0.30, 'Gulu': 0.50, 'Mbale':0.90, 'Lira': 1.2}

        if area_dict[area]:
            area_size = float (area_dict[area])

        return area_size

    #A function to get the density of women in the various location
    def calculate_density():
        num_of_women = add_num_of_women(area)
        size = add_area(area)

        density_of_women = float (num_of_women/size)

        return density_of_women

    #A function that returns the characteristics of a given area
    def get_characteristics():
        num_of_women = add_num_of_women(area)
        size = add_area(area)
        density_of_women = calculate_density()
            
        characteristics = {'num_of_women':num_of_women, 'size':size,
                               'density_of_women': density_of_women}
        return characteristics

    #A function to get the total number of workers in the database
    def total_number_of_workers():
        #The workers_list placed as a local variable so that ot can rmain unchanged
        workers_list =['Paul', 'Dan', 'Amali', 'Deo', 'Charles',
                       'Patricia', 'Samuel', 'Arnold', 'Jackie', 'Patience',
                       'Derrick', 'Maria', 'Mary', 'Chantal', 'Peace',
                       'Emma', 'Janet']
        number_of_workers = len(workers_list)

        return number_of_workers

    #A function that gets the total number of workers in the database and
    #calculates the number of workers to be assigned per area
    def add_workers_numbers():
        num_of_women = add_num_of_women(area)
        size = add_area(area)
        density_of_women = calculate_density()
        total_number_of_women = total_num_of_women()

        num_of_workers = total_number_of_workers()

        num_of_women_per_worker = total_number_of_women/num_of_workers

         
        workers_per_unit_area = density_of_women/num_of_women_per_worker

        workers_in_area = int (workers_per_unit_area * size)
        return workers_in_area


    #A function to assign workers to the different areas
    def assign_workers():
        workers_in_area = add_workers_numbers()

        count = 0
        workers_left = len(workers_list)
        last_count = len(workers_list)-1

        workers_assigned = []

        #assign workers to different areas
        if workers_in_area > workers_left:
            workers_assigned.extend(workers_list)
            print "The number of workers available is less than the required number"
            print " "  #for space
            print "%d workers assigned instead of %d" %(workers_left,workers_in_area)
            print " "
        else:
            while count < workers_in_area:
                number = randint(0, last_count)
                worker = workers_list[number]
                workers_assigned.append(worker)
                del workers_list[number]
                last_count-=1
                
                count+=1
        print "Workers Assigned: ", workers_assigned
        print " "
                                 
        message = "The workers scheduled successfully"
        return message
    
elif w == 2:
    '''This is for the subsequent visit'''
    #A dictionary showing the women in different locations. These
    #will be got later from the database
    women_dict = {'Kampala':['Mary', 'Judith', 'Flavia', 'Peace', 'Gracious', 'Rachel'],
                          'Gulu':['Eunice', 'Janet', 'Daniela', 'Esther', 'Joan', 'Winnie'], 
                           'Mbale':['Assumpta', 'Esther', 'Barbara'],
                          'Lira':['Gina', 'Vicky', 'Albright']}

    #A dictionary showing the workers available
    #will be got later from the database
    workers_list =['Paul', 'Dan', 'Amali', 'Deo', 'Charles',
                       'Patricia', 'Samuel', 'Arnold', 'Jackie', 'Patience',
                       'Derrick', 'Maria', 'Mary', 'Chantal', 'Peace',
                       'Emma', 'Janet']

    #A list of all the areas to be visited as from the database
    area_list = ['Kampala','Gulu','Mbale','Lira']

    #A function to get the number of women in a particular area
    def add_num_of_women(area):
        women_list = []

        if women_dict[area]:
            for women in women_dict[area]:
                women_list.append(women)

        num_of_women = len (women_list)

        return num_of_women

    #A function to get the total number of women in the database
    def total_num_of_women():
        women_list = []
            
        for area in area_list:
            for women in women_dict[area]:
                women_list.append(women)
            
        total_num_of_women = len (women_list) 
        return total_num_of_women

    #A function to add the women in a particular area
    #to a list so that it can  be manipulated
    def add_list_of_women(area):
        women_list = []

        if women_dict[area]:
            for women in women_dict[area]:
                women_list.append(women)

        return women_list

    #A function to get the area of a particular location from the database
    def add_area(area):
        #A dictionary showing the different locations and their areas
        area_dict = {'Kampala': 0.30, 'Gulu': 0.50, 'Mbale':0.90, 'Lira': 1.2}

        if area_dict[area]:
            area_size = float (area_dict[area])

        return area_size

    #A function to get the density of women in the various location
    def calculate_density():
        num_of_women = add_num_of_women(area)
        size = add_area(area)

        density_of_women = float (num_of_women/size)

        return density_of_women

    #A function that returns the characteristics of a given area
    def get_characteristics ():
        num_of_women = add_num_of_women(area)
        size = add_area(area)
        density_of_women = calculate_density()
            
        characteristics = {'num_of_women':num_of_women, 'size':size,
                               'density_of_women': density_of_women}
        return characteristics

    #A function to get the total number of workers in the database
    def total_number_of_workers():
        #The workers_list placed as a local variable so that it can remain unchanged
        workers_list =['Paul', 'Dan', 'Amali', 'Deo', 'Charles',
                       'Patricia', 'Samuel', 'Arnold', 'Jackie', 'Patience',
                       'Derrick', 'Maria', 'Mary', 'Chantal', 'Peace',
                       'Emma', 'Janet']
        number_of_workers = len(workers_list)

        return number_of_workers

    #A function that gets the total number of workers in the database and
    #calculates the number of workers to be assigned per area
    def add_workers_numbers():
        #The workers_list placed as a local variable so that ot can rmain unchanged
        num_of_women = add_num_of_women(area)
        size = add_area(area)
        density_of_women = calculate_density()
        list_of_women = add_list_of_women(area)
        total_number_of_women = total_num_of_women()

        num_of_workers = total_number_of_workers()

        num_of_women_per_worker = total_number_of_women/num_of_workers

         
        workers_per_unit_area = density_of_women/num_of_women_per_worker

        workers_in_area = int (workers_per_unit_area * size)
        return workers_in_area

    #A function to assign workers to the different areas
    def assign_workers():
        num_of_women = add_num_of_women(area)
        size = add_area(area)
        density_of_women = calculate_density()
        list_of_women = add_list_of_women(area)
        total_number_of_women = total_num_of_women()

        num_of_workers = total_number_of_workers()

        num_of_women_per_worker = total_number_of_women/num_of_workers

         
        workers_per_unit_area = density_of_women/num_of_women_per_worker
        
        workers_in_area = add_workers_numbers()

        count = 0
        workers_left = len(workers_list)
        last_count = len(workers_list)-1

        workers_assigned = []

        if workers_in_area > workers_left:
            workers_assigned.extend(workers_list)
            print "The number of workers available is less than the required number"
            print " "  #for space
            print "%d workers assigned instead of %d" %(workers_left,workers_in_area)
        else:
            while count < workers_in_area:
                number = randint(0, last_count)
                worker = workers_list[number]
                workers_assigned.append(worker)
                del workers_list[number]
                last_count-=1
                
                count+=1                
                                 
            #assign workers to different women

        workers = []
        x = {}
        while len(list_of_women)!=0:
            for worker in workers_assigned:
                if len(list_of_women)==0:
                    break
                else:
                    i= 0
                    while i < num_of_women_per_worker:
                        map_dict = dict()
                        map_dict[worker] = list_of_women[i]
                        del list_of_women[i]
                        
                        i+=1
                workers.append(map_dict)
        print "Workers Assigned: ", workers_assigned
        print " "
        print " "

        print "The women attached to workers: ", workers
        print " "
        print " "

        #This code allows you to find out the exact women any worker has been
        #assigned to
        w = raw_input("Enter the worker (to see the women that he has been assigned to): ")
        k = []
        n = 0
        l = 0
        length1 = len(workers)
        length2 = len(workers_assigned)
        while l<length2:
            if w==workers_assigned[l]:
                worker = w
                print worker
                while n<length1:
                    the_key = workers[n].keys()[0]
                    if the_key == worker:
                        k.append(workers[n][worker])
                    n+=1
                print "The women assigned to ", w ," are: " ,k
                print " "
                break
            l+=1
        message= "The workers scheduled successfully"
        return message
else:
    print "Wrong option chosen"

#The main function
area_list = ['Kampala','Gulu','Mbale','Lira']

for area in area_list:
    name = area
    area_list = ['Kampala','Gulu','Mbale','Lira']

    count = 0

    while count< len(area_list):
        if name == area_list[count]:
            characteristics = get_characteristics()
            workers_numbers = add_workers_numbers()
            print name
            print " " #space
            print "Properties: ", characteristics
            print " "
            print "The number of workers to be assigned to this area is: ", workers_numbers
            print " "
            workers_assigned = assign_workers()
            print workers_assigned
            print " "
            print " "
            break
        count +=1