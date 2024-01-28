The `aclustermap` package takes a [YAMLized](https://yaml.org/) pandas DataFrame as input, with optional formatting keywords, and outputs a Seaborn clustermap .png image:

```
cat example.yaml | aclustermap > example.png
```

If YAMLizing a pandas DataFrame is a new concept, here is a quick tutorial.

Let's create a Python module `generate_example.py`
```
import pandas, yaml;

# Generate random data with make_blobs to yield interesting clustering behavior
from sklearn.datasets import make_blobs; 
example = pandas.DataFrame(make_blobs(n_samples=36, centers=3, n_features=10)[0])

# Convert the DataFrame to a dict
df_dict = example.to_dict()

# Convert the dataframe to a dict, then YAMLize the dict
yml = yaml.dump(df_dict)

# Print to stdout
print(yml)
```

Here is a one-liner that combines the previous code to generate this dataframe, safe it to a file, and then output it as a clustermap to example.png:

```
python generate_example.py > example.yaml
cat example.yaml | aclustermap > example.png
```

Saving the dataframe to a file is not necessary, as it can be piped directly to aclustermap:

```
python generate_example.py | aclustermap > example.png
```

`aclustermap` uses the simplest possible way to tweak the visualization, which is to pass a second YAML dict containing keyword argumnets for [seaborn.clustermap](https://seaborn.pydata.org/generated/seaborn.clustermap.html) and [see also](https://seaborn.pydata.org/generated/seaborn.heatmap.html#seaborn.heatmap), [seaborn.set_context](https://seaborn.pydata.org/generated/seaborn.set_context.html), [pyplot.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html) with the Artist being the clustermap's `xticklabels` or `yticklabels`, or [pyplot.rcParams](https://matplotlib.org/stable/users/explain/customizing.html).

The formatting must be enclosed in a dict labeled according to the function it applies to. Here is the default formatting, which will be used if no formatting is specified.
Otherwise, simply `cat` a YAMLized nested dictionary with a structure similar to the following. 
```
format:
  seaborn:
    clustermap:
      cmap: CET_CBL1
      annot: true
    set_context:
      context: notebook
  pyplot:
    setp:
      xticklabels:
        rotation: 0
      yticklabels:
        rotation: 0
    rcParams:
      font.size: 12
```

A convenient way to specify minor formatting tweaks directly at the command line is with a HereDoc:

```
(python generate_example.py; cat <<EOF) | python -m aclustermap > example.png
format:
  seaborn:
    clustermap:
      annot: false

EOF
```
