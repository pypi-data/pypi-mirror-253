import jax.numpy as jnp

from hypervecs.hypervector import MAPhv

__all__ = ["concatenate", "stack"]


def stack(arr: list[MAPhv], axis: int = 0) -> MAPhv:
    _type = arr[0].__class__
    _vsa = arr[0].vsa
    _arr = [_t.data for _t in arr]
    _out = jnp.stack(_arr, axis=axis)

    return _type(_out, vsa=_vsa)


def concatenate(arr: list[MAPhv], axis: int = 0) -> MAPhv:
    _type = arr[0].__class__
    _vsa = arr[0].vsa
    _arr = [_t.data for _t in arr]
    _out = jnp.concatenate(_arr, axis=axis)

    return _type(_out, vsa=_vsa)
