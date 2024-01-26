import glob
import hashlib
import io
import json
import logging
import multiprocessing
import os
import random
import sys
import tarfile
import time
import urllib
import warnings
from pathlib import Path
from datetime import datetime
import re
import codecs
from typing import Optional

import jsonlines
import numpy as np
import requests
import torch
import torchaudio
import yaml
import types

from torch import nn
from tqdm import tqdm
from ..thread.my_thread import GxlDynamicThreadPool, GxlFixedThreadPool
HAS_SET_LOGGING = False


def set_logging():
    """
    设置日志输出的格式
    :return: 
    """
    global HAS_SET_LOGGING
    HAS_SET_LOGGING = True
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s')


def logging_print(*args):
    global HAS_SET_LOGGING
    if not HAS_SET_LOGGING:
        set_logging()
    string_temp = " ".join([str(arg) for arg in args])
    logging.info(string_temp)


def print_list(data: list):
    logging_print('_________print_list_start_______________')
    for item in data:
        logging_print(item)
    logging_print('_________print_list_end____total:%d' % len(data))


def print_dict(data: dict):
    logging_print('_________print_dict_start_______________')
    for k, v in data.items():
        logging_print(f'{k} :\t{v}')
    logging_print('_________print_dict_end____total:%d' % len(data))


def print_checkpoint(checkpoint):
    if not isinstance(checkpoint, dict):
        checkpoint = torch.load(checkpoint, map_location='cpu')
    logging_print('_________print_checkpoint_start_______________')
    for k, v in checkpoint.items():
        logging_print(f'{k} :\t{v.shape}')
    logging_print('_________print_checkpoint_end____total:%d' % len(checkpoint))


def get_dir_size(dir_path: str):
    """
    单位:MB
    """
    size = 0
    for root, dirs, files in os.walk(dir_path):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size / (1024 ** 2)


def get_file_size(file_path):
    """单位：MB"""
    return os.path.getsize(file_path) / (1024 ** 2)


def load_list_file_clean(path: str):
    """
    得到不包含换行符的str_list
    :param path:
    :return:
    """
    with codecs.open(path, 'r', encoding='utf=8') as f:
        cat_to_name: list = f.read().splitlines()
        # cat_to_name: list = f.readlines() -> 包含换行符
        logging_print(f"load_list_file_clean()_数据总条数为:{len(cat_to_name)}")
    return cat_to_name


def load_list_file_unclean(path: str):
    """
    得到包含换行符的str_list
    :param path:
    :return:
    """
    with codecs.open(path, 'r', encoding='utf=8') as f:
        # cat_to_name: list = f.read().splitlines()
        cat_to_name: list = f.readlines()  # -> 包含换行符
        logging_print("load_list_file_unclean()_数据总条数为:", len(cat_to_name))
    return cat_to_name


def load_dict_from_json(path) -> dict:
    """"""
    with codecs.open(path, 'r', encoding='utf=8') as f:
        cat_to_name: dict = json.load(f)
        logging_print("load_dict_from_json()_数据总条数为:", len(cat_to_name))
    return cat_to_name


