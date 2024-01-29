# paramspy
container for global (Singelton) loading and saving parameters

## Usage example
On load, need to be called once:
```
Params(LOCATION_OF_PARMAS_JSON)
```
On usage, after calling the above
```
param_dict=Params()
```

`params.json` is a nested parameters json, e.g.;
```
{
    "data": {
        "granularity": 21600,
        "header": [
            "d_price"
        ],
        "look_back": 42,
        "mean": 6.477538237436277,
        "n_test": 64,
        "std": 257.3105989979195,
        "time_decay_sec": 3000000,
        "weight_bias": 0.1
    },
    "data_collection": {
        "n_record_per_fetch": 280,
        "time_span_days": 20000
    },
    "logging": {
        "model_folder": "models",
        "output_folder": "logdir",
        "plot_every": 32
    },
    "train": {
        "batch_size": 6400,
        "learn_rate": 0.0001,
        "n_epochs": 60000
    }
}

```

<!---
deploy
```
python setup.py sdist
twine upload  dist/*
```
-->



