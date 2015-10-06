# -*- coding: utf-8 -*-
import PCS


if __name__ == '__main__':
    quota_info = PCS.get_pcs_quota()
    print quota_info['quota']
    print quota_info['used']
