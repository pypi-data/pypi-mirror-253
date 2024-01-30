
# -- import packages: ---------------------------------------------------------
import ABCParse
import adata_query
import anndata
import numpy as np


# -- Controller class: --------------------------------------------------------
class PerturbationGenes(ABCParse.ABCParse):
    def __init__(
        self,
        obs_key: str = "Cell type annotation",
        obs_val: str = "Undifferentiated",
        q: float = 0.80,
        *args,
        **kwargs,
    ):
        """
        Args:
            obs_key (str): Description.

            obs_val (str): Description.

            q (float): Description. **Default**: 0.80
        
        Returns:
            None
        """
        self.__parse__(locals())

    @property
    def _adata_subset(self):
        """subset adata based on obs"""
        return self._adata[self._adata.obs[self._obs_key] == self._obs_val]

    def _compute_total_counts(self, adata, key: str = "X"):
        """compute total counts"""
        self._X = adata_query.fetch(adata, key=key, torch=False)
        return self._X.sum(0).flatten()

    @property
    def _NON_NEGATIVE(self):
        return not np.any(self._X < 0)

    @property
    def total_counts(self):
        """total counts per gene in progenitor cells (step 1)"""

        if not hasattr(self, "_TOTAL_COUNTS"):
            self._TOTAL_COUNTS = self._compute_total_counts(
                self._adata_subset, key=self._use_rep
            )
        return self._TOTAL_COUNTS

    @property
    def _N_ZERO(self) -> int:
        return sum(self.total_counts == 0)

    @property
    def _N_POS(self) -> int:
        return sum(self.total_counts > 0)

    @property
    def _N_NEG(self) -> int:
        return sum(self.total_counts < 0)

    @property
    def non_neg_total_counts(self):
        if not hasattr(self, "_NN_TOTAL_COUNTS"):
            self._NN_TOTAL_COUNTS = self.total_counts[self.total_counts > 0]
        return self._NN_TOTAL_COUNTS

    @property
    def expr_quantile(self):
        if self._NON_NEGATIVE:
            return np.quantile(self.non_neg_total_counts, self._q)
        return np.quantile(self.total_counts, self._q)

    @property
    def _MASK(self) -> np.ndarray:
        return self.total_counts > self.expr_quantile

    def _update_adata(self) -> None:
        """Add bool vector of selected genes to adata.var and add the list to
        adata.uns[key_added]
        """
        key_added = f"{self._obs_val}_genes"
        
        self._adata.var[key_added] = self._MASK
        self._adata.uns[key_added] = self._adata.var.loc[self._adata.var[key_added]].index.tolist()
        
    def __call__(self, adata, use_rep: str = "X", *args, **kwargs):
        self.__parse__(locals())

        # step 1: isolate progenitor cells and sum total counts per gene
        tc = self.total_counts
        # step 2: compute quantiled expression value cutoff and generate a mask
        eq = self.expr_quantile

        # step 3: add to anndata
        self._update_adata()


# -- API-facing function: -----------------------------------------------------
def annotate_perturbation_target_genes(
    adata: anndata.AnnData,
    obs_key: str,
    obs_val: str,
    q: float = 0.80,
    use_rep: str = "X",
    return_cls: bool = False,
):
    """Annotate the genes expressed at a specified quantile in a subset of cells.
    
    Quantiled expression is computed in the subset of indicated cells and the
    adata object is updated accordingly.
    
    Args:
        adata (anndata.AnnData): Description.

        obs_key (str)

        obs_val (str)

        q (float): Description. **Default**: 0.80

        use_rep (str): Description. **Default**: "X"

        return_cls (bool): Indicate if the controller class should be returned. **Default**: False

    Returns:
        None
    """
    pg = PerturbationGenes(obs_key=obs_key, obs_val=obs_val, q=q)
    pg(adata=adata, use_rep=use_rep)

    if return_cls:
        return pg
