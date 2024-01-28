import glob
import os
import threading
import tqdm

from gxl_ai_utils.utils import utils_file

NEW2OLD_TABLE = {}
VAD_INFO_TABLE = {}
THREAD_NUM = 10


def handle_path(input_new_tts_final_path):
    """"""
    # 郭钊版：/root/path/282492425329_CPKwq_86_6299.wav
    file_name = utils_file.get_file_pure_name_from_path(input_new_tts_final_path)
    file_name_item_list = file_name.strip().split("_")
    parent_new_name = file_name_item_list[0] + "_" + file_name_item_list[1]
    index = int(file_name_item_list[2])
    millisecond_num = int(file_name_item_list[3])
    return parent_new_name, index, millisecond_num


def fix_path(output_dir, parent_new_name, index, millisecond_num):
    """"""
    # 郭钊版:/root/path/282492425329_CPKwq_86_6299.wav
    file_name = parent_new_name + "_" + str(index) + "_" + str(millisecond_num) + ".wav"
    file_name_rough = parent_new_name + "_" + str(index) + "_" + "*" + ".wav"
    true_wav_path_list = glob.glob(os.path.join(output_dir, file_name_rough))
    true_wav_path = true_wav_path_list[0]
    _, _, duration = handle_path(true_wav_path)
    if abs(duration - millisecond_num) < 10:
        return true_wav_path
    else:
        utils_file.logging_print(
            f"fix_path(): abs(duration - millisecond_num) > 10={abs(duration - millisecond_num)}, 采用真实的音频地址")
        return true_wav_path


def do_handle_wav(wav_new_path, output_dir="./"):
    """"""
    # 首先得到小段音频对应长短音频的名字。282492425329_CPKwq_86_6299.txt
    little_new_name = utils_file.get_file_pure_name_from_path(wav_new_path)
    temp_name_apart = little_new_name.strip().split("_")
    little_new_name = temp_name_apart[0] + "_" + temp_name_apart[1]
    the_old_wav_path = NEW2OLD_TABLE[little_new_name]
    long_old_clean_wav_dir = os.path.join(output_dir, "temp_long_old_clean_wav")
    utils_file.makedir_sil(long_old_clean_wav_dir)
    long_old_clean_path = os.path.join(long_old_clean_wav_dir, little_new_name + ".wav")
    if not os.path.exists(long_old_clean_path):
        # 先规范化音频
        clean_wav(the_old_wav_path, long_old_clean_path)
        # 开始切割音频
        vad_info_txt_path = VAD_INFO_TABLE[little_new_name]
        final_wav_dir = os.path.join(output_dir, "final_wav")
        utils_file.makedir_sil(final_wav_dir)
        slicing_wav(long_old_clean_path, vad_info_txt_path, final_wav_dir, little_new_name)


def clean_wav(input_file_path, output_file_path):
    """
    将音频整理成标准格式， 16K采样， 单通道，补齐音频头
    :param input_file_path:
    :param output_file_path:
    :return:
    """
    os.system(f"ffmpeg -i '{input_file_path}' -ac 1 -ar 16000 -vn {output_file_path}")


def little_func4slicing_wav(i, vad_info, input_file_path, output_dir, wav_new_name):
    print(vad_info)
    start_time = vad_info[0]
    end_time = vad_info[1]
    duration = int(end_time) - int(start_time)
    start_sample = int(start_time) * 16
    end_sample = int(end_time) * 16
    output_path = os.path.join(output_dir, f"{wav_new_name}_{i}_{duration}.wav")
    utils_file.do_extract_audio_segment(input_file_path, output_path, start_sample, end_sample)


