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


"""Build ERDDAP `datasets.xml` file described in `datasets.yaml` file.
"""
from pathlib import Path

import yaml


def main(config_path, datasets_xml):
    with config_path.open("rt") as _config:
        config = yaml.safe_load(_config)

    ds_tree = Path(config["datasets tree"])
    prefix = ds_tree / config["prefix"]
    postfix = ds_tree / config["postfix"]
    ds_descs = [ds_tree/ds_desc for ds_desc in config["datasets"]]

    with datasets_xml.open("wt") as _datasets_xml:
        _write_section(prefix, _datasets_xml)
        for ds_desc in ds_descs:
            _write_section(ds_desc, _datasets_xml)
        _write_section(postfix, _datasets_xml, end="")

def _write_section(section, _datasets_xml, end="\n"):
    with section.open("rt") as _section:
        _datasets_xml.write(_section.read())
    _datasets_xml.write(end)


if __name__ == "__main__":
    config_path = Path("datasets.yaml")
    datasets_xml = Path("test_datasets.xml")
    main(config_path, datasets_xml)
