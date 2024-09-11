import os
import chess
import chess.engine


os.system('title CHESS AI')

engine_path = r""#stockfish경로

def suggest_best_move(board):
    with chess.engine.SimpleEngine.popen_uci(engine_path) as engine:
        result = engine.play(board, chess.engine.Limit(time=2.0))
        return result.move

def update_board(board, move):
    try:
        board.push_san(move)
    except ValueError:
        print(f"잘못된 수: {move}. 다시 시도하세요.")

def play_chess():
    board = chess.Board()
    user_move = input("\n당신의 첫 수를 입력하세요 (예: e2e4): ")
    update_board(board, user_move)

    while not board.is_game_over():
        os.system('cls')

        print("\n현재 체스판 상태:")
        print(board)
        opponent_move = input("\n상대방의 수를 입력하세요 (예: e7e5): ")
        update_board(board, opponent_move)

        if board.is_game_over():
            break 
        best_move = suggest_best_move(board)
        print(f"체스 AI가 추천하는 당신의 최적의 수: {best_move}")
        input("이 수를 두려면 엔터를 누르세요...")
        board.push(best_move)
    print("\n게임 종료!")
    if board.is_checkmate():
        print("체크메이트!")
    elif board.is_stalemate():
        print("스테일메이트!")
    elif board.is_insufficient_material():
        print("기물 부족으로 무승부!")
    else:
        print("게임이 종료되었습니다.")

# 체스 게임 시작
play_chess()
