#Set the seed for every experiement
random_state = 1234

#Numbre of folding used in cross validation 
#Can be 1,2,3,4 or 5
NN = 5

#Do you want to use only 100 entries for each dataset ? 
#(Usefull to test for new features)
small = True

#Lunch in parallel or not
para = True

#Select target model
from .. import models as m  #Don't touch this line ! 
#models = [m.RandomForest,m.AdaBoost,m.AdaBoost_Bks,m.AdaBoost_Bks_Ba]
models = [m.AdaBoost,m.AdaBoost_Bks,m.AdaBoost_Bks_Ba]
