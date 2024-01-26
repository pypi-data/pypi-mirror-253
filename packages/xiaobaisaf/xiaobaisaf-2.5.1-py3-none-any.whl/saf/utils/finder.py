#! /usr/bin/env python
'''
@Author: xiaobaiTser
@Time  : 2023/12/25 0:22
@File  : finder.py
'''

import tkinter as tk
from tkinter.ttk import Progressbar
import glob
import threading
from concurrent.futures import ThreadPoolExecutor


class FileSearcher(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.input_box = tk.Entry(self, width=50)
        self.search_button = tk.Button(self, text="搜索", command=self.on_search)
        self.results_box = tk.Text(self, height=10)

        self.input_box.pack()
        self.search_button.pack()
        self.results_box.pack()

        self.progress_bar = tk.ttk.Progressbar(self, orient="horizontal", length=100)
        self.progress_bar.pack()

        self.cancel_button = tk.Button(self, text="取消", command=self.on_cancel)
        self.cancel_button.pack()

    def on_search(self):
        self.progress_bar.value = 0
        self.progress_bar["maximum"] = 100
        self.results = []

        # 获取所有可用盘符
        self.drives = [f"{letter}:\\" for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

        # 创建线程池
        pool = ThreadPoolExecutor(len(self.drives))

        # 启动多个线程搜索文件
        for drive in self.drives:
            self.results.append(pool.submit(self._search_drive, args=(drive, self.progress_bar)).result())

        # # 等待所有线程完成
        # pool.close()
        # pool.join()

        # # 显示搜索结果
        # for task in self.results:
        #     result = task#.get()
        #     self.results += result
        #

        self.results_box.delete(1.0, "end")
        for result in self.results:
            self.progress_bar.value += 100 / len(self.drives)
            self.results_box.insert("end", result + "\n")

    def on_cancel(self):
        self.progress_bar.stop()

    def _search_drive(self, drive, progress_bar):
        results = glob.glob(f"{drive}**{self.input_box.get()}**", recursive=True)

        # 更新进度条
        progress_bar.value += 100 / len(self.drives)

        return results


root = tk.Tk()
file_searcher = FileSearcher(root)
file_searcher.pack()
root.mainloop()
