# -*- coding: utf-8 -*-
main_menu = """
1: dspawpy更新 
2: structure结构转化
3: volumetricData数据处理
4: band能带数据处理
5: dos态密度数据处理
6: bandDos能带和态密度共同显示
7: optical光学性质数据处理
8: neb过渡态计算数据处理
9: phonon声子计算数据处理
10: aimd分子动力学模拟数据处理
11: Polarization铁电极化数据处理
12: ZPE零点振动能数据处理
13: TS的热校正能
--> 输入数字后回车选择功能："""

menu3 = """
=== 3 volumetricData数据处理 ===

  1: volumetricData可视化
  2: 差分volumetricData可视化
  3: volumetricData面平均
  
  0: 返回主菜单
  --> 输入数字后回车选择功能："""


menu4 = """
=== 4 band能带数据处理 ===

  1: 普通能带
  2: 将能带投影到每一种元素分别作图，数据点大小表示该元素对该轨道的贡献
  3: 能带投影到不同元素的不同轨道
  4: 将能带投影到不同原子的不同轨道
  5: 能带反折叠处理
  6. band-compare能带对比图处理
  
  0: 返回主菜单
  --> 输入数字后回车选择功能："""

menu5 = """
=== 5 dos态密度数据处理 ===

  1: 总的态密度
  2: 将态密度投影到不同的轨道上
  3: 将态密度投影到不同的元素上
  4: 将态密度投影到不同原子的不同轨道上
  5: 将态密度投影到不同原子的分裂d轨道(t2g, eg)上
  6: d-带中心分析
  
  0: 返回主菜单
  --> 输入数字后回车选择功能："""

menu6 = """
=== 6 bandDos能带和态密度共同显示 ===

  1: 将能带和态密度显示在一张图上
  2: 将能带和投影态密度显示在一张图上

  0: 返回主菜单
  --> 输入数字后回车选择功能："""

menu8 = """
=== 8 neb过渡态计算数据处理 ===

  1: 输入文件之生成中间构型
  2: 绘制能垒图
  3: 过渡态计算概览
  4: NEB链可视化
  5: 计算构型间距
  6: neb续算

  0: 返回主菜单
  --> 输入数字后回车选择功能："""

menu9 = """
=== 9 phonon声子计算数据处理 ===

  1: 声子能带数据处理
  2: 声子态密度数据处理
  3: 声子热力学数据处理

  0: 返回主菜单
  --> 输入数字后回车选择功能："""

menu10 = """
=== 10 aimd分子动力学模拟数据处理 ===

  1: 轨迹文件转换格式为.xyz或.dump
  2: 动力学过程中能量、温度等变化曲线
  3: 均方位移（MSD）
  4. 均方根偏差（RMSD）
  5. 径向分布函数（RDF）

  0: 返回主菜单
  --> 输入数字后回车选择功能："""

menu13 = """
=== 13 TS的热校正能 ===

  1: 吸附质
  2: 理想气体

  0: 返回主菜单
  --> 输入数字后回车选择功能："""

import os  # noqa: E402
from argparse import ArgumentParser  # noqa: E402

argparser = ArgumentParser("dspawpy命令行交互小工具")
argparser.add_argument(
    "-q", "--quick", action="store_true", help="不联网检查dspawpy版本"
)
argparser.add_argument(
    "-c", "--clean", action="store_true", help="不显示dspawpy_logo，直接显示菜单"
)
args = argparser.parse_args()


try:
    pass
except ImportError:
    cmd = "pip install dspawpy"
    if os.system(cmd) != 0:
        raise ImportError(f"无法自动配置依赖库，请手动安装后再试 $ {cmd}")


def online_check(dv, df):
    latest_version = None
    try:  # 如果正常导入dspawpy，应当有 requests库（pymatgen和mp-api的依赖）
        print("正在联网检查dspawpy版本... 使用 -q 参数启动此程序可跳过检查")
        response = get("https://pypi.org/pypi/dspawpy/json", timeout=3)
        latest_version = response.json()["info"]["version"]
        error_message = None
    except ImportError:
        error_message = "无法导入 requests 库"
    except exceptions.Timeout:
        error_message = "requests联网检查dspawpy版本超时"
    except exceptions.RequestException as e:
        error_message = f"requests联网检查dspawpy版本时出现异常: {e}"
    except Exception as e:
        error_message = f"联网检查dspawpy版本失败: {e}"
    finally:
        if latest_version:
            if latest_version != dv:
                print(
                    f"\n 成功导入 {dv}（不是最新版本 {latest_version}），可尝试使用功能1升级"
                )
                print(
                    f" 导入的dspawpy模块文件路径为（如果不符合预期，请检查环境变量)：\n {df}\n"
                )
            else:
                print(f"\n         成功导入 {dv}（最新版）dspawpy\n")

            with open(os.path.expanduser("~/.dspawpy_latest_version"), "w") as fin:
                fin.write(latest_version)
        else:
            print(f"\n         成功导入 {dv}（无法联网检查最新版本）dspawpy\n")

    return error_message


def verify_dspawpy_version(skip=False):
    error_message = None
    try:
        import dspawpy

        try:
            dv = dspawpy.__version__
        except Exception:  # 老版本没有__version__属性
            dv = "??? 版本过老，无法检测"
        finally:
            df = os.path.dirname(dspawpy.__file__)

        if skip:
            print(f"\n         成功导入 dspawpy={dv}\n")
        else:
            # 检查是否存在 ~/.dspawpy_latest_version 文件，存在则读取其中写的版本号信息
            # 如果不存在，或者读取失败，则联网检查最新版本，并在检查成功后写入 ~/.dspawpy_latest_version 文件
            if os.path.isfile(os.path.expanduser("~/.dspawpy_latest_version")):
                with open(os.path.expanduser("~/.dspawpy_latest_version"), "r") as fin:
                    latest_version = fin.read().strip()
                if dv == latest_version:
                    print(f"\n         成功导入 {dv}（最新版）dspawpy\n")
                else:
                    error_message = online_check(dv, df)
            else:
                error_message = online_check(dv, df)

    except ImportError:
        print("     我们检测到您并未安装dspawpy，试试菜单1快速安装吧     ")
    except Exception as e:
        error_message = f"导入dspawpy失败: {e}"

    print("********这是dspawpy命令行交互小工具，预祝您使用愉快********")
    if error_message is not None:
        print(error_message)


