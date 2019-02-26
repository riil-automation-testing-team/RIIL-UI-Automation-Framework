import sys
import shutil
import zipfile
from pathlib import Path
from rill_framework.autotest import Autotest
from rill_framework.report import reporter


def extract(zfile, path):
    f = zipfile.ZipFile(zfile, 'r')
    for file in f.namelist():
        f.extract(file, path)


def rill_framework():
    rill_framework_dir = Path(__file__).resolve().parents[0]
    example_dir = rill_framework_dir /'example' / 'rill_framework_example.zip'
    extract(str(example_dir), Path.cwd())
    print('\n\n生成 rill_framework example 成功\n快速体验，请输入如下命令，进入示例目录，启动运行脚本\n\ncd rill_framework_example\npython start.py')
