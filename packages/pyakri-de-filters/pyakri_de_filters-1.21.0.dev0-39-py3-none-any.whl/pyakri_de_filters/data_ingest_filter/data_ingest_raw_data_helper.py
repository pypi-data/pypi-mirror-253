import os
import tempfile

from pyakri_de_filters.data_ingest_filter.data_ingest_filter_wrapper import (
    DataIngestWrapper,
)

params_list = [
    "num_components",
    "fraction_rows",
    "fraction_coreset",
    "overwrite",
    "coreset_mode",
    "feature_n",
    "feature_m",
    "feature_f",
    "text_search",
]


def get_init_params():
    init_params = dict()
    for param in params_list:
        if param in os.environ:
            init_params[param] = os.environ[param]
    return init_params


def run_data_ingest_filter(input_dir, output_dir):
    with tempfile.NamedTemporaryFile() as fp:
        data_ingest_wrapper = DataIngestWrapper()
        data_ingest_wrapper.init(**get_init_params())

        data_ingest_wrapper.run(src_dir=input_dir, dst_dir=output_dir, tmp_file=fp.name)

        data_ingest_wrapper.cleanup()