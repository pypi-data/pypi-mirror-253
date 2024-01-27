import os
import numpy as np
import pandas as pd
import h5py
import anndata
import anndata.utils
from scipy.sparse import csr_matrix

def sample_reads(x, n, seed=0):
    """
    Subsample counts.
    
    Example:
    # data looks like
    x = [1, 2, 3, 1]
    total_counts = 7
    
    # draw 4 counts
    sample_indices = [0, 1, 0, 1, 1, 0, 1]  # length 7, keep 1s, drop 0s
    
    # get indices
    count_indices = [0, 1, 1, 2, 2, 2, 3]  # length 7, used for grouping
    
    # group by indices and sum
    sample_counts = [0, 1, 2, 1]
    """
    assert n < x.sum(), f"n ({n}) must be smaller than total counts ({x.sum()})"
    np.random.seed(seed)
    total_count = x.sum()
    sample_indices = np.random.binomial(1, n / total_count, total_count)
    count_indices = np.repeat(np.arange(len(x)), x)
    sample_counts = np.bincount(count_indices, weights=sample_indices).astype("int32")
    return sample_counts

class MoleculeInfo:
    """
    Class to represent, manipulate, filter and summarise molecule info.
    """
    
    def __init__(self, path, v=1):
        self.path = path
        self.v = v
        self.is_sampled = False
        self._load()
        if v > 0:
            print(self.__str__())
    
    def __len__(self):
        return len(self.umi[self.count > 0])

    def __str__(self):
        return f"MoleculeInfo: {len(self)} UMIs | {len(self.feature_names)} features"
    
    def __repr__(self):
        return f"MoleculeInfo: {len(self)} UMIs | {len(self.feature_names)} features"
    
    def _load(self):
        with h5py.File(self.path, "r") as h5:
            self.umi = h5["umi"][()]
            self.count = h5["count"][()]
            self.count_raw = self.count.copy()  # count can be overwritten by sample()
            self.barcode_idx = h5["barcode_idx"][()]
            self.feature_idx = h5["feature_idx"][()]
            self.barcodes = h5["barcodes"][()]
            self.feature_names = h5["features"]["name"][()]
            self.feature_names = np.char.upper(self.feature_names.astype(str))
            self.feature_names = anndata.utils.make_index_unique(pd.Index(self.feature_names))

    def _get_counts(self):
        """Return a cell x gene matrix with unique UMI counts for each cell and features"""
        # filter data
        filter_ids = self.count > 0
        barcode_idx = self.barcode_idx[filter_ids]
        feature_idx = self.feature_idx[filter_ids]
        
        # get unique counts
        combined = np.column_stack((barcode_idx, feature_idx))
        coordinates, counts = np.unique(combined, axis=0, return_counts=True)
        csr_counts = csr_matrix((counts, (coordinates[:, 0], coordinates[:, 1])))
        return csr_counts

    def sample_reads(self, n, seed=0):
        """Subsample counts"""
        self.count = sample_reads(self.count_raw, n, seed=seed)
        self.is_sampled = True
    
    def reset(self):
        """Reset counts to original"""
        self.count = self.count_raw
        self.is_sampled = False
    
    def summary_barcodes(self):
        """Summarise barcodes"""
        
        # TODO: filter features?
        
        # filter
        filter_ids = self.count > 0
        count = self.count[filter_ids]
        barcode_idx = self.barcode_idx[filter_ids]
        feature_idx = self.feature_idx[filter_ids]
        barcodes = self.barcodes[barcode_idx]

        # aggregate
        if self.v > 0:
            print(f"Aggregating {len(barcodes)} barcodes...")
        df_raw = pd.DataFrame({
            "counts": count,
            "barcodes": barcodes,
            "feature_idx": feature_idx,
        })
        df_agg = df_raw.groupby("barcodes").agg(
            umis=("counts", len),
            counts=("counts", "sum"),
            features=("feature_idx", "nunique")
        )
        return df_agg
    
    def to_adata(self, add_dash_1=True):
        """Convert to adata. Calculates unique counts."""
        
        # get counts
        counts = self._get_counts()
        
        # filter barcodes (index cannot be higher than counts dimension)
        barcodes = self.barcodes[:counts.shape[0]]
        feature_names = self.feature_names[:counts.shape[1]]
        
        # convert to adata
        adata = anndata.AnnData(
            X=counts,
            obs=pd.DataFrame(index=barcodes),
            var=pd.DataFrame(index=feature_names)
        )
        if add_dash_1:
            adata.obs_names = adata.obs_names + "-1"
        return adata
            
