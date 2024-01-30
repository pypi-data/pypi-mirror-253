
# -- import packages: ---------------------------------------------------------
import ABCParse
import numpy as np
import pandas as pd


# -- set typing: --------------------------------------------------------------
from typing import List, Optional, Union


# -- operational class: -------------------------------------------------------
class TargetGenes(ABCParse.ABCParse):
    """GeneLookUp"""

    def __init__(self, *args, **kwargs):
        """ """
        self.__parse__(locals())

    @property
    def _GENE_SET(self) -> pd.Index:
        if not hasattr(self, "_gene_set"):
            if hasattr(self, "_gene_id_key"):
                self._gene_set = self._adata.var[self._gene_id_key]
            else:
                self._gene_set = self._adata.var_names
        return self._gene_set

    @property
    def _GENES(self) -> List:
        return ABCParse.as_list(self._genes)

    def forward(self, gene) -> np.ndarray:
        return np.where(self._GENE_SET == gene)[0][0]

    def __call__(
        self,
        adata,
        genes: Union[List, List[str]],
        gene_id_key: Optional[str] = None,
        *args,
        **kwargs,
    ) -> List[np.ndarray]:

        """Return where (idx) the genes are located in adata.

        Args:
            adata (anndata.AnnData): Description.

            genes (Union[List, List[str]]): Description.
        """
        self.__update__(locals())

        return [self.forward(gene) for gene in self._GENES]
