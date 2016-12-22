# topology_diagram_from_lldp_neighbors
Based on a yml file, the script gets lldp neighbors info and then builds a topology diagram automatically
It requires graphvi to be installed ( yum install graphviz) and fabric module to be installed.
In the yml file specify the devices in your setup.
topo_diag.py has default username/password set. Change it to the right username/password. If the devices have different username/password, fabric.api.env has to be populated accordingly.
python topo_diag.py <setup-filename-without-.yml-extension>. if your yml is setup.yml , then run as 'python topo_diag.py setup'
this will create a setup.txt and setup.pdf files. The pdf file is topology diagram while the .txt has information as txt.
