import os


def run(cmd, is_print: bool = True) -> list[str]:
    """
    运行命令
    :param cmd: 要执行的命令
    :param is_print: 是否在控制台打印信息
    :return: 命令输出信息
    """
    output = os.popen(cmd)
    line_list = output.buffer.read().decode('utf-8').split('\n')
    if is_print:
        for tmp_line in line_list:
            print(tmp_line)
    return line_list
