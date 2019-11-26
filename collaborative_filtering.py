import pickle
import numpy as np

def collaborative_filtering(user_id, num_of_predictions, recipe_history=[]):
  '''
  Parameters
  ----------
  user_id: [int] ID of user. Corresponds to row in user matrix which represents user recipe rating history as 100 dimensional vector.
  
  num_of_predictions: [int] Number of recipe ids function should return.
  
  recipe_history: [Python List of strings] List of ids of recipes user has already rated. Function will not return these recipes as predictions.
  '''
  with open("U.pickle","rb") as fh:
    U = pickle.load(fh)
  with open("Vt.pickle","rb") as fh:
    Vt = pickle.load(fh)
  with open("sigma.pickle","rb") as fh:
    sigma = pickle.load(fh)
  with open("column_recipe_indices.pickle","rb") as fh:
    column_recipe_ids = pickle.load(fh)
  with open("recipe_id_dict.pickle","rb") as fh:
    recipe_id_dict = pickle.load(fh)
    
  user_vector = U[user_id]
    
  pred_values = np.dot(np.dot(user_vector, sigma), Vt) 
  
  pred_indices = np.argsort(pred_values)
  pred_recipe_ids = column_recipe_ids[pred_indices]
  pred_recipe_ids = np.array([id for id in pred_recipe_ids if id not in recipe_history])
  return [recipe_id_dict[int(idx)] for idx in pred_recipe_ids[-num_of_predictions:]]
  
# #testing
with open("recipe_history_0.pickle","rb") as fh:
  recipe_history_0 = pickle.load(fh)
 
print(collaborative_filtering(0, 10, recipe_history_0))
print(collaborative_filtering(0, 10))