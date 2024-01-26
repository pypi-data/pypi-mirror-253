import os
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

if __name__ == '__main__':
    # clean_wav("E:\gengxuelong_study\server_local_adapter\\ai\data\small_aishell\dev\BAC009S0724W0121.wav", "./gxl.wav")
    """"""
    input_dir = "/home/work_nfs8/kxxia/data/vad_result1"
    vad_res_scp = utils_file.get_scp_for_wav_dir(input_dir, suffix="txt")
    utils_file.write_dict_to_scp(vad_res_scp, "vad_res.scp")

