*****************************
SalishSeaCast ERDDAP Datasets
*****************************

This repo contains files related to the configuration and maintenance of the SalishSeaCast
ERDDAP server at https://salishsea.eos.ubc.ca/erddap/.

The key configuration files are:

* ``datasets.xml`` that defines the collection of datasets that the ERDDAP instance serves
* ``setup.xml`` that includes the HTML for the server landing page that provides information
  about the SalishSeaCast ERDDAP server as well as about ERDDAP in general

Also in the repo are:

* the collection of XML fragments for each dataset that are composed to create ``datasets.xml``
* Python scripts to check that the XML fragments are well-formed,
  and to build ``datasets.xml`` from the dataset description fragments
* Jupyter notebooks that are used to generate and maintain the dataset description fragments
* conda environment description YAML files to build conda environment in which the above code 
  can be executed


Python Scripts
==============

``check_datasets_xml.py``
-------------------------

Script that checks that the datasets described in ``datasets.yaml`` file are well-formed XML.
Execution::

  conda activate erddap-datasets-dev
  python -m check_datasets_xml

The ``check_datasets_xml.py`` is run by a `GitHub Action`_ whenever changes are pushed to the repo
on GitHub.
The results of those runs are at
https://github.com/SalishSeaCast/erddap-datasets/actions/workflows/check-datasets-xml.yaml

.. _GitHub Action: https://github.com/SalishSeaCast/erddap-datasets/blob/main/.github/workflows/check-datasets-xml.yaml


``build_datasets_xml.py``
-------------------------

Script that builds the ERDDAP ``datasets.xml`` file described in the ``datasets.yaml`` file.
Execution::

  conda activate erddap-datasets-dev
  python -m build_datasets_xml


Jupyter Notebooks
=================

`ERDDAP_datasets.ipynb`_
-------------------------

.. _ERDDAP_datasets.ipynb: https://nbviewer.org/github/SalishSeaCast/erddap-datasets/blob/main/ERDDAP_datasets.ipynb

**Building ERDDAP Datasets**

This notebook documents the process of creating XML fragments for nowcast system
run results files for inclusion in ``/results/erddap-datasets/datasets.xml``
which is symlinked to ``/opt/tomcat/content/erddap/datasets.xml`` on the
``skookum`` ERDDAP server instance.

The contents are a combination of:

* instructions for using the ``GenerateDatasetsXml.sh`` tool found in the
  ``/opt/tomcat/webapps/erddap/WEB-INF/`` directory
* code and metadata to transform the output of ``GenerateDatasetsXml.sh`` into XML fragments
  that are ready for inclusion in ``/results/erddap-datasets/datasets.xml``
* instructions for forcing the server to update the datasets collection via the
  ``/results/erddap/flags/`` directory


`WWatch3_datasets.ipynb`_
-------------------------

.. _WWatch3_datasets.ipynb: https://nbviewer.org/github/SalishSeaCast/erddap-datasets/blob/main/WWatch3_datasets.ipynb

**Building WaveWatch3®(TM) ERDDAP Datasets**

This notebook documents the process of creating XML fragments for SalishSeaCast
rolling forecast WaveWatch3® run results files for inclusion in
/results/erddap-datasets/datasets.xml which is symlinked to /opt/tomcat/content/erddap/datasets.xml
on the skookum ERDDAP server instance.

The contents are a combination of:

    * instructions for using the GenerateDatasetsXml.sh and DasDds.sh tools found in the
      /opt/tomcat/webapps/erddap/WEB-INF/ directory
    * instructions for forcing the server to update the datasets collection via the
      /results/erddap/flags/ directory
    * code and metadata to transform the output of GenerateDatasetsXml.sh into XML fragments
      that are ready for inclusion in /results/erddap-datasets/datasets.xml


License
=======

The SalishSeaCast ocean model automation system code and documentation  are copyright 2013 – present
by the `SalishSeaCast Project Contributors`_ and The University of British Columbia.

.. _SalishSeaCast Project Contributors: https://github.com/SalishSeaCast/docs/blob/main/CONTRIBUTORS.rst

They are licensed under the Apache License, Version 2.0.
http://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file for details of the license.