def load_dict_list_from_jsonl(jsonl_file_path) -> list:
    """"""
    with codecs.open(jsonl_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        logging_print("load_dict_list_from_jsonl()_数据总条数为:", len(lines))
        lines = [json.loads(x) for x in lines]
        return lines


def load_dict_from_scp(label_scp_file: str) -> dict:
    """
    得到scp文件的内容,要求key value以空格分割， 第一个为key,剩下的都是value。
    :param label_scp_file:
    :return:
    """
    res = {}
    with codecs.open(label_scp_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            items = line.split()
            if len(items) < 2:
                logging_print('warning_gxl:, this row not conform to the regulation of scp(key content) and skip it:',
                              line)
                continue
            elif len(items) == 2:
                res[items[0].strip()] = items[1].strip()
            else:
                # logging_print(
                #     'warning_gxl:, this row not conform to the regulation of'
                #     ' scp(key content) and no skip it,第一个为key,剩下的都是value:',
                #     line)
                res[items[0].strip()] = (' '.join(items[1:])).strip()
    total_len = len(res)
    logging_print("load_dict_from_scp()_数据总条数为:", total_len)
    return res


def load_tuple_list_from_scp(label_scp_file: str) -> list:
    res = []
    with codecs.open(label_scp_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            items = line.split()
            if len(items) < 2:
                logging_print('warning_gxl:, this row not conform to the regulation of scp(key content) and skip it:',
                              line)
                continue
            elif len(items) == 2:
                res.append((items[0].strip(), items[1].strip()))
            else:
                logging_print(
                    'warning_gxl:, this row not conform to the regulation of'
                    ' scp(key content) and no skip it,第一个为key,剩下的都是value:',
                    line)
                res.append((items[0].strip(), ' '.join(items[1:]).strip()))
    total_len = len(res)
    logging_print("load_tuple_list_from_scp()_数据总条数为:", total_len)
    return res


def write_list_to_file(data_list: list, path: str, is_append: bool = False):
    """
    要求data_list中每个元素(str)末尾没有换行, 该写入程序为每个item生成一个结尾的换行符
    :param data_list:
    :param path:
    :return:
    """
    makedir_for_file(path)
    logging_print("write_list_to_file()_数据总条数为:", len(data_list))
    with codecs.open(path, 'w' if not is_append else 'a', encoding='utf=8') as f:
        for data in data_list:
            f.write(data + '\n')


def write_dict_to_json(dic, json_file_path):
    logging_print("write_dict_to_json()_数据总条数为:", len(dic))
    os.makedirs(os.path.dirname(json_file_path), exist_ok=True)
    with codecs.open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump(dic, f, ensure_ascii=False, indent=4)


def write_dict_list_to_jsonl(dict_list, jsonl_file_path, is_append: bool = False):
    logging_print("write_dict_list_to_jsonl()_数据总条数为:", len(dict_list))
    if not is_append:
        if os.path.exists(jsonl_file_path):
            os.remove(jsonl_file_path)
    os.makedirs(os.path.dirname(jsonl_file_path), exist_ok=True)
    # for dic in dict_list:
    #     with jsonlines.open(jsonl_file_path, mode='a') as f:
    #         f.write(dic)
    with jsonlines.open(jsonl_file_path, mode='w') as f:
        f.write_all(dict_list)


def write_single_dict_to_jsonl(dic, jsonl_file_path):
    with jsonlines.open(jsonl_file_path, mode='a') as f:
        f.write(dic)


def write_dict_to_scp(dic: dict, scp_file_path: str):
    logging_print("write_dict_to_scp()_数据总条数为:", len(dic))
    os.makedirs(os.path.dirname(scp_file_path), exist_ok=True)
    with codecs.open(scp_file_path, 'w', encoding='utf-8') as f:
        for k, v in dic.items():
            f.write(f"{k} {v}\n")


def makedir(path):
    if isinstance(path, str):
        path = Path(path)
        # os.makedirs(path)
    if not path.exists():
        logging_print(f'路径{path.absolute()}不存在,现创建')
        path.mkdir(parents=True, exist_ok=True)
    else:
        logging_print(f'路径{path.absolute()}已存在,不用创建')


def makedir_sil(path):
    if isinstance(path, str):
        os.makedirs(path, exist_ok=True)
        return
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)


def makedir_for_file(filepath):
    # dirpath = os.path.dirname(filepath)
    if isinstance(filepath, str):
        filepath = Path(filepath)
    dirpath = filepath.parent
    makedir_sil(dirpath)


def makedir_for_file_or_dir(filepath):
    def ends_with_dot_and_non_slash_backslash(text):
        pattern = r'\.[^/\\]+$'
        return re.search(pattern, text) is not None

    # dirpath = os.path.dirname(filepath)
    if ends_with_dot_and_non_slash_backslash(filepath):
        makedir_for_file(filepath)
    else:
        makedir_sil(filepath)


def get_now(the_format='%Y-%m-%d_%H_%M_%S'):
    """
    获取当前日期和时间, 以字符串的形式返回
    :param the_format:
    :return:
    """
    current_datetime = datetime.now()
    # 格式化日期为字符串
    formatted_date = current_datetime.strftime(the_format)
    return formatted_date


def _join_path(path1, path2):
    if path1 is None or path2 is None or len(path1) == 0 or len(path2) == 0:
        return ""
    while path1[-1] == '/' or path1[-1] == '\\':
        path1 = path1[:-1]
    while path2[0] == '/' or path2[0] == '\\':
        path2 = path2[1:]
    return f'{path1}/{path2}'


def join_path(*args):
    """
    安全拼接若干路径, 再也不用担心分路径结尾和开头的分隔符的困扰了
    """
    lens = len(args)
    if lens == 0:
        return ""
    path = args[0]
    for i in range(1, lens):
        path = _join_path(path, args[i])
    return path


def do_convert_wav_text_scp_to_jsonl(wav_scp_file_path: str,
                                     text_scp_file_path: str,
                                     target_jsonl_file_path: str = None):
    """
    convert wav text scp to jsonl,
    如果target_josnl_file为None， 则直接返回dict_list
    """
    wav_dic = load_dict_from_scp(wav_scp_file_path)
    text_dic = load_dict_from_scp(text_scp_file_path)
    if len(wav_dic) != len(text_dic):
        logging_print("warning: wav_scp文件和text_scp文件长度不一致")
    if target_jsonl_file_path is not None:
        makedir_for_file(target_jsonl_file_path)
        if os.path.exists(target_jsonl_file_path):
            os.remove(target_jsonl_file_path)
        for k, v in wav_dic.items():
            if k not in text_dic:
                logging_print('warning: {} not in text_dic'.format(k))
                continue
            text = text_dic[k]
            write_single_dict_to_jsonl({'key': k, 'wav': v, 'txt': text}, target_jsonl_file_path)
    else:
        res_list = []
        for k, v in wav_dic.items():
            if k not in text_dic:
                logging_print('warning: {} not in text_dic'.format(k))
                continue
            text = text_dic[k]
            res_list.append({'key': k, 'wav': v, 'txt': text})
        return res_list


def do_convert_wav_text_scp_to_json(wav_scp_file_path: str, text_scp_file_path, target_json_file_path: str):
    """
    convert wav text scp to json
    """
    makedir_for_file(target_json_file_path)
    wav_dic = load_dict_from_scp(wav_scp_file_path)
    text_dic = load_dict_from_scp(text_scp_file_path)
    if len(wav_dic) != len(text_dic):
        logging_print("warning: wav_scp文件和text_scp文件长度不一致")
    os.remove(target_json_file_path)
    res_dic = {}
    for k, v in wav_dic.items():
        if k not in text_dic:
            logging_print('warning: {} not in text_dic'.format(k))
            continue
        text = text_dic[k]
        res_dic[k] = {'wav': v, 'txt': text}
    write_dict_to_json(res_dic, target_json_file_path)


def get_file_pure_name_from_path(path: str):
    """得到单纯的文件名，没有后缀和目录名"""
    return os.path.splitext(os.path.basename(path))[0]


def get_scp_for_wav_dir(wav_dir: str, wav_scp_file_path: str = None, suffix: str = '.wav', recursive=False):
    """
    生成wav.scp
    :param wav_dir:
    :param wav_scp_file_path: ,如果为None，则就直接返回dict
    :param suffix:
    :return:
    """
    if suffix[0] != '.':
        suffix = '.' + suffix
    if recursive:
        wav_path_list = glob.glob(os.path.join(wav_dir, f'**/*{suffix}'), recursive=True)
    else:
        wav_path_list = glob.glob(os.path.join(wav_dir, f'*{suffix}'))
    if wav_scp_file_path is None:
        logging_print('存储地址为None，就直接返回dict')
        res_dict = {}
        for wav_path in wav_path_list:
            res_dict[get_file_pure_name_from_path(wav_path)] = wav_path
        return res_dict
    else:
        makedir_for_file(wav_scp_file_path)
        with codecs.open(wav_scp_file_path, 'w', encoding='utf-8') as f:
            for wav_path in wav_path_list:
                f.write(f"{get_file_pure_name_from_path(wav_path)} {wav_path}\n")


def make_scp_file_for_wav_dir(wav_dir: str, wav_scp_file_path: str):
    get_scp_for_wav_dir(wav_dir, wav_scp_file_path)


def get_other_file_in_same_dir(old_file, new_file_name):
    dirname = os.path.dirname(old_file)
    return os.path.join(dirname, new_file_name)


def get_clean_filename(filename: str):
    """
    将一个字符串转为一个可以作为文件名的形式, 将非法字符替换为-,保留25个字符
    """
    # # 移除非法字符
    # filename = filename.replace(' ', '')
    # cleaned_filename = re.sub(r'[\/:*?"<>|]', '-', filename)
    # # 截断文件名，以确保它在不同系统下都有效, 本来是255, 但实验表明在windows下还是因为长度报错了,所有索性改为25
    # cleaned_filename = cleaned_filename[:25]
    # return cleaned_filename
    A = re.sub(r"[^\u4e00-\u9fa5a-zA-Z0-9]", "", filename)
    return A[:25]


class GxlDownloader_Encrypt:
    encrypted_hash_file_name = 'encrypted_hash.json'
    encrypted_dict = {}

    def __init__(self, root_dir: str):
        """
        使用urllib库对链接进行下载
        :param root_dir:
        """
        makedir_sil(root_dir)
        self.root = root_dir
        self.suffix = 'gxlfile'
        # self.file_lock = threading.Lock()
        if os.path.exists(os.path.join(self.root, self.encrypted_hash_file_name)):
            self.encrypted_dict = load_dict_from_json(os.path.join(self.root, self.encrypted_hash_file_name))

    def __del__(self):
        logging_print(f"Object {self} is being destroyed")
        write_dict_to_json(self.encrypted_dict, os.path.join(self.root, self.encrypted_hash_file_name))

    @classmethod
    def generate_hash(cls, input_file, hash_algorithm='sha256'):
        """
        读取一个文件的数据， 并生成其对应的hash值
        """
        # 读取文件的字节数据
        if isinstance(input_file, str):
            with codecs.open(input_file, 'rb') as file:
                data = file.read()
        else:
            data = input_file
        # 使用指定哈希算法计算哈希值
        hash_function = hashlib.new(hash_algorithm)
        hash_function.update(data)
        hash_value = hash_function.hexdigest()

        return hash_value

    def get_expected_encrypted_for_filename(self, filename):
        """"""
        return self.encrypted_dict.get(filename, None)

    def add_encrypted_hash_item(self, filename: str):
        """"""
        self.encrypted_dict[filename] = self.generate_hash(os.path.join(self.root, filename))

    def set_suffix(self, suffix: str):
        self.suffix = suffix

    def download(self, url: str, suffix: str = None, filename: str = None):
        if filename is None:
            filename = get_clean_filename(os.path.basename(url))
        if suffix is None:
            suffix = self.suffix
        filename = filename + "." + suffix
        logging_print(f'开始下载:{filename},url:{url}')
        download_target = os.path.join(self.root, filename)
        expected_sha256 = self.get_expected_encrypted_for_filename(filename)
        if os.path.exists(download_target) and os.path.isfile(download_target):
            if self.generate_hash(download_target) == expected_sha256:
                logging_print('文件已经存在')
                return download_target
            else:
                warnings.warn(
                    f"{download_target} exists, but the SHA256 checksum does not match; re-downloading the file"
                )

        with urllib.request.urlopen(url) as source, codecs.open(download_target, "wb") as output:
            with tqdm(
                    total=int(source.info().get("Content-Length", -1)),
                    ncols=80,
                    unit="iB",
                    unit_scale=True,
                    unit_divisor=1024,
            ) as loop:
                while True:
                    buffer = source.read(8192)
                    if not buffer:
                        break
                    output.write(buffer)
                    loop.update(len(buffer))
        self.add_encrypted_hash_item(filename)
        logging_print(f'下载完成:{filename},url:{url}')
        return download_target


class GxlDownloader:
    def __init__(self, root_dir: str = None):
        """
        使用urllib库对链接进行下载
        :param root_dir:
        """
        if root_dir is None:
            root_dir = './output/'
        makedir_sil(root_dir)
        self.root = root_dir
        self.suffix = 'wav'

    def set_suffix(self, suffix: str):
        self.suffix = suffix

    def download(self, url: str, target_dir: str = None, filename: str = None, suffix: str = None, ):
        if filename is None:
            filename = get_clean_filename(os.path.basename(url))
        if suffix is None:
            suffix = self.suffix
        if target_dir is None:
            target_dir = self.root
        if suffix.startswith('.'):
            suffix = suffix[1:]
        filename = filename + "." + suffix
        makedir_sil(target_dir)
        logging_print(f'开始下载:{filename},url:{url}')
        download_target = os.path.join(target_dir, filename)
        if os.path.exists(download_target) and os.path.isfile(download_target):
            warnings.warn(
                f"{download_target} exists, don't download again"
            )
            return

        with urllib.request.urlopen(url) as source, codecs.open(download_target, "wb") as output:
            with tqdm(
                    total=int(source.info().get("Content-Length", -1)),
                    ncols=80,
                    unit="iB",
                    unit_scale=True,
                    unit_divisor=1024,
            ) as loop:
                while True:
                    buffer = source.read(8192)
                    if not buffer:
                        break
                    output.write(buffer)
                    loop.update(len(buffer))
        logging_print(f'下载完成:{filename},url:{url}')
        return download_target


def download_file(url: str, target_dir: str = None, filename: str = None, suffix: str = None, ):
    if filename is None:
        filename = get_clean_filename(os.path.basename(url))
    if suffix is None:
        suffix = 'wav'
    if target_dir is None:
        target_dir = './output/'
    makedir_sil(target_dir)
    if suffix.startswith('.'):
        suffix = suffix[1:]
    filename = filename + "." + suffix
    download_target = os.path.join(target_dir, filename)
    logging_print(f'开始下载: {filename} , url: {url} , target: {download_target}')
    if os.path.exists(download_target) and os.path.isfile(download_target):
        logging.debug(
            f"{download_target} exists, don't download again"
        )
        return

    with urllib.request.urlopen(url) as source, codecs.open(download_target, "wb") as output:
        with tqdm(
                total=int(source.info().get("Content-Length", -1)),
                ncols=80,
                unit="iB",
                unit_scale=True,
                unit_divisor=1024,
        ) as loop:
            while True:
                buffer = source.read(8192)
                if not buffer:
                    break
                output.write(buffer)
                loop.update(len(buffer))
    logging_print(f'下载完成:{filename},url:{url},target:{download_target}')
    return download_target


def download_file_by_request(url: str, target_dir: str = None, filename: str = None, suffix: str = None, ):
    if filename is None:
        filename = get_clean_filename(os.path.basename(url))
    if suffix is None:
        suffix = 'wav'
    if target_dir is None:
        target_dir = './output/'
    makedir_sil(target_dir)
    if suffix.startswith('.'):
        suffix = suffix[1:]
    filename = filename + "." + suffix
    download_target = os.path.join(target_dir, filename)
    logging_print(f'开始下载: {filename} , url: {url} , target: {download_target}')
    if os.path.exists(download_target) and os.path.isfile(download_target):
        logging.debug(
            f"{download_target} exists, don't download again"
        )
        return

    response = requests.get(url, stream=True)
    # 获取文件大小
    total_size = int(response.headers.get('content-length', 0))
    chunk_size = 128
    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)
    with open(download_target, 'wb') as file:
        for chunk in response.iter_content(chunk_size=chunk_size):
            file.write(chunk)
            progress_bar.update(len(chunk))


def remove_file(file_path: str):
    if os.path.exists(file_path):
        os.remove(file_path)


def do_split_dict(original_dict, num_subsets):
    """
    多余的那些和最后一个块放在一起，所以最后一个块是最多的
    :param original_dict:
    :param num_subsets:
    :return:
    """
    # 计算每个子集的键的数量
    keys_per_subset = len(original_dict) // num_subsets

    # 将字典的键转换为列表
    keys = list(original_dict.keys())

    # 初始化子集字典列表
    subsets = []

    # 分割字典
    for i in range(num_subsets):
        # 计算当前子集的起始和结束索引
        start_index = i * keys_per_subset
        end_index = (i + 1) * keys_per_subset if i < num_subsets - 1 else None

        # 提取当前子集的键
        subset_keys = keys[start_index:end_index]

        # 创建子集字典
        subset_dict = {key: original_dict[key] for key in subset_keys}

        # 将子集字典添加到列表中
        subsets.append(subset_dict)

    return subsets


def do_merge_scp(input_dir, output_scp_file):
    """

    :param input_dir:
    :param output_scp_file:
    :return:
    """
    little_scp_list = glob.glob(os.path.join(input_dir, '*.scp'))
    res_dict = {}
    for little_scp_path in little_scp_list:
        little_dict = load_dict_from_scp(little_scp_path)
        res_dict.update(little_dict)
    write_dict_to_scp(res_dict, output_scp_file)


def normal_path(path: str):
    return path.replace('\\', '/')


def load_dict_from_yaml(file_path: str):
    with open(file_path, 'rt', encoding='utf-8') as f:
        dict_1 = yaml.load(f, Loader=yaml.FullLoader)
    return dict_1


def write_dict_to_yaml(dic: dict, file_path: str):
    with open(file_path, 'w', encoding='utf-8') as f:
        yaml.dump(dic, f, default_flow_style=False, allow_unicode=True)


def do_dict2simpleNamespaceObj(dict_obj: dict):
    """
    将一个字典转换为命名空间对象,
    命名空间对象可以修改key对应的value值
    可以通过.的方式调用键值对用的value值,如果调用没设置的键值,则直接报错,
    :param dict_obj:
    :return:
    """
    return types.SimpleNamespace(**dict_obj)


def do_add_dir_to_path(dir_path: str):
    sys.path.append(dir_path)


def set_seed(seed):
    # 设置Python随机数生成器的种子
    random.seed(seed)

    # 设置NumPy的随机数生成器的种子
    np.random.seed(seed)

    # 设置PyTorch的随机数生成器的种子
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

    # 以下是为了确保CuDNN在训练过程中的确定性，但可能会影响性能
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def convert_namespaceObj_to_dict(obj):
    return vars(obj)


class AslpDataset:
    def __init__(self):
        self.save_path = join_path(os.path.expanduser("~"), ".aslp", "aslp_dataset.json")
        self.scp_root_dir = '/home/work_nfs5_ssd/hfxue/data/data4w/source_1'
        self.raw_list_dir = '/home/work_nfs6/xlgeng/data/asr_data_shard_list'
        self.shard_list_dir = '/home/work_nfs6/xlgeng/data/asr_data_raw_list'
        self.key_dict = {}
        self.index_dict = {}
        makedir_for_file_or_dir(self.save_path)
        if not os.path.exists(self.save_path):
            all_key = os.listdir(self.scp_root_dir)
            for i, key in enumerate(all_key):
                the_key = key.lower()
                self.key_dict[the_key] = dict(
                    wav_scp=os.path.join(self.scp_root_dir, key, 'wav.scp'),
                    text=os.path.join(self.scp_root_dir, key, 'text'),
                    shard_list=os.path.join(self.shard_list_dir, key, "shard_list.txt"),
                    datyamla_list=os.path.join(self.raw_list_dir, key, "data.list"),
                )
            write_dict_to_json(self.key_dict, self.save_path)
        else:
            self.key_dict = load_dict_from_json(self.save_path)
        for i, key in enumerate(self.key_dict.keys()):
            the_key = key.lower()
            self.index_dict[the_key] = i

    def print_all_keys(self):
        """
        打印出所有数据集的名称。
        :return:
        """
        print_dict(self.index_dict)
        logging_print('该函数打印出了所有数据集的名称和其对应的id。')
        logging_print('使用get_path_info_by_key_or_id（）函数和key或id可获取对应的路径信息，以字典形式返回。')

    def print_all_data(self):
        print_dict(self.key_dict)

    def get_path_info_by_key_or_id(self, key):
        key = key if isinstance(key, str) else self.index_dict.get(key, "未找到对应的key")
        info = self.key_dict.get(key, "未找到对应的key")
        if info == "未找到对应的key":
            logging_print(f"未找到对应的key:{key}")
            return None
        return info

    def download_file(self, output_dir: str):
        makedir_sil(output_dir)
        output_path = join_path(output_dir, "aslp_dataset.json")
        copy_file(self.save_path, output_path)

    def search(self, keyword: str):
        right_dict = {}
        keyword = keyword.lower()
        for key, i in self.index_dict.items():
            if keyword in key:
                right_dict[key] = i
        print_dict(right_dict)


def copy_file(source_path, destination_path):
    makedir_sil(os.path.dirname(destination_path))
    try:
        with open(source_path, 'rb') as source_file:
            content = source_file.read()

        with open(destination_path, 'wb') as destination_file:
            destination_file.write(content)

        print(f"文件 {source_path} 已成功复制到 {destination_path}")
    except Exception as e:
        print(f"复制文件时发生错误：{e}")


def copy_file_to_dir(source_path, destination_dir):
    makedir_sil(destination_dir)
    try:
        with open(source_path, 'rb') as source_file:
            content = source_file.read()
        destination_path = join_path(destination_dir, os.path.basename(source_path))
        with open(destination_path, 'wb') as destination_file:
            destination_file.write(content)

        print(f"文件 {source_path} 已成功复制到 {destination_path}")
    except Exception as e:
        print(f"复制文件时发生错误：{e}")


def do_change_file_suffix(tar_file_path, param):
    str_1 = tar_file_path.split('.')[:-1]
    return '.'.join(str_1) + '.' + param


def print_model_size(model: nn.Module):
    """
    打印模型的大小， 单位为M（1024*1024）
    :param model:
    :return:
    """
    num_params = sum(p.numel() for p in model.parameters())
    print('the number of model params: {:,f}M'.format(num_params / 1024 / 1024))


def do_set_cuda_env(gpu_ids: str = '0,1,2,3'):
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    os.environ["CUDA_VISIBLE_DEVICES"] = gpu_ids


def do_from_mono_wav_txt_to_scp(wav_dir: str, output_dir=None):
    """
    处理场景:
    一个目录中零散分布着wav文件和针对单个wav文件的txt文件
    :param wav_dir:
    :return:
    """
    logging_print("开始处理,处理场景:一个目录中零散分布着wav文件和针对单个wav文件的txt文件")
    wav_path_list = glob.glob(f'{wav_dir}/**/*.wav', recursive=True)
    txt_path_list = glob.glob(f'{wav_dir}/**/*.txt', recursive=True)
    wav_dict = {}
    txt_dict = {}
    for wav_path in wav_path_list:
        key = os.path.basename(wav_path).split('.')[0]
        wav_dict[key] = wav_path
    for txt_path in txt_path_list:
        key = os.path.basename(txt_path).split('.')[0]
        txt_dict[key] = txt_path
    if output_dir is not None:
        makedir_sil(output_dir)
        write_dict_to_scp(wav_dict, os.path.join(output_dir, 'wav.scp'))
        write_dict_to_scp(txt_dict, os.path.join(output_dir, 'text'))
        return
    return wav_dict, txt_dict


def write_to_tar_file(data_list: list[tuple], tar_file_path: str, resample=16000, i=-1):
    """
    将数据写入tar文件，
    data_list: item: (key, text.txt, wav_path)
    """
    print(f'开始处理第{i}个shard')
    AUDIO_FORMAT_SETS = {'flac', 'mp3', 'm4a', 'ogg', 'opus', 'wav', 'wma'}
    from .utils_file import makedir_for_file
    makedir_for_file(tar_file_path)
    finished_path = do_change_file_suffix(tar_file_path, 'finished')
    with tarfile.open(tar_file_path, "w") as tar:
        for item in tqdm(data_list, total=len(data_list), desc=f"shard_{i}"):
            key, txt, wav = item
            suffix = wav.split('.')[-1]
            assert suffix in AUDIO_FORMAT_SETS, f"不支持的音频格式{suffix},仅支持{AUDIO_FORMAT_SETS}"
            # read & resample
            audio, sample_rate = torchaudio.load(wav, normalize=False)
            if sample_rate != resample:
                audio = torchaudio.transforms.Resample(
                    sample_rate, resample)(audio.float())
                audio = audio.to(torch.int16)
            # change format to wav
            f = io.BytesIO()
            torchaudio.save(f, audio, resample, format="wav", bits_per_sample=16)
            suffix = "wav"
            f.seek(0)
            data = f.read()
            assert isinstance(txt, str), f"txt必须是str类型"
            txt_file_name = key + '.txt'
            txt = txt.encode('utf8')
            txt_data = io.BytesIO(txt)
            txt_info = tarfile.TarInfo(txt_file_name)
            txt_info.size = len(txt)
            tar.addfile(txt_info, txt_data)

            wav_file = key + '.' + suffix
            wav_data = io.BytesIO(data)
            wav_info = tarfile.TarInfo(wav_file)
            wav_info.size = len(data)
            tar.addfile(wav_info, wav_data)
    print(f'第{i}个shard处理完成')
    with open(finished_path, 'w') as f:
        pass


def do_make_shard_file(wav_scp_file_path: str, text_scp_file_path: str, output_dir: str, num_utt_per_shard: int = 1000,
                       num_threads=32, prefix_for_tar_file: str = "shard", resample: int = 16000,
                       ):
    """
    得到一个shard文件组成的目录, logger must is not None
    """
    logging_print('开始打shard for ' + prefix_for_tar_file)
    logging_print('wav_scp: ' + wav_scp_file_path)
    logging_print('text_scp: ' + text_scp_file_path)
    from .utils_file import load_dict_from_scp
    wav_dic = load_dict_from_scp(wav_scp_file_path)
    data = []
    text_dic = load_dict_from_scp(text_scp_file_path)
    for k, text in text_dic.items():
        if k not in wav_dic:
            logging_print(f"warning: {k}不在wav_scp文件中")
            continue
        data.append((k, text, wav_dic[k]))
    logging_print(f"共有{len(data)}个utt")
    chunks = [data[i:i + num_utt_per_shard] for i in range(0, len(data), num_utt_per_shard)]
    os.makedirs(output_dir, exist_ok=True)
    logging_print(f"共有{len(chunks)}个shard")
    # Using thread pool to speedup
    pool = multiprocessing.Pool(processes=num_threads)
    shards_list = []
    for i, chunk in enumerate(chunks):
        tar_file_path = os.path.join(output_dir,
                                     '{}_{:09d}.tar'.format(prefix_for_tar_file, i))
        shards_list.append(tar_file_path)
        finished_file_path = do_change_file_suffix(tar_file_path, 'finished')
        if os.path.exists(finished_file_path):
            continue
        pool.apply_async(
            write_to_tar_file,
            (chunk, tar_file_path, resample, i))

    pool.close()
    pool.join()
    logging_print('打shard结束, 保存shard列表')
    with open(os.path.join(output_dir, 'shards_list.txt'), 'w', encoding='utf8') as fout:
        for name in shards_list:
            fout.write(name + '\n')
    logging_print('打shard完全结束')


def get_random_subdict(source_dict: dict, num_value: int):
    keys = list(source_dict.keys())
    random.shuffle(keys)
    return {key: source_dict[key] for key in keys[:num_value]}


def do_convert_jsonl_to_wav_text_scp(jsonl_path, scp_path=None, text_path=None):
    """
    将jsonl文件转换为wav和text的scp文件
    :param jsonl_path:
    :param scp_path:
    :param text_path:
    :return:
    """

    dict_list = load_dict_list_from_jsonl(jsonl_path)
    wav_dict = {}
    text_dict = {}
    for item in dict_list:
        wav_dict[item['key']] = item['wav']
        text_dict[item['key']] = item['txt']
    if scp_path is not None:
        write_dict_to_scp(wav_dict, scp_path)
    if text_path is not None:
        write_dict_to_scp(text_dict, text_path)
    return wav_dict, text_dict


def do_split_list(source_list, num_subsets):
    """
    最后一个块包含多余的余数
    :param source_list:
    :param num_subsets:
    :return:
    """
    keys_per_subset = len(source_list) // num_subsets
    # 初始化子集字典列表
    subsets = []
    # 分割字典
    for i in range(num_subsets):
        # 计算当前子集的起始和结束索引
        start_index = i * keys_per_subset
        end_index = (i + 1) * keys_per_subset if i < num_subsets - 1 else None
        subset_list = source_list[start_index:end_index]
        subsets.append(subset_list)
    return subsets
