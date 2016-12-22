import re
class Topology(object):
   def __init__(self, info):
       self.info = info
       self.nodes = self.info.keys()
       self.links = []
       self.link_names = []


   def update_topo(self):
       for node in self.info:
           for link in self.info[node]:
               self.add_link(node, link[0], link[1], link[2])

   def check_link_present(self, name):
       return name in self.link_names

   def add_link(self, nodeA, intA, nodeB, intB):
       link = Link(nodeA, intA, nodeB, intB)
       names = link.get_names()
       if self.check_link_present(names[0]) or self.check_link_present(names[1]):
          return
       if nodeB not in self.nodes:
          self.nodes.append(nodeB)
       self.links.append(link)
       self.link_names.extend(names)
       return
       
   def print_info(self):
       msg = ''
       msg += '\n' +'*' * 25
       msg += '\n' +'Nodes are:'+ '\n'.join(self.nodes)
       msg += '\n' +'*' * 25
       msg += '\n' +'links are:'
       msg += '\n' +'*' * 25
       for link in self.links:
           msg += '\n' +link.nodeA + '_'+ link.intA+ '------>'+ link.nodeB+ '_'+ link.intB
       msg += '\n' +'*' * 25
       print msg
       return msg


class Link(object):
   def __init__(self, nodeA, intA, nodeB, intB):
       self.nodeA = nodeA
       self.intA  = intA
       self.nodeB = nodeB
       self.intB  = intB
       
   def get_names(self):
       nameA = '_'.join([self.nodeA, self.intA, self.nodeB, self.intB]) 
       nameB = '_'.join([self.nodeB, self.intB, self.nodeA, self.intA]) 
       return nameA, nameB
