import tkinter as tk
from tkinter import ttk, messagebox
import math

class GridCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("纸张方格计算器v0.01（luwentao@gmail.com）")
        self.root.geometry("650x550")
        self.root.configure(bg='#f0f8ff')
        
        # 创建样式
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f8ff')
        self.style.configure('TLabel', background='#f0f8ff', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10, 'bold'))
        self.style.configure('Header.TLabel', font=('Arial', 14, 'bold'), foreground='#2c3e50')
        
        # 创建主框架
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 标题
        title_label = ttk.Label(self.main_frame, text="纸张方格布局计算器", style='Header.TLabel')
        title_label.grid(row=0, column=0, columnspan=4, pady=(0, 20))
        
        # 纸张尺寸输入
        paper_frame = ttk.LabelFrame(self.main_frame, text="纸张尺寸 (厘米)")
        paper_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky="we")
        
        ttk.Label(paper_frame, text="高度:").grid(row=0, column=0, padx=5, pady=5, sticky="e")  # 改为高度
        self.height_entry = ttk.Entry(paper_frame, width=10)  # 变量名改为height
        self.height_entry.grid(row=0, column=1, padx=5, pady=5)
        self.height_entry.insert(0, "29.7")  # A4纸高度
        
        ttk.Label(paper_frame, text="宽度:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.width_entry = ttk.Entry(paper_frame, width=10)
        self.width_entry.grid(row=0, column=3, padx=5, pady=5)
        self.width_entry.insert(0, "21.0")  # A4纸宽度
        
        # 留白区域输入
        margin_frame = ttk.LabelFrame(self.main_frame, text="留白区域 (厘米)")
        margin_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=5, sticky="we")
        
        ttk.Label(margin_frame, text="上留空:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.top_entry = ttk.Entry(margin_frame, width=10)
        self.top_entry.grid(row=0, column=1, padx=5, pady=5)
        self.top_entry.insert(0, "2.0")
        
        ttk.Label(margin_frame, text="下留空:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.bottom_entry = ttk.Entry(margin_frame, width=10)
        self.bottom_entry.grid(row=0, column=3, padx=5, pady=5)
        self.bottom_entry.insert(0, "2.0")
        
        ttk.Label(margin_frame, text="左留空:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.left_entry = ttk.Entry(margin_frame, width=10)
        self.left_entry.grid(row=1, column=1, padx=5, pady=5)
        self.left_entry.insert(0, "2.0")
        
        ttk.Label(margin_frame, text="右留空:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        self.right_entry = ttk.Entry(margin_frame, width=10)
        self.right_entry.grid(row=1, column=3, padx=5, pady=5)
        self.right_entry.insert(0, "2.0")
        
        # 字数输入
        chars_frame = ttk.LabelFrame(self.main_frame, text="字数设置")
        chars_frame.grid(row=3, column=0, columnspan=4, padx=10, pady=5, sticky="we")
        
        ttk.Label(chars_frame, text="总字数:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.chars_entry = ttk.Entry(chars_frame, width=15)
        self.chars_entry.grid(row=0, column=1, padx=5, pady=5)
        self.chars_entry.insert(0, "400")
        
        # 按钮
        self.calc_button = ttk.Button(self.main_frame, text="计算最佳布局", command=self.calculate_grids)
        self.calc_button.grid(row=4, column=0, columnspan=4, pady=20)
        
        # 结果区域
        result_frame = ttk.LabelFrame(self.main_frame, text="计算结果")
        result_frame.grid(row=5, column=0, columnspan=4, padx=10, pady=5, sticky="we")
        
        # 结果标签
        self.result_text = tk.Text(result_frame, height=8, width=60, font=('Arial', 10), bg='#f9f9f9')
        self.result_text.grid(row=0, column=0, padx=10, pady=10)
        self.result_text.insert(tk.END, "输入参数后点击计算按钮，结果将显示在这里...")
        self.result_text.config(state=tk.DISABLED)
        
        # 纸张示意图
        self.canvas = tk.Canvas(self.main_frame, width=400, height=200, bg='white', bd=1, relief=tk.SUNKEN)
        self.canvas.grid(row=6, column=0, columnspan=4, pady=20)
        
        # 添加示例图
        self.draw_paper_example()
        
        # 状态栏
        self.status_var = tk.StringVar()
        self.status_var.set("就绪 - 输入参数后点击计算按钮")
        status_bar = ttk.Label(root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def draw_paper_example(self):
        """绘制纸张示意图"""
        self.canvas.delete("all")
        
        # 纸张外框
        self.canvas.create_rectangle(50, 30, 350, 170, outline='#333', width=2)
        self.canvas.create_text(200, 15, text="纸张示意图", font=('Arial', 10, 'bold'))
        
        # 留白区域
        self.canvas.create_rectangle(60, 40, 340, 60, fill='#e6f2ff', outline='')  # 上留空
        self.canvas.create_rectangle(60, 150, 340, 160, fill='#e6f2ff', outline='')  # 下留空
        self.canvas.create_rectangle(60, 40, 70, 160, fill='#e6f2ff', outline='')    # 左留空
        self.canvas.create_rectangle(330, 40, 340, 160, fill='#e6f2ff', outline='')  # 右留空
        
        # 标注
        self.canvas.create_text(65, 50, text="上留空", anchor=tk.W, font=('Arial', 8))
        self.canvas.create_text(65, 155, text="下留空", anchor=tk.W, font=('Arial', 8))
        self.canvas.create_text(65, 100, text="左留空", anchor=tk.W, font=('Arial', 8))
        self.canvas.create_text(335, 100, text="右留空", anchor=tk.E, font=('Arial', 8))
        
        # 可用区域
        self.canvas.create_rectangle(70, 60, 330, 150, fill='#d9ead3', outline='')
        self.canvas.create_text(200, 105, text="可用区域", font=('Arial', 10))
    
    def draw_grid_layout(self, rows, cols, usable_width, usable_height):
        """绘制网格布局示意图"""
        self.canvas.delete("all")
        
        # 纸张外框
        self.canvas.create_rectangle(50, 30, 350, 170, outline='#333', width=2)
        self.canvas.create_text(200, 15, text="网格布局示意图", font=('Arial', 10, 'bold'))
        
        # 可用区域
        self.canvas.create_rectangle(70, 60, 330, 150, fill='#d9ead3', outline='')
        
        # 计算每个格子的大小
        cell_width = usable_width / cols
        cell_height = usable_height / rows
        
        # 缩放因子，使网格适应画布
        scale_x = 260 / usable_width
        scale_y = 90 / usable_height
        scale = min(scale_x, scale_y)
        
        # 计算偏移量以居中显示
        scaled_width = usable_width * scale
        scaled_height = usable_height * scale
        start_x = 70 + (260 - scaled_width) / 2
        start_y = 60 + (90 - scaled_height) / 2
        
        # 绘制网格
        for i in range(rows + 1):
            y = start_y + i * cell_height * scale
            self.canvas.create_line(start_x, y, start_x + scaled_width, y, fill='#6aa84f')
        
        for j in range(cols + 1):
            x = start_x + j * cell_width * scale
            self.canvas.create_line(x, start_y, x, start_y + scaled_height, fill='#6aa84f')
        
        # 标注信息
        # 格子尺寸向下取整到小数点后一位
        cell_width_floor = math.floor(cell_width * 10) / 10
        cell_height_floor = math.floor(cell_height * 10) / 10
        info_text = f"布局: {rows}行 × {cols}列  格子尺寸: {cell_height_floor:.1f}×{cell_width_floor:.1f}厘米"
        self.canvas.create_text(200, 170, text=info_text, font=('Arial', 9))
    
    def calculate_grids(self):
        """计算网格布局"""
        try:
            # 获取输入值
            height = float(self.height_entry.get())  # 改为高度
            width = float(self.width_entry.get())
            top = float(self.top_entry.get())
            bottom = float(self.bottom_entry.get())
            left = float(self.left_entry.get())
            right = float(self.right_entry.get())
            num_chars = int(self.chars_entry.get())
            
            # 验证输入
            if height <= 0 or width <= 0:
                messagebox.showerror("错误", "纸张尺寸必须大于0")
                return
            if top < 0 or bottom < 0 or left < 0 or right < 0:
                messagebox.showerror("错误", "留空值不能为负数")
                return
            if num_chars <= 0:
                messagebox.showerror("错误", "字数必须大于0")
                return
            
            # 计算可用区域
            usable_height = height - top - bottom  # 使用高度计算
            usable_width = width - left - right
            
            if usable_height <= 0 or usable_width <= 0:
                messagebox.showerror("错误", "无效的留空设置，可用区域为负！")
                return
            
            # 初始化最佳方案
            best_size = 0.0
            best_rows = 0
            best_cols = 0
            best_type = ""
            
            # 方法1：按高度划分行
            max_rows = int(usable_height)  # 最大可能行数
            for rows in range(1, max_rows + 1):
                cell_height = usable_height / rows
                cols = math.floor(usable_width / cell_height)  # 计算列数
                if cols < 1:
                    continue  # 列数不能小于1
                if rows * cols >= num_chars:
                    if cell_height > best_size:
                        best_size = cell_height
                        best_rows = rows
                        best_cols = cols
                        best_type = "正方形（按高度划分）"
            
            # 方法2：按宽度划分列
            max_cols = int(usable_width)  # 最大可能列数
            for cols in range(1, max_cols + 1):
                cell_width = usable_width / cols
                rows = math.floor(usable_height / cell_width)  # 计算行数
                if rows < 1:
                    continue  # 行数不能小于1
                if rows * cols >= num_chars:
                    if cell_width > best_size:
                        best_size = cell_width
                        best_rows = rows
                        best_cols = cols
                        best_type = "正方形（按宽度划分）"
            
            # 显示结果
            if best_size > 0:
                # 格子尺寸向下取整到小数点后一位
                cell_size_floor = math.floor(best_size * 10) / 10
                
                self.result_text.config(state=tk.NORMAL)
                self.result_text.delete(1.0, tk.END)
                result = f"最佳布局方案：\n"
                result += f"布局类型: {best_type}\n"
                result += f"行数（每列格子数）: {best_rows}\n"
                result += f"列数: {best_cols}\n"
                result += f"格子尺寸: {cell_size_floor:.1f} × {cell_size_floor:.1f} 厘米 (向下取整)\n"
                result += f"总格子数: {best_rows * best_cols} (≥ 字数 {num_chars})\n"
                result += f"可用区域尺寸: {usable_width:.2f} × {usable_height:.2f} 厘米\n"
                # 计算纸张利用率
                total_area = best_rows * best_cols * best_size**2
                utilization = total_area / (usable_width * usable_height) * 100
                result += f"纸张利用率: {utilization:.1f}%"
                
                self.result_text.insert(tk.END, result)
                self.result_text.config(state=tk.DISABLED)
                
                # 绘制网格布局
                self.draw_grid_layout(best_rows, best_cols, usable_width, usable_height)
                
                self.status_var.set(f"计算完成 - 找到最佳布局: {best_rows}行 × {best_cols}列")
            else:
                messagebox.showwarning("警告", "无法排列：可用区域不足或字数过多！")
                self.status_var.set("错误：可用区域不足或字数过多")
        
        except ValueError:
            messagebox.showerror("输入错误", "请输入有效的数字！")
            self.status_var.set("错误：输入值无效")

if __name__ == "__main__":
    root = tk.Tk()
    app = GridCalculatorApp(root)
    root.mainloop()