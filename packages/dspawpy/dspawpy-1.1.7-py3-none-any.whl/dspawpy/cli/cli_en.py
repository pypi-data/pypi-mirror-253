# -*- coding: utf-8 -*-
main_menu = """
1: dspawpy upgrading
2: structure file transforming
3: volumetric data processing
4: band plotting
5: dos plotting  
6: bandDos aligned plotting
7: optical calculation post processing 
8: neb calculation pre&post processing 
9: phonon calculation post processing 
10: aimd calculation post processing 
11: polarization calculation post processing 
12: ZPE correction 
13: entropy correction
--> enter a number and press 'Enter' to select corresponding action: """

menu3 = """
=== 3 volumetric data processing ===

  1: volumetricData visualization 
  2: volumetricData difference visualization 
  3: planer averaged volumetricData 
  
  0: return to main menu 
  --> enter a number and press 'Enter' to select corresponding action: """

menu4 = """
=== 4 band plotting ===

  1: regular band plotting 
  2: element projected band plotting (contributions are represented by point size)
  3: element's orbital projected band plotting (contributions are represented by point size)
  4: atom's orbital projected band plotting (contributions are represented by point size)
  5: band unfolding plotting 
  6. band-compare plotting
  
  0: return to main menu 
  --> enter a number and press 'Enter' to select corresponding action: """

menu5 = """
=== 5 dos plotting ===

  1: total dos plotting 
  2: orbital projected dos plotting 
  3: element projected dos plotting 
  4: atom's orbital projected dos plotting 
  5: atom's splited d orbital (t2g, eg) projected dos plotting 
  6: d-band center analysis
  
  0: return to main menu 
 --> enter a number and press 'Enter' to select corresponding action: """

menu6 = """
=== 6 bandDos aligned plotting ===

  1: regular band and total dos aligned plotting 
  2: regular band and projected dos aligned plotting 
  
  0: return to main menu 
  --> enter a number and press 'Enter' to select corresponding action: """

menu8 = """
=== 8 neb calculation pre&post processing ===

  1: input structure file preparing : structure interpolation 
  2: barrier plotting 
  3: NEB calculation inspecting
  4: NEB movie
  5: root mean square displacement between structures calculating 
  6: neb restarting 
  
  0: return to main menu 
  --> enter a number and press 'Enter' to select corresponding action: """

menu9 = """
=== 9 phonon calculation post processing ===

  1: phonon band plotting
  2: phonon dos plotting
  3: thermo data from phonon
  
  0: return to main menu 
  --> enter a number and press 'Enter' to select corresponding action: """

menu10 = """
  === 10 aimd calculation post processing ===
  
  1: trajectory file transforming
  2: calculation monitoring: energy, temperature, volume...
  3: MSD deriving
  4. RMSD deriving
  5. RDF deriving
  
  0: return to main menu 
  --> enter a number and press 'Enter' to select corresponding action: """

menu13 = """
  === 13 entropy thermal correction ===
  
  1: adsorption entropy correction
  2: ideal gas entropy correction
  
  0: return to main menu 
  --> enter a number and press 'Enter' to select corresponding action: """


import os  # noqa: E402
from argparse import ArgumentParser  # noqa: E402

argparser = ArgumentParser("dspawpy command line interface tool")
argparser.add_argument(
    "-q", "--quick", action="store_true", help="do not check for updates"
)
argparser.add_argument("-c", "--clean", action="store_true", help="hide dspawpy_logo")
args = argparser.parse_args()

try:
    pass
except ImportError:
    cmd = "pip install dspawpy"
    if os.system(cmd) != 0:
        raise ImportError(
            f"Failed to install dependencies, please manually try this command $ {cmd}"
        )


def online_check(dv, df):
    latest_version = None
    try:
        print("Checking for updates..., you may skip this using -q option")
        response = get("https://pypi.org/pypi/dspawpy/json", timeout=3)
        latest_version = response.json()["info"]["version"]
        error_message = None
    except ImportError:
        error_message = "cannot import requests"
    except exceptions.Timeout:
        error_message = "requests timeout"
    except exceptions.RequestException as e:
        error_message = f"requests got error: {e}"
    except Exception as e:
        error_message = f"failed to check dspawpy versioon: {e}"
    finally:
        if latest_version:
            if latest_version != dv:
                print(
                    f"\n imported dspawpy={dv} (latest={latest_version}), you may upgrade it by calling module 1.2"
                )
                print(
                    f" dspawpy is in (if not as expected, please check env settings): \n {df}\n"
                )
            else:
                print(f"\n         imported dspawpy={dv} (latest) \n")

            with open(os.path.expanduser("~/.dspawpy_latest_version"), "w") as fin:
                fin.write(latest_version)

        else:
            print(
                f"\n         imported dspawpy={dv} (failed to check the latest version online)\n"
            )

    return error_message