def collect_user_input() -> list:
    """让用户选择功能，这一步不用记录日志，直接打印提示信息"""

    if args.clean:  # 不显示 dspawpy_logo
        dspawpy_logo = ""
    else:
        dspawpy_logo = r"""
********这是dspawpy命令行交互小工具，预祝您使用愉快********
    ( )
   _| |  ___  _ _      _ _  _   _   _  _ _    _   _
 /'_` |/',__)( '_`\  /'_` )( ) ( ) ( )( '_`\ ( ) ( )
( (_| |\__, \| (_) )( (_| || \_/ \_/ || (_) )| (_) |
`\__,_)(____/| ,__/'`\__,_)`\___x___/'| ,__/'`\__, |
             | |                      | |    ( )_| |
             (_)                      (_)    `\___/'
"""
    print(dspawpy_logo)

    if args.quick:
        iskip = True
    else:
        iskip = False

    verify_dspawpy_version(skip=iskip)

    while True:  # 主菜单选择
        n = input(main_menu)
        if n == "1":  # 环境部署比较特殊，不要进入主程序
            cmd = "pip install dspawpy --user -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install -U dspawpy -i https://pypi.org/simple --user"
            while True:
                yn = input(f"更新dspawpy将执行\n {cmd}\n (y/n)? ")
                if yn.lower() == "y":
                    if os.system(cmd) == 0:
                        print(">>>>>> 执行成功")
                        print("请重新运行程序，使安装生效")
                    else:
                        print("!!!!!! 执行失败")
                    break
                elif yn.lower() == "n":
                    print("###### 放弃执行")
                    break
                else:
                    print("!!! 输入错误，请重试")
                    continue

        elif n == "2":
            return 2, 0

        elif n == "3":
            while True:
                n = input(menu3)
                if n not in ["0", "1", "2", "3"]:
                    print("!!! 输入错误，请重试")
                    continue
                elif n == "1":
                    return 3, 1
                elif n == "2":
                    return 3, 2
                elif n == "3":
                    return 3, 3
                else:
                    break
            if n == "0":
                continue
            break

        elif n == "4":
            while True:
                n = input(menu4)
                if n not in ["0", "1", "2", "3", "4", "5", "6"]:
                    print("!!! 输入错误，请重试")
                    continue
                elif n == "1":
                    return 4, 1
                elif n == "2":
                    return 4, 2
                elif n == "3":
                    return 4, 3
                elif n == "4":
                    return 4, 4
                elif n == "5":
                    return 4, 5
                elif n == "6":
                    return 4, 6
                else:
                    break
            if n == "0":
                continue
            break

        elif n == "5":
            while True:
                n = input(menu5)
                if n not in ["0", "1", "2", "3", "4", "5", "6"]:
                    print("!!! 输入错误，请重试")
                    continue
                elif n == "1":
                    return 5, 1
                elif n == "2":
                    return 5, 2
                elif n == "3":
                    return 5, 3
                elif n == "4":
                    return 5, 4
                elif n == "5":
                    return 5, 5
                elif n == "6":
                    return 5, 6
                else:
                    break

            if n == "0":
                continue
            break

        elif n == "6":
            while True:
                n = input(menu6)
                if n not in ["0", "1", "2"]:
                    print("!!! 输入错误，请重试")
                    continue
                elif n == "1":
                    return 6, 1
                elif n == "2":
                    return 6, 2
                else:
                    break
            if n == "0":
                continue
            break

        elif n == "7":
            return 7, 0
        elif n == "8":
            while True:
                n = input(menu8)
                if n not in ["0", "1", "2", "3", "4", "5", "6"]:
                    print("!!! 输入错误，请重试")
                    continue
                elif n == "1":  # 插值
                    return 8, 1
                elif n == "2":  # 能垒图
                    return 8, 2
                elif n == "3":  # 总结
                    return 8, 3
                elif n == "4":  # 可视化链
                    return 8, 4
                elif n == "5":  # 计算距离
                    return 8, 5
                elif n == "6":  # 重启
                    return 8, 6
                else:
                    break
            if n == "0":
                continue
            break

        elif n == "9":
            while True:
                n = input(menu9)
                if n not in ["0", "1", "2", "3"]:
                    print("!!! 输入错误，请重试")
                    continue
                elif n == "1":
                    return 9, 1
                elif n == "2":
                    return 9, 2
                elif n == "3":
                    return 9, 3
                else:
                    break

            if n == "0":
                continue
            break

        elif n == "10":
            while True:
                n = input(menu10)
                if n not in ["0", "1", "2", "3", "4", "5"]:
                    print("!!! 输入错误，请重试")
                    continue
                elif n == "1":
                    return 10, 1
                elif n == "2":
                    return 10, 2
                elif n == "3":
                    return 10, 3
                elif n == "4":
                    return 10, 4
                elif n == "5":
                    return 10, 5
                else:
                    break

            if n == "0":
                continue
            break

        elif n == "11":
            return 11, 0

        elif n == "12":
            return 12, 0

        elif n == "13":
            while True:
                n = input(menu13)
                if n not in ["0", "1", "2"]:
                    logger.error("!!! 输入错误，请重试")
                    continue
                elif n == "1":
                    return 13, 1
                elif n == "2":
                    return 13, 2
                else:
                    break
            if n == "0":
                continue
            break

        else:
            print("XXXXXX 输入错误，请重试 XXXXXX")
            continue


from multiprocessing.pool import ThreadPool  # noqa: E402

from requests import exceptions, get  # noqa: E402

pool = ThreadPool(processes=1)
async_result = pool.apply_async(collect_user_input)


def main():
    """run specific task by user selected task number"""
    # print('entering main...') # uncomment this to see the speed impact
    task_number = async_result.get()
    pool.close()
    # print('got task number') # uncomment this to see the speed impact
    tasks = Tasks()
    if task_number[0] == 2:
        tasks.s2()

    elif task_number == (3, 1):
        tasks.s3_1()
    elif task_number == (3, 2):
        tasks.s3_2()
    elif task_number == (3, 3):
        tasks.s3_3()

    elif task_number[0] == 4:  # band
        if task_number[1] != 6:
            infile = prompt("待解析文件路径（包含文件名）：", completer=pc)
            ylims = check_lims(
                "输入y轴范围（先小后大，以空格分隔，直接回车可跳过设置）："
            )
            outfile = prompt("输出图片路径（包含文件名）：", completer=pc)
        if task_number[1] == 1:  # band
            tasks.s4_1(infile, ylims, outfile)
        elif task_number[1] == 2:  # band-proj
            tasks.s4_2(infile, ylims, outfile)
        elif task_number[1] == 3:  # band-proj-element
            tasks.s4_3(infile, ylims, outfile)
        elif task_number[1] == 4:  # band-proj-site
            tasks.s4_4(infile, ylims, outfile)
        elif task_number[1] == 5:  # band-unfold
            tasks.s4_5(infile, ylims, outfile)
        elif task_number[1] == 6:  # band-compare
            tasks.s4_6()

    elif task_number[0] == 5:  # dos
        infile = prompt("待解析文件路径（包含文件名）：", completer=pc)
        from dspawpy.io.read import get_dos_data

        dosdata = get_dos_data(infile)
        from pymatgen.electronic_structure.plotter import DosPlotter

        dos_plotter = DosPlotter(stack=False, zero_at_efermi=True)
        if task_number[1] != 6:
            xlims = check_lims(
                "输入x轴范围（先小后大，以空格分隔，直接回车可跳过设置）："
            )
            ylims = check_lims(
                "输入y轴范围（先小后大，以空格分隔，直接回车可跳过设置）："
            )
            outfile = prompt("输出图片路径（包含文件名）：", completer=pc)
        if task_number[1] == 1:  # tdos
            tasks.s5_1(dosdata, dos_plotter, xlims, ylims, outfile)
        elif task_number[1] == 2:
            tasks.s5_2(dosdata, dos_plotter, xlims, ylims, outfile)
        elif task_number[1] == 3:
            tasks.s5_3(dosdata, dos_plotter, xlims, ylims, outfile)
        elif task_number[1] == 4:
            tasks.s5_4(dosdata, dos_plotter, xlims, ylims, outfile)
        elif task_number[1] == 5:
            tasks.s5_5(dosdata, dos_plotter, xlims, ylims, outfile)
        elif task_number[1] == 6:
            tasks.s5_6(dosdata)

    elif task_number[0] == 6:
        infile1 = prompt("待解析能带band文件路径（包含文件名）：", completer=pc)
        infile2 = prompt("待解析态密度dos文件路径（包含文件名）：", completer=pc)
        ylims = check_lims("输入y轴范围（先小后大，以空格分隔，直接回车可跳过设置）：")
        outfile = prompt("输出图片路径（包含文件名）：", completer=pc)
        if task_number[1] == 1:
            tasks.s6_1(infile1, infile2, ylims, outfile)
        else:
            tasks.s6_2(infile1, infile2, ylims, outfile)

    elif task_number[0] == 7:
        tasks.s7()

    elif task_number[0] == 8:
        if task_number[1] == 1:
            tasks.s8_1()
        elif task_number[1] == 2:
            tasks.s8_2()
        elif task_number[1] == 3:
            tasks.s8_3()
        elif task_number[1] == 4:
            tasks.s8_4()
        elif task_number[1] == 5:
            tasks.s8_5()
        elif task_number[1] == 6:
            tasks.s8_6()

    elif task_number[0] == 9:
        if task_number[1] == 1:
            tasks.s9_1()
        elif task_number[1] == 2:
            tasks.s9_2()
        elif task_number[1] == 3:
            tasks.s9_3()

    elif task_number[0] == 10:
        if task_number[1] == 1:
            tasks.s10_1()
        elif task_number[1] == 2:
            tasks.s10_2()
        elif task_number[1] == 3:
            tasks.s10_3()
        elif task_number[1] == 4:
            tasks.s10_4()
        elif task_number[1] == 5:
            tasks.s10_5()

    elif task_number[0] == 11:
        tasks.s11()

    elif task_number[0] == 12:
        tasks.s12()

    elif task_number[0] == 13:
        if task_number[1] == 1:
            tasks.s13_1()
        elif task_number[1] == 2:
            tasks.s13_2()


