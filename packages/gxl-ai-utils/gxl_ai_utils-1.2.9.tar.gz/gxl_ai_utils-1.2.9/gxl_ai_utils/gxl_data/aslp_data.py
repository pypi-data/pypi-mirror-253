import os

from ..utils import utils_file


class AslpDataset:
    def __init__(self):
        self.scp_root_dir = '/home/work_nfs5_ssd/hfxue/gxl_data/data4w/source_1'
        self.shard_list_dir = '/home/work_nfs6/xlgeng/gxl_data/asr_data_shard_list'
        self.key_dict = {}
        all_key = os.listdir(self.scp_root_dir)
        for i, key in enumerate(all_key):
            self.key_dict[i] = utils_file.normal_path(key)

    def print_all_keys(self):
        """
        打印出所有数据集的名称。
        :return:
        """
        print_dict(self.key_dict)
        logging_print('该函数打印出了所有数据集的名称和其对应的id。')
        logging_print('使用get_path_info_by_key_or_id（）函数和key或id可获取对应的路径信息，以字典形式返回。')

    def get_path_info_by_key_or_id(self, key: str | int):
        key = key if isinstance(key, str) else self.key_dict[key]
        path = os.path.join(self.scp_root_dir, key)
        info = {'key': key, 'wav_scp': os.path.join(path, 'wav.scp'), 'text': os.path.join(path, 'text'),
                'shard_list': os.path.join(self.shard_list_dir, key, "shard_list.txt")}
        return info
