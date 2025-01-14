from game import MultiAgentSearchAgent

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.
    """
    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

# Definition of AlphaBetaAgent class
class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning.
    """
    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        with alpha-beta pruning.
        """
        alpha = float('-inf')
        beta = float('inf')
        action, _ = self.alphabeta(gameState, 0, 0, alpha, beta)
        return action

    def alphabeta(self, gameState, depth, agentIndex, alpha, beta):
        # Alpha-beta pruning implementation goes here
        pass
class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning.
    """
    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        with alpha-beta pruning.
        """
        alpha = float('-inf')
        beta = float('inf')
        action, _ = self.alphabeta(gameState, 0, 0, alpha, beta)
        return action

    def alphabeta(self, gameState, depth, agentIndex, alpha, beta):
        # Check if we have reached a terminal state or the maximum depth
        if depth == self.depth or gameState.isWin() or gameState.isLose():
            return None, self.evaluationFunction(gameState)
        
        # Roll over agent index to 0 (Pacman) if all agents have played their turn
        if agentIndex >= gameState.getNumAgents():
            agentIndex = 0
            depth += 1  # Increase depth when all agents have played

        # If Pacman's turn (Maximizer)
        if agentIndex == 0:
            return self.maxValue(gameState, depth, agentIndex, alpha, beta)
        # If it's one of the ghost's turn (Minimizer)
        else:
            return self.minValue(gameState, depth, agentIndex, alpha, beta)

    def maxValue(self, gameState, depth, agentIndex, alpha, beta):
        # Maximizer for Pacman
        maxEval = float('-inf')
        bestAction = None

        for action in gameState.getLegalActions(agentIndex):
            successor = gameState.generateSuccessor(agentIndex, action)
            _, evaluation = self.alphabeta(successor, depth, agentIndex + 1, alpha, beta)
            
            if evaluation > maxEval:
                maxEval = evaluation
                bestAction = action
            
            alpha = max(alpha, maxEval)
            
            # Pruning
            if beta <= alpha:
                break
        
        return bestAction, maxEval

    def minValue(self, gameState, depth, agentIndex, alpha, beta):
        # Minimizer for Ghosts
        minEval = float('inf')
        bestAction = None

        for action in gameState.getLegalActions(agentIndex):
            successor = gameState.generateSuccessor(agentIndex, action)
            _, evaluation = self.alphabeta(successor, depth, agentIndex + 1, alpha, beta)
            
            if evaluation < minEval:
                minEval = evaluation
                bestAction = action

            beta = min(beta, minEval)
            
            # Pruning
            if beta <= alpha:
                break
        
        return bestAction, minEval
