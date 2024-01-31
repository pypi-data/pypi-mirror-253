from setuptools import setup, find_packages
import os
import shutil
from setuptools.command.install import install
import subprocess

# class CustomInstallCommand(install):
#     def run(self):
#         install.run(self)
#         self.download_data()
#     def download_data(self):
#         subprocess.run(['wget','-O','./Prior/Opn_median_mm9.bed','https://github.com/SUwonglab/PECA/raw/master/Prior/Opn_median_mm9.bed'])
#         subprocess.run(['wget','-O','./Prior/Opn_median_mm10.bed','https://github.com/SUwonglab/PECA/raw/master/Prior/Opn_median_mm10.bed'])
#         subprocess.run(['wget','-O','./Prior/Opn_median_hg19.bed','https://github.com/SUwonglab/PECA/raw/master/Prior/Opn_median_hg19.bed'])
#         subprocess.run(['wget','-O','./Prior/Opn_median_hg38.bed','https://github.com/SUwonglab/PECA/raw/master/Prior/Opn_median_hg38.bed'])
#         subprocess.run(['wget','-O','./Prior/RE_gene_corr_mm9.bed','https://github.com/SUwonglab/PECA/raw/master/Prior/RE_gene_corr_mm9.bed'])
#         subprocess.run(['wget','-O','./Prior/RE_gene_corr_mm10.bed','https://github.com/SUwonglab/PECA/raw/master/Prior/RE_gene_corr_mm10.bed'])
#         subprocess.run(['wget','-O','./Prior/RE_gene_corr_hg19.bed','https://github.com/SUwonglab/PECA/raw/master/Prior/RE_gene_corr_hg19.bed'])
#         subprocess.run(['wget','-O','./Prior/RE_gene_corr_hg38.bed','https://github.com/SUwonglab/PECA/raw/master/Prior/RE_gene_corr_hg38.bed'])
#         subprocess.run(['wget','-O','./Prior/TFTG_corr_mouse.mat','https://github.com/SUwonglab/PECA/raw/master/Prior/TFTG_corr_mouse.mat'])
#         subprocess.run(['wget','-O','./Prior/TFTG_corr_human.mat','https://github.com/SUwonglab/PECA/raw/master/Prior/TFTG_corr_human.mat'])

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='scPECA_test',
    version='1.1',
    author='Jiahao Zhang',
    author_email='zhangjiahao@amss.ac.cn',
    description='PECA2 gene regulatory network construction for single-cell data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/zhangjiahao1234/scPECA',
    packages=find_packages(),
    include_package_data=True,
    # cmdclass={'install':  CustomInstallCommand}
)