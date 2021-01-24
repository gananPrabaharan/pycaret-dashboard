# import regression module
from pycaret.regression import setup, compare_models, save_model, pull, tune_model, automl
from pycaret.datasets import get_data


def get_model_results(data_df, target_col, n_models=5):

    # https://towardsdatascience.com/build-your-own-automl-in-power-bi-using-pycaret-8291b64181d

    # init setup
    reg1 = setup(data=data_df, target=target_col, silent=True, html=False)
    # compare models
    top_n = compare_models(n_select=n_models)

    # return the performance metrics df
    results = pull()

    # tune top5 models
    tuned_topn = [tune_model(i) for i in top_n]

    # select best model
    best = automl()
    # save best model
    save_model(best, 'best-model-power')

    # return the performance metrics df
    final_results = results
    return final_results


if __name__ == "__main__":
    data = get_data("juice")
    data.to_csv("juice.csv", index=False)
    target = "Purchase"
    data[target] = data[target].apply(lambda x: int(x == "MM"))

    result_df = get_model_results(data, target)
    print(result_df)