def verify_dspawpy_version(skip=False):
    error_message = None
    try:
        import dspawpy

        try:
            dv = dspawpy.__version__
        except Exception:
            dv = "??? version too old to have __version__ attribute"
        finally:
            df = os.path.dirname(dspawpy.__file__)

        if skip:
            print(f"\n         imported dspawpy={dv}\n")
        else:
            if os.path.isfile(os.path.expanduser("~/.dspawpy_latest_version")):
                with open(os.path.expanduser("~/.dspawpy_latest_version"), "r") as fin:
                    latest_version = fin.read().strip()
                if dv == latest_version:
                    print(f"\n         imported dspawpy={dv} (latest) \n")
                else:
                    error_message = online_check(dv, df)
            else:
                error_message = online_check(dv, df)

    except ImportError:
        print("  Can't import dspawpy, Please install. Try tag 1 in following menu")
    except Exception as e:
        error_message = f"something wrong when importing dspawpy: {e}"

    print("This is a command line interactive tool based on dspawpy, enjoy")
    if error_message is not None:
        print(error_message)


def collect_user_input() -> list:
    if args.clean:
        dspawpy_logo = ""
    else:
        dspawpy_logo = r"""
This is a command line interactive tool based on dspawpy, enjoy
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

    while True:
        n = input(main_menu)
        if n == "1":
            cmd = "pip install dspawpy --user -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install -U dspawpy -i https://pypi.org/simple --user"
            while True:
                yn = input(f"About to run\n {cmd}\n (y/n)? ")
                if yn.lower() == "y":
                    if os.system(cmd) == 0:
                        print(">>>>>> Succeed")
                        print("Restart this tool to use")
                    else:
                        print("!!!!!! Failed")
                    break
                elif yn.lower() == "n":
                    print("###### Cancelled")
                    break
                else:
                    print("!!! Invalid input, Please try again")
                    continue

        elif n == "2":
            return 2, 0

        elif n == "3":
            while True:
                n = input(menu3)
                if n not in ["0", "1", "2", "3"]:
                    print("!!! unacceptable input, Please try again")
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
                    print("!!! unacceptable input, Please try again")
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
                    print("!!! unacceptable input, Please try again")
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
                    print("!!! unacceptable input, Please try again")
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
                    print("!!! unacceptable input, Please try again")
                    continue
                elif n == "1":
                    return 8, 1
                elif n == "2":
                    return 8, 2
                elif n == "3":
                    return 8, 3
                elif n == "4":
                    return 8, 4
                elif n == "5":
                    return 8, 5
                elif n == "6":
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
                    print("!!! unacceptable input, Please try again")
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
                    print("!!! unacceptable input, Please try again")
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
                    logger.error("!!! unacceptable input, Please try again")
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
            print("XXXXXX unacceptable input, Please try again XXXXXX")
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
            infile = prompt(
                "Please enter the path to the file (including file name): ",
                completer=pc,
            )
            ylims = check_lims(
                "Please input y-axis range (less and larger, separated by space): "
            )
            outfile = prompt(
                "Please enter the path to the output file (including file name): ",
                completer=pc,
            )
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
        infile = prompt(
            "Please enter the path to the file (including file name): ", completer=pc
        )
        from dspawpy.io.read import get_dos_data

        dosdata = get_dos_data(infile)
        from pymatgen.electronic_structure.plotter import DosPlotter

        dos_plotter = DosPlotter(stack=False, zero_at_efermi=True)
        if task_number[1] != 6:
            xlims = check_lims(
                "Please input x-axis range (less and larger, separated by space):"
            )
            ylims = check_lims(
                "Please input y-axis range (less and larger, separated by space): "
            )
            outfile = prompt(
                "Please enter the path to the output file (including file name): ",
                completer=pc,
            )
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
        infile1 = prompt(
            "Please enter the path to the band file (including file name): ",
            completer=pc,
        )
        infile2 = prompt(
            "Please enter the path to the dos file (including file name): ",
            completer=pc,
        )
        ylims = check_lims(
            "Please input y-axis range (less and larger, separated by space): "
        )
        outfile = prompt(
            "Please enter the path to the output file (including file name): ",
            completer=pc,
        )
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

matplotlib.use("agg")
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
            print("!!! unacceptable input, Please try again")
            continue


def check_lims(user_prompt):
    # return None or [float, float]
    while True:
        userInput = input(user_prompt).strip()
        if userInput == "":
            return None
        else:
            if " " not in userInput:
                logger.warning(
                    f"!!! {userInput} num1 and num2 should be separated by space"
                )
                continue
            elif len(userInput.split(" ")) != 2:
                logger.warning(f"!!! {userInput} expecting num1 and num2")
                continue
            else:
                try:
                    float(userInput.split(" ")[0])
                    float(userInput.split(" ")[1])
                    return userInput.split(" ")  # return '1_2'
                except Exception:
                    logger.warning(f"!!! {userInput} num1 and num2 should be numeric")
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
            "Please enter the path to the file (including file name, support h5, json, pdb, as, hzw, ...): ",
            completer=pc,
        )
        outfile = prompt(
            "Please enter the path to the output file (include file name, support pdb, xyz, dump, json, as, hzw, ...): ",
            completer=pc,
        )
        logger.info("Processing...")

        from dspawpy.io.structure import convert

        convert(infile=infile, outfile=outfile)

    @logger.catch
    def s3_1(
        self,
    ):
        infile = prompt(
            "Please enter the path to the file (including file name): ", completer=pc
        )
        _list = ["rho", "potential", "elf", "pcharge", "rhoBound"]
        wc = WordCompleter(_list)
        task = until_give_valid_input(
            f"Task type{_list}:",
            _list,
            completer=wc,
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
                        f"Got no subtype, please check {infile} or given task type!"
                    )
                elif len(keys) == 1:
                    subtype = keys[0]
                else:
                    subtype = until_give_valid_input(
                        f"Got {keys} subtype, select one: ",
                        keys,
                        completer=WordCompleter(keys),
                    )

            elif infile.endswith(".json"):
                import json

                with open(infile, "r") as fin:
                    data = json.load(fin)
                    if "Potential" not in data.keys():
                        raise ValueError(
                            f"Got no subtype, please check {infile} or given task type!"
                        )
                    keys = data["Potential"].keys()

                if len(keys) == 1:
                    subtype = keys[0]
                else:
                    subtype = until_give_valid_input(
                        f"Got {keys} subtype, select one: ",
                        keys,
                        completer=WordCompleter(keys),
                    )
            else:
                raise ValueError(
                    f"{infile.split('.')[-1]} is neither h5 nor json format!"
                )

        outfile = prompt(
            "Please enter the path to the output file (include file name, support .cube / .vasp / .vesta suffix): ",
            completer=pc,
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
                " specify format (cube, vasp): ", ["cube", "vesta", "vasp"]
            )

        logger.info("Processing...")
        from dspawpy.io.write import write_VESTA

        write_VESTA(
            in_filename=infile,
            data_type=task,
            out_filename=outfile,
            subtype=subtype,
            format=cube_or_vasp,
        )
        logger.info("You may visualize the output file by VESTA software")

    @logger.catch
    def s3_2(
        self,
    ):
        total = prompt(
            "Please enter the total charge density (include file name): ", completer=pc
        )
        individuals = []
        while True:
            individual = prompt(
                "Please enter the individual charge density (include file name, directly Enter to skip):",
                completer=pc,
            )
            if individual == "":
                break
            individuals.append(individual)

        outfile = prompt(
            "Please enter the path to the output file (include file name, support .cube / .vasp): ",
            completer=pc,
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
                " specify format (cube, vesta): ", ["cube", "vesta", "vasp"]
            )

        logger.info("Processing...")
        from dspawpy.io.write import write_delta_rho_vesta

        write_delta_rho_vesta(
            total=total, individuals=individuals, output=outfile, format=cube_or_vasp
        )
        logger.info("You may visualize the output file by VESTA software")

    @logger.catch
    def s3_3(
        self,
    ):
        infile = prompt(
            "Please enter the path to the file (including file name): ", completer=pc
        )
        axes = until_give_valid_input("Along what axes (0, 1, 2):", ["0", "1", "2"])
        _list = ["rho", "potential", "elf", "pcharge", "rhoBound"]
        task = until_give_valid_input(
            f"Task type {_list}:",
            _list,
            completer=WordCompleter(_list),
        )
        outfile = prompt(
            "Please enter the path to the output file (including file name): ",
            completer=pc,
        )

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
                        f"Got no subtype, please check {infile} or given task type!"
                    )
                elif len(keys) == 1:
                    subtype = keys[0]
                else:
                    subtype = until_give_valid_input(
                        f"Got {keys} subtype, select one: ",
                        keys,
                        completer=WordCompleter(keys),
                    )
            elif infile.endswith(".json"):
                import json

                with open(infile, "r") as fin:
                    data = json.load(fin)
                    if "Potential" not in data.keys():
                        raise ValueError(
                            f"Got no subtype, please check {infile} or given task type!"
                        )
                    keys = data["Potential"].keys()

                if len(keys) == 1:
                    subtype = keys[0]
                else:
                    subtype = until_give_valid_input(
                        f"Got {keys} subtype, select one: ",
                        keys,
                        completer=WordCompleter(keys),
                    )
            else:
                raise ValueError(
                    f"{infile.split('.')[-1]} is neither h5 nor json format!"
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

        logger.info("Processing...")
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
            logger.info("Processing...")
            bsp = BSPlotter(band_data)
            bsp.get_plot(ylim=ylims)
        else:
            while True:
                shift = input("Non-metallic system, shift the Efermi?(y/n)")
                if shift.lower().startswith("y"):
                    logger.info("Processing...")
                    from dspawpy.io.read import get_band_data

                    band_data = get_band_data(infile, zero_to_efermi=True)
                    bsp = BSPlotter(band_data)
                    bsp.get_plot(False, ylim=ylims)
                    break
                elif shift.lower().startswith("n"):
                    logger.info("Processing...")
                    bsp = BSPlotter(band_data)
                    bsp.get_plot(ylim=ylims)
                    break
                else:
                    print("Invalid input, please re-enter")
                    continue

        save_figure_dpi300(outfile)

    @logger.catch
    def s4_2(self, infile, ylims, outfile):
        from dspawpy.io.read import get_band_data
        from pymatgen.electronic_structure.plotter import BSPlotterProjected

        band_data = get_band_data(infile)
        is_metal = band_data.is_metal()
        if is_metal:
            logger.info("Processing...")
            bsp = BSPlotterProjected(band_data)
            bsp.get_elt_projected_plots(ylim=ylims)
        else:
            while True:
                shift = input("Non-metallic system, shift the Efermi?(y/n)")
                if shift.lower().startswith("y"):
                    logger.info("Processing...")
                    band_data = get_band_data(infile, zero_to_efermi=True)
                    bsp = BSPlotterProjected(band_data)
                    bsp.get_elt_projected_plots(False, ylim=ylims)
                    break
                elif shift.lower().startswith("n"):
                    logger.info("Processing...")
                    bsp = BSPlotterProjected(band_data)
                    bsp.get_elt_projected_plots(ylim=ylims)
                    break
                else:
                    print("Invalid input, please re-enter")
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
            print("Avaliable elements: ", str(e))
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
            print(f"Avaliable orbitals for {str(e)}", unique_orbitals)

        dictio = {}
        while True:
            _e = input("Select one element (Enter to skip): ")
            if _e == "":
                break
            _o = input(f"Select orbital for {_e} (separated by space): ")
            _os = _o.split(" ")
            dict_eo = {_e: _os}
            # update dictio
            dictio.update(dict_eo)

        print("Summary for your selection: ", dictio)

        is_metal = band_data.is_metal()
        if is_metal:
            logger.info("Processing...")
            bsp = BSPlotterProjected(band_data)
            bsp.get_projected_plots_dots(dictio)
        else:
            while True:
                shift = input("Non-metallic system, shift the Efermi?(y/n)")
                if shift.lower().startswith("y"):
                    logger.info("Processing...")
                    band_data = get_band_data(infile, zero_to_efermi=True)
                    bsp = BSPlotterProjected(band_data)
                    bsp.get_projected_plots_dots(dictio, False, ylim=ylims)
                    break
                elif shift.lower().startswith("n"):
                    logger.info("Processing...")
                    bsp = BSPlotterProjected(band_data)
                    bsp.get_projected_plots_dots(dictio, ylim=ylims)
                    break
                else:
                    print("Invalid input, please re-enter")
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
            print(f"Avaliable orbitals for {str(e)}", unique_orbitals)

        dictio = {}
        while True:
            _n = input("--> Select one atom index (Enter to skip): ")
            if _n == "":
                break
            _e = band_data.structure.sites[int(_n)].species_string
            dictpa = {_e: [int(_n) + 1]}
            _o = input(f" Select orbital for {_n} atom ({_e}) (separated by space): ")
            _os = _o.split(" ")
            dict_eo = {_e: _os}
            # update dictio
            dictio.update(dict_eo)

        logger.info("------------------------------------")
        logger.info("Summary for your selection: ", dictio)
        logger.info(" dictpa_d number starts from 1, not 0, FYI")

        is_metal = band_data.is_metal()
        if is_metal:
            logger.info("Processing...")
            bsp = BSPlotterProjected(band_data)
            bsp.get_projected_plots_dots_patom_pmorb(dictio, dictpa, ylim=ylims)
        else:
            while True:
                shift = input("Non-metallic system, shift the Efermi?(y/n)")
                if shift.lower().startswith("y"):
                    logger.info("Processing...")
                    band_data = get_band_data(infile, zero_to_efermi=True)
                    bsp = BSPlotterProjected(band_data)
                    bsp.get_projected_plots_dots_patom_pmorb(
                        dictio, dictpa, zero_to_efermi=False, ylim=ylims
                    )
                    break
                elif shift.lower().startswith("n"):
                    logger.info("Processing...")
                    bsp = BSPlotterProjected(band_data)
                    bsp.get_projected_plots_dots_patom_pmorb(dictio, dictpa, ylim=ylims)
                    break
                else:
                    print("Invalid input, please re-enter")
                    continue

        save_figure_dpi300(outfile)

    @logger.catch
    def s4_5(self, infile, ylims, outfile):
        logger.info("Processing...")

        from dspawpy.plot import plot_bandunfolding

        plot_bandunfolding(infile)
        plt.ylim(ylims)
        save_figure_dpi300(outfile)

    @logger.catch
    def s4_6(
        self,
    ):
        infile1 = prompt(
            "Please the the path to wannier.h5/wannier.json to be parsed (include file name): ",
            completer=pc,
        )
        infile2 = prompt(
            "Please the the path to dft band structure file to be parsed (include file name): ",
            completer=pc,
        )
        if infile1.endswith(".json"):
            infile3 = prompt(
                "Please the the path to the system.json to be parsed(the same path to wannier.json, include file name): ",
                completer=pc,
            )
            infile1 = [infile1, infile3]
        ylims = check_lims(
            "Please input y-axis range (less and larger, separated by space):"
        )
        outfile = prompt(
            "Please enter the path to the output file (including file name): ",
            completer=pc,
        )
        logger.info("Processing...")

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
        logger.info("Processing...")
        dos_plotter.add_dos("total dos", dos=dos_data)
        dos_plotter.get_plot(xlim=xlims, ylim=ylims)
        save_figure_dpi300(outfile)

    @logger.catch
    def s5_2(self, dos_data, dos_plotter, xlims, ylims, outfile):
        logger.info("Processing...")
        dos_plotter.add_dos_dict(dos_data.get_spd_dos())
        dos_plotter.get_plot(xlim=xlims, ylim=ylims)
        save_figure_dpi300(outfile)

    @logger.catch
    def s5_3(self, dos_data, dos_plotter, xlims, ylims, outfile):
        logger.info("Processing...")
        dos_plotter.add_dos_dict(dos_data.get_element_dos())
        dos_plotter.get_plot(xlim=xlims, ylim=ylims)
        save_figure_dpi300(outfile)

    @logger.catch
    def s5_4(self, dos_data, dos_plotter, xlims, ylims, outfile):
        iShift = input("Shift Efermi? (y/n): ")
        while True:
            if iShift.lower().startswith("y"):
                break
            elif iShift.lower().startswith("n"):
                from pymatgen.electronic_structure.plotter import DosPlotter

                dos_plotter = DosPlotter(stack=False, zero_at_efermi=False)
                break
            else:
                iShift = input("Invalid input, please retry")
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
            print(f"Avaliable orbitals for {str(e)}", unique_orbitals)

        ns = []
        oss = []
        while True:
            _n = input("--> Select one atom index (Enter to skip): ")
            if _n == "":
                break
            _e = dos_data.structure.sites[int(_n)].species_string
            _o = input(f" Select orbital for {_n} atom ({_e}) (separated by space): ")
            _os = _o.split(" ")
            ns.append(_n)
            oss.append(_os)

        logger.info("Processing...")
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
        iShift = input("Shift Efermi? (y/n): ")
        while True:
            if iShift.lower().startswith("y"):
                break
            elif iShift.lower().startswith("n"):
                from pymatgen.electronic_structure.plotter import DosPlotter

                dos_plotter = DosPlotter(stack=False, zero_at_efermi=False)
                break
            else:
                iShift = input("Invalid input, please retry")
                continue

        print(dos_data.structure)
        ais = input("Select atom index (separated by space)")
        logger.info("Processing...")

        atom_indices = [int(ai) for ai in ais.split()]
        for atom_index in atom_indices:
            dos_plotter.add_dos_dict(
                dos_data.get_site_t2g_eg_resolved_dos(dos_data.structure[atom_index])
            )

        dos_plotter.get_plot(xlim=xlims, ylim=ylims)
        save_figure_dpi300(outfile)

    @logger.catch
    def s5_6(self, dos_data):
        outfile = prompt(
            "Please enter the path to the output txt file (include file name): ",
            completer=pc,
        )
        logger.info("Processing...")

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
        logger.info("Processing...")
        from dspawpy.io.read import get_band_data, get_dos_data

        band_data = get_band_data(bfile)
        dos_data = get_dos_data(dfile)
        from pymatgen.electronic_structure.plotter import BSDOSPlotter

        bdp = BSDOSPlotter(dos_projection=None)
        from dspawpy.plot import pltbd

        pltbd(bdp, band_data, dos_data, ylim=ylims, filename=outfile)

    @logger.catch
    def s6_2(self, bfile, dfile, ylims, outfile):
        logger.info("Processing...")
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
        infile = prompt(
            "Please enter the path to the file (including file name): ", completer=pc
        )
        _list = [
            "AbsorptionCoefficient",
            "ExtinctionCoefficient",
            "RefractiveIndex",
            "Reflectance",
        ]
        key = until_give_valid_input(
            f"Data type {_list}: ",
            _list,
            completer=WordCompleter(_list),
        )
        _list2 = ["X", "Y", "Z", "XY", "YZ", "ZX"]
        label = until_give_valid_input(
            f"Specify data {_list2}: ",
            _list2,
            completer=WordCompleter(_list2),
        )

        outfile = prompt(
            "Please enter the path to the output file (include file name): ",
            completer=pc,
        )
        logger.info("Processing...")

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
        inis = prompt(
            "Please the the path to the initial structure file (include file name): ",
            completer=pc,
        )
        fins = prompt(
            "Please the the path to the final structure file (include file name): ",
            completer=pc,
        )
        nmiddle = int(input("How many images do you want to insert:"))
        method = until_give_valid_input(
            "Interpolation method(IDPP/Linear):", ["IDPP", "Linear"]
        )
        outdir = prompt(
            "Please enter the path to the output structures: ", completer=pc
        )
        if outdir == "":
            outdir = "."
        logger.info("Processing...")

        from dspawpy.diffusion.neb import NEB, write_neb_structures
        from dspawpy.io.structure import read

        init_struct = read(inis)[0]
        final_struct = read(fins)[0]

        neb = NEB(init_struct, final_struct, nmiddle + 2)
        if method == "Linear":
            structures = neb.linear_interpolate()
        elif method == "IDPP":
            try:
                structures = neb.idpp_interpolate()
            except Exception:
                logger.error("  IDPP failed! Please check the structures")
                structures = neb.linear_interpolate()
                logger.warning("  Switched to Linear...")
        else:
            raise ValueError("Unknown interpolation method: {}".format(method))
        absdir = os.path.abspath(outdir)
        os.makedirs(os.path.dirname(absdir), exist_ok=True)
        write_neb_structures(structures, fmt="as", path=absdir)
        logger.info(f"Interpolated structure files have been saved in {absdir}")

        while True:
            yn = input("Preview NEB chain? (y/n)")
            if yn.lower().startswith("y"):
                from dspawpy.diffusion.nebtools import write_json_chain

                write_json_chain(preview=True, directory=absdir)
                break
            elif yn.lower().startswith("n"):
                break
            else:
                print("Invalid input, please retry")
                continue

    @logger.catch
    def s8_2(
        self,
    ):
        infile = prompt(
            "Please enter the path to neb.h5/neb.json to be parsed (include file name) or the path of the neb calculation:",
            completer=pc,
        )
        outfile = prompt(
            "Please enter the path to the output file (including file name): ",
            completer=pc,
        )
        logger.info(
            "The interpolation method uses pchip by default, and if you want to use other methods, use a self-editing script"
        )
        logger.info("Processing...")

        from dspawpy.diffusion.nebtools import plot_barrier

        if os.path.isdir(infile):
            plot_barrier(directory=infile, figname=outfile, show=False)
        elif os.path.isfile(infile):
            plot_barrier(datafile=infile, figname=outfile, show=False)
        else:
            raise ValueError(f"{infile} must be file or folder path")

    @logger.catch
    def s8_3(
        self,
    ):
        datafolder = prompt(
            "Please enter the the path to the neb calculation: ", completer=pc
        )
        outdir = prompt("Please enter the path to the output folder: ", completer=pc)
        logger.info("Processing...")

        from dspawpy.diffusion.nebtools import summary

        assert os.path.isdir(datafolder), f"{datafolder} must be folder path"
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
        preview = until_give_valid_input("Preview NEB chain (y/n): ", ["y", "n"])
        directory = prompt("NEB calculation folder: ", completer=pc)
        if preview == "y":
            step = 0
        else:
            step = int(input("Ionic step index (start from 1, -1 means the last step"))
        dst = prompt("Output to folder: ", completer=pc)
        json_or_xyz = until_give_valid_input(
            "Output file format (json/xyz): ", ["json", "xyz"]
        )
        logger.info("Processing...")

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
        infile1 = prompt("Structure1 file path (including file name): ", completer=pc)
        infile2 = prompt("Structure2 file path (including file name): ", completer=pc)
        logger.info("Processing...")

        from dspawpy.io.structure import read

        s1 = read(infile1)[0]
        s2 = read(infile2)[0]
        from dspawpy.diffusion.nebtools import get_distance

        dist = get_distance(
            s1.frac_coords, s2.frac_coords, s1.lattice.matrix, s2.lattice.matrix
        )
        logger.info("Distance between them: ", dist, "Angstrom")

    @logger.catch
    def s8_6(
        self,
    ):
        dataFolder = prompt("NEB calculation folder: ", completer=pc)
        outdir = prompt("Back up to: ", completer=pc)
        logger.info("Processing...")

        from dspawpy.diffusion.nebtools import restart

        restart(dataFolder, outdir)

    @logger.catch
    def s9_1(
        self,
    ):
        infile = prompt(
            "Please enter the path to the file (including file name): ", completer=pc
        )
        ylims = check_lims(
            "Please input y-axis range (less and larger, separated by space):"
        )
        outfile = prompt(
            "Please enter the path to the output txt file (include file name): ",
            completer=pc,
        )
        logger.info("Processing...")

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
        infile = prompt(
            "Please enter the path to the file (including file name): ", completer=pc
        )
        xlims = check_lims(
            "Please input x-axis range (less and larger, separated by space):"
        )
        ylims = check_lims(
            "Please input y-axis range (less and larger, separated by space):"
        )
        outfile = prompt(
            "Please enter the path to the output txt file (include file name): ",
            completer=pc,
        )
        logger.info("Processing...")

        from dspawpy.io.read import get_phonon_dos_data

        dos = get_phonon_dos_data(infile)
        with HiddenPrints():
            from pymatgen.phonon.plotter import PhononDosPlotter
        dp = PhononDosPlotter(stack=False, sigma=None)
        dp.add_dos(label="Phonon", dos=dos)
        dp.get_plot(
            xlim=xlims,
            ylim=ylims,
            units="thz",
        )

        save_figure_dpi300(outfile)

    @logger.catch
    def s9_3(
        self,
    ):
        infile = prompt(
            "Please enter the path to the file (including file name): ", completer=pc
        )
        outfile = prompt(
            "Please enter the path to the output txt file (include file name): ",
            completer=pc,
        )
        logger.info("Processing...")

        from dspawpy.plot import plot_phonon_thermal

        plot_phonon_thermal(infile, outfile, False)

    @logger.catch
    def s10_1(
        self,
    ):
        infile = prompt(
            "Please enter the path to the file (including file name): ", completer=pc
        )
        outfile = prompt(
            "Please enter the output file path (including .xyz or .dump file name): ",
            completer=pc,
        )
        logger.info("Processing...")

        from dspawpy.io.structure import convert

        convert(infile, outfile=outfile)

    @logger.catch
    def s10_2(
        self,
    ):
        infile = prompt(
            "Please enter the path to the file (including file name): ", completer=pc
        )
        outfile = prompt(
            "Please enter the path to the output txt file (include file name): ",
            completer=pc,
        )
        logger.info("Processing...")

        from dspawpy.plot import plot_aimd

        plot_aimd(infile, show=False, figname=outfile)

    @logger.catch
    def s10_3(
        self,
    ):
        infile = prompt(
            "Please enter the path to the file (including file name): ", completer=pc
        )
        outfile = prompt(
            "Please enter the output file path (including file name): ", completer=pc
        )
        logger.info("Processing...")

        from dspawpy.analysis.aimdtools import MSD, _get_time_step, plot_msd
        from dspawpy.io.structure import read

        structures = read(infile)
        elements = [str(i) for i in structures[0].species]
        unique_elements = list(set(elements))
        select_str = input(
            f" Elements: {elements}\n Unique elements:{unique_elements}\nSelect atoms (separated by space):"
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
                    raise ValueError(f"Invalid input for {select_str=}")
            else:
                # single symbol or atom index
                # boss may be H1, must remove digit before checking
                if boss in unique_elements:
                    select = boss  # symbol
                elif boss.isdigit():
                    select = int(boss)  # atom index
                else:
                    raise ValueError(f"Invalid input for {select_str=}")

        print(select)
        msd_type = until_give_valid_input(
            "MSD type, select from xyz,xy,xz,yz,x,y,z, (Defaults to 'xyz', means all)",
            ["xyz", "xy", "xz", "yz", "x", "y", "z", ""],
        )
        timestep = input(
            f"time interval (fs), defaults to read from {infile}, if fail to read, set back to 1.0: "
        )
        xlims = check_lims(
            "Please input x-axis range (less and larger, separated by space):"
        )
        ylims = check_lims(
            "Please input y-axis range (less and larger, separated by space):"
        )

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
        infile = prompt(
            "Please enter the path to the file (including file name): ", completer=pc
        )
        timestep = input(
            f"time interval (fs), defaults to read from {infile}, if fail to read, set back to 1.0: "
        )
        if timestep == "":
            timestep = None
        else:
            timestep = float(timestep)
        xlims = check_lims(
            "Please input x-axis range (less and larger, separated by space):"
        )
        ylims = check_lims(
            "Please input y-axis range (less and larger, separated by space):"
        )
        outfile = prompt(
            "Please enter the output file path (including file name): ", completer=pc
        )
        logger.info("Processing...")

        from dspawpy.analysis.aimdtools import get_lagtime_rmsd, plot_rmsd

        lagtime, rmsd = get_lagtime_rmsd(infile, timestep)
        plot_rmsd(lagtime, rmsd, xlims, ylims, outfile, False)

    @logger.catch
    def s10_5(
        self,
    ):
        infile = prompt(
            "Please enter the path to the file (including file name): ", completer=pc
        )
        logger.info("Processing...")
        from dspawpy.analysis.aimdtools import get_rs_rdfs, plot_rdf
        from dspawpy.io.structure import read

        strs = read(datafile=infile)
        elements = [str(i) for i in strs[0].species]
        unique_elements = list(set(elements))
        print(f" Elements: {elements}\n Unique elements {unique_elements}")
        ele1 = until_give_valid_input(
            "--> Select one central element: ", unique_elements
        )
        ele2 = until_give_valid_input("--> Select one ref element", unique_elements)

        rmin = input("Minimum radius, Å  (Defaults to 0):")
        if rmin == "":
            rmin = 0
        else:
            rmin = float(rmin)

        rmax = input("Maximum radius, Å (Defaults to 10):")
        if rmax == "":
            rmax = 10
        else:
            rmax = float(rmax)

        ngrid = input("Grid number (Defaults to 101, including endpoints):")
        if ngrid == "":
            ngrid = 101
        else:
            ngrid = int(ngrid)

        sigma = input("Sigma value (Gaussian smooth, defaults to 0):")
        if sigma == "":
            sigma = 0
        else:
            sigma = float(sigma)

        xlims = [rmin, rmax]
        ylims = check_lims(
            "Please input y-axis range (less and larger, separated by space):"
        )
        outfile = prompt(
            "Please enter the output file path (including file name): ", completer=pc
        )

        rs, rdfs = get_rs_rdfs(infile, ele1, ele2, rmin, rmax, ngrid, sigma)
        plot_rdf(rs, rdfs, ele1, ele2, xlims, ylims, outfile, False)

    @logger.catch
    def s11(
        self,
    ):  # --> pol.png
        infile = prompt(
            "Please enter the path to the file to be parsed: ", completer=pc
        )
        repetition = int(input("Repetition (defaultss to 2): "))
        if repetition == "":
            repetition = 2
        outfile = prompt("Please enter the path to the output file: ", completer=pc)
        logger.info("Processing...")

        from dspawpy.plot import plot_polarization_figure

        plot_polarization_figure(infile, repetition, figname=outfile, show=False)

    @logger.catch
    def s12(
        self,
    ):
        infile = prompt("frequency.txt file path (including file name): ", completer=pc)
        outfile = prompt(
            "Please enter the path to the output txt file (include file name): ",
            completer=pc,
        )
        logger.info("Processing...")

        from dspawpy.io.utils import getZPE

        print(getZPE(infile, outfile))

    @logger.catch
    def s13_1(
        self,
    ):
        infile = prompt("frequency.txt file path (including file name): ", completer=pc)
        temperature = float(input("Temperature (K): "))
        outfile = prompt(
            "Please enter the path to the output txt file (include file name): ",
            completer=pc,
        )
        logger.info("Processing...")

        from dspawpy.io.utils import getTSads

        TSads = getTSads(infile, temperature, outfile)
        print("Entropy contribution, T*S (eV): ", TSads)

    @logger.catch
    def s13_2(
        self,
    ):
        fretxt = prompt("frequency.txt file path (including file name): ", completer=pc)
        infile = prompt("h5/json file path (including file name): ", completer=pc)
        temperature = float(input("Temperature (K): "))
        pressure = float(input("Preassure (Pa): "))
        outfile = prompt(
            "Please enter the path to the output txt file (include file name): ",
            completer=pc,
        )
        logger.info("Refers to user script for more options")
        logger.info("Processing...")

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
