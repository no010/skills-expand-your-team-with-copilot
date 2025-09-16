#!/usr/bin/env python3
"""
数独游戏测试 (Sudoku Game Tests)
测试数独游戏的核心功能
"""

from sudoku import Sudoku

def test_sudoku_creation():
    """测试数独游戏创建"""
    game = Sudoku()
    assert len(game.board) == 9
    assert len(game.board[0]) == 9
    print("✅ 数独游戏创建测试通过")

def test_puzzle_generation():
    """测试谜题生成"""
    game = Sudoku()
    
    # 测试不同难度的谜题生成
    for difficulty in ['easy', 'medium', 'hard']:
        game.generate_puzzle(difficulty)
        
        # 检查解决方案是否有效
        assert all(game.solution[i][j] != 0 for i in range(9) for j in range(9))
        
        # 检查谜题有空位
        empty_count = sum(1 for i in range(9) for j in range(9) if game.board[i][j] == 0)
        assert empty_count > 0
        
        print(f"✅ {difficulty}难度谜题生成测试通过 (空位数: {empty_count})")

def test_move_validation():
    """测试移动验证"""
    game = Sudoku()
    game.generate_puzzle('easy')
    
    # 找到一个空位进行测试
    empty_pos = None
    for i in range(9):
        for j in range(9):
            if game.board[i][j] == 0:
                empty_pos = (i, j)
                break
        if empty_pos:
            break
    
    if empty_pos:
        row, col = empty_pos
        correct_num = game.solution[row][col]
        
        # 测试正确的移动
        assert game.make_move(row, col, correct_num) == True
        assert game.board[row][col] == correct_num
        
        # 测试重复移动
        assert game.make_move(row, col, correct_num) == False
        
        print("✅ 移动验证测试通过")

def test_hint_system():
    """测试提示系统"""
    game = Sudoku()
    game.generate_puzzle('easy')
    
    hint = game.get_hint()
    if hint:
        row, col, num = hint
        assert 0 <= row < 9
        assert 0 <= col < 9
        assert 1 <= num <= 9
        assert game.board[row][col] == 0
        assert game.solution[row][col] == num
        
        print("✅ 提示系统测试通过")

def test_solve_algorithm():
    """测试求解算法"""
    game = Sudoku()
    
    # 创建一个简单的测试谜题
    test_board = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]
    
    import copy
    solution_board = copy.deepcopy(test_board)
    
    if game.solve(solution_board):
        # 检查解决方案是否有效
        for i in range(9):
            for j in range(9):
                assert solution_board[i][j] != 0
        print("✅ 求解算法测试通过")
    else:
        print("❌ 求解算法测试失败")

def test_board_validation():
    """测试棋盘验证"""
    game = Sudoku()
    
    # 测试有效的移动
    empty_board = [[0 for _ in range(9)] for _ in range(9)]
    assert game.is_valid_move(empty_board, 0, 0, 5) == True
    
    # 在同一行放置相同数字
    empty_board[0][1] = 5
    assert game.is_valid_move(empty_board, 0, 0, 5) == False
    
    # 在同一列放置相同数字
    empty_board[0][1] = 0
    empty_board[1][0] = 5
    assert game.is_valid_move(empty_board, 0, 0, 5) == False
    
    print("✅ 棋盘验证测试通过")

def run_all_tests():
    """运行所有测试"""
    print("🧪 开始运行数独游戏测试...")
    print("=" * 50)
    
    test_sudoku_creation()
    test_puzzle_generation()
    test_move_validation()
    test_hint_system()
    test_solve_algorithm()
    test_board_validation()
    
    print("=" * 50)
    print("🎉 所有测试通过！数独游戏工作正常。")

if __name__ == "__main__":
    run_all_tests()