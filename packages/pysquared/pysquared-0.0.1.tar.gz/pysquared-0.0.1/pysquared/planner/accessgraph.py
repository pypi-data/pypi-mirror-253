import networkx as nx
import pandas as pd

from ..utils import get_logger_shortcuts

class AccessGraph:
    def __init__(self, inp_g, node_set, logger=None):
        self.log = get_logger_shortcuts(logger)

        self.g = nx.DiGraph()
        self.g.add_nodes_from(node_set)
        for nodeA, nodeB in inp_g.edges:
            if nodeA in node_set and nodeB in node_set:
                self.g.add_edge(nodeA, nodeB)
        self.log.debug(f"AccessGraph nodes = {repr(list(self.g.nodes))}")
        self.log.debug(f"AccessGraph edges = {repr(list(self.g.edges))}")
        
        for node in self.g.nodes:
            self.g.nodes[node]['is_item'] = inp_g.nodes[node]['is_item']
            if self.g.nodes[node]['is_item']:
                if 'item' in inp_g.nodes[node] and inp_g.nodes[node]['item'].non_empty:
                    self.g.nodes[node]['known'] = True
                    self.g.nodes[node]['active'] = True
                    self.log.debug(f"Node '{node}' is known")
                else:
                    self.g.nodes[node]['known'] = False
                    self.g.nodes[node]['active'] = False
                    self.log.debug(f"Node '{node}' is not known")
            else:
                self.g.nodes[node]['active'] = False
        
        self.log.debug("Before propagation:\n" + self.get_state())
        converged = False
        while not converged:
            converged = True
            for node in self.g.nodes:
                if not self.g.nodes[node]['is_item']:
                    all_inputs_active = True
                    for nb in self.g.predecessors(node):
                        all_inputs_active = all_inputs_active and self.g.nodes[nb]['active']
                    
                    if not self.g.nodes[node]['active'] and all_inputs_active:
                        self.g.nodes[node]['active'] = True
                        converged = False
                    elif self.g.nodes[node]['active'] and not all_inputs_active:
                        self.g.nodes[node]['active'] = False
                        converged = False
                
            for node in self.g.nodes:
                if self.g.nodes[node]['is_item']:
                    some_source_is_active = False
                    for nb in self.g.predecessors(node):
                        some_source_is_active = some_source_is_active or self.g.nodes[nb]['active']

                    if not self.g.nodes[node]['active'] and some_source_is_active:
                        self.g.nodes[node]['active'] = True
                        converged = False
        self.log.debug("After propagation:\n" + self.get_state())
    
    def paths_iterate(self, target):
        prospects = [[node] for node in self.g.predecessors(target) if self.g.nodes[node]['active']]
        while len(prospects) > 0:
            cur_prospect = prospects.pop()
            loose_ends = []
            all_ends = []

            incorrect_prospect = False
            for node in self.g.nodes:
                required = False
                employing_tr_idxs = []
                for employing_transform in self.g.successors(node):
                    if employing_transform in cur_prospect:
                        employing_tr_idxs.append(cur_prospect.index(employing_transform))
                        required = True
                
                if not required:
                    continue
                
                n_formed = 0
                forming_idxs = []
                for forming_transform in self.g.predecessors(node):
                    if forming_transform in cur_prospect:
                        n_formed += 1
                        forming_idxs.append(cur_prospect.index(forming_transform))
                if n_formed > 1:
                    incorrect_prospect = True
                elif n_formed == 1:
                    forming_idx = forming_idxs[0]
                    for employing_tr_idx in employing_tr_idxs:
                        if employing_tr_idx > forming_idx:
                            incorrect_prospect = True
                            break
                else:
                    all_ends.append(node)
                    if not self.g.nodes[node]['known']:
                        loose_ends.append(node)
                
                if incorrect_prospect:
                    break
            
            if incorrect_prospect:
                cur_prospect.reverse()
                self.log.warning(f"Incorrect prospect was encountered and ignored: {repr(cur_prospect)}")
                continue 

            if len(loose_ends) == 0: # Yield a final and checked sequence
                ret_list = list(reversed(cur_prospect))
                yield ret_list
            
            # Look for prospects if there are loose ends
            for item_node in all_ends:
                for next_transorm in self.g.predecessors(item_node):
                    if not self.g.nodes[next_transorm]['active']:
                    #     or next_transorm in cur_prospect:
                        continue
                    new_prospect = [*cur_prospect, next_transorm]
                    if new_prospect not in prospects:
                        prospects.append(new_prospect)
        
    def get_state(self):
        data = []
        for node in self.g.nodes:
            data.append({**{'node': node}, **{key: value for key, value in self.g.nodes[node].items()}})
        df = pd.DataFrame(data)
        return repr(df[df['is_item']])
    
    def get_all_ends(self, seq):
        seq = list(reversed(seq))
        all_ends = []

        for node in self.g.nodes:
            required = False
            employing_tr_idxs = []
            for employing_transform in self.g.successors(node):
                if employing_transform in seq:
                    employing_tr_idxs.append(seq.index(employing_transform))
                    required = True
            
            if not required:
                continue
            
            n_formed = 0
            forming_idxs = []
            for forming_transform in self.g.predecessors(node):
                if forming_transform in seq:
                    n_formed += 1
                    forming_idxs.append(seq.index(forming_transform))
            
            # Skipped some checks here
            
            if n_formed == 0:
                all_ends.append(node)
        return all_ends
