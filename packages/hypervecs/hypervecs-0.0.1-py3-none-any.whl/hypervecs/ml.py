import jax.numpy as jnp
import equinox as eqx

from hypervecs import MAPhv as hv
import hypervecs as hvx
from hypervecs.embeddings import RFF

from typing import Tuple

__all__ = ["CentroidClf"]


class CentroidClf(eqx.Module):
    encoder: RFF
    centroids: hv
    n: int
    _bw: jnp.ndarray | float

    def __init__(
        self,
        sigma: float | jnp.ndarray,
        n: int,
        in_dim: int,
        nclasses: int = 2,
        dim: int = 2048,
    ):
        super().__init__()

        self.encoder = RFF(in_dim, dim, sigma)
        self.centroids = hv.empty(shape=(nclasses, 2048))
        self._bw = sigma
        self.n = n

    def __call__(self, x: jnp.ndarray) -> Tuple[jnp.ndarray, hv]:
        _x = self.encoder(x)
        _const = (jnp.pi * 2) ** (1 / 2)
        _p_x = _x.sim(self.centroids).squeeze() / (_const * self.n * self._bw)

        return _p_x, _x

    def one_shot(self, x: jnp.ndarray, y: jnp.ndarray) -> "CentroidClf":
        _nc = self.centroids.shape[0]
        data = self.encoder(x)
        labels = y.squeeze()
        updates = [data[labels == lbl].multiset() for lbl in range(_nc)]
        updates = hvx.stack(updates).squeeze()
        new_centers = self.centroids + updates

        def where(m):
            return m.centroids

        new = eqx.tree_at(where, self, new_centers)
        return new

    def itrain(self, x: jnp.ndarray, y: jnp.ndarray) -> "CentroidClf":
        _nc = self.centroids.shape[0]
        scores, x_hv = self(x)
        preds = jnp.argmax(scores, axis=1)

        misclassified_data = x_hv[preds != y]
        misclassified_lbls = y[preds != y]
        wrong_preds = preds[preds != y]

        # adding x to the correct centroids
        updates = [
            misclassified_data[misclassified_lbls == lbl].multiset()
            for lbl in range(_nc)
        ]
        updates = hvx.stack(updates)
        new_centers = self.centroids + updates

        # removing x from the wrong centroids
        updates = [
            misclassified_data[wrong_preds == lbl].multiset() for lbl in range(_nc)
        ]
        updates = hvx.stack(updates)
        new_centers = new_centers - updates

        def where(m):
            return m.centroids

        new = eqx.tree_at(where, self, new_centers)

        return new
