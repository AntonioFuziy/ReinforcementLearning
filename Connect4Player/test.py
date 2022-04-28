from Player import Player
import numpy as np

class FuziyPlayer(Player):
  def name(self):
    return "Fuziy Player"

  def max_value(self, board, action, alpha, beta, player_code, p):
    if p == 0:
      result = self.eval(player_code, board), action
      return result
    sucessors = self.sucessores(player_code, board)
    for s in sucessors:
      mv, ac = self.min_value(s['board'], s['action'], alpha, beta, player_code, p-1)
      if (mv > alpha):
        alpha = mv
        action = ac
      if (alpha >= beta):
        return alpha, action
    return alpha, action
  
  def min_value(self, board, action, alpha, beta, player_code, p):
    if p == 0:
      result = self.eval(player_code, board), action
      return result
    sucessors = self.sucessores(player_code, board)
    for s in sucessors:
      mv, ac = self.max_value(s['board'], s['action'], alpha, beta, player_code, p-1)
      if (mv < beta):
        beta = mv
        action = ac
      if (beta <= alpha):
        return beta, action 
    return beta, action

  def move(self, player_code, board):
    _, action = self.max_value(board, None, -999999, 999999, player_code, 5)

    attack, attack_position = self.defence_play(player_code, board)
    if attack:
      print("VITORIA")
      return None, attack_position

    near_lost, defence_position = self.defence_play(self.enemy(player_code), board)
    if near_lost:
      print("DEFESA")
      return None, defence_position

    if (self.emergency(board, player_code)):
      sucessores = self.sucessores(self.enemy(player_code), board)
      for s in sucessores:
        result = self.eval(self.enemy(player_code), s['board'])
        if (result > 70000):
          return None, s['action']
    return None, action

  def sucessores(self, player_code, board):
    sucessors = []
    for i in range(0,7):
      b = self.movement(player_code, board, i)
      if(b is not None):
        sucessors.append({'board':b, 'action':i})
    return sucessors

  def enemy(self, player):
    if player == 1:
      return 2
    else:
      return 1

  def eval(self, player, board): 
    lines = self.count_row_line(player, board)
    cols = self.count_row_column(player, board)
    diags = self.count_row_diag(player, board)
    diags2 = self.count_row_diag(player, board[::-1])
    possible_path = lines['2'] + cols['2'] + diags['2'] + diags2['2']
    near_to_win = lines['3'] + cols['3'] + diags['3'] + diags2['3']
    almost_win = lines['4'] + cols['4'] + diags['4'] + diags2['4']
    win = 100000*almost_win + 1000*near_to_win + 10*possible_path

    enemy = self.enemy(player)
    enemy_lines = self.count_row_line(enemy, board)
    enemy_cols = self.count_row_column(enemy, board)
    enemy_digs = self.count_row_diag(enemy, board)
    enemy_digs2 = self.count_row_diag(enemy, board[::-1])
    possible_path_lost = enemy_lines['2'] + enemy_cols['2'] + enemy_digs['2'] + enemy_digs2['2']
    near_to_lost = enemy_lines['3'] + enemy_cols['3'] + enemy_digs['3'] + enemy_digs2['3']
    almost_lost = enemy_lines['4'] + enemy_cols['4'] + enemy_digs['4'] + enemy_digs2['4']
    lost = 100000*almost_lost + 1000*near_to_lost + 10*possible_path_lost
    
    return (win - lost)

  def count_row_line(self, player, board):
    retorno = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}
    for i in range(6):
      counter = 0
      for j in range(6):
        if ((board[i, j] == player) and (board[i, j] == board[i, j + 1])):
          counter = counter + 1
        else:
          counter = 0
        if (counter==1):
          retorno['2'] = retorno['2'] + 1
        if (counter==2):
          retorno['3'] = retorno['3'] + 1
        if (counter==3):
          retorno['4'] = retorno['4'] + 1
    return retorno
  
  def count_row_column(self, player, board):
    retorno = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}
    for i in range(6):
      counter = 0
      for j in range(5):
        if ((board[j, i] == player) and (board[j,i] == board[j+1,i])):
          counter = counter + 1
        else:
          counter = 0
        if (counter==1):
          retorno['2'] = retorno['2'] + 1
        if (counter==2):
          retorno['3'] = retorno['3'] + 1
        if (counter==3):
          retorno['4'] = retorno['4'] + 1
    return retorno
  
  def count_row_diag(self, player, board):
    retorno = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}
    for k in range(-2,4):
      counter = 0
      x = np.diag(board, k=k)
      for i in range(0,len(x)-1):
        if ((x[i] == player) and (x[i] == x[i+1])):
          counter = counter + 1
        else:
          counter = 0
        if (counter==1):
          retorno['2'] = retorno['2'] + 1
        if (counter==2):
          retorno['3'] = retorno['3'] + 1
        if (counter==3):
          retorno['4'] = retorno['4'] + 1
    return retorno

  def count_last_line(self, player, board):
    counter = 0
    for i in range(6):
      if (board[5, i] == player):
        counter = counter + 1
    return counter

  def emergency(self, board, player_code):
    enemy = self.enemy(player_code)
    enemy_lines = self.count_row_line(enemy, board)
    enemy_cols = self.count_row_column(enemy, board)
    enemy_digs = self.count_row_diag(enemy, board)
    enemy_digs2 = self.count_row_diag(enemy, board[::-1])
    if (enemy_cols['3'] > 0 or enemy_lines['3'] > 0 or enemy_digs['3'] > 0 or enemy_digs2['3']> 0):
      return True
    return False

  def defence_play(self, player_code, board):
    threat = None
    for i in range(6):
      counter = 0
      for j in range(6):
        if ((board[i, j] == player_code) and (board[i, j+1] == player_code)):
          counter = counter + 1
        else:
          counter = 0
        if counter >= 2:
          if i == 5 and i <= 3:
            if board[i,j+2] == 0:
              threat = j+2
              return True, threat
          if i == 5 and j >= 2:
            if board[i,j-2] == 0:
              threat = j-2
              return True, threat
          else:
            if j <= 3:
              if (board[i,j+2] == 0) and (board[i+1,j+2] != 0):
                threat = j+2
                return True, threat
            if j >= 2:
              if board[i,j-2] == 0 and (board[i+1,j-2] != 0):
                threat = j-2
                return True, threat
        if (counter >= 1):
          if i == 5 and i <= 3:
            if (board[i, j+3] == player_code) and (board[i,j+2] == 0):
              threat = j+2
              return True, threat 
          if i == 5 and j >= 2:
            if (board[i,j-2] == player_code) and (board[i,j-1] == 0):
              threat = j-1
              return True, threat
          else:
            if j <= 3:
              if (board[i, j+3] == player_code) and (board[i,j+2] == 0) and (board[i+1,j+2] != 0):
                threat = j+2
                return True, threat 
            if j >= 2:
              if (board[i,j-2] == player_code) and (board[i,j-1] == 0) and (board[i+1,j-1] != 0):
                threat = j-1
                return True, threat
              
    return False, threat
  
  def movement(self, player, board, column):
    result_board = np.matrix(board)
    for i in range(5,-2,-1):
      if (board[i,column] == 0):
        break
    if(i < 0):
      return None
    result_board[i, column] = player
    return result_board

