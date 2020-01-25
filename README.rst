*************************************
Salish Sea NEMO Model ERDDAP Datasets
*************************************

This repo contains the ``datasets.xml`` file that provides the dataset descriptions for the Salish Sea NEMO Model ERDDAP server at https://salishsea.eos.ubc.ca/erddap/.

Also in the repo are files,
chiefly a Jupyter notebook,
used to maintain the ``datasets.xml`` file,
and notes in this file about maintenance of the datasets file and the ERDDAP server.


`ERDDAP_datasets.ipynb`_
========================

.. _ERDDAP_datasets.ipynb: https://nbviewer.jupyter.org/github/SalishSeaCast/erddap-datasets/blob/master/ERDDAP_datasets.ipynb

**Building ERDDAP Datasets**

This notebook documents the process of creating XML fragments for nowcast system run results files for inclusion in ``/results/erddap-datasets/datasets.xml`` which is symlinked to ``/opt/tomcat/content/erddap/datasets.xml`` on the ``skookum`` ERDDAP server instance.

The contents are a combination of:

* instructions for using the ``GenerateDatasetsXml.sh`` tool found in the ``/opt/tomcat/webapps/erddap/WEB-INF/`` directory
* code and metadata to transform the output of ``GenerateDatasetsXml.sh`` into XML fragments that are ready for inclusion in ``/results/erddap-datasets/datasets.xml``
* instructions for forcing the server to update the datasets collection via the ``/results/erddap/flags/`` directory


`WWatch3_datasets.ipynb`_
=========================

.. _WWatch3_datasets.ipynb: https://nbviewer.jupyter.org/github/SalishSeaCast/erddap-datasets/blob/master/WWatch3_datasets.ipynb

**Building WaveWatch3®(TM) ERDDAP Datasets**

This notebook documents the process of creating XML fragments for SalishSeaCast rolling forecast WaveWatch3® run results files for inclusion in /results/erddap-datasets/datasets.xml which is symlinked to /opt/tomcat/content/erddap/datasets.xml on the skookum ERDDAP server instance.

The contents are a combination of:

    instructions for using the GenerateDatasetsXml.sh and DasDds.sh tools found in the /opt/tomcat/webapps/erddap/WEB-INF/ directory
    instructions for forcing the server to update the datasets collection via the /results/erddap/flags/ directory
    code and metadata to transform the output of GenerateDatasetsXml.sh into XML fragments that are ready for inclusion in /results/erddap-datasets/datasets.xml


License
=======

The Salish Sea NEMO model nowcast system code and documentation are copyright 2013-2020 by the `Salish Sea MEOPAR Project Contributors`_ and The University of British Columbia.

.. _Salish Sea MEOPAR Project Contributors: https://bitbucket.org/salishsea/docs/src/tip/CONTRIBUTORS.rst

They are licensed under the Apache License, Version 2.0.
http://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file for details of the license.
