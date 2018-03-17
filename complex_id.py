from Bio.PDB.Structure import Structure
from Bio.PDB.Model import Model

class Node(object):

    def __init__(self, chain_type, chain, complex_id,pos):
        self.chain = chain
        self.interaction_list = complex_id.get_all_interactions_of_chain(self.chain_type)
        self.chain_type = chain_type
        self.pos = pos

    def add_interaction(self, node,interaction):

             self.interaction_list[interaction] = node

    def get_chain_type(self):
        return self.chain_type




def get_nodes_from_structure(structure):
    return []

def compare_complex_ids(complex1, complex2):
    pass



def pop_structure(structure, complex_id):
    pass

class ComplexId(object):

    def __init__(self, structure,interaction_dict,id_dict):
        self.nodes = get_nodes_from_structure(structure)
        self.id_dict = id_dict
        self.interaction_dict = interaction_dict

    def get_all_interactions_of_chain(self,chain_type):

        interaction_list = {}

        for pair in [pair for pair in self.interaction_dict if chain_type in pair]:
            for interaction in self.interaction_dict[pair]:
                interaction_list[interaction] = None

        return interaction_list

    def add_node(self, interaction, chain, node = None):

        if self.id_dict[interaction[0]] == self.id_dict[interaction[1]]:
            chain_type = self.id_dict[interaction[0]]
        else:
            chain_type = [self.id_dict[chain] for chain in interaction if self.id_dict[node.chain] != self.id_dict[chain]]

        new_node = Node(chain_type, chain,self,len(self.nodes))

        new_node.add_interaction(node,interaction)

        self.nodes.append(new_node)

        node.add_interaction(new_node,interaction)

    def get_nodes(self):
        return self.nodes

    def get_id_dict(self):
        return self.id_dict

    def get_interaction_dict(self):
        return self.interaction_dict


if __name__ == '__main__':
    pass