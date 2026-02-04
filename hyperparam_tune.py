import optuna




def objective(trial):

    hidden_layer_dict = {}

    lr = trial.suggest_float("lr", 1e-4, 1e-2, log=True)
    num_hidden_layers = trial.suggest_int("Number_hidden_layers", 1, 5)
    for i in range(num_hidden_layers):
        #This is hardcoded for now but come back later and make this a function of the initial provided conditions
        hidden_dim = trial.suggest_int(f"hidden_dim_width_{i+1}", 2, 20)
        hidden_layer_dict[f"Hidden Layer {i+1}"]
        

    #INSERT REST OF MODELING PROCESS HERE









