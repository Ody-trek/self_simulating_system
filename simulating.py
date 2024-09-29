import random

class SelfSimulatingSystem:
    def __init__(self):
        self.state = "neutral"
        self.energy = 100
        self.knowledge_base = []
    
    # 感知外部输入
    def perceive(self, input_data):
        if input_data == "positive":
            self.state = "happy"
            self.energy += 10
        elif input_data == "negative":
            self.state = "sad"
            self.energy -= 10
        else:
            self.state = "neutral"
        
        self.feedback(input_data)
    
    # 模拟自身的状态
    def simulate_self(self):
        if self.energy < 50:
            self.state = "tired"
        elif self.energy > 150:
            self.state = "energetic"
        else:
            self.state = "neutral"
    
    # 根据输入和自身状态作出反应
    def feedback(self, input_data):
        # 将输入添加到知识库
        self.knowledge_base.append(input_data)
        
        # 对输入做出反馈
        print(f"Perceived input: {input_data}. Current state: {self.state}. Energy: {self.energy}.")
        
        # 自我模拟后调整状态
        self.simulate_self()
        print(f"After self-simulation: Current state: {self.state}. Energy: {self.energy}.")
    
    # 随机生成外部输入
    def random_input(self):
        return random.choice(["positive", "negative", "neutral"])
    
    # 系统运行循环
    def run(self, iterations=10):
        for _ in range(iterations):
            input_data = self.random_input()
            self.perceive(input_data)

# 创建并运行系统
system = SelfSimulatingSystem()
system.run()
