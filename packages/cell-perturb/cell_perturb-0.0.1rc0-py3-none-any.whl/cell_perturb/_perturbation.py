
# -- import packages: -----------------------------------
import ABCParse
import sklearn.decomposition
import anndata
import numpy as np

# -- import local dependencies: -------------------------
from ._target_cells import TargetCells
from ._target_genes import TargetGenes

# -- set typing: ----------------------------------------
from typing import Any, Dict, List, Optional, Union


# -- operational class: ---------------------------------
class Perturbation(ABCParse.ABCParse):
    """Manipulate gene values in cells"""

    def __init__(
        self,
        use_key: str = "X_scaled",
        replicates: int = 5,
        N: int = 200,
        seed: int = 0,
        *args,
        **kwargs,
    ):
        """"""
        self.__parse__(locals())

    @property
    def target_cells(self):
        if not hasattr(self, "_target_cells"):
            self._target_cells = TargetCells(
                subset_key=self._subset_key,
                subset_val=self._subset_val,
                seed=self._seed,
            )
        return self._target_cells(
            adata=self._adata,
            replicates=self._replicates,
            use_key=self._use_key,
            N=self._N,
        )

    @property
    def target_genes(self):
        if not hasattr(self, "_target_genes"):
            self._target_genes = TargetGenes()
        return self._target_genes(
            adata=self._adata, genes=self._genes, gene_id_key=self._gene_id_key
        )

    def _format_adata_prtb(self, X_ctrl, X_prtb, idx):

        adata_prtb = anndata.AnnData(
            X_prtb,
            layers={"X_ctrl": X_ctrl},
            obs=self._adata[idx].obs,
        )
        adata_prtb.var_names = self._adata.var_names
        adata_prtb.obs = adata_prtb.obs.reset_index().rename(
            {"index": "obs_idx"}, axis=1
        )

        return adata_prtb

    def _annotate_perturbed_genes(self, adata_prtb):
        adata_prtb.var["prtb"] = adata_prtb.var_names.isin(
            adata_prtb.uns["target_genes"]["genes"]
        )
        adata_prtb.var["prtb_zscore"] = adata_prtb.X.mean(0)
        adata_prtb.var["ctrl_zscore"] = adata_prtb.layers["X_ctrl"].mean(0)
        return adata_prtb

    def _compile_adata_prtb_over_replicates(self, PerturbedAnnDataObjects: Dict):

        adata_prtb = anndata.concat(list(PerturbedAnnDataObjects.values()))
        adata_prtb.obs = adata_prtb.obs.reset_index(drop=True)
        adata_prtb.uns["target_genes"] = dict(
            genes=self._genes, gene_indices=self.target_genes
        )
        adata_prtb.obs.index = adata_prtb.obs.index.astype(str)
        adata_prtb.var.index = adata_prtb.var.index.astype(str)
        adata_prtb.uns["seed"] = self._seed
        adata_prtb.uns["N"] = self._N
        return self._annotate_perturbed_genes(adata_prtb)

    def forward(self) -> anndata.AnnData:
        """Impart perturbations to target cells/genes for each replicate and
        assemble into AnnData.
        Returns:
            adata_prtb (anndata.AnnData)
                Compiled (over each replicate) AnnData object containing
                perturbed and control states.
        """
        PerturbedAnnDataObjects = {}
        # make perturbation

        for replicate, X_target in self.target_cells["X_target"].items():
            X_ctrl = X_target.copy()
            X_prtb = X_target.copy()
            X_prtb[:, self.target_genes] = self._target_value
            adata_prtb = self._format_adata_prtb(
                X_ctrl, X_prtb, self.target_cells["idx"][replicate]
            )
            adata_prtb.obs["replicate"] = replicate
            if hasattr(self, "_PCA"):

                adata_prtb.obsm["X_pca_prtb"] = self._PCA.transform(adata_prtb.X)
                adata_prtb.obsm["X_pca_ctrl"] = (
                    self._adata[self._target_cells.sample_idx].obsm["X_pca"].toarray()
                )
            adata_prtb.obs.index = f"rep{replicate}." + adata_prtb.obs.index.astype(
                "str"
            )
            PerturbedAnnDataObjects[replicate] = adata_prtb

        adata_prtb = self._compile_adata_prtb_over_replicates(PerturbedAnnDataObjects)
        self._check_output(adata_prtb)
        return adata_prtb

    def _check_output(self, adata_prtb):
        """Ensure all perturbed values match the target value"""
        assert np.all(
            adata_prtb.X[:, self.target_genes] == self._target_value
        ), "Not all cells/genes mutated properly."

    def __call__(
        self,
        adata: anndata.AnnData,
        subset_key: str,
        subset_val: Any,
        genes: Union[List, List[str]],
        target_value: float,
        gene_id_key: Optional[str] = None,
        use_key: str = "X_scaled",
        PCA: Optional[sklearn.decomposition.PCA] = None,
        *args,
        **kwargs,
    ) -> anndata.AnnData:

        """
        Impart perturbations and format accordingly as AnnData.

        Args:
            adata (anndata.AnnData)
                Description.

            subset_key (str)
                Description.

            subset_val (Any)
                Description.

            genes: Union[List, List[str]]
                Description.

            target_value: float
                Description.

            gene_id_key: Optional[str] = None
                Description.

            use_key: str = "X_scaled"
                Description.

            PCA: Optional[sklearn.decomposition.PCA] = None
                Description.


        Returns:
            adata_prtb (anndata.AnnData).
            Has ctrl cells built-in.
        """

        self.__update__(locals())
        self._gene_id_key = gene_id_key

        return self.forward()
