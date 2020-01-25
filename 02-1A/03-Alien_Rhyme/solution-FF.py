#!/usr/bin/env python3
class Node:
    def __init__(self, name):
        self._name = name
        self._chdr = {}
        self._tot_cnt = 0

    def get_name(self):
        return self._name

    def get_chdr(self):
        return self._chdr

    # Add a single child
    def add_chd(self, child):
        lttr = child._name
        if lttr in self._chdr:
            raise ValueError('E: add, chdr exists')
        self._chdr[lttr] = child
        self._tot_cnt += 1

    def del_chd(self, lttr):
        if lttr not in self._chdr:
            raise ValueError('E: del, no chdr')
        del self._chdr[lttr]
        self._tot_cnt -= 1

    # This cnt also supposed add all chdr's chdr's ... chdr
    def get_tot_cnt(self):
        return self._tot_cnt

    def add_tot_cnt(self, lttr):
        if lttr not in self._chdr:
            raise ValueError('E: add, no chdr')
        self._tot_cnt += 1

    def sub_tot_cnt(self, lttr):
        if lttr not in self._chdr:
            raise ValueError('E: sub, no chdr')
        self._tot_cnt -= 1

    def get_max_tot_cnt_lttr(self):
        dic = {lttr: node.get_tot_cnt()
               for lttr, node in self._chdr.items()}
        max_tot_cnt = max(dic.values())
        for lttr, cnt in dic.items():
            if cnt == max_tot_cnt:
                return (max_tot_cnt, lttr)

    def get_cnt(self):
        return len(self._chdr)


# Actually the top node
class Tree(Node):
    def __init__(self):
        super().__init__('top')

    # Add a not-reversed word to tree
    def add_word(self, word):
        # Duplicates
        cur_node = self
        word_rev = word[::-1]
        new_brch = False
        print(word)
        for i in range(len(word)):
            lttr = word_rev[i]
            cur_chdr = cur_node.get_chdr()
            if lttr in cur_chdr:
                cur_node.add_tot_cnt(lttr)
                cur_node = cur_chdr[lttr]
            else:
                new_brch = True
                j = len(word) - i
                break
        # New branch
        if new_brch:
            base_node = Node(word[0])
            for lttr in word[1:j]:
                new_node = Node(lttr)
                new_node.add_chd(base_node)
                base_node = new_node
            cur_node.add_chd(base_node)

    # def del_word(self, word):
    #     # Duplicates
    #     dup_nodes = []
    #     cur_node = self
    #     word_rev = word[::-1]
    #     for i in len(word):
    #         lttr = word_rev[i]
    #         cur_chdr = cur_node.get_chdr()
    #         if lttr in cur_chdr:
    #             cur_tot_cnt = cur_node.get_tot_cnt()
    #             if cur_tot_cnt > 1:
    #                 dup_nodes.append((lttr, cur_node))
    #                 cur_node = cur_chdr[lttr]
    #             elif cur_tot_cnt < 1:
    #                 raise ValueError('E: inval chdr cnt')
    #             else:
    #                 j = i
    #                 cur_node = cur_chdr[lttr]
    #                 break
    #         else:
    #             raise ValueError('E: del, no chdr')
    #     # Check branch
    #     for lttr in word_rev[j+1:]:
    #         cur_chdr = cur_node.get_chdr()
    #         if lttr in cur_chdr:
    #             if cur_node.get_tot_cnt() == 1:
    #                 cur_node = cur_chdr[lttr]
    #             else:
    #                 raise ValueError('E: inval chdr cnt')
    #         else:
    #             raise ValueError('E: del, no chdr')
    #     # Deletion
    #     last_lttr, last_node = dup_nodes.pop()
    #     last_node.del_chd(last_lttr)
    #     for lttr, node in dup_nodes:
    #         node.sub_tot_cnt(lttr)

    def del_rhyme_pair(self):
        # Find
        print(self.get_chdr(), self.get_tot_cnt(), self.get_cnt())
        node_his = []
        cur_node = self
        engh_tot_chdr = cur_node.get_tot_cnt() > 2
        not_dist_brch = True
        while engh_tot_chdr and not_dist_brch:
            print(cur_node.get_name(), cur_node.get_chdr())
            max_tot_cnt, lttr = cur_node.get_max_tot_cnt_lttr()
            node_his.append((lttr, cur_node))
            cur_node = cur_node.get_chdr()[lttr]
            engh_tot_chdr = cur_node.get_tot_cnt() > 2
            not_dist_brch = cur_node.get_tot_cnt() != cur_node.get_cnt()
        if node_his:
            if not engh_tot_chdr:
                # cur_node.get_tot_cnt() == 2
                last_lttr, last_node = node_his.pop()
                last_node.del_chd(last_lttr)
            else:
                for lttr in tuple(cur_node.get_chdr())[:2]:
                    cur_node.del_chd(lttr)
            for lttr, node in node_his:
                node.sub_tot_cnt(lttr)
        elif not engh_tot_chdr:
            lttr = tuple(self.get_chdr())[0]
            self.sub_tot_cnt(lttr)
            self.del_chd(lttr)


def main():
    t = int(input())
    for i in range(1, t+1):
        n = int(input())
        words = [input() for _ in range(n)]
        tree = Tree()
        for word in words:
            tree.add_word(word)
        res = 0
        while tree.get_tot_cnt() != tree.get_cnt():
            tree.del_rhyme_pair()
            res += 1
        print('Case #{}: {}'.format(i, res))


if __name__ == '__main__':
    main()
