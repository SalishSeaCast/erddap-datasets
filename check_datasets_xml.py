# Copyright 2013 – present by the SalishSeaCast Project contributors
# and The University of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# SPDX-License-Identifier: Apache-2.0


"""Check that datasets described in `datasets.yaml` file are well-formed XML.
"""
import logging
import os
from pathlib import Path

import lxml.etree
import yaml

import structlog

logger = structlog.get_logger()


def main(config_path):
    with config_path.open("rt") as _config:
        config = yaml.safe_load(_config)

    ds_tree = Path(config["datasets tree"])
    ds_descs = [ds_tree/ds_desc for ds_desc in config["datasets"]]
    # ds_descs = [Path("test_datasets.xml")]

    exit_code = 0
    for ds_desc in ds_descs:
        try:
            lxml.etree.parse(ds_desc)
            logger.info("lxml parse", dataset_description=os.fspath(ds_desc), status="ok")
        except lxml.etree.LxmlError as exc:
            exit_code = 2
            logger.info("lxml parse", dataset_description=os.fspath(ds_desc), status="not well-formed XML!")
            logger.exception(exc)
    raise SystemExit(exit_code)


if __name__ == "__main__":
    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(min_level=logging.DEBUG)
    )
    config_path = Path("datasets.yaml")
    main(config_path)
