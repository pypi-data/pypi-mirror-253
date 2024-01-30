
# -- import packages: ---------------------------------------------------------
import ABCParse
import numpy as np
import pandas as pd
import anndata
import adata_query


# -- set typing: --------------------------------------------------------------
from typing import Any, Dict


# -- operational class: -------------------------------------------------------
class TargetCells(ABCParse.ABCParse):
    """Currently written in the context of initial (t0) cells"""
    def __init__(
        self,
        subset_key: str,
        subset_val: Any,
        seed: int = 0,
        *args,
        **kwargs,
    ):
        """
        Args:
            seed (int): description. **Default** = 0.
            
            subset_key (str): description.
            
            subset_val (float): description.
            
        Returns:
            None
        """
        self.__parse__(locals())

        np.random.seed(self._seed)

        self._SampleIndices = {}

    @property
    def _cell_subset(self) -> pd.DataFrame:
        """ """
        return self._adata.obs.loc[self._adata.obs[self._subset_key] == self._subset_val]

    @property
    def sample_idx(self) -> pd.Index:
        """ """
        return self._cell_subset.sample(self._N).index

    def forward(self, i: int) -> np.ndarray:
        """ """
        idx = self.sample_idx
        self._SampleIndices[i] = idx
        return adata_query.fetch(self._adata[idx], key=self._use_key, torch=False)

    def __call__(
        self,
        adata: anndata.AnnData,
        replicates: int = 5,
        use_key: str = "X_scaled",
        N: int = 200,
        *args,
        **kwargs,
    ) -> Dict[int, np.ndarray]:
        
        """
        Args:
            adata (anndata.AnnData): description.
            
            replicates (int): description. **Default**: 5.
            
            use_key (str): description. **Default**: "X_scaled".
            
            N (int): description. **Default**: 200.
            
        Returns:
            TargetCellDict (Dict[int, np.ndarray]): keys: replicates,
            values: array of cell values.
        """
        self.__update__(locals())

        self._TargetCellDict = {i: self.forward(i) for i in range(replicates)}
        
        return {"idx": self._SampleIndices, "X_target": self._TargetCellDict}
        