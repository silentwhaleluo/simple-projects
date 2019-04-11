from sklearn.model_selection import GridSearchCV
def selectRFParam(model_name,clf,params,X_train,y_train):
    print('Tuning ',model_name)
    grid_search = GridSearchCV(clf, param_grid = params, n_jobs=-1)
    start = time.time()
    grid_search.fit(X_train,y_train)
    print("GridSearchCV took %.2f seconds for %d candidate parameter settings."
          % (time.time() - start, len(grid_search.cv_results_['params'])))
    print(grid_search.best_score_)
    print(grid_search.best_params_)
    return grid_search
grid_search = selectRFParam(model_name,clf,params,X_train,y_train)

model_name,clf,params = ("ExtraTreeClassifier" , ExtraTreeClassifier() ,
                           {'criterion':['gini','entropy'],
							'splitter': ['random','best'],
							'max_depth':[None,1000],
							'min_samples_split':[round(x,2) for x in np.arange(0.1,1,0.2)],
							'min_samples_leaf':[1,2,3,4,5],
							 'min_weight_fraction_leaf':[round(x,2) for x in np.arange(0.1,0.5,0.1)],
							 'max_features':['auto',None,'sqrt','log2'],
							 'max_leaf_nodes':[None,2,10,100],
							 'min_impurity_decrease' : [10**(-x) for x in range(1,9,2)],
							 'min_impurity_split':[10**(-x) for x in range(1,9,2)],
							 'class_weight':['balanced',None],})
 
 
 model_name,clf,params = (" DecisionTreeClassifier" ,  DecisionTreeClassifier() ,
                           
						   {'criterion':['gini','entropy'],
							'splitter': ['random','best'],
							'max_depth':[None,1000],
							'min_samples_split':[round(x,2) for x in np.arange(0.1,1,0.2)],
							'min_samples_leaf':[1,2,3,4,5],
							 'min_weight_fraction_leaf':[round(x,2) for x in np.arange(0.1,0.5,0.1)],
							 'max_features':['auto',None,'sqrt','log2'],
							 'max_leaf_nodes':[None,2,10,100],
							 'min_impurity_decrease' : [10**(-x) for x in range(1,9,2)],
							 'min_impurity_split':[10**(-x) for x in range(1,9,2)],
							 'class_weight':['balanced',None],})
							 
 model_name,clf,params = (" KNeighborsClassifier" ,  KNeighborsClassifier(5) ,
                           
						  {'weights':['uniform','distance'],
							'algorithm':['auto','ball_tree','kd_tree','brute'],
							'p':[1,2]})
							
							
 model_name,clf,params = (" LinearDiscriminantAnalysis" ,  LinearDiscriminantAnalysis() ,
							{"solver":['svd','lsqr','eigen'],
							"n_components":[100,200,300,None],})
# using svd
{"n_components":[100,200,300,None],
 "store_covariance":[True,False]
"tol":[10**(-x) for x in range(1,9,2)]}

#using 'lsqr' or 'eigen'
{"shrinkage":[None,'auto']+[round(x,2) for x in np.arange(0.1,1,0.1)],
    "n_components":[100,200,300,None],
"tol":[10**(-x) for x in range(1,9,2)]}