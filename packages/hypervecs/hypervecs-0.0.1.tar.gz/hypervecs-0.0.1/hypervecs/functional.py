import jax
import jax.numpy as jnp
from hypervecs import VSA, Hypervector

__all__ = ["random_hv"]


def random_hv(
    shape: tuple[int, ...], vsa: VSA = "MAPI", key: jnp.ndarray = jax.random.PRNGKey(0)
) -> Hypervector:
    _key, _ = jax.random.split(key)

    if vsa == "MAPI":
        _hv = 2 * jax.random.bernoulli(_key, p=0.5, shape=shape) - 1
    elif vsa == "MAP":
        _hv = jax.random.normal(_key, shape=shape)

    hv = Hypervector(_hv, vsa=vsa)

    return hv
