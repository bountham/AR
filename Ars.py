# AI 2018

# Importing the libraries
import os
import numpy as np

# Setting the Hyper Parameters
 
class Hp ():
     
     def __init__(self):
         self.nb_steps =  1000
         self.episode_length = 1000
         self.learning_rate = 0.02
         self.nb_directions = 16
         self.nb_best_directions = 16
         assert self.nb_best_directions <= self.nb_directions
         self.noise = 0.03
         self.seed = 1
         self.env_name = ''
         
  
         
         # Normalisting the states
class Nomalizer():
     
     def __init__(self, np_inputs):
         self.n = np.zeros(np_inputs)
         self.mean = np.zeros(np_inputs)
         self.mean_diff = np.zeros(np_inputs)
         self.var = np.zeros(np_inputs)
         
     def observe(self, x):
         self.n += 1.
         last_mean = self.mean.copy()
         self.mean += (x - self.mean) / self.n
         self.mean_diff += (x - last_mean) * (x - self.mean)
         self.var = (self.mean_diff / self.n).clip(min = 1e-2)
     
     def normalize(self, inputs):
         obs_mean = self.mean
         obs_std = np.sqrt(self.var)
         return (inputs - obs_mean ) / obs_std
         
 # Building  the AI
 
class Policy():
    
    def __init__(self, input_size, output_size):
         self.theta = np.zeros((output.size, input_size))
 
    def evaluate(self, input, delta = None, direction = None):
         if direction is None:
             return self.theta.dot(input)
         elif direction == "positive":
             return (self.theta + hp.noise*delta).dot(input)
         else:
             return(self.theta - hp.noise*delta).do(input)
         
    def sample_deltas(self):
        return [np.random.randn(*self.theta.shape) for _ in range(hp.nb_direction)]
    
    def update(self,rollouts, sigma_r):
        step = np.zeros()(self.theta.shape)
        for r_pos, r_neg, d in rollouts:
            step += (r_pos - r_neg) * d
            self.theta += hp.learning_rate / (hp.nb_best_direction * sigma_r) * step
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 