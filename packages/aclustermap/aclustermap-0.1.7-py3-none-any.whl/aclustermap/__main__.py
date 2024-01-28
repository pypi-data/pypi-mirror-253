import sys, yaml
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import colorcet as cc
import argparse
from importlib import resources

def iteritems(dct, key):
    if key in dct and dct[key] is not None:
        for k, v in dct[key].items():
            yield (k, v)

def recursive_update(A, B):
    for key, val in B.items():
        if key in A and key in B:
            if isinstance(A[key], dict):
                A = recursive_update(A[key], B[key])
            else:
                A[key] = B[key]
        else:
            A[key] = B[key]
    return A

def clustermap(df, params):
    fmt = params.get('format')
    if fmt is not None:
        seaborn_params = fmt.get('seaborn')
        pyplot_params = fmt.get('pyplot')

        if seaborn_params.get('set_context') is not None:
            sns.set_context(**seaborn_params.get('set_context'))

        for key, val in iteritems(pyplot_params, 'rcParams'):
            plt.rcParams[key] = val
    
    try:
        cmap = seaborn_params.get('clustermap').pop('cmap')
        g = sns.clustermap(df, cmap = cc.cm[cmap], **seaborn_params['clustermap'])
    except:
        if fmt is not None:
            g = sns.clustermap(df, **seaborn_params['clustermap'])
        else:
            g = sns.clustermap(df)
    
    if fmt is not None:
        for key, val in iteritems(pyplot_params, 'setp'):
            if key == 'xticklabels':
                plt.setp(g.ax_heatmap.get_xticklabels(), **val)
            if key == 'yticklabels':
                plt.setp(g.ax_heatmap.get_yticklabels(), **val)

    g.savefig(sys.stdout.buffer, format='png')


def parse_args():
    parser = argparse.ArgumentParser(description="Convert a YAMLized pandas DataFrame to a clustermap")
    
    args = parser.parse_args()
    return args

def main():
    df = None
    with resources.files('aclustermap').joinpath('default_format.yaml').open() as f:
        clustermap_params = yaml.full_load(f)
    
    try:
        stdin = sys.stdin.read()
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

    if 'format' in yml:
        try:
            recursive_update(clustermap_params['format'], yml['format'])
            del yml['format']
        except:
            print("seaborn.clustermap visualization parameter YAML is misformatted. Possible solutions: \
                \n - leave it out for sensible default choices \
                \n - generate it from a python dict \
                \n - use a HereDoc")

    try:
        if 'pandas.DataFrame' in yml:
            df = pd.DataFrame(yml['pandas.DataFrame'])
        else:
            df = pd.DataFrame(yml)
    except:
        print("pandas.DataFrame is misformatted. Try producing it via yaml.dump({'pandas.DataFrame': df.to_dict()}, default_flow_style=False)")

    clustermap(df, clustermap_params)
    



    

if __name__ == "__main__":
    main()
