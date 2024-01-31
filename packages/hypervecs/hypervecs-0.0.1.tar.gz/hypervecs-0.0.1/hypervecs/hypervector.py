import jax
import jax.numpy as jnp
import numpy as np

from typing import Tuple

from hypervecs import VSA

# import hypervecs.functional as F

__all__ = ["Hypervector", "MAPhv"]


def _random_hv(
    shape: tuple[int, ...], vsa: VSA = "MAPI", key: jnp.ndarray = jax.random.PRNGKey(0)
) -> jnp.ndarray:
    _key, _ = jax.random.split(key)

    if vsa == "MAPI":
        hv = 2 * jax.random.bernoulli(_key, p=0.5, shape=shape) - 1
    elif vsa == "MAP":
        hv = jax.random.normal(_key, shape=shape)

    return hv


class Hypervector:
    data: jnp.ndarray
    vsa: VSA
    quantized: bool = False

    def __init__(self, data: np.ndarray | jnp.ndarray | None, vsa: VSA):
        super().__init__()

        assert vsa in ["MAP"], f"vsa must be one of ['MAP'], got {vsa}"
        self.vsa = vsa

        ## Error checking
        if data is None:
            raise ValueError("Data must be provided")
        else:
            if isinstance(data, jnp.ndarray):
                _hv = data
            else:
                _hv = jnp.asarray(data)

        self.data = _hv

    def __jax_array__(self, dtype=None) -> jnp.ndarray:
        if dtype is None:
            return self.data
        else:
            return self.data.astype(dtype)

    def __repr__(self):
        return f"Hypervector(data={self.data}, vsa={self.vsa})"

    @property
    def shape(self):
        return self.data.shape

    @property
    def ndim(self):
        return self.data.ndim

    @property
    def size(self):
        return self.data.size

    @property
    def dtype(self):
        return self.data.dtype

    @property
    def T(self):
        return self.__class__(self.data.T, vsa=self.vsa)

    @property
    def D(self):
        return self.data.shape[-1]

    def __len__(self):
        return len(self.data)

    def __add__(self, other: "Hypervector | int | float") -> "Hypervector":
        raise NotImplementedError

    def __sub__(self, other: "Hypervector | int | float") -> "Hypervector":
        raise NotImplementedError

    def __mul__(self, other: "Hypervector | int | float") -> "Hypervector":
        raise NotImplementedError

    def multiset(self):
        raise NotImplementedError

    def multibind(self):
        raise NotImplementedError


# Define the flatten function for Hypervector
def hypervector_flatten(hv: Hypervector):
    # Returns the data (leaves) and None (auxiliary data)
    return [hv.data], hv.vsa


# Define the unflatten function for Hypervector
def hypervector_unflatten(aux_data, children):
    # Reconstructs the Hypervector from the leaves
    return Hypervector(data=children[0], vsa=aux_data)


# Register Hypervector with JAX's pytree system
jax.tree_util.register_pytree_node(
    Hypervector, hypervector_flatten, hypervector_unflatten
)


class MAPhv(Hypervector):  # Fixed: Added colon here
    def __init__(
        self,
        data: np.ndarray | jnp.ndarray | None = None,
        shape: Tuple[int, ...] | None = None,
        key: jnp.ndarray = jax.random.PRNGKey(0),
        quantized: bool = False,
        **kwargs,
    ):
        if data is None and shape is not None:
            data = _random_hv(shape, vsa="MAP", key=key)

            if quantized:
                data = jnp.sign(data)

        super().__init__(data=data, vsa="MAP")  # Fixed: Pass data and vsa to superclass

    @classmethod
    def empty(cls, shape: tuple[int, ...]) -> "MAPhv":
        _data = jnp.zeros(shape)
        return cls(data=_data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.__class__(self.data[idx])

    def __neg__(self):
        return self.__class__(-self.data)

    def __pos__(self):
        return self

    @staticmethod
    @jax.jit
    def add_hypervector(data1: jnp.ndarray, data2: jnp.ndarray) -> jnp.ndarray:
        return data1 + data2

    def __add__(self, other: "MAPhv | int | float") -> "MAPhv":
        if isinstance(other, MAPhv):
            # Call the JIT-compiled function with the raw JAX array data
            new_data = self.add_hypervector(self.data, other.data)
            return self.__class__(data=new_data)
        else:
            _result = self.add_scalar(self.data, other)

        return self.__class__(_result)

    @staticmethod
    @jax.jit
    def add_scalar(a, other: int | float) -> jnp.ndarray:
        new_data = a + other
        return new_data

    def __sub__(self, other: "MAPhv | int | float") -> "MAPhv":
        if isinstance(other, MAPhv):
            _result = self.add_hypervector(self.data, -other.data)
        else:
            _result = self.add_scalar(self.data, -other)

        return self.__class__(_result)

    @staticmethod
    @jax.jit
    def mul_hypervector(data1: jnp.ndarray, data2: jnp.ndarray) -> jnp.ndarray:
        return data1 * data2

    @staticmethod
    @jax.jit
    def mul_scalar(a, other: int | float) -> jnp.ndarray:
        new_data = a * other
        return new_data

    def __mul__(self, other: "MAPhv | int | float") -> "MAPhv":
        if isinstance(other, MAPhv):
            _result = self.mul_hypervector(self.data, other.data)
        else:
            _result = self.mul_scalar(self.data, other)

        return self.__class__(_result)

    @staticmethod
    @jax.jit
    def div_scalar(a: jnp.ndarray, scalar: int | float) -> jnp.ndarray:
        new_data = a / scalar
        return new_data

    def __truediv__(self, scalar: int | float) -> "MAPhv":
        _result = self.div_scalar(self.data, scalar)

        return self.__class__(_result)

    @staticmethod
    @jax.jit
    def cos_sim(a: jnp.ndarray, b: jnp.ndarray) -> float | jnp.ndarray:
        _norm1 = jnp.linalg.norm(a, axis=-1, keepdims=True)
        _norm2 = jnp.linalg.norm(b, axis=-1, keepdims=True)

        _a = a / _norm1
        _b = b / _norm2

        cos_sim = a @ b.T

        return cos_sim.squeeze()  # ** 2

    def sim(self, other: "MAPhv") -> jnp.ndarray:
        return self.cos_sim(self.data, other.data)

    def multiset(self, axis: int = 0, q=False) -> "MAPhv":
        _result = jnp.sum(self.data, axis=axis)

        if q:
            _result = jnp.sign(_result)

        return self.__class__(_result)

    def multibind(self, axis: int = 0, q=False) -> "MAPhv":
        _result = jnp.prod(self.data, axis=axis)
        if q:
            _result = jnp.sign(_result)

        return self.__class__(_result)

    def squeeze(self, axis: int | None = None) -> "MAPhv":
        return self.__class__(self.data.squeeze(axis=axis))

    def sign(self) -> "MAPhv":
        return self.__class__(jnp.sign(self.data))