def slicing_wav(input_file_path, vad_info_txt_path, output_dir, wav_new_name):
    """
    将一个音频,依据时间戳, 切分成若干小音频. 此处可以多线程并行处理
    """
    vad_info_str_list = utils_file.load_list_file_clean(vad_info_txt_path)
    vad_info_list = []
    for vad_info_str in vad_info_str_list:
        vad_i = vad_info_str.strip().split(",")
        vad_info_list.append(vad_i)
    sorted_list = sorted(vad_info_list, key=lambda x: int(x[0]))
    thread_num = THREAD_NUM if len(sorted_list) > THREAD_NUM else len(sorted_list)
    runner = utils_file.GxlFixedThreadPool(thread_num)
    for i, vad_info in enumerate(sorted_list):
        i = i + 1
        runner.add_thread(little_func4slicing_wav, [i, vad_info, input_file_path, output_dir, wav_new_name])
    runner.start()


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
    if os.path.isfile(input_dir):
        utils_file.copy_file(input_dir, os.path.join(output_dir, "old2new.scp"))
        return
    old2new_path_list = glob.glob(f"{input_dir}/old2new*.scp")
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
    thread_num = 1  # 暂时不支持多线程， 多线程没法保证不同时切割同一条长音频。
    runner = utils_file.GxlDynamicThreadPool()
    little_dict_list = utils_file.do_split_dict(final_dict, thread_num)
    lock4write = threading.Lock()
    asr_final_list_path = os.path.join(output_dir, "asr_final_list.txt")
    if os.path.exists(asr_final_list_path):
        # 此处必须， 后面逻辑是在文本末尾累加写入，一旦程序中断重新运行，如果不删原来的，
        # 就会出问题， 文件写入内容本身不占用太多时间，时间主要是在于切分以您，此处已做了
        # 防中断处理。可放心随意重新运行程序， 而不会重复工作。
        os.remove(asr_final_list_path)
    for little_final_dict in little_dict_list:
        # 此处的多线程不太长成熟， 一旦多个线程同时处理同一个长音频的小音频，就会同时对该长音频的原始音频做再切割，
        # 而我们是只需要切一次， 不是多次。在切音频时仍然可以多线程， 此处无多线程也无所谓。
        runner.add_task(little_func4get_final_jsonl,
                        [little_final_dict, asr_final_list_path, lock4write, output_dir])
    runner.start()


def little_func4get_final_jsonl(final_dict, asr_final_jsonl_path, lock4write, output_dir):
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
        txt = txt.strip().split("\t")[1]
        do_handle_wav(wav_path, output_dir)
        parent_new_filename, index, duration = handle_path(wav_path)
        asr_final_wav_dir = os.path.join(output_dir, "final_wav")
        wav_path = fix_path(asr_final_wav_dir, parent_new_filename, index, duration)
        dict_i = dict(key=key, wav=wav_path, txt=txt)
        with lock4write:
            utils_file.write_single_dict_to_jsonl(dict_i, asr_final_jsonl_path)


def main(old2new_dir, input_vad_info_dir, final_scp_path, output_dir):
    """"""
    utils_file.makedir_sil(output_dir)
    do_get_vad_scp_file(input_vad_info_dir, output_dir)
    do_get_old2new_scp_file(old2new_dir, output_dir)
    NEW2OLD_TABLE = utils_file.load_dict_from_scp(os.path.join(output_dir, "old2new.scp"))
    VAD_INFO_TABLE = utils_file.load_dict_from_scp(os.path.join(output_dir, "./vad_res.scp"))
    do_get_final_jsonl(final_scp_path,
                       output_dir=output_dir)


def split_source(input_tts_scp_path, output_dir, split_ratio=None):
    """将一个scp文件分成若干个小文件"""
    if split_ratio is None:
        split_ratio = [0.45, 0.55]
    all_dict = utils_file.load_dict_from_scp(input_tts_scp_path)
    last = 0
    total_len = len(all_dict)
    for i, rat_i in enumerate(split_ratio):
        little_dict = utils_file.get_subdict(all_dict, last, total_len * rat_i)
        utils_file.write_dict_to_scp(little_dict, os.path.join(output_dir, f"final_scp_part_{i}.scp"))