import matplotlib  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

matplotlib.use("agg")  # to avoid qt error on some linux servers.
import sys  # noqa: E402

from prompt_toolkit import prompt  # noqa: E402
from prompt_toolkit.completion import PathCompleter, WordCompleter  # noqa: E402

pc = PathCompleter(expanduser=True)

from loguru import logger  # noqa: E402

logger.remove()
logger.add(
    sys.stderr,
    level="INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <cyan>{message}</cyan>",
)
logger.add(
    ".dspawpycli-debug.log",
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
)


def until_give_valid_input(user_prompt, valid_input, completer=None):
    while True:
        n = prompt(user_prompt, completer=completer)
        if n in valid_input:
            return n
        else:
            print("!!! 输入错误，请重试")
            continue


def check_lims(user_prompt):
    # return None or [float, float]
    while True:
        userInput = input(user_prompt).strip()
        if userInput == "":
            return None
        else:
            if " " not in userInput:
                logger.warning(f"!!! {userInput}没有以空格分隔，请重试")
                continue
            elif len(userInput.split(" ")) != 2:
                logger.warning(f"!!! {userInput}参数长度不为2")
                continue
            else:
                try:
                    float(userInput.split(" ")[0])
                    float(userInput.split(" ")[1])
                    return userInput.split(" ")  # return '1_2'
                except Exception:
                    logger.warning(f"!!! {userInput}不全是数字，请重试")
                    continue


class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


