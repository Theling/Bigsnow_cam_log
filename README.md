# Bigsnow Camera Logger

## Installation

```bash
conda create -n scrape python=3.10
conda activate scrape
pip install selenium Pillow
```

## Setup

1. Clone this repository, the default path for saving screenshots is ```"./log"```
1. ```python run.py```

## Optional Arguments

```bash
$ python run.py --help
usage: run.py [-h] [--step_time STEP_TIME] [--keep_num_screenshots KEEP_NUM_SCREENSHOTS] [--prod PROD] [--push PUSH] [--log_path LOG_PATH]

Capture frames from a video element and save them as images.

options:
  -h, --help            show this help message and exit
  --step_time STEP_TIME
                        Length of time interval between two screenshots in seconds, default 900.
  --keep_num_screenshots KEEP_NUM_SCREENSHOTS
                        The number of screenshots kept in the directory, default 5.
  --prod PROD           Product mode, whether to switch to prod branch, default True.
  --push PUSH           Whether to push screenshots, default False.
  --log_path LOG_PATH   Directory to save screenshots, default ./log
```
