from dataclasses import dataclass
from typing import Union, TypeVar, Iterable, Any

from jsonargparse.typing import register_type
from ray.tune.search.sample import Domain

T = TypeVar("T")


@dataclass
class GridItem:
    grid_search: Iterable


Param = Union[Domain, GridItem, T]


def _ray_domain_deserializer(v: Any):
    if isinstance(v, str):
        # TODO SECURITY WARNING
        return eval(f'exec("import ray.tune") or {v}')
    elif isinstance(v, dict) and any(["sample_from" in k for k in v.keys()]):
        # the str value "ray.tune.sample_from(lambda spec: spec.config.uniform * 0.01)"
        # is parsed as a dict {"ray.tune.sample_from(lambda spec": "spec.config.uniform * 0.01)"}
        v = ", ".join([f"{k}: {v}" for k, v in v.items()])
        return _ray_domain_deserializer(v)
    else:
        return v


register_type(Domain, deserializer=_ray_domain_deserializer)
