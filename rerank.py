import torch

from typing import List

from config import args
from triplet import EntityDict
from dict_hub import get_link_graph
from doc import Example


def rerank_by_graph(batch_score: torch.tensor,
                    examples: List[Example],
                    entity_dict: EntityDict):

    for idx in range(batch_score.size(0)):
        cur_ex = examples[idx]
        n_hop_indices = get_link_graph().get_n_hop_entity_indices(cur_ex.head_id,
                                                                  entity_dict=entity_dict,
                                                                  n_hop=args.rerank_n_hop)
        delta = torch.tensor([args.neighbor_weight for _ in n_hop_indices]).to(batch_score.device)
        n_hop_indices = torch.LongTensor(list(n_hop_indices)).to(batch_score.device)

        batch_score[idx].index_add_(0, n_hop_indices, delta)


        if args.task == 'FB15k237':
            n_hop_indices = get_link_graph().get_n_hop_entity_indices(cur_ex.head_id,
                                                                      entity_dict=entity_dict,
                                                                      n_hop=1)
            n_hop_indices.remove(entity_dict.entity_to_idx(cur_ex.head_id))
            delta = torch.tensor([-0.5 for _ in n_hop_indices]).to(batch_score.device)
            n_hop_indices = torch.LongTensor(list(n_hop_indices)).to(batch_score.device)
        
            batch_score[idx].index_add_(0, n_hop_indices, delta)