def get_little_final(input_final_scp_path, output_dir):
    """从非常大的tts_final_scp中取出一小点，组成一个测试用的小的tts_final_scp文件"""
    all_dict = utils_file.load_dict_from_scp(input_final_scp_path)
    little_dict = utils_file.get_random_subdict(all_dict, 5)
    utils_file.write_dict_to_scp(little_dict, os.path.join(output_dir, f"final_scp_part_0.scp"))


if __name__ == '__main__':
    """
    任务说明：
    tts那边将原始音频经过降噪-》切句-》asr识别三个步骤，最终结果： '干净音频-文本'对
    我们拿到其对干净音频的识别结果， 和切句信息记录， 对原始音频做如下处理：
    根据切句信息对原始音频进行切句 -》 将切句的短音频和tts那边的asr识别结果进行配对， 最终结果：'吵杂音频-文本'对
    
    代码逻辑:
    根据tts那边提供的final.scp(包含干净音频-文本对 的文件），逐条映射为asr的final_scp文件（包含吵杂音频-文本对的文件）
    映射过程为： 对于一条干净的短音频，首先求得其原始长音频的“新名字”， 该根据新名字得到其原始吵杂音频的路径(然后对其进行规范化,统一成16k，单声道)，然后利用vad信息
    对原始音频进行切分， 最后将干净短音频地址根据其在长音频中的位置（index）替换为吵杂短音频的地址， 得到asr_final_scp.
    
    任务分配：
    目前tts那边给出三个子数据块供我们处理， 后续会相继给出其他数据块，
    对于当前数据块，做出如下分配：
    戴宇航， 李龙豪， 负责：xmly2T热点 负责人：戴宇航
    林振南， 林书亦，负责：xmly2T广播剧 负责人：林振南
    邵明辰， 李国建， 负责：xmly10T历史-0 负责人：邵明辰
    
    负责人任务： 
    将tts_final_scp分为两个字final_sc文件，
    其中一份占比0.45， 另一份占比0.55，负责人处理略少的一份。 划分函数以在do_handle.py中定义。
    负责人还需要在/home/node36_data/xlgeng/asr_data_from_pachong/目
    录下创建一个目录，目录名为所负责处理的数据块的名称（并将中文换成英文，
    防止最后音频路径带中文导致未知麻烦），并将目录为另一个人授权写入。
    
    处理人任务：
    每一个人在其相应的数据块的输出目录下，如/home/node36_data/xlgeng/asr_data_from_pachong/xmly10T-history-0/,
    创建一个以自己名字字母命名的目录，如yhdai,并将其作为自己的最终输出目录。
    然后，分别将 自己的output_dir，  input_vad_info_dir，old2new_dir ，final_tts_scp_path传入main函数即可。
    之后就坐等程序运行完毕。
    input_vad_info_dir，old2new_dir均直接填写表格中的内容。
    final_tts_scp_path 填写自己负责的被负责人划分过的小块的final_tts_scp_path。
    output_dir即上述的自己的最终的输出目录。
    
    运行前的小测试：
    强烈建议运行前做小测试：
    从自己负责的tts_final_scp中提取几条组成一个小的final_scp文件（提取函数已在do_handle.py中定义）
    然后用这个little_final_scp先试着跑一次。 然后看能否跑通和最终的产出的wav和txt是否真的对应，出现任何问题随时问我（耿雪龙）。
    
    环境需要：只需要： pip install gxl_ai_utils， 
    python最好>=3.10 , 运行do_handle.py后报缺什么包就安装什么包，可能安装个两三次就行了，有问题随时找我。
    """
    output_dir = "/home/node36_data/xlgeng/asr_data_from_pachong/xmly10-history-0"
    input_vad_info_dir = "/home/node36_data/zhguo/history_10T/part_0/vad/txts"
    # 表格里写的如果不是dir,而是成品scp文件， 就把scp文件的路径传入即可
    old2new_dir = "/home/node36_data/zhguo/history_10T/part_0/list/init_lists"
    final_tts_scp_path = "/home/work_nfs8/lhma/double_check_lists/zhguo_lishi_part0_3700h.scp"
    main(old2new_dir, input_vad_info_dir, final_tts_scp_path, output_dir)
