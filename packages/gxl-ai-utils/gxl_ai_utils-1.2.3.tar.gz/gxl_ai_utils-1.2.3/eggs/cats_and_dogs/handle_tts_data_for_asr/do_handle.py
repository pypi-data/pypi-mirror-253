import glob
import os

import tqdm

from gxl_ai_utils.utils import utils_file


def do_handle():
    """"""


def clean_wav(input_file_path, output_file_path):
    """
    将音频整理成标准格式， 16K采样， 单通道，补齐音频头
    :param input_file_path:
    :param output_file_path:
    :return:
    """
    os.system(f"ffmpeg -i {input_file_path} -ac 1 -ar 16000 -vn {output_file_path}")


def slicing_wav(input_file_path, timestamp_path_path, output_dir):
    """
    将一个音频,依据时间戳, 切分成若干小音频.
    :param input_file_path:
    :param output_dir:
    :return:
    """

def do_get_vad_scp_file(input_dir, output_dir='./'):
    """
    tts处理流程中会对每一个音频生成一个vad_info的txt文件, 我们得到一个key vad_info.txt的字典
    :param input_dir:
    :return:
    """
    vad_res_scp = utils_file.get_scp_for_wav_dir(input_dir, suffix="txt")
    utils_file.write_dict_to_scp(vad_res_scp, os.path.join(output_dir, "vad_res.scp"))

def do_get_old2new_scp_file(input_dir, output_dir='./'):
    """
    这个input_dir中包含大量的old2new_*.txt文件, 我们得到一个key old2new.txt的字典
    :param input_dir:
    :return:
    """
    old2new_path_list = glob.glob(f"{input_dir}/old2new_*.scp")
    res_dict = {}
    for old2new_path in old2new_path_list:
        old2new_dict = utils_file.load_dict_from_scp(old2new_path)
        res_dict.update(old2new_dict)
    utils_file.write_dict_to_scp(res_dict, os.path.join(output_dir, "old2new.scp"))

def do_get_final_jsonl(input_scp_path, output_dir='./'):
    """"""
    final_dict = utils_file.load_dict_from_scp(final_scp_path)
    final_dict_list = []
    thread_num = 100
    runner = utils_file.GxlDynamicThreadPool()
    final_dict_list = utils_file.get_random_subdict(final_dict, thread_num)
    for little_final_dict in final_dict_list:
        runner.add_task(little_func4get_final_jsonl, [little_final_dict, final_dict_list])
    runner.start()
    utils_file.write_dict_list_to_jsonl(final_dict_list, "./final_data.list")

def little_func4get_final_jsonl(final_dict, final_dict_list):
    """"""
    for key, value in tqdm.tqdm(final_dict.items(),total=len(final_dict)):
        value_list = value.strip().split(r' ')
        if len(value_list) != 2:
            print(f"key:{key} value:{value}")
        wav_path = value_list[0]
        txt_path = value_list[1]
        txt_list = utils_file.load_list_file_clean(txt_path)
        if len(txt_list) != 1:
            print(f"key:{key} wav_path:{wav_path} txt_path:{txt_path}")
            continue
        txt = txt_list[0]
        txt = txt.strip().split("\t")[1:]
        dict_i = dict(key=key, wav=wav_path, txt=txt)
        final_dict_list.append(dict_i)

if __name__ == '__main__':
    # clean_wav("E:\gengxuelong_study\server_local_adapter\\ai\data\small_aishell\dev\BAC009S0724W0121.wav", "./gxl.wav")
    """"""
    input_vad_info_dir = "/home/node36_data/zhguo/history_10T/part_0/vad/txts"
    do_get_vad_scp_file(input_vad_info_dir)
    old2new_dir = "/home/node36_data/zhguo/history_10T/part_0/list/init_lists"
    do_get_old2new_scp_file(old2new_dir)

    # handle final
    final_scp_path = "/home/work_nfs8/lhma/double_check_lists/zhguo_lishi_part0_3700h.scp"
    do_get_final_jsonl(final_scp_path)