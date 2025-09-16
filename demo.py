#!/usr/bin/env python3
"""
数独游戏演示 (Sudoku Game Demo)
展示数独游戏的基本功能
"""

from sudoku import Sudoku

def demo():
    """演示数独游戏的功能"""
    print("🎮 数独游戏演示")
    print("=" * 50)
    
    # 创建游戏实例
    game = Sudoku()
    
    # 生成简单难度的谜题
    print("📋 生成简单难度的数独谜题...")
    game.generate_puzzle('easy')
    
    print("🎯 初始谜题:")
    game.print_board()
    
    # 演示一些移动
    print("\n🎲 演示游戏操作:")
    
    # 获取提示
    hint = game.get_hint()
    if hint:
        row, col, num = hint
        print(f"💡 提示: 位置 ({row+1}, {col+1}) 可以放置数字 {num}")
        
        # 应用提示
        if game.make_move(row, col, num):
            print("✅ 成功放置数字!")
            game.print_board()
        
        # 演示无效移动
        print(f"\n❌ 尝试在同一位置再次放置数字 {num}:")
        game.make_move(row, col, num)
        
        # 演示移除数字
        print(f"\n🔄 移除位置 ({row+1}, {col+1}) 的数字:")
        game.remove_number(row, col)
        game.print_board()
    
    print("\n📊 游戏状态:")
    print(f"游戏是否完成: {game.is_complete()}")
    
    # 显示解决方案的一部分
    print("\n🔍 解决方案预览 (前3行):")
    for i in range(3):
        row = "│ "
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row += "│ "
            row += f"  {game.solution[i][j]} "
        row += "│"
        print(row)
    
    print("\n🎉 演示完成！运行 'python3 sudoku.py' 开始游戏")

if __name__ == "__main__":
    demo()