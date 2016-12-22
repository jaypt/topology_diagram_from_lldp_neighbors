
main_template='''
graph topology {
    rankdir=LR;
%s
%s
}
'''

node_template = '    "{node}" [label="{node}"];\n'
link_template = '    "{nodeA}" -- "{nodeB}" [label="{intA} {intB}"];\n'

def dot_info(topo):
    nodes = [node_template.format(node=x) for x in topo.nodes]
    links = [link_template.format(nodeA=x.nodeA, intA=x.intA, 
             nodeB=x.nodeB, intB=x.intB) for x in topo.links]
    nodes = ''.join(nodes)
    links = ''.join(links)
    return main_template%(nodes, links)