class Tasks:
    @logger.catch
    def s2(
        self,
    ):
        infile = prompt(
            "待解析文件路径（包含文件名，支持h5, json, pdb, as, hzw等格式）：",
            completer=pc,
        )
        outfile = prompt(
            "输出文件路径（包含文件名，支持pdb, xyz, dump, json, as, hzw等格式）：",
            completer=pc,
        )
        logger.info("正在处理，请稍等...")

        from dspawpy.io.structure import convert

        convert(infile=infile, outfile=outfile)

    @logger.catch
    def s3_1(
        self,
    ):
        infile = prompt("待解析文件路径（包含文件名）：", completer=pc)
        _list = ["rho", "potential", "elf", "pcharge", "rhoBound"]
        task = until_give_valid_input(
            f"任务类型{_list}：",
            _list,
            completer=WordCompleter(_list),
        )

        subtype = None
        if task == "potential":
            if infile.endswith(".h5"):
                from dspawpy.io.read import load_h5

                data = load_h5(infile)
                keys = [
                    k.split("/")[-1] for k in data.keys() if k.startswith("/Potential")
                ]

                if len(keys) == 0:
                    raise ValueError(
                        f"未检测到数据集，请检查文件{infile}路径或者任务类型是否正确！"
                    )
                elif len(keys) == 1:
                    subtype = keys[0]
                else:
                    subtype = until_give_valid_input(
                        f"检测到 {keys} 数据集，请选择其中之一：",
                        keys,
                        completer=WordCompleter(keys),
                    )

            elif infile.endswith(".json"):
                import json

                with open(infile, "r") as fin:
                    data = json.load(fin)
                    if "Potential" not in data.keys():
                        raise ValueError(
                            f"未检测到数据集，请检查文件{infile}路径或者任务类型是否正确！"
                        )
                    keys = data["Potential"].keys()

                if len(keys) == 1:
                    subtype = keys[0]
                else:
                    subtype = until_give_valid_input(
                        f"检测到 {keys} 数据集，请选择其中之一：",
                        keys,
                        completer=WordCompleter(keys),
                    )
            else:
                raise ValueError(
                    f"仅支持h5和json格式，不支持{infile.split('.')[-1]}格式的数据文件！"
                )

        outfile = prompt(
            "输出文件路径（包含文件名，支持.cube和.vasp格式）：", completer=pc
        )
        if outfile.split(".")[-1].lower() == "cube":
            cube_or_vasp = "cube"
        elif (
            outfile.split(".")[-1].lower() == "vesta"
            or outfile.split(".")[-1].lower() == "vasp"
        ):
            cube_or_vasp = "vesta"
        else:
            cube_or_vasp = until_give_valid_input(
                "请指定输出文件格式（cube, vasp）：", ["cube", "vesta", "vasp"]
            )

        logger.info("正在处理，请稍等...")
        from dspawpy.io.write import write_VESTA

        write_VESTA(
            in_filename=infile,
            data_type=task,
            out_filename=outfile,
            subtype=subtype,
            format=cube_or_vasp,
        )
        logger.info("可直接使用VESTA软件打开")

    @logger.catch
    def s3_2(
        self,
    ):
        total = prompt("体系总电荷密度文件路径（包含文件名）:", completer=pc)
        individuals = []
        while True:
            individual = prompt(
                "体系各组分电荷密度文件路径，(包含文件名，直接回车表示停止输入）:",
                completer=pc,
            )
            if individual == "":
                break
            individuals.append(individual)

        outfile = prompt(
            "输出文件路径（包含文件名，支持.cube和.vasp格式）：", completer=pc
        )

        if outfile.split(".")[-1].lower() == "cube":
            cube_or_vasp = "cube"
        elif (
            outfile.split(".")[-1].lower() == "vesta"
            or outfile.split(".")[-1].lower() == "vasp"
        ):
            cube_or_vasp = "vesta"
        else:
            cube_or_vasp = until_give_valid_input(
                "请指定输出文件格式（cube, vesta）：", ["cube", "vesta", "vasp"]
            )

        logger.info("正在处理，请稍等...")
        from dspawpy.io.write import write_delta_rho_vesta

        write_delta_rho_vesta(
            total=total, individuals=individuals, output=outfile, format=cube_or_vasp
        )
        logger.info("可直接使用VESTA软件打开")

    @logger.catch
    def s3_3(
        self,
    ):
        infile = prompt("待解析文件路径（包含文件名）：", completer=pc)
        axes = until_give_valid_input("沿哪些轴平均（0, 1, 2）：", ["0", "1", "2"])
        _list = ["rho", "potential", "elf", "pcharge", "rhoBound"]
        task = until_give_valid_input(
            f"任务类型{_list}：",
            _list,
            completer=WordCompleter(_list),
        )
        outfile = prompt("输出图片路径（包含文件名）：", completer=pc)

        subtype = None
        if task == "rho":
            k = "TotalCharge"
        elif task == "potential":
            if infile.endswith(".h5"):
                from dspawpy.io.read import load_h5

                data = load_h5(infile)
                keys = [
                    k.split("/")[-1] for k in data.keys() if k.startswith("/Potential")
                ]

                if len(keys) == 0:
                    raise ValueError(
                        f"未检测到数据集，请检查文件{infile}路径或者任务类型是否正确！"
                    )
                elif len(keys) == 1:
                    subtype = keys[0]
                else:
                    subtype = until_give_valid_input(
                        f"检测到 {keys} 数据集，请选择其中之一：",
                        keys,
                        completer=WordCompleter(keys),
                    )

            elif infile.endswith(".json"):
                import json

                with open(infile, "r") as fin:
                    data = json.load(fin)
                    if "Potential" not in data.keys():
                        raise ValueError(
                            f"未检测到数据集，请检查文件{infile}路径或者任务类型是否正确！"
                        )
                    keys = data["Potential"].keys()

                if len(keys) == 1:
                    subtype = keys[0]
                else:
                    subtype = until_give_valid_input(
                        f"检测到 {keys} 数据集，请选择其中之一：",
                        keys,
                        completer=WordCompleter(keys),
                    )
            else:
                raise ValueError(
                    f"仅支持h5和json格式，不支持{infile.split('.')[-1]}格式的数据文件！"
                )
            k = subtype
        elif task == "elf":
            k = "TotalELF"
        elif task == "pcharge":
            k = "TotalCharge"
        elif task == "rhoBound":
            k = "Rho"
        else:
            raise ValueError(f"Unknown task: {task}")

        logger.info("正在处理，请稍等...")
        axes_indices = [int(i) for i in axes.split()]
        for ai in axes_indices:
            from dspawpy.plot import average_along_axis

            average_along_axis(infile, axis=ai, label=f"axis{ai}", subtype=subtype)
        if len(axes_indices) > 1:
            plt.legend()

        plt.xlabel("Grid Index")
        plt.ylabel(k)
        absfile = os.path.abspath(outfile)
        os.makedirs(os.path.dirname(os.path.abspath(absfile)), exist_ok=True)
        plt.savefig(absfile, dpi=300)

    @logger.catch
    def s4_1(self, infile, ylims, outfile):
        from dspawpy.io.read import get_band_data
        from pymatgen.electronic_structure.plotter import BSPlotter

        band_data = get_band_data(infile)
        is_metal = band_data.is_metal()
        if is_metal:
            logger.info("正在处理，请稍等...")
            bsp = BSPlotter(band_data)
            bsp.get_plot(ylim=ylims)
        else:
            while True:
                shift = input(
                    "此为非金属体系，是否要将能量零点从价带顶平移至费米能级？(y/n)"
                )
                if shift.lower().startswith("y"):
                    logger.info("正在处理，请稍等...")
                    from dspawpy.io.read import get_band_data

                    band_data = get_band_data(infile, zero_to_efermi=True)
                    bsp = BSPlotter(band_data)
                    bsp.get_plot(False, ylim=ylims)
                    break
                elif shift.lower().startswith("n"):
                    logger.info("正在处理，请稍等...")
                    bsp = BSPlotter(band_data)
                    bsp.get_plot(ylim=ylims)
                    break
                else:
                    print("输入有误，请重新输入！")
                    continue

        save_figure_dpi300(outfile)

    @logger.catch
    def s4_2(self, infile, ylims, outfile):
        from dspawpy.io.read import get_band_data
        from pymatgen.electronic_structure.plotter import BSPlotterProjected

        band_data = get_band_data(infile)
        is_metal = band_data.is_metal()
        if is_metal:
            logger.info("正在处理，请稍等...")
            bsp = BSPlotterProjected(band_data)
            bsp.get_elt_projected_plots(ylim=ylims)
        else:
            while True:
                shift = input(
                    "此为非金属体系，是否要将能量零点从价带顶平移至费米能级？(y/n)"
                )
                if shift.lower().startswith("y"):
                    logger.info("正在处理，请稍等...")
                    band_data = get_band_data(infile, zero_to_efermi=True)
                    bsp = BSPlotterProjected(band_data)
                    bsp.get_elt_projected_plots(False, ylim=ylims)
                    break
                elif shift.lower().startswith("n"):
                    logger.info("正在处理，请稍等...")
                    bsp = BSPlotterProjected(band_data)
                    bsp.get_elt_projected_plots(ylim=ylims)
                    break
                else:
                    print("输入有误，请重新输入！")
                    continue
        save_figure_dpi300(outfile)

    @logger.catch
    def s4_3(self, infile, ylims, outfile):
        from dspawpy.io.read import get_band_data
        from pymatgen.electronic_structure.plotter import BSPlotterProjected

        band_data = get_band_data(infile)
        # 获取元素和轨道列表
        es = band_data.structure.composition.elements
        for e in es:
            print("可选元素:", str(e))
            available_orbitals = ["s"]
            orbitals = e.atomic_orbitals
            for o in orbitals:
                if "p" in o:
                    available_orbitals.append("p")
                elif "d" in o:
                    available_orbitals.append("d")
                elif "f" in o:
                    available_orbitals.append("f")
            unique_orbitals = list(set(available_orbitals))
            print(f"{str(e)}元素的可选轨道: ", unique_orbitals)

        dictio = {}
        while True:
            _e = input("选择一种元素（直接回车表示选择结束）: ")
            if _e == "":
                break
            _o = input(f"选择{_e}元素的原子轨道（用空格分隔）: ")
            _os = _o.split(" ")
            dict_eo = {_e: _os}
            # update dictio
            dictio.update(dict_eo)

        print("选定的轨道元素字典: ", dictio)

        is_metal = band_data.is_metal()
        if is_metal:
            logger.info("正在处理，请稍等...")
            bsp = BSPlotterProjected(band_data)
            bsp.get_projected_plots_dots(dictio)
        else:
            while True:
                shift = input(
                    "此为非金属体系，是否要将能量零点从价带顶平移至费米能级？(y/n)"
                )
                if shift.lower().startswith("y"):
                    logger.info("正在处理，请稍等...")
                    band_data = get_band_data(infile, zero_to_efermi=True)
                    bsp = BSPlotterProjected(band_data)
                    bsp.get_projected_plots_dots(dictio, False, ylim=ylims)
                    break
                elif shift.lower().startswith("n"):
                    logger.info("正在处理，请稍等...")
                    bsp = BSPlotterProjected(band_data)
                    bsp.get_projected_plots_dots(dictio, ylim=ylims)
                    break
                else:
                    print("输入有误，请重新输入！")
                    continue

        save_figure_dpi300(outfile)

    @logger.catch
    def s4_4(self, infile, ylims, outfile):
        from dspawpy.io.read import get_band_data
        from pymatgen.electronic_structure.plotter import BSPlotterProjected

        band_data = get_band_data(infile)
        print(band_data.structure)
        es = band_data.structure.composition.elements
        for e in es:
            available_orbitals = ["s"]
            orbitals = e.atomic_orbitals
            for o in orbitals:
                if "p" in o:
                    available_orbitals.append("p")
                    available_orbitals.append("px")
                    available_orbitals.append("py")
                    available_orbitals.append("pz")
                elif "d" in o:
                    available_orbitals.append("d")
                    available_orbitals.append("dxy")
                    available_orbitals.append("dyz")
                    available_orbitals.append("dxz")
                    available_orbitals.append("dx2")
                    available_orbitals.append("dz2")
                elif "f" in o:
                    available_orbitals.append("f")
                    available_orbitals.append("f_3")
                    available_orbitals.append("f_2")
                    available_orbitals.append("f_1")
                    available_orbitals.append("f0")
                    available_orbitals.append("f1")
                    available_orbitals.append("f2")
                    available_orbitals.append("f3")

            unique_orbitals = list(set(available_orbitals))
            print(f"{str(e)}元素的可选轨道: ", unique_orbitals)

        dictio = {}
        while True:
            _n = input("--> 请选择一个原子序号（直接回车表示不再输入）: ")
            if _n == "":
                break
            _e = band_data.structure.sites[int(_n)].species_string
            dictpa = {_e: [int(_n) + 1]}
            _o = input(f" 请选择第{_n}号原子（{_e}）的轨道（用空格分隔）: ")
            _os = _o.split(" ")
            dict_eo = {_e: _os}
            # update dictio
            dictio.update(dict_eo)

        logger.info("------------------------------------")
        logger.info("选定的轨道元素字典: ", dictio)
        logger.info(" dictpa_d number 从1开始，而不是0")

        is_metal = band_data.is_metal()
        if is_metal:
            logger.info("正在处理，请稍等...")
            bsp = BSPlotterProjected(band_data)
            bsp.get_projected_plots_dots_patom_pmorb(dictio, dictpa, ylim=ylims)
        else:
            while True:
                shift = input(
                    "此为非金属体系，是否要将能量零点从价带顶平移至费米能级？(y/n)"
                )
                if shift.lower().startswith("y"):
                    logger.info("正在处理，请稍等...")
                    band_data = get_band_data(infile, zero_to_efermi=True)
                    bsp = BSPlotterProjected(band_data)
                    bsp.get_projected_plots_dots_patom_pmorb(
                        dictio, dictpa, zero_to_efermi=False, ylim=ylims
                    )
                    break
                elif shift.lower().startswith("n"):
                    logger.info("正在处理，请稍等...")
                    bsp = BSPlotterProjected(band_data)
                    bsp.get_projected_plots_dots_patom_pmorb(dictio, dictpa, ylim=ylims)
                    break
                else:
                    print("输入有误，请重新输入！")
                    continue

        save_figure_dpi300(outfile)

    @logger.catch
    def s4_5(self, infile, ylims, outfile):
        logger.info("正在处理，请稍等...")

        from dspawpy.plot import plot_bandunfolding

        plot_bandunfolding(infile)
        plt.ylim(ylims)
        save_figure_dpi300(outfile)

    @logger.catch
    def s4_6(
        self,
    ):
        infile1 = prompt("待解析瓦尼尔能带文件路径（包含文件名）：", completer=pc)
        infile2 = prompt("待解析普通能带文件路径（包含文件名）：", completer=pc)
        if infile1.endswith(".json"):
            infile3 = prompt(
                "待解析system.json文件路径（与wannier.json所在文件夹一致，包含文件名）：",
                completer=pc,
            )
            infile1 = [infile1, infile3]
        ylims = check_lims("输入y轴范围（先小后大，以空格分隔，直接回车可跳过设置）：")
        outfile = prompt("输出图片路径（包含文件名）：", completer=pc)
        logger.info("正在处理，请稍等...")

        from dspawpy.io.read import get_band_data
        from pymatgen.electronic_structure.plotter import BSPlotter

        if isinstance(infile1, list):  # wannier
            bd1 = get_band_data(infile1[0], infile1[1])
        else:  # str
            bd1 = get_band_data(infile1)
        bsp = BSPlotter(bs=bd1)
        bd2 = get_band_data(infile2)  # dft
        bsp2 = BSPlotter(bs=bd2)
        bsp.add_bs(bsp2._bs)
        bsp.get_plot(bs_labels=["wannier interpolated", "DFT"], ylim=ylims)
        save_figure_dpi300(outfile)

    @logger.catch
    def s5_1(self, dos_data, dos_plotter, xlims, ylims, outfile):
        """暂不支持修改绘图风格"""
        logger.info("正在处理，请稍等...")
        dos_plotter.add_dos("total dos", dos=dos_data)
        dos_plotter.get_plot(xlim=xlims, ylim=ylims)
        save_figure_dpi300(outfile)

    @logger.catch
    def s5_2(self, dos_data, dos_plotter, xlims, ylims, outfile):
        logger.info("正在处理，请稍等...")
        dos_plotter.add_dos_dict(dos_data.get_spd_dos())
        dos_plotter.get_plot(xlim=xlims, ylim=ylims)
        save_figure_dpi300(outfile)

    @logger.catch
    def s5_3(self, dos_data, dos_plotter, xlims, ylims, outfile):
        logger.info("正在处理，请稍等...")
        dos_plotter.add_dos_dict(dos_data.get_element_dos())
        dos_plotter.get_plot(xlim=xlims, ylim=ylims)
        save_figure_dpi300(outfile)

    @logger.catch
    def s5_4(self, dos_data, dos_plotter, xlims, ylims, outfile):
        iShift = input("是否平移费米能级？（y/n）：")
        while True:
            if iShift.lower().startswith("y"):
                break
            elif iShift.lower().startswith("n"):
                from pymatgen.electronic_structure.plotter import DosPlotter

                dos_plotter = DosPlotter(stack=False, zero_at_efermi=False)
                break
            else:
                iShift = input("输入错误，请重新输入：")
                continue

        # 获取元素和轨道列表
        print(dos_data.structure)
        es = dos_data.structure.composition.elements
        for e in es:
            available_orbitals = ["s"]
            orbitals = e.atomic_orbitals
            for o in orbitals:
                if "p" in o:
                    available_orbitals.append("p")
                    available_orbitals.append("px")
                    available_orbitals.append("py")
                    available_orbitals.append("pz")
                elif "d" in o:
                    available_orbitals.append("d")
                    available_orbitals.append("dxy")
                    available_orbitals.append("dyz")
                    available_orbitals.append("dxz")
                    available_orbitals.append("dx2")
                    available_orbitals.append("dz2")
                elif "f" in o:
                    available_orbitals.append("f")
                    available_orbitals.append("f_3")
                    available_orbitals.append("f_2")
                    available_orbitals.append("f_1")
                    available_orbitals.append("f0")
                    available_orbitals.append("f1")
                    available_orbitals.append("f2")
                    available_orbitals.append("f3")
            unique_orbitals = list(set(available_orbitals))
            print(f"{str(e)}元素的可选轨道: ", unique_orbitals)

        ns = []
        oss = []
        while True:
            _n = input("--> 请选择一个原子序号（直接回车表示不再输入）: ")
            if _n == "":
                break
            _e = dos_data.structure.sites[int(_n)].species_string
            _o = input(f" 请选择第{_n}号原子（{_e}）的轨道（用空格分隔）: ")
            _os = _o.split(" ")
            ns.append(_n)
            oss.append(_os)

        logger.info("正在处理，请稍等...")
        from pymatgen.electronic_structure.core import Orbital

        for _n, _os in zip(ns, oss):
            for _orb in _os:
                print(f"atom-{_n} {_orb}")
                dos_plotter.add_dos(
                    f"{_e}(atom-{_n}) {_orb}",  # label
                    dos_data.get_site_orbital_dos(
                        dos_data.structure[int(_n)], getattr(Orbital, _orb)
                    ),
                )
        dos_plotter.get_plot(xlim=xlims, ylim=ylims)
        save_figure_dpi300(outfile)

    @logger.catch
    def s5_5(self, dos_data, dos_plotter, xlims, ylims, outfile):
        iShift = input("是否平移费米能级？（y/n）：")
        while True:
            if iShift.lower().startswith("y"):
                break
            elif iShift.lower().startswith("n"):
                from pymatgen.electronic_structure.plotter import DosPlotter

                dos_plotter = DosPlotter(stack=False, zero_at_efermi=False)
                break
            else:
                iShift = input("输入错误，请重新输入：")
                continue

        print(dos_data.structure)
        ais = input("选择原子序号（用空格分隔）: ")
        logger.info("正在处理，请稍等...")

        atom_indices = [int(ai) for ai in ais.split()]
        for atom_index in atom_indices:
            dos_plotter.add_dos_dict(
                dos_data.get_site_t2g_eg_resolved_dos(dos_data.structure[atom_index])
            )

        dos_plotter.get_plot(xlim=xlims, ylim=ylims)
        save_figure_dpi300(outfile)

    @logger.catch
    def s5_6(self, dos_data):
        outfile = prompt("输出文本文件路径（包含文件名）：", completer=pc)
        logger.info("正在处理，请稍等...")

        from dspawpy.io.utils import d_band

        os.makedirs(os.path.dirname(os.path.abspath(args[-1])), exist_ok=True)
        with open(outfile, "w") as f:
            for spin in dos_data.densities:
                # up, down = (1, -1)
                if spin.value == 1:
                    s = "up"
                elif spin.value == -1:
                    s = "down"
                print("spin=", s)
                f.write(f"spin={s}\n")
                c = d_band(spin, dos_data)
                f.write(str(c) + "\n")
                print(c)

    @logger.catch
    def s6_1(self, bfile, dfile, ylims, outfile):
        logger.info("正在处理，请稍等...")
        from dspawpy.io.read import get_band_data, get_dos_data

        band_data = get_band_data(bfile)
        dos_data = get_dos_data(dfile)
        from pymatgen.electronic_structure.plotter import BSDOSPlotter

        bdp = BSDOSPlotter(dos_projection=None)
        from dspawpy.plot import pltbd

        pltbd(bdp, band_data, dos_data, ylim=ylims, filename=outfile)

    @logger.catch
    def s6_2(self, bfile, dfile, ylims, outfile):
        logger.info("正在处理，请稍等...")
        from dspawpy.io.read import get_band_data, get_dos_data

        band_data = get_band_data(bfile)
        dos_data = get_dos_data(dfile)
        from pymatgen.electronic_structure.plotter import BSDOSPlotter

        bdp = BSDOSPlotter(dos_projection="element")
        from dspawpy.plot import pltbd

        pltbd(bdp, band_data, dos_data, ylim=ylims, filename=outfile)

    @logger.catch
    def s7(
        self,
    ):
        infile = prompt("待解析文件路径（包含文件名）：", completer=pc)
        _list = [
            "AbsorptionCoefficient",
            "ExtinctionCoefficient",
            "RefractiveIndex",
            "Reflectance",
        ]
        key = until_give_valid_input(
            f"数据类型（可选 {_list}）：",
            _list,
            completer=WordCompleter(_list),
        )
        _list2 = ["X", "Y", "Z", "XY", "YZ", "ZX"]
        label = until_give_valid_input(
            f"指定数据 {_list2}：",
            _list2,
            completer=WordCompleter(_list2),
        )

        outfile = prompt("输出文件路径（包含文件名）：", completer=pc)
        logger.info("正在处理，请稍等...")

        from dspawpy.plot import plot_optical

        # given X, index=0, given Y, index=1, given Z, index=2
        dd = {"X": 0, "Y": 1, "Z": 2, "XY": 3, "YZ": 4, "ZX": 5}

        plot_optical(datafile=infile, key=key, index=dd[label])
        plt.xlabel("Photon energy (eV)")
        plt.ylabel(key)
        plt.tick_params()
        absfile = os.path.abspath(outfile)
        os.makedirs(os.path.dirname(absfile), exist_ok=True)
        plt.tight_layout()
        plt.savefig(absfile, dpi=300)

    @logger.catch
    def s8_1(
        self,
    ):
        """插值NEB链"""
        inis = prompt("初态构型文件路径（包含文件名）：", completer=pc)
        fins = prompt("末态构型文件路径（包含文件名）：", completer=pc)
        nmiddle = int(input("初末态之间插入几个构型："))
        method = until_give_valid_input("插值方法（IDPP/Linear）：", ["IDPP", "Linear"])
        outdir = prompt("输出文件夹（直接回车表示当前文件夹）：", completer=pc)
        if outdir == "":
            outdir = "."
        logger.info("正在处理，请稍等...")

        from dspawpy.diffusion.neb import NEB, write_neb_structures
        from dspawpy.io.structure import read

        init_struct = read(inis)[0]
        final_struct = read(fins)[0]

        neb = NEB(init_struct, final_struct, nmiddle + 2)
        if method == "Linear":
            structures = neb.linear_interpolate()  # 线性插值
        elif method == "IDPP":
            try:
                structures = neb.idpp_interpolate()  # idpp插值
            except Exception:
                logger.error("  IDPP插值失败，请检查构型是否合理！")
                structures = neb.linear_interpolate()
                logger.warning("  已自动转为线性插值！")
        else:
            raise ValueError("Unknown interpolation method: {}".format(method))
        # 保存 as 结构文件到 dest 路径下
        absdir = os.path.abspath(outdir)
        os.makedirs(os.path.dirname(absdir), exist_ok=True)
        write_neb_structures(structures, fmt="as", path=absdir)
        logger.info(f"已将插值后的构型保存到{absdir}路径下")

        while True:
            yn = input("是否预览插值链？（y/n）")
            if yn.lower().startswith("y"):
                from dspawpy.diffusion.nebtools import write_json_chain

                write_json_chain(preview=True, directory=absdir)
                break
            elif yn.lower().startswith("n"):
                break
            else:
                print("输入错误，请重新输入！")
                continue

    @logger.catch
    def s8_2(
        self,
    ):
        """绘制NEB势垒"""
        infile = prompt(
            "待解析neb.h5/neb.json路径（包含文件名）或NEB文件夹：", completer=pc
        )
        outfile = prompt("输出图片路径（包含文件名）：", completer=pc)
        logger.info("插值方法默认使用pchip，如果要用其他方法，请使用独立脚本")
        logger.info("正在处理，请稍等...")

        from dspawpy.diffusion.nebtools import plot_barrier

        if os.path.isdir(infile):
            plot_barrier(directory=infile, figname=outfile, show=False)
        elif os.path.isfile(infile):
            plot_barrier(datafile=infile, figname=outfile, show=False)
        else:
            raise ValueError(f"{infile} 必须是文件或文件夹路径")

    @logger.catch
    def s8_3(
        self,
    ):
        """输出NEB计算结果"""
        datafolder = prompt("NEB计算文件夹：", completer=pc)
        outdir = prompt("输出到文件夹（直接回车表示当前文件夹）：", completer=pc)
        logger.info("正在处理，请稍等...")

        from dspawpy.diffusion.nebtools import summary

        assert os.path.isdir(datafolder), f"{datafolder} 必须是文件夹路径"
        absdir = os.path.abspath(outdir)
        os.makedirs(os.path.dirname(absdir), exist_ok=True)
        summary(
            directory=datafolder,
            outdir=absdir,
            figname=f"{absdir}/neb_summary.png",
            show=False,
        )

    @logger.catch
    def s8_4(
        self,
    ):
        """输出插值链"""
        preview = until_give_valid_input(
            "预览插值生成的NEB链（无需完成计算）（y/n）：", ["y", "n"]
        )
        directory = prompt("NEB计算文件夹：", completer=pc)
        if preview == "y":
            step = 0
        else:
            step = int(input("第几个离子步（从1开始计数，-1表示最新构型）："))
        dst = prompt("输出到文件夹（直接回车表示当前文件夹）：", completer=pc)
        json_or_xyz = until_give_valid_input(
            "输出文件格式（json/xyz）：", ["json", "xyz"]
        )
        logger.info("正在处理，请稍等...")

        if json_or_xyz.startswith("xyz"):
            from dspawpy.diffusion.nebtools import write_xyz_chain

            write_xyz_chain(False, directory, step, dst)
        else:
            from dspawpy.diffusion.nebtools import write_json_chain

            write_json_chain(False, directory, step, dst)

    @logger.catch
    def s8_5(
        self,
    ):
        """计算两个构型的距离"""
        infile1 = prompt("第一个构型路径（包含文件名）：", completer=pc)
        infile2 = prompt("第二个构型路径（包含文件名）：", completer=pc)
        logger.info("正在处理，请稍等...")

        from dspawpy.io.structure import read

        s1 = read(infile1)[0]
        s2 = read(infile2)[0]
        from dspawpy.diffusion.nebtools import get_distance

        dist = get_distance(
            s1.frac_coords, s2.frac_coords, s1.lattice.matrix, s2.lattice.matrix
        )
        logger.info(f"两个构型的距离为：{dist} Angstrom")

    @logger.catch
    def s8_6(
        self,
    ):
        """续算"""
        dataFolder = prompt("NEB计算文件夹：", completer=pc)
        outdir = prompt("备份文件夹：", completer=pc)
        logger.info("正在处理，请稍等...")

        from dspawpy.diffusion.nebtools import restart

        restart(dataFolder, outdir)

    @logger.catch
    def s9_1(
        self,
    ):
        infile = prompt("待解析文件路径（包含文件名）：", completer=pc)
        ylims = check_lims("输入y轴范围（先小后大，空格分隔，直接回车可跳过）：")
        outfile = prompt("输出文件路径（包含文件名）：", completer=pc)
        logger.info("正在处理，请稍等...")

        from dspawpy.io.read import get_phonon_band_data

        band_data = get_phonon_band_data(infile)  # 读取声子能带

        with HiddenPrints():
            from pymatgen.phonon.plotter import PhononBSPlotter

        bsp = PhononBSPlotter(band_data)
        bsp.get_plot(ylim=ylims)
        save_figure_dpi300(outfile)

    @logger.catch
    def s9_2(
        self,
    ):
        infile = prompt("待解析文件路径（包含文件名）：", completer=pc)
        xlims = check_lims("输入x轴范围（先小后大，空格分隔，直接回车可跳过）：")
        ylims = check_lims("输入y轴范围（先小后大，空格分隔，直接回车可跳过）：")
        outfile = prompt("输出文件路径（包含文件名）：", completer=pc)
        logger.info("正在处理，请稍等...")

        from dspawpy.io.read import get_phonon_dos_data

        dos = get_phonon_dos_data(infile)  # 读取声子能带
        with HiddenPrints():
            from pymatgen.phonon.plotter import PhononDosPlotter
        dp = PhononDosPlotter(stack=False, sigma=None)
        dp.add_dos(label="Phonon", dos=dos)
        dp.get_plot(
            xlim=xlims,  # x轴范围
            ylim=ylims,  # y轴范围
            units="thz",  # 单位
        )

        save_figure_dpi300(outfile)

    @logger.catch
    def s9_3(
        self,
    ):
        infile = prompt("待解析文件路径（包含文件名）：", completer=pc)
        outfile = prompt("输出文件路径（包含文件名）：", completer=pc)
        logger.info("正在处理，请稍等...")

        from dspawpy.plot import plot_phonon_thermal

        plot_phonon_thermal(infile, outfile, False)

    @logger.catch
    def s10_1(
        self,
    ):
        infile = prompt("待解析文件路径（包含文件名）：", completer=pc)
        outfile = prompt("输出文件路径（包含.xyz或.dump文件名）：", completer=pc)
        logger.info("正在处理，请稍等...")

        from dspawpy.io.structure import convert

        convert(infile, outfile=outfile)

    @logger.catch
    def s10_2(
        self,
    ):
        infile = prompt("待解析文件路径（包含文件名）：", completer=pc)
        outfile = prompt("输出文件路径（包含文件名）：", completer=pc)
        logger.info("正在处理，请稍等...")

        from dspawpy.plot import plot_aimd

        plot_aimd(infile, show=False, figname=outfile)

    @logger.catch
    def s10_3(
        self,
    ):
        infile = prompt("待解析文件路径（包含文件名）：", completer=pc)
        outfile = prompt("MSD图片输出路径（包含文件名）：", completer=pc)
        logger.info("正在处理，请稍等...")

        from dspawpy.analysis.aimdtools import MSD, _get_time_step, plot_msd
        from dspawpy.io.structure import read

        structures = read(infile)
        elements = [str(i) for i in structures[0].species]
        unique_elements = list(set(elements))
        select_str = input(
            f"元素列表\n{elements}\n去重后\n{unique_elements}\n选择原子或元素（以空格隔开）："
        )
        boss = select_str.strip()
        if boss == "":
            select = "all"
        else:
            if ":" in boss:  # slice, '1:3', '1:3:2'
                select = boss
            elif " " in boss:  # list of symbols or atom indices, '1 2 3', 'H He Li'
                raw_list = boss.split()
                if all([i.isdigit() for i in raw_list]):
                    select = [int(i) for i in raw_list]
                elif all([i in unique_elements for i in raw_list]):
                    select = raw_list
                else:
                    raise ValueError(f"Invalid input for select_str={select_str}")
            else:
                # single symbol or atom index
                # boss may be H1, must remove digit before checking
                if boss in unique_elements:
                    select = boss  # symbol
                elif boss.isdigit():
                    select = int(boss)  # atom index
                else:
                    raise ValueError(f"Invalid input for select_str={select_str}")

        print(select)
        msd_type = until_give_valid_input(
            "计算MSD的类型，可选xyz,xy,xz,yz,x,y,z，（直接回车等同于'xyz'，表示计算所有分量）",
            ["xyz", "xy", "xz", "yz", "x", "y", "z", ""],
        )
        timestep = input(
            f"输入时间步长（fs），直接回车将尝试从{infile}中自动读取，失败则此数值将设为1.0："
        )
        xlims = check_lims("输入x轴下限和上限，用空格分隔，直接回车将自动设置")
        ylims = check_lims("输入y轴下限和上限，用空格分隔，直接回车将自动设置")

        if msd_type == "":
            msd_type = "xyz"

        if timestep == "":
            if isinstance(infile, str) or len(infile) == 1:
                ts = _get_time_step(infile)
            else:
                logger.warning(
                    "For multiple datafiles, you must manually specify the timestep. It will default to 1.0fs."
                )
                ts = 1.0
        else:
            ts = float(timestep)

        msd_calculator = MSD(structures, select, msd_type)
        msd = msd_calculator.run()

        import numpy as np

        xs = np.arange(msd_calculator.n_frames) * ts
        plot_msd(xs, msd, xlims, ylims, figname=outfile, show=False)

    @logger.catch
    def s10_4(
        self,
    ):
        infile = prompt("待解析文件路径（包含文件名）：", completer=pc)
        timestep = input(
            f"输入时间步长（fs），直接回车将尝试从{infile}中自动读取，失败则此数值将设为1.0："
        )
        if timestep == "":
            timestep = None
        else:
            timestep = float(timestep)
        xlims = check_lims("输入x轴下限和上限，用空格分隔，直接回车将自动设置")
        ylims = check_lims("输入y轴下限和上限，用空格分隔，直接回车将自动设置")
        outfile = prompt("RMSD图片输出路径（包含文件名）：", completer=pc)
        logger.info("正在处理，请稍等...")

        from dspawpy.analysis.aimdtools import get_lagtime_rmsd, plot_rmsd

        lagtime, rmsd = get_lagtime_rmsd(infile, timestep)
        plot_rmsd(lagtime, rmsd, xlims, ylims, outfile, False)

    @logger.catch
    def s10_5(
        self,
    ):
        infile = prompt("待解析文件路径（包含文件名）：", completer=pc)
        logger.info("正在处理，请稍等...")
        from dspawpy.analysis.aimdtools import get_rs_rdfs, plot_rdf
        from dspawpy.io.structure import read

        strs = read(datafile=infile)
        elements = [str(i) for i in strs[0].species]
        unique_elements = list(set(elements))
        print(f" 元素列表：{elements}\n 去重后：{unique_elements}")
        ele1 = until_give_valid_input("--> 请选择一个中心元素：", unique_elements)
        ele2 = until_give_valid_input("--> 请选择一个对象元素：", unique_elements)

        rmin = input("请输入最小半径, Å （默认0）:")
        if rmin == "":
            rmin = 0
        else:
            rmin = float(rmin)

        rmax = input("请输入最大半径, Å（默认10）:")
        if rmax == "":
            rmax = 10
        else:
            rmax = float(rmax)

        ngrid = input("请输入网格数（默认101，包含端点）:")
        if ngrid == "":
            ngrid = 101
        else:
            ngrid = int(ngrid)

        sigma = input("请输入sigma值（用于一维高斯函数平滑处理，默认0，不处理）:")
        if sigma == "":
            sigma = 0
        else:
            sigma = float(sigma)

        xlims = [rmin, rmax]
        ylims = check_lims("请依次输入y轴下限与上限，用空格分隔（默认不指定）:")
        outfile = prompt("RDF图片输出路径（包含文件名）：", completer=pc)

        rs, rdfs = get_rs_rdfs(infile, ele1, ele2, rmin, rmax, ngrid, sigma)
        plot_rdf(rs, rdfs, ele1, ele2, xlims, ylims, outfile, False)

    @logger.catch
    def s11(
        self,
    ):  # --> pol.png
        infile = prompt("已完成铁电极化计算任务的文件夹：", completer=pc)
        repetition = int(input("请输入数据点绘图时重复次数（默认2）："))
        if repetition == "":
            repetition = 2
        outfile = prompt("图片输出路径（包含文件名）：", completer=pc)
        logger.info("正在处理，请稍等...")

        from dspawpy.plot import plot_polarization_figure

        plot_polarization_figure(infile, repetition, figname=outfile, show=False)

    @logger.catch
    def s12(
        self,
    ):
        infile = prompt("待解析frequency.txt文件路径（包含文件名）：", completer=pc)
        outfile = prompt("输出文本文件路径（包含文件名）：", completer=pc)
        logger.info("正在处理，请稍等...")

        from dspawpy.io.utils import getZPE

        print(getZPE(infile, outfile))

    @logger.catch
    def s13_1(
        self,
    ):
        infile = prompt("待解析frequency.txt文件路径（包含文件名）：", completer=pc)
        temperature = float(input("请输入温度(K)："))
        outfile = prompt("输出文本文件路径（包含文件名）：", completer=pc)
        logger.info("正在处理，请稍等...")

        from dspawpy.io.utils import getTSads

        TSads = getTSads(infile, temperature, outfile)
        print("Entropy contribution, T*S (eV): ", TSads)

    @logger.catch
    def s13_2(
        self,
    ):
        fretxt = prompt("待解析frequency.txt文件路径（包含文件名）：", completer=pc)
        infile = prompt("待解析h5/json文件路径（包含文件名）：", completer=pc)
        temperature = float(input("请输入温度(K)："))
        pressure = float(input("请输入压强(Pa)："))
        outfile = prompt("输出文本文件路径（包含文件名）：", completer=pc)
        logger.info("如果要设置更多参数，请参考手册相应章节的独立脚本")
        logger.info("正在处理，请稍等...")

        from dspawpy.io.utils import getTSgas

        TSgas = getTSgas(
            fretxt=fretxt,
            datafile=infile,
            temperature=temperature,
            pressure=pressure,
            outfile=outfile,
        )
        print("--> T*S (eV): ", TSgas)


@logger.catch
def save_figure_dpi300(outfile):
    absfile = os.path.abspath(outfile)
    os.makedirs(os.path.dirname(absfile), exist_ok=True)
    plt.tight_layout()
    plt.savefig(absfile, dpi=300)
    print(f"--> {absfile}")


if __name__ == "__main__":
    main()
