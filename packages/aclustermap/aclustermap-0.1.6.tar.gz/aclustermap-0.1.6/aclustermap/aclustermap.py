import sys, yaml
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import colorcet as cc

def iteritems(dct, key):
    if key in dct and dct[key] is not None:
        for k, v in dct[key].items():
            yield (k, v)

def save_clustermap(df, params):
    seaborn_clustermap = params['seaborn.clustermap']

    sns.set_context(**params['seaborn.set_context'])

    for key, val in iteritems(params, 'pyplot.rcParams'):
        matplotlib.rcParam[key] = val
    
    cmap = seaborn_clustermap.pop('cmap')
    g = sns.clustermap(df, cmap = cc.cm[cmap], **seaborn_clustermap)

    for key, val in iteritems(params, 'pyplot.setp'):
        if key == 'xticklabels':
            plt.setp(g.ax_heatmap.get_xticklabels(), **val)
        if key == 'yticklabels':
            plt.setp(g.ax_heatmap.get_yticklabels(), **val)

    g.savefig(params['output_file'])

def main():
    df = None
    clustermap_params = yaml.full_load(open("default_format.yaml"))

    try:
        stdin = sys.stdin.read()
        if str(stdin) == "":
            print("aclustermap expects YAML from stdin containing at least a dict called pandas.DataFrame, \
                \n from which a pandas DataFrame can be constructed and typically produced via \
                \nyaml.dump({'pandas.DataFrame': df.to_dict()}, default_flow_style=False), \
                \nand optionally a second YAML dict called seaborn.clustermap, \
                \napplying custom visualization parameters to the clustermap. \
                \n\nArguments to seaborn.set_context, pyplot.rcParams, seaborn.clustermap, seaborn.heatmap \
                \n can be directly specified in YAML and passed through to: \
                \n- https://seaborn.pydata.org/generated/seaborn.plotting_context.html#seaborn.plotting_context \
                \n- https://matplotlib.org/stable/users/explain/customizing.html \
                \n- https://seaborn.pydata.org/generated/seaborn.clustermap.html \
                \n- https://seaborn.pydata.org/generated/seaborn.heatmap.html")
        yml = yaml.full_load(stdin)
    except:
        print("YAML input from stdin appears to be misformatted. \
            \nIf the pandas DataFrame is the problem, try producing it via via \
            \nyaml.dump({'pandas.DataFrame': df.to_dict()}, default_flow_style=False). \
            \nIf you're trying to enter seaborn.clustermap visualization parameters via the terminal, try \
            \n - leave it out for sensible default choices \
            \n - generate it from a python dict \
            \n - use a HereDoc")
        return

    try:
        df = pd.DataFrame(yml['pandas.DataFrame'])
    except KeyError:
        print("Input YAML must contain a dict called pandas.DataFrame")
    except:
        print("pandas.DataFrame is misformatted. Try producing it via yaml.dump({'pandas.DataFrame': df.to_dict()}, default_flow_style=False)")
    
    if 'seaborn.clustermap' in yml:
        try:
            clustermap_params['seaborn.clustermap'].update(yml['seaborn.clustermap'])
        except:
            print("seaborn.clustermap visualization parameter YAML is misformatted. Possible solutions: \
                \n - leave it out for sensible default choices \
                \n - generate it from a python dict \
                \n - use a HereDoc")

    save_clustermap(df, clustermap_params)
    



    

if __name__ == "__main__":
    main()
