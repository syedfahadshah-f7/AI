class Environment:
    
    def __init__(self,vulner):
        self.vulner = vulner
    
    def display(self):
        print(f"Vulnerabilities : {self.vulner}")
        
    def get_vulnerability(self, i):
        return self.vulner[i]
    

class SecurityAgent:
    def __init__(self):
        self.patching = []
    
    def Scan(self, env):
        size = len(env.vulner)
        for i in range(0,size):
            if env.vulner[i] == "Safe":
                print("Logged \n")
            else:
                print("Warning \n")
                self.patching.append(i)
    
    def PatchingVulnerabilities(self, env):
        
        psize = len(self.patching)
        
        for i in range(psize):
           if env.vulner[self.patching[i]] == "Low Risk Vulnerable":
               env.vulner[self.patching[i]] = "Safe"
           else:
               print("need for premium service to patch them.\n")
               
               
def Run_Agent(agent, env):
    env.display()
    agent.Scan(env)
    agent.PatchingVulnerabilities(env)
    env.display()
    
env = Environment(["Safe", "Low Risk Vulnerable","High Risk Vulnerable","Low Risk Vulnerable","Low Risk Vulnerable","High Risk Vulnerable","Safe"])
agent = SecurityAgent()
Run_Agent(agent,env)
