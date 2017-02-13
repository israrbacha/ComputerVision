from knn.from_scratch_knn import *
import numpy as np
from knn import plot as p


def test1():


    data = [] 
    sample = []
    num = 25 #number of elements
    # Feature set containing (x,y) values of 25 known/training data
    #Create arrays of 25x1 of the range (0, 99)
    x = np.random.randint(0,100,(num,1)).astype(np.float32)
    y = np.random.randint(0,100,(num,1)).astype(np.float32)
    
    for i in range(0,num): 
        sample.append([x[i][0], y[i][0]])

    
    arraynp = np.asarray(sample)

    # Labels each one either Red or Blue with numbers 0 and 1
    #Create array of data 25x1 fo the range 0,2
    responses = np.random.randint(0,2,(num,1)).astype(np.float32)

    """Example for doing something awesome
    plt.scatter(blue[:,0],blue[:,1],80,'b','s')
    """

    
    #print sample
    #print arraynp
    #print len(arraynp)

    data.append(arraynp[responses.ravel() ==1 ])
    data.append(arraynp[responses.ravel() ==0 ])
    
    p.plot(data)



def test2():

    #All the sample
    data = load_data_set("datasets/flowers.csv")
    
    #The training set is going to be the 99 %
    training_set = get_training_set(0.99, data)

    #The test set
    test_set = get_test_set(training_set, data) 


    #This give me the kind of plants
    kind_of_plants = data["Family"].unique()
    
    

    k= 3
    #This columns are the selected features  for doing the euclidean distance.
    #columns = ["a", "b", "c", "d"]
    columns = ["a", "b"]
    predictions = knn(training_set, test_set, k, columns)
    for predict in predictions:
        print("Data to  predict")
        
        id_to = predict[0]
        k_nearest = predict[1]
        print (data.loc[id_to])
        print("\n")
        
        
        
        print ("\tK-nearest-neighbors")
        for n in k_nearest:
            distance = n[0]
            id_neigh = n[1]
            print ("Distance to the neighbor {} is {} ".format(n[1], n[0]))
            #print (data.loc[id_neigh])
            #print()



if (__name__ == "__main__"):
    test1()