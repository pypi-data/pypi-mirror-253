from chemscripts.mylogging import createLogger

class AnyPathSelector:
    def select(seqs, logger=None, **attrs):
        if len(seqs) > 0:
            if logger is None:
                logger = createLogger("ShortestPath")
            if len(seqs) > 1:
                logger.warning("Choosing arbitrary valid route")
            return [seqs[0]]
        else:
            return []


class ShortestPathSelector:
    def select(seqs, g, ag, logger=None, **attrs):
        if logger is None:
            logger = createLogger("ShortestPath")
        logger.info("ENTER")
        unique_seqs = []
        def is_extention(a, b): # Checks if 'a' is extension of 'b'
            if len(a) <= len(b):
                return False
            for itemA in a:
                if itemA not in b:
                    return False
            return True
            # b_idx = len(b) - 1
            # for itemA in reversed(a[len(a)-len(b):]):
            #     if b[b_idx] != itemA:
            #         return False
            #     b_idx -= 1
            # return True

        # print(repr(seqs))

        min_length = None
        for path in seqs:
            if min_length is None or min_length > len(path):
                min_path = path
                min_length = len(path)
            # logger.info(f"Processing {repr(path)}")
            # delete_idxs = []
            # match = False

            # for trial_i, trial_path in enumerate(unique_seqs):
            #     if is_extention(path, trial_path):
            #         print("MATCH")
            #         match=True
            #     elif is_extention(trial_path, path):
            #         delete_idxs.append(trial_i)
            
            # if not match:
            #     unique_seqs.append(path)
            #     logger.info(f"Added {path}")
            
            # delete_idxs.sort(reverse=True)
            # for idx in delete_idxs:
            #     logger.info(f"Removed {unique_seqs[idx]}")
            #     del unique_seqs[idx]
        return [min_path]


class ChooseSourcesPathSelector:
    def __init__(self, sources, strict=True):
        self.sources = sources
        self.strict = strict
    
    def select(self, seqs, g, ag, logger=None, **attrs):
        if logger is None:
            logger = createLogger("ChosenSources")
        
        chosen_paths = []
        for path in seqs:
            # logger.debug(f"------ Processing path {repr(path)} -------")
            all_ends = ag.get_all_ends(path)
            # logger.debug(f"All ends = {repr(all_ends)}")
            # logger.debug(f"Sources = {repr(self.sources)}")
            if self.strict and set(all_ends) == set(self.sources):
                # logger.debug(f"Route '{repr(path)}' is accepted (strict)")
                chosen_paths.append(path)
            elif not self.strict:
                includes = True
                for item in self.sources:
                    if item not in all_ends:
                        # logger.debug(f"Route '{repr(path)}' is discarded")
                        includes = False
                        break
                if includes:
                    chosen_paths.append(path)
        return chosen_paths