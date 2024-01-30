#Set the seed for every experiement
random_state = 1234

#Numbre of folding used in cross validation 
#Can be 1,2,3,4 or 5
NN = 5

#Do you want to use only 100 entries for each dataset ? 
#(Usefull to test for new features)
small = False

#Lunch in parallel or not
para = True

#Select target model
from .. import models as m #Don't touch this line ! 
#Choose which target model you want to use
models = [m.RandomForest]
