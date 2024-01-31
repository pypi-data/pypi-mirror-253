import jax
import jax.numpy as jnp
import equinox as eqx

from hypervecs import MAPhv as hv

from loguru import logger


class RFF(eqx.Module):
    proj: jnp.ndarray
    bias: jnp.ndarray
    quantize: bool
    bandwidth: jnp.ndarray | float

    def __init__(
        self,
        in_dim: int,
        dim: int,
        bandwidth: jnp.ndarray | float = 1.0,
        key: jnp.ndarray = jax.random.PRNGKey(0),
        quantize: bool = False,
        **kwargs,
    ):
        super().__init__()

        self.quantize = quantize
        _key1, _key2 = jax.random.split(key)
        _mu = jnp.zeros(in_dim)

        if isinstance(bandwidth, float) or not hasattr(bandwidth, "__len__"):
            _bandwidth = bandwidth * jnp.eye(in_dim)
        elif bandwidth.shape == (in_dim,):
            _bandwidth = jnp.diag(bandwidth)
        else:
            _bandwidth = bandwidth

        logger.debug(f"Bandwidth: {_bandwidth} | shape {_bandwidth.shape}")
        self.bandwidth = _bandwidth
        _w = kwargs.get("proj", None)
        _b = kwargs.get("bias", None)

        if _w is None:
            # reparameterization trick
            _noise_cov = jnp.eye(in_dim)
            _noise = jax.random.multivariate_normal(
                _key1, jnp.zeros(in_dim), _noise_cov, shape=(dim,)
            )
            # _ncov = jnp.linalg.cholesky(_cov)

            _cov = in_dim / (_bandwidth**2)

            inf_mask = jnp.isinf(_cov)
            _cov = jnp.where(inf_mask, 0.0, _cov)

            logger.debug(f"w | Cov: {_cov} | shape {_cov.shape}")
            _sigma = jnp.sqrt(_cov) * jnp.eye(in_dim)
            logger.debug(f"w | Sigma: {_sigma} | shape {_sigma.shape}")

            _w = (_mu + _noise @ _sigma).T

        if _b is None:
            _b = jax.random.uniform(_key2, shape=(dim,), minval=0, maxval=2 * jnp.pi)

        logger.debug(f"RFF: w:{_w.shape} b: {_b.shape}")
        self.proj = _w
        self.bias = _b

    @jax.jit
    def _ufunc(self, x):
        # _proj = (x / (2 * self.bandwidth)) @ self.proj + self.bias
        _proj = x @ self.proj + self.bias
        _proj = jnp.cos(_proj) * jnp.sqrt(2 / self.proj.shape[-1])

        return _proj

    def __call__(self, x: jnp.ndarray) -> hv:
        if self.quantize:
            return hv(jnp.sign(self._ufunc(x)))

        return hv(self._ufunc(x))
