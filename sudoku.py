#!/usr/bin/env python3
"""
数独游戏 (Sudoku Game)
一个完整的数独游戏实现，包含游戏逻辑、求解算法和用户界面
"""

import random
import copy


class Sudoku:
    """数独游戏类"""
    
    def __init__(self):
        """初始化数独游戏"""
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.solution = [[0 for _ in range(9)] for _ in range(9)]
        
    def print_board(self, board=None):
        """打印数独棋盘"""
        if board is None:
            board = self.board
            
        print("\n  " + "─" * 37)
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("  " + "─" * 37)
            
            row = "│ "
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    row += "│ "
                
                if board[i][j] == 0:
                    row += "  . "
                else:
                    row += f"  {board[i][j]} "
            row += "│"
            print(row)
        print("  " + "─" * 37)
        
    def is_valid_move(self, board, row, col, num):
        """检查在指定位置放置数字是否有效"""
        # 检查行
        for j in range(9):
            if board[row][j] == num:
                return False
        
        # 检查列
        for i in range(9):
            if board[i][col] == num:
                return False
        
        # 检查3x3宫格
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        
        return True
    
    def solve(self, board):
        """使用回溯算法求解数独"""
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if self.is_valid_move(board, i, j, num):
                            board[i][j] = num
                            if self.solve(board):
                                return True
                            board[i][j] = 0
                    return False
        return True
    
    def generate_puzzle(self, difficulty='medium'):
        """生成数独谜题"""
        # 首先生成一个完整的解决方案
        self.solution = [[0 for _ in range(9)] for _ in range(9)]
        self._fill_diagonal_boxes()
        self.solve(self.solution)
        
        # 复制解决方案到游戏板
        self.board = copy.deepcopy(self.solution)
        
        # 根据难度移除数字
        difficulty_settings = {
            'easy': 35,      # 移除35个数字
            'medium': 45,    # 移除45个数字
            'hard': 55       # 移除55个数字
        }
        
        cells_to_remove = difficulty_settings.get(difficulty, 45)
        
        # 随机移除数字
        positions = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(positions)
        
        for i in range(cells_to_remove):
            row, col = positions[i]
            self.board[row][col] = 0
    
    def _fill_diagonal_boxes(self):
        """填充对角线上的3x3宫格"""
        for box in range(0, 9, 3):
            self._fill_box(box, box)
    
    def _fill_box(self, row, col):
        """填充3x3宫格"""
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        
        for i in range(3):
            for j in range(3):
                self.solution[row + i][col + j] = numbers[i * 3 + j]
    
    def make_move(self, row, col, num):
        """在指定位置放置数字"""
        if 0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9:
            if self.board[row][col] == 0:
                if self.is_valid_move(self.board, row, col, num):
                    self.board[row][col] = num
                    return True
                else:
                    print("无效的移动！这个数字违反了数独规则。")
                    return False
            else:
                print("这个位置已经有数字了！")
                return False
        else:
            print("无效的输入！请输入正确的行、列和数字。")
            return False
    
    def remove_number(self, row, col):
        """移除指定位置的数字"""
        if 0 <= row < 9 and 0 <= col < 9:
            self.board[row][col] = 0
            return True
        return False
    
    def is_complete(self):
        """检查游戏是否完成"""
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return False
        return True
    
    def get_hint(self):
        """获取提示"""
        empty_cells = [(i, j) for i in range(9) for j in range(9) if self.board[i][j] == 0]
        if empty_cells:
            row, col = random.choice(empty_cells)
            correct_num = self.solution[row][col]
            return row, col, correct_num
        return None


def main():
    """主游戏循环"""
    print("欢迎来到数独游戏！")
    print("=" * 50)
    
    game = Sudoku()
    
    while True:
        print("\n请选择:")
        print("1. 开始新游戏")
        print("2. 退出")
        
        choice = input("请输入选择 (1-2): ").strip()
        
        if choice == '1':
            # 选择难度
            print("\n请选择难度:")
            print("1. 简单 (easy)")
            print("2. 中等 (medium)")
            print("3. 困难 (hard)")
            
            difficulty_choice = input("请输入难度 (1-3): ").strip()
            difficulty_map = {'1': 'easy', '2': 'medium', '3': 'hard'}
            difficulty = difficulty_map.get(difficulty_choice, 'medium')
            
            print(f"\n生成{difficulty}难度的数独谜题...")
            game.generate_puzzle(difficulty)
            
            # 游戏循环
            while True:
                game.print_board()
                
                if game.is_complete():
                    print("\n🎉 恭喜你！你成功完成了数独游戏！")
                    break
                
                print("\n操作选项:")
                print("1. 放置数字 (格式: 行 列 数字, 例如: 1 2 5)")
                print("2. 移除数字 (格式: r 行 列, 例如: r 1 2)")
                print("3. 获取提示 (输入: hint)")
                print("4. 返回主菜单 (输入: quit)")
                
                user_input = input("请输入操作: ").strip().lower()
                
                if user_input == 'quit':
                    break
                elif user_input == 'hint':
                    hint = game.get_hint()
                    if hint:
                        row, col, num = hint
                        print(f"提示: 在位置 ({row+1}, {col+1}) 可以放置数字 {num}")
                    else:
                        print("没有更多提示了！")
                elif user_input.startswith('r '):
                    try:
                        parts = user_input.split()
                        row, col = int(parts[1]) - 1, int(parts[2]) - 1
                        if game.remove_number(row, col):
                            print("数字已移除！")
                        else:
                            print("无效的位置！")
                    except (ValueError, IndexError):
                        print("输入格式错误！请使用格式: r 行 列")
                else:
                    try:
                        parts = user_input.split()
                        if len(parts) == 3:
                            row, col, num = int(parts[0]) - 1, int(parts[1]) - 1, int(parts[2])
                            game.make_move(row, col, num)
                        else:
                            print("输入格式错误！请使用格式: 行 列 数字")
                    except ValueError:
                        print("请输入有效的数字！")
        
        elif choice == '2':
            print("感谢游玩数独游戏！再见！")
            break
        else:
            print("无效的选择，请重新输入。")


if __name__ == "__main__":
    main()