#!/usr/bin/env python
# coding: utf-8

# . What is the estimated depth of a Decision Tree trained (unrestricted) on a one million instance training set?
# 

# the depth of a well _balanced binary tree containing m leaves is equal to log2(m)3, roundedup .a BINARY Decision tree as is the case off tress will end up more or less well balanced at the end of training, with one leaf per training instance if it is trained without restrictions. if the traning set contain one million instances the decision tree have a depth of log2(160)=20

# 2. Is the Gini impurity of a node usually lower or higher than that of its parent? Is it always lower/greater, or is it usually lower/greater?
# 

# A node’s Gini impurity is normally lower than its figure’s. that is ensured via the CART training algorithm’s value feature, which splits each node in a manner that minimizes the weighted sum of its kids’s Gini impurities. but, if one infant is smaller than the alternative, it's far possible for it to have a better Gini impurity than its discern, so long as this increase is more than compensated for with the aid of a lower of the opposite baby’s impurity. for example, do not forget a node containing 4 times of class A and 1 of sophistication B. Its Gini impurity is 1 − 1/five^2 − four/5^2 = 0.32. Now suppose the dataset is one-dimensional and the times are covered up in the following order: A, B, A, A, A. you could confirm that the set of rules will split this node after the second example, generating one toddler node with instances A, B, and the other infant node with instances A, A, A. the primary infant node’s Gini impurity is 1 − half^2 − half of^2 = zero.five, that is better than its determine. this is compensated for by using the fact that the alternative node is pure, so the overall weighted Gini impurity is 25 × zero.five + 35 × 0 = zero.2 , that is lower than the discern’s Gini impurity.
# 

# 3. Explain if its a good idea to reduce max depth if a Decision Tree is overfitting the training set?
# 

# If a selection Tree is overfitting the schooling set, it can be a very good idea to lower max_depth, seeing that this can constrain the version, regularizing it

# 4. Explain if its a  good idea to try scaling the input features if a Decision Tree underfits the training set?
# 

# choice trees don’t care whether or now not the education data is scaled or focused; that’s one of the pleasant things about them. So if a selection Tree underfits the education set, scaling the enter functions will simply be a waste of time.

# 5. How much time will it take to train another Decision Tree on a training set of 10 million instances if it takes an hour to train a Decision Tree on a training set with 1 million instances?
# 

# The computational complexity of training a decision Tree is O(n × m log(m)). So if you multiply the training set size by using 10, the training time could be extended through ok = (n × 10m × log(10m)) / (n × m × log(m)) = 10 × log(10m) / log(m). If m = 106, then k ≈ 11.7, so you can assume the education time to be more or less eleven.7 hours

# 6. Will setting presort=True speed up training if your training set has 100,000 instances?
# 

# Presorting the schooling set quickens training only if the dataset is smaller than some thousand instances. If it incorporates one hundred,000 instances, putting presort=proper will drastically slow down education.
# 

# 7. Follow these steps to train and fine-tune a Decision Tree for the moons dataset:
# 

# Use make_moons(n_samples=10000, noise=0.4) to generate a moons dataset.
# Use train_test_split() to cut up the dataset into a schooling set and a test set.
# Use grid seek with cross-validation (with the help of the GridSearchCV elegance) to locate precise hyperparameter values for a DecisionTreeClassifier. trace: try numerous values for max_leaf_nodes.
# train it on the whole education set the usage of these hyperparameters, and degree your version’s overall performance at the take a look at set. You must get more or less 85% to 87% accuracy.

#  8.Follow these steps to grow a forest:
# 

# persevering with the previous exercising, generate 1,000 subsets of the schooling set, each containing a 100 selected randomly. hint: you may use Scikit-analyze’s ShuffleSplit elegance for this.
# 
# educate one selection Tree on every subset, using the pleasant hyperparameter values located in the preceding exercising. compare those 1,000 decision trees on the check set. given that they have been trained on smaller units, these choice timber will possibly perform worse than the first choice Tree, attaining simplest approximately 80% accuracy.
# 
# Now comes the magic. For every take a look at set instance, generate the predictions of the 1,000 decision timber, and keep only the most common prediction (you may use SciPy’s mode() characteristic for this). This technique gives you majority-vote predictions over the test set.
# 
# examine these predictions on the test set: you have to obtain a slightly higher accuracy than your first model (about 0.5 to at least one.5% higher). Congratulations, you have educated a Random wooded area classifier!

# In[ ]:




