
# coding: utf-8

# In[18]:

import random
import numpy as np
import matplotlib.pyplot as plt

# The first part of the code creates population distribution of three different types.

def create_unif_pop(n): # This creates a uniform population
    z = random.random()*n  #this generates a random number from 0 to n. 
    set_1 ={}
    a = 0 # 
    while a < 100:  # This function will make 100 copies of that same number in the set to make a uniform distribution. 
        set.append(z)
        a +=1
    return set_1
    
def create_norm_pop(mean,std): # This creates a normal distribution of the population based on given mean and standard dev. 
    set_1 = np.random.normal(mean,std,(100,))
    return set_1

def create_random_pop(scale):  # This creates a random population by chooding random numbers and adding them to the list. 
    set_1 = {}
    a = 0 
    while a < 100:
        b = scale*random.random() #This line outputs one random number from 1 to 100. 
        set_1.append(b)  # we add it to the thresholds set. We do this 500 times. 
        a +=1
    return set_1

import scipy.stats as st

def significance(alpha, mean1, mean2, sd1, sd2, size1, size2):  # This function is for significance test. 
    diff_in_means = mean2 - mean1 # We calculate the difference in means 
    
    print "The difference in means is " + str(diff_in_means) + " \n"
    
    # We use the formula for calculating the Standard error. 
    standard_error = ((sd1**2)/size1 + (sd2**2)/size2)**0.5
    print "The pooled standard error is " + str(standard_error) + " \n"
    
    # We calculate the Z-Score for the difference in the means. 
    # I have mentioned "0" here as well because it is the null hypothesis. 
    # The null hypothesis is difference in means = 0, so it lies at the centre. 
    
    z_score = ( diff_in_means - 0 ) / standard_error
    
    # This function gives me the area from the other(left) side of the graph to the point 
    area = st.norm.cdf(z_score)
    
    # Now we have to determine on which side of the graph is the point. 
    
    if area>0.5:# If it lies on right side, then we must subtract it from total area to get p-value
        p_value = 1 - area 
    else:          # Otherwise, it is itself the p-value
        p_value = area
    
    print "The p-value for the difference in the means is " + str(p_value) + " \n"
    if p_value <alpha:   # Now, if p-value is less than alpha, then the result is significant. 
        print "There is a statistically significant difference" + " \n"
    
    if p_value >alpha:   # If p-value is greater than alpha, the result is not significant. 
        print "The difference in the means is not statistically significant." + " \n"
        
    # Now calculating the pooled standard deviation for the efect size. 
    pooled_standard_deviation = (((size1-1)*(sd1**2) + (size2-1)*(sd2**2))/(size1 + size2 - 2))**0.5
    
    #Calculating Cohen's D through the formula. 
    cohen_d = diff_in_means/pooled_standard_deviation
    
    # We know the range of Cohen's D and how significance varies with it. 
    # The code checks for it and comments on the practical significance. 
    
    print "The Effect Size or Cohen's d is " + str(cohen_d) + " \n"
    
    if abs(cohen_d) <0.2:
        print "The results are not very practically significant." + " \n"
    elif abs(cohen_d) > 0.2 and abs(cohen_d) <= 0.5: # A value between 0.2 and 0.5 implies less practical significance. 
        print "The results are somewhat practically significant." + " \n"
    elif abs(cohen_d) > 0.5 and abs(cohen_d) <= 0.8: # A value between 0.5 and 0.8 implies good practical signifiance. 
        print "The results are quite practically significant." + " \n"
    elif abs(cohen_d) > 0.8:                         # A value of 0.8 and above implies very high practical significance. 
        print "The results are very practically significant." + " \n"
    
    upper_bound = 0 + standard_error*1.96   # Calculating upper bound of Confidence interval
    
    #Calculating The Z-Score of the upper bound relative to the alternative distribution. 
    relative_z_score = (upper_bound - diff_in_means)/standard_error
    
    #Power is the area from the right tail, so we subtract it from total area
    power = 1 - area
    
    print "The power of the experiment is " + str(power*100) + " %" + " \n"
    print "Thus, there is a " + str(power*100) + " % chance that we'll reject the null hypothesis correctly" 
    print "and accept the alternative hypothesis correctly." + " \n" + " \n"
    
# This is an opening text to give the operator a brief overview of the code. 
print "Hi, Thanks for using our simulator. This simulator applies the intervention of listening and learnign music"
print "to a group of randomly selected people and creates the distribution of these people based on your preferences." + "\n"
print "It follows the strategy of Category 2 Quasi Experiment where the intervention is introduced, then removed and"
print "then introduced again.The code also executes a test on the data for statistical significance, effect size and power."+ "\n"
print "The intervention is based on a uniform decrease in severities followed by the effect of some confounding variables" 
print "whose values are determined by your responses. We hope you like the code. Go ahead and put in your preferences."

