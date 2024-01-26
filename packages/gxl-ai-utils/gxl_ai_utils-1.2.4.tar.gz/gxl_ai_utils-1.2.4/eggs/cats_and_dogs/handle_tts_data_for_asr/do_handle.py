import glob
import os
import threading
import ast
import tqdm

from gxl_ai_utils.utils import utils_file

NEW2OLD_TABLE = {}
VAD_INFO_TABLE = {}


def do_handle_wav(wav_new_path, output_dir="./"):
    """"""
    # 首先得到小段音频对应长短音频的名字。282492425329_CPKwq_86_6299.txt
    little_new_name = utils_file.get_file_pure_name_from_path(wav_new_path)
    temp_name_apart = little_new_name.strip().split("_")
    little_new_name = temp_name_apart[0] + "_" + temp_name_apart[1]
    index = int(temp_name_apart[2])
    millisecond_num = int(temp_name_apart[3])
    the_old_wav_path = NEW2OLD_TABLE[little_new_name]
    long_old_clean_wav_dir = os.path.join(output_dir, "temp_long_old_clean_wav")
    long_old_clean_path = os.path.join(long_old_clean_wav_dir, little_new_name + ".wav")
    if not os.path.exists(long_old_clean_path):
        # 先规范化音频
        clean_wav(the_old_wav_path, long_old_clean_path)
        # 开始切割音频
        vad_info_txt_path = VAD_INFO_TABLE[little_new_name]
        final_wav_dir = os.path.join(output_dir, "final_wav")
        slicing_wav(long_old_clean_path,vad_info_txt_path, final_wav_dir)

def clean_wav(input_file_path, output_file_path):
    """
    将音频整理成标准格式， 16K采样， 单通道，补齐音频头
    :param input_file_path:
    :param output_file_path:
    :return:
    """
    os.system(f"ffmpeg -i {input_file_path} -ac 1 -ar 16000 -vn {output_file_path}")


def slicing_wav(input_file_path, vad_info_txt_path, output_dir):
    """
    将一个音频,依据时间戳, 切分成若干小音频.
    :param input_file_path:
    :param output_dir:
    :return:
    """
    vad_info = utils_file.load_first_row_clean(vad_info_txt_path)
    vad_info_list = ast.literal_eval(vad_info)
    for vad_info in vad_info_list:
        print(vad_info)



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
    """
    多线程实现
    :param input_scp_path:
    :param output_dir:
    :return:
    """
    final_dict = utils_file.load_dict_from_scp(input_scp_path)
    thread_num = 100
    runner = utils_file.GxlDynamicThreadPool()
    little_dict_list = utils_file.do_split_dict(final_dict, thread_num)
    lock4write = threading.Lock()
    for little_final_dict in little_dict_list:
        runner.add_task(little_func4get_final_jsonl,
                        [little_final_dict, os.path.join(output_dir, 'asr_data_final.list'), lock4write])
    runner.start()


def little_func4get_final_jsonl(final_dict, asr_final_jsonl_path, lock4write):
    """
    主要的处理逻辑
    :param final_dict:
    :param final_dict_list:
    :return:
    """
    for key, value in tqdm.tqdm(final_dict.items(), total=len(final_dict)):
        value_list = value.strip().split(r' ')
        if len(value_list) != 2:
            print(f"key:{key} value:{value}")
        wav_path = value_list[0]
        txt_path = value_list[1]
        txt = utils_file.load_first_row_clean(txt_path)
        if len(txt) == 0:
            print(f"txt_path文件内部无内容， key:{key} wav_path:{wav_path} txt_path:{txt_path}")
            continue
        txt = txt.strip().split("\t")[1:]
        do_handle()
        dict_i = dict(key=key, wav=wav_path, txt=txt)
        with lock4write:
            utils_file.write_single_dict_to_jsonl(dict_i, asr_final_jsonl_path)


if __name__ == '__main__':
    """"""
    # input_vad_info_dir = "/home/node36_data/zhguo/history_10T/part_0/vad/txts"
    # do_get_vad_scp_file(input_vad_info_dir)
    # old2new_dir = "/home/node36_data/zhguo/history_10T/part_0/list/init_lists"
    # do_get_old2new_scp_file(old2new_dir)
    final_scp_path = "/home/work_nfs8/lhma/double_check_lists/zhguo_lishi_part0_3700h.scp"
    final_scp_path = "./test_final.scp"
    do_get_final_jsonl(final_scp_path)

