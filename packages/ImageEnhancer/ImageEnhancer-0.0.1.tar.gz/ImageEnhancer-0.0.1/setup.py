#!/usr/bin/env python

from setuptools import find_packages, setup

import os
import subprocess
import time

version_file = 'ImageEnhancer/realesrgan/version.py'


def readme():
    with open('README.md', encoding='utf-8') as f:
        content = f.read()
    return content


def get_git_hash():

    def _minimal_ext_cmd(cmd):
        # construct minimal environment
        env = {}
        for k in ['SYSTEMROOT', 'PATH', 'HOME']:
            v = os.environ.get(k)
            if v is not None:
                env[k] = v
        # LANGUAGE is used on win32
        env['LANGUAGE'] = 'C'
        env['LANG'] = 'C'
        env['LC_ALL'] = 'C'
        out = subprocess.Popen(cmd, stdout=subprocess.PIPE, env=env).communicate()[0]
        return out

    try:
        out = _minimal_ext_cmd(['git', 'rev-parse', 'HEAD'])
        sha = out.strip().decode('ascii')
    except OSError:
        sha = 'unknown'

    return sha


def get_hash():
    if os.path.exists('.git'):
        sha = get_git_hash()[:7]
    else:
        sha = 'unknown'

    return sha


def write_version_py():
    content = """# GENERATED VERSION FILE
# TIME: {}
__version__ = '{}'
__gitsha__ = '{}'
version_info = ({})
"""
    sha = get_hash()
    with open('VERSION', 'r') as f:
        SHORT_VERSION = f.read().strip()
    VERSION_INFO = ', '.join([x if x.isdigit() else f'"{x}"' for x in SHORT_VERSION.split('.')])

    version_file_str = content.format(time.asctime(), SHORT_VERSION, sha, VERSION_INFO)
    with open(version_file, 'w') as f:
        f.write(version_file_str)


def get_version():
    with open(version_file, 'r') as f:
        exec(compile(f.read(), version_file, 'exec'))
    return locals()['__version__']


def get_requirements(filename='requirements.txt'):
    here = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(here, filename), 'r') as f:
        requires = [line.replace('\n', '') for line in f.readlines()]
    return requires


if __name__ == '__main__':
    write_version_py()
    setup(
        name='ImageEnhancer',
        version='0.0.1',
        description="Real-ESRGAN strives to create effective algorithms for general image restoration, while GFPGAN focuses on enhancing the clarity of facial features in blurred images.",
        long_description="Rauhan Ahmed Siddiqui's web application, hosted on Hugging Face Spaces, is your one-stop shop for AI-powered image enhancement and upscaling. This innovative tool leverages the power of two Generative Adversarial Networks (GANs): Real-ESRGAN for seamlessly upscaling image backgrounds and GFPGAN for masterfully enhancing facial details in portraits. Deploying Gradio for production-ready deployment, this app breathes new life into your photos, transforming blurry memories and low-resolution gems into crisp, high-quality masterpieces. Experience the magic of AI-powered image restoration – upscale your cherished moments and rediscover the beauty hidden within!",
        author='Rauhan Ahmed Siddiqui',
        author_email='rauhaan.siddiqui@gmail.com',
        keywords='computer vision, pytorch, image restoration, super-resolution, esrgan, real-esrgan, gfpgan, facial image restoration, image enhancer, image upscaler, upscaler',
        packages=find_packages(exclude=('options', 'datasets', 'experiments', 'results', 'tb_logger', 'wandb')),
        classifiers=[
            'Development Status :: 4 - Beta',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
        ],
        license='BSD-3-Clause License',
        setup_requires=['cython', 'numpy'],
        install_requires=get_requirements(),
        zip_safe=False)
