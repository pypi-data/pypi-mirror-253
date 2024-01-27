# rayconfig
Polymorphic structured [`jsonargparse`](https://github.com/omni-us/jsonargparse)-friendly configurations as [`dataclasses`](https://docs.python.org/3.10/library/dataclasses.html) for [`ray`](https://github.com/ray-project/ray) jobs.
Write [`jsonargparse`](https://github.com/omni-us/jsonargparse) CLI's for [`ray`](https://github.com/ray-project/ray) jobs.
Pass configurations as typed objects.
Configure hyperparameters [search space](https://docs.ray.io/en/releases-2.9.1/tune/api/search_space.html).

Mainly `rayconfig` does the following:
- Enables conversion between python `dict` and corresponding polymorphic `dataclass` by using the convention of [`jsonargparse`](https://github.com/omni-us/jsonargparse) using `class_path` and `init_args` config fields
  - `rayconfig` adapts [`dacite`](https://github.com/konradhalas/dacite/)'s `from_dict` function to convert python `dict` to corresponding python `dataclass`.
  - `rayconfig` adapts python's `dataclasses.asdict` function to convert a `dataclass` to a python `dict`.
- Introduces `Param[T]` type to enable configuring hyperparameters of type `T` using [Ray Tune Search Space API](https://docs.ray.io/en/releases-2.9.1/tune/api/search_space.html)


## Installation

```
$ pip install rayconfig
```

## Quick start

```python
from dataclasses import dataclass
from rayconfig import asdict, from_dict


@dataclass
class Config:
    user: str
    port: int


config_dict = {
    'user': 'Ahmed',
    'port': 8080,
}

config_obj = Config(user='Ahmed', port=8080)

assert config_dict == asdict(config_obj)
assert config_obj == from_dict(data_class=Config, data=config_dict)
```

## Basic Example


- Write polymorphic nested config types with tunable hyperparameters:
  - All classes should be annotated with `@dataclass`.
  - Extendable classes must inherit from `abc.ABC`.
  - Tunable hyperparameters of type `T` should use `Param[T]`.
```python
from abc import ABC
from dataclasses import dataclass
from rayconfig import Param


@dataclass
class ModelConfig(ABC):
    name: str

@dataclass
class ModelAConfig(ModelConfig):
    n1_dropout: Param[float]
    hidden_dim: Param[int]
    
@dataclass
class ModelBConfig(ModelConfig):
    fc_out: Param[int]
    embed_dim: Param[int]

@dataclass
class OptimizerConfig(ABC):
    name: str

@dataclass
class OptimizerAConfig(OptimizerConfig):
    lr: Param[float]

@dataclass
class OptimizerBConfig(OptimizerConfig):
    lr: Param[float]
    momentum: Param[float]

@dataclass
class TrainConfig:
    model: ModelConfig
    optimizer: OptimizerConfig
    batch_size: Param[int]
```

- Write [`jsonargparse`](https://github.com/omni-us/jsonargparse) CLI
```python
from jsonargparse import ArgumentParser, ActionConfigFile

def main():
    parser_train = ArgumentParser()
    parser_train.add_argument("config", type=TrainConfig)

    parser = ArgumentParser(prog="app")
    parser.add_argument("--config", action=ActionConfigFile)

    subcommands = parser.add_subcommands()
    subcommands.add_subcommand("train", parser_train)
    subcommands.add_subcommand("tune", parser_train)

    config = parser.instantiate_classes(parser.parse_args())

    if "train" in config:
        train(config.train.config)
    elif "tune" in config:
        tune(config.tune.config)

if __name__ == "__main__":
    main()
```

- Convert config object to dictionary when needed using `asdict`
```python
import ray
from rayconfig import asdict

def train(config: TrainConfig):
    ...
    trainer = ray.train.torch.TorchTrainer(
        train_func,
        train_loop_config=asdict(config) # <--- HERE
    )
    ...
    result = trainer.fit()
    ...

def tune(config: TrainConfig):
    ...
    trainer = ray.train.torch.TorchTrainer(
        train_func,
    )
    ...
    tuner = ray.tune.Tuner(
        trainer,
        param_space={
            "train_loop_config": asdict(config) # <--- HERE
        },
    )
    ...
    result_grid = tuner.fit()
    ...
```

- Convert config dictionary to object when needed using `from_dict`
```python
from rayconfig import from_dict

def train_func(config_dict):
    ...
    config = from_dict(data_class=TrainConfig, data=config_dict) # <--- HERE
    ...
    optimizer = get_optimizer(config.optimizer)
    ...
    model = get_model(config.model)
    ...
```

- Write configurations, e.g. yaml file:
  - Classes extending from base classes must be qualified by `class_path`, a python import path,
  and fields grouped under `init_args`
  - Hyperparameters can take a single value or to be configured using [Ray Tune Search Space API](https://docs.ray.io/en/releases-2.9.1/tune/api/search_space.html)
  - WARNING: currently `rayconfig` uses `eval` to evaluate ray tune param configurations.
  This can introduce security risks. So, use with caution if you only trust your execution environment.
```yaml
tune:
  config:
    model:
      class_path: app.ModelAConfig
      init_args:
        n1_dropout: ray.tune.uniform(0.4, 0.6)
        hidden_dim: "ray.tune.sample_from(lambda _: 2 ** __import__('numpy').random.randint(7, 9))"
    optimizer:
      class_path: app.OptimizerBConfig
      init_args:
        lr: ray.tune.grid_search([0.001, 0.01, 0.1])
        momentum: 0.9
    batch_size: ray.tune.grid_search([32, 64, 128])
```