# The code asks for your preference on what kind of distribution you want to see in the severities and the ages. 
x = int(raw_input("What kind of distribution would you like the severity of symptoms to have? 1 for Uniform,2 for Normal,3 for Random"))
y = int(raw_input("What kind of distribution would you like the ages of the participants to have? 1 for Uniform,2 for Normal,3 for Random"))
print "\n"
#Based on your preferences, it creates either a uniform, normal and random population.     
if x==1:  #  Severities are measured on a 10 point scale and is the relative accuracy of memory. 
            # 10 is severe loss of memory while 0 and below is normal memory. 
    severities = create_unif_pop(10)  # A uniform population of any number between 0 and 10. 
if x==2: 
    severities = create_norm_pop(5,2) # A normal distributon with 5 as mean and 2 as Std results in dist. touching 1 and 9.  
if x==3:
    severities = create_random_pop(10) # A random population with numbers between 0 and 10. 

if y==1:
    ages = 40 + create_unif_pop(50) # uniform population with ages below 90 above 40. 
if y==2:
    ages = create_norm_pop(65,15)# a normal distribution with mean 65 and std 30. This touches 40 and 90. 
if y==3:
    ages = 40 + create_random_pop(50) # A random population with numbers below 90 and above 40.  

# This prints the whole data set. We've specifically not disclosed any names to avoid any racial or other biases. (blinding)

a = 1 
while a<101:
    print "Participant " + str(a) + " :" + "Name_" + str(a) + ", Age: " + str(ages[a-1]) + ", Severity of memory loss: " + str(severities[a-1])
    a += 1
print "\n"
#Treatment 
severities_2 = []

b=0
while b<100: #This function introduces the intervention
    # It subtracts 1 on from each severity as an assumption that music cures memory. 
    
    # Age is considered a confounding variable here and 2% of the age is deducted from it. 
    # The logic behind this is that more is that age, more likely the effect is visible. 
    
    # The severity itself is also a confounding variable here. It adds 1% of the severities. 
    # The logic behind this is that more is the severity, more is the opposite effect of getting worse. 
    
    severities_2.append(severities[b] -1 -0.02*ages[b] + 0.01*severities[b])
    b +=1

number_of_healed = 0

for e in severities_2:
    if e<0: # This tracks if someone's severity went below 0. If yes, they were cured. 
        number_of_healed += 1 
        
print "Results for the first phase of intervention" + '\n'
# Plots the original distribution and severity distribution after intervention. 
plt.hist(severities)
plt.text(-2,-3,"Figure 1.Distribution of the severities of the patients before intervention ")
plt.show()
    
plt.hist(severities_2)
plt.text(-4,-3,"Figure 2. Distribution of the severities of the patients after intervention")
plt.show()

#This tests whether the results are statistically significant, calculates cohen's d and power. 
significance(0.025,np.mean(severities),np.mean(severities_2),np.std(severities),np.std(severities_2),100,100)

print "After the first intervention, " + str(number_of_healed) + " number of patients were completed cured." + "\n" + "\n"
severities_3 = []

c=0  # This is the second phase of the experiment where intervention is removed. 
while c<100:
    severities_3.append(severities_2[c] + 1) # Each person's severity increases because of natural increase in severity. 
    c +=1
    
number_of_healed_2 = 0

for e in severities_3:
    if e<0: # Tracking how many people came back from being cured to being a patient again. (Severity came above 0)
        number_of_healed_2 += 1 
    
print "Results for the second phase of removal of intervention" + '\n'

#Plots the new severity distribution. 
plt.hist(severities_3)
plt.text(-4,-3,"Figure 3. Distribution of the severities of the patients in 3rd phase after no intervention")
plt.show()

#The significance test for the distribution of intervention and then removal of intervention.
significance(0.025,np.mean(severities_2),np.mean(severities_3),np.std(severities_2),np.std(severities_3),100,100)

#This tracks how many people became a patient again because of natural increase in severity. 
# Basically tracks how many patient's severity rose above 0 again. 
print "After removing the intervention, " + str(number_of_healed - number_of_healed_2) + " number of patients developed Alzhiemer's again." + "\n"
severities_4 =[]

d=0
while d<100: # The final intervention. This creates the same intervention again with same confounding variables. 
    severities_4.append(severities_3[d] - 1 - 0.02*ages[d] + 0.01*severities_3[d])
    d +=1
    
number_of_healed_3 = 0

for e in severities_4:
    if e<0: # Tracks the number of patients that got cured this time. 
        number_of_healed_3 += 1 

print "Results for the third phase of reintroduction of intervention" + '\n'

#Plots the final distribution. 
plt.hist(severities_4)
plt.text(-6,-3,"Figure 4. Distribution of the severities of the patients in 3rd phase after intervention")
plt.show()

#The significance test for the no intervention and 2nd intervention distribution. 
significance(0.025,np.mean(severities_3),np.mean(severities_4),np.std(severities_3),np.std(severities_4),100,100)

#Final number of people cured whose severity went less than 0. 
print "After introducing the intervention again, " + str(number_of_healed_3) + " number of patients out of 100 were declared as cured." + "\n" + "\n"
print "Overarching Results" + '\n'
# This does a significance test on the first original distribution and the final distribution to check the final significance. 
significance(0.025,np.mean(severities),np.mean(severities_4),np.std(severities),np.std(severities_4),100,100)